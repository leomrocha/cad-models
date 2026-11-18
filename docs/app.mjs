import {search} from './engine.mjs';
const $ = id => document.getElementById(id);
const url = new URL(location.href);
if (url.searchParams.get('engine') === 'duckdb') $('engine').value = 'duckdb';
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
      else resolve(data.rows);
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
  $('status').textContent = 'Searching…';
  const args = ['query', 'field', 'value'].map(id => $(id).value);
  const engine = $('engine').value;
  try {
    const rows = await (engine === 'sqlite' ? sqlite(request, args) : search(engine, ...args));
    if (request !== generation) return;
    $('results').replaceChildren(...rows.map(card));
    $('status').textContent = rows.length ? `${rows.length} model${rows.length === 1 ? '' : 's'} shown` : 'No matches. Try a different search or clear the filter.';
  } catch (error) {
    if (request !== generation) return;
    console.error(error);
    $('results').replaceChildren();
    $('status').textContent = 'Search is unavailable. Open Browse subjects to view catalogue entries.';
  }
  if (request === generation) $('status').dataset.completed = String(request);
}
$('search').addEventListener('submit', event => {event.preventDefault(); render();});
$('engine').addEventListener('change', render);
render();
