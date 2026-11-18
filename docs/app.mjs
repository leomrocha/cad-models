import {pageSize, search} from './engine.mjs';
const $ = id => document.getElementById(id);
const url = new URL(location.href);
const options = url.searchParams;
if (options.get('engine') === 'duckdb') $('engine').value = 'duckdb';
$('query').value = options.get('q') || '';
$('field').value = options.has('tag') ? 'tags' : (options.get('field') || '');
$('value').value = options.get('tag') || options.get('value') || '';
const initialPage = Number(options.get('page') || 1);
let page = Number.isSafeInteger(initialPage) && initialPage >= 1 && initialPage <= 1_000_000 ? initialPage : 1;
const pagers = [...document.querySelectorAll('.pagination')];
let worker;
let generation = 0;
function sqlite(request, args) {
  worker ??= new Worker(new URL('./sqlite-worker.mjs', location.href), {type:'module'});
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
async function render() {
  const request = ++generation;
  for (const pager of pagers) for (const button of pager.querySelectorAll('button')) button.disabled = true;
  $('status').textContent = 'Searching…';
  const args = ['query', 'field', 'value'].map(id => $(id).value);
  const engine = $('engine').value;
  const state = new URL(location.href);
  state.search = '';
  for (const [key, value] of Object.entries({engine, q:args[0], field:args[1], value:args[2]})) {
    if (value && !(key === 'engine' && value === 'sqlite')) state.searchParams.set(key, value);
  }
  if (page > 1) state.searchParams.set('page', page);
  history.replaceState(null, '', state);
  try {
    const {rows, hasNext} = await (engine === 'sqlite' ? sqlite(request, [...args, page]) : search(engine, ...args, page));
    if (request !== generation) return;
    $('results').replaceChildren(...rows.map(card));
    const first = (page - 1) * pageSize + 1;
    $('status').textContent = rows.length ? `Models ${first}–${first + rows.length - 1}` : 'No matches. Try a different search or clear the filter.';
    for (const pager of pagers) {
      pager.hidden = page === 1 && !hasNext;
      pager.querySelector('[data-page="-1"]').disabled = page === 1;
      pager.querySelector('[data-page="1"]').disabled = !hasNext;
      pager.querySelector('[data-page-number]').textContent = `Page ${page}`;
    }
  } catch (error) {
    if (request !== generation) return;
    console.error(error);
    $('results').replaceChildren();
    for (const pager of pagers) pager.hidden = true;
    $('status').textContent = 'Search is unavailable. Open Browse subjects to view catalogue entries.';
  }
  if (request === generation) $('status').dataset.completed = String(request);
}
function newSearch() {
  page = 1;
  render();
}
$('search').addEventListener('submit', event => {event.preventDefault(); newSearch();});
$('engine').addEventListener('change', newSearch);
for (const selector of document.querySelectorAll('#search-tags [data-tag]')) {
  selector.addEventListener('click', event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    $('field').value = 'tags';
    $('value').value = selector.dataset.tag;
    newSearch();
  });
}
for (const pager of pagers) {
  pager.addEventListener('click', event => {
    const button = event.target.closest('button[data-page]');
    if (!button || button.disabled) return;
    page += Number(button.dataset.page);
    render();
    if (pager === pagers.at(-1)) $('status').scrollIntoView({block:'start'});
  });
}
render();
