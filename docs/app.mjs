import {pageSize, search} from './engine.mjs?v=3';
const $ = id => document.getElementById(id);
function readState(url) {
  const params = url.searchParams;
  const parsedPage = Number(params.get('page') || 1);
  return {
    engine: params.get('engine') === 'duckdb' ? 'duckdb' : 'sqlite',
    query: params.get('q') || '',
    field: params.has('tag') ? 'tags' : (params.get('field') || ''),
    value: params.get('tag') || params.get('value') || '',
    page: Number.isSafeInteger(parsedPage) && parsedPage >= 1 && parsedPage <= 1_000_000 ? parsedPage : 1,
  };
}
function fillForm({engine, query, field, value}) {
  $('engine').value = engine;
  $('query').value = query;
  $('field').value = field;
  $('value').value = value;
}
function resultUrl({engine, query, field, value, page}) {
  const url = new URL(location.href);
  url.search = '';
  for (const [key, text] of Object.entries({engine, q: query, field, value})) {
    if (text && !(key === 'engine' && text === 'sqlite')) url.searchParams.set(key, text);
  }
  if (page > 1) url.searchParams.set('page', page);
  return url;
}
function clearState(engine) {
  return {engine, query: '', field: '', value: '', page: 1};
}
let active = readState(new URL(location.href));
fillForm(active);
const pagers = [...document.querySelectorAll('.pagination')];
let worker;
let generation = 0;
function sqlite(request, args) {
  worker ??= new Worker(new URL('./sqlite-worker.mjs?v=3', import.meta.url), {type:'module'});
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
    image.src = new URL(url.replace(/^\//, ''), import.meta.url).href;
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
function setPagerLink(link, state) {
  if (state) {
    link.href = resultUrl(state).href;
    link.removeAttribute('aria-disabled');
  } else {
    link.removeAttribute('href');
    link.setAttribute('aria-disabled', 'true');
  }
}
async function render(state, action = 'replaceState') {
  const request = ++generation;
  active = state;
  const {engine, query, field, value, page} = state;
  history[action](null, '', resultUrl(state));
  $('explore-all').href = resultUrl(clearState(engine)).href;
  $('status').textContent = 'Searching…';
  $('results').setAttribute('aria-busy', 'true');
  try {
    const args = [query, field, value, page];
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
      setPagerLink(pager.querySelector('[data-page="-1"]'), page > 1 ? {...state, page: page - 1} : null);
      setPagerLink(pager.querySelector('[data-page="1"]'), hasNext ? {...state, page: page + 1} : null);
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
    field: $('field').value, value: $('value').value, page: 1}, 'pushState');
}
function plainClick(event) {
  return !event.ctrlKey && !event.metaKey && !event.shiftKey && !event.altKey && event.button === 0;
}
$('search').addEventListener('submit', event => {event.preventDefault(); newSearch();});
$('engine').addEventListener('change', newSearch);
$('explore-all').addEventListener('click', event => {
  if (!plainClick(event)) return;
  event.preventDefault();
  const state = clearState($('engine').value);
  fillForm(state);
  render(state, 'pushState');
});
for (const selector of document.querySelectorAll('#search-tags [data-tag]')) {
  selector.addEventListener('click', event => {
    if (!plainClick(event)) return;
    event.preventDefault();
    $('field').value = 'tags';
    $('value').value = selector.dataset.tag;
    newSearch();
  });
}
for (const pager of pagers) {
  pager.addEventListener('click', event => {
    const link = event.target.closest('a[data-page][href]');
    if (!link || !plainClick(event)) return;
    event.preventDefault();
    const state = readState(new URL(link.href));
    if (state.page === active.page || $('results').hasAttribute('aria-busy')) return;
    render(state, 'pushState');
    if (pager === pagers.at(-1)) $('status').scrollIntoView({block:'start'});
  });
}
window.addEventListener('popstate', () => {
  const state = readState(new URL(location.href));
  fillForm(state);
  render(state);
});
render(active);
