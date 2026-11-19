import {pageSizes, search} from './engine.mjs?v=6';
const $ = id => document.getElementById(id);
function readState(url) {
  const params = url.searchParams;
  const parsedPage = Number(params.get('page') || 1);
  const parsedSize = Number(params.get('size'));
  return {
    engine: params.get('engine') === 'duckdb' ? 'duckdb' : 'sqlite',
    query: params.get('q') || '',
    field: params.has('tag') ? 'tags' : (params.get('field') || ''),
    value: params.get('tag') || params.get('value') || '',
    pageSize: pageSizes.includes(parsedSize) ? parsedSize : pageSizes[0],
    page: Number.isSafeInteger(parsedPage) && parsedPage >= 1 && parsedPage <= 1_000_000 ? parsedPage : 1,
  };
}
function fillForm({engine, query, field, value, pageSize}) {
  $('engine').value = engine;
  $('query').value = query;
  $('field').value = field;
  $('value').value = value;
  $('page-size').value = pageSize;
}
function resultUrl({engine, query, field, value, page, pageSize}) {
  const url = new URL(location.href);
  url.search = '';
  for (const [key, text] of Object.entries({engine, q: query, field, value})) {
    if (text && !(key === 'engine' && text === 'sqlite')) url.searchParams.set(key, text);
  }
  if (page > 1) url.searchParams.set('page', page);
  if (pageSize !== pageSizes[0]) url.searchParams.set('size', pageSize);
  return url;
}
let active = readState(new URL(location.href));
fillForm(active);
const pagers = [...document.querySelectorAll('.pagination')];
let worker;
let generation = 0;
function sqlite(request, args) {
  worker ??= new Worker(new URL('./sqlite-worker.mjs?v=6', import.meta.url), {type:'module'});
  return new Promise((resolve, reject) => {
    function cleanup() {
      worker.removeEventListener('message', receive);
      worker.removeEventListener('error', failed);
    }
    function receive({data}) {
      if (data.request !== request) return;
      cleanup();
      if (data.error) reject(new Error(data.error));
      else resolve(data.result);
    }
    function failed(event) {
      cleanup();
      reject(new Error(event.message || 'Search worker failed'));
    }
    worker.addEventListener('message', receive);
    worker.addEventListener('error', failed);
    worker.postMessage({request, args});
  });
}
function card(row) {
  const article = document.createElement('article');
  article.className = 'card';
  const subject = document.createElement('small');
  subject.textContent = row.subject;
  const title = document.createElement('h2');
  const link = document.createElement('a');
  link.href = './models/' + encodeURIComponent(row.id) + '.html';
  link.textContent = row.name;
  title.append(link);
  const summary = document.createElement('p');
  summary.textContent = row.description;
  if (row.preview) {
    const {url, alt} = JSON.parse(row.preview);
    const image = document.createElement('img');
    image.className = 'thumbnail';
    image.src = url;
    image.alt = alt;
    image.loading = 'lazy';
    article.append(image);
  }
  article.append(subject, title, summary);
  if (row.needs_information) {
    const note = document.createElement('small');
    note.textContent = 'Needs more information';
    article.append(note);
  }
  return article;
}
async function render(state, action = 'replaceState') {
  const request = ++generation;
  active = state;
  const {engine, query, field, value, page, pageSize} = state;
  history[action](null, '', resultUrl(state));
  $('status').textContent = 'Searching…';
  $('results').setAttribute('aria-busy', 'true');
  try {
    const args = [query, field, value, page, pageSize];
    const {rows, hasNext, total} = await (engine === 'sqlite' ? sqlite(request, args) : search(engine, ...args));
    if (request !== generation) return;
    $('results').replaceChildren(...rows.map(card));
    const first = (page - 1) * pageSize + 1;
    const filter = field === 'needs' ? 'Needs more information' : value && field ? value : '';
    const context = [query && `Search: “${query}”`, filter && `Filter: ${filter}`].filter(Boolean).join(' · ');
    const summary = rows.length ? `Showing ${first}–${first + rows.length - 1} of ${total} models` : 'No matches';
    $('status').textContent = context ? `${summary} · ${context}` : summary;
    for (const pager of pagers) {
      pager.hidden = page === 1 && !hasNext;
      pager.querySelector('[data-page="-1"]').hidden = page === 1;
      pager.querySelector('[data-page="1"]').hidden = !hasNext;
      pager.querySelector('[data-page-number]').textContent = `Page ${page}`;
    }
  } catch (error) {
    if (request !== generation) return;
    console.error(error);
    $('results').replaceChildren();
    for (const pager of pagers) pager.hidden = true;
    $('status').textContent = 'Search is unavailable. Open Browse subjects to view catalogue entries.';
  } finally {
    if (request === generation) {
      $('results').removeAttribute('aria-busy');
      $('status').dataset.completed = String(request);
    }
  }
}
function newSearch() {
  render({engine: $('engine').value, query: $('query').value,
    field: $('field').value, value: $('value').value, page: 1, pageSize: Number($('page-size').value)}, 'pushState');
}
function plainClick(event) {
  return !event.ctrlKey && !event.metaKey && !event.shiftKey && !event.altKey && event.button === 0;
}
$('search').addEventListener('submit', event => {event.preventDefault(); newSearch();});
$('engine').addEventListener('change', newSearch);
$('page-size').addEventListener('change', () => {
  render({...active, pageSize: Number($('page-size').value), page: 1}, 'pushState');
});
$('search-tags').addEventListener('click', event => {
  const selector = event.target.closest('[data-tag]');
  if (!selector || !plainClick(event)) return;
  event.preventDefault();
  $('field').value = 'tags';
  $('value').value = selector.dataset.tag;
  newSearch();
});
for (const pager of pagers) {
  pager.addEventListener('click', event => {
    const button = event.target.closest('button[data-page]');
    if (!button || button.hidden || $('results').hasAttribute('aria-busy')) return;
    const page = active.page + Number(button.dataset.page);
    render({...active, page}, 'pushState');
    if (pager === pagers.at(-1)) $('status').scrollIntoView({block:'start'});
  });
}
window.addEventListener('popstate', () => {
  const state = readState(new URL(location.href));
  fillForm(state);
  render(state);
});
render(active);
