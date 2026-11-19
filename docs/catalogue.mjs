const base = 'https://raw.githubusercontent.com/leomrocha/cad-models/master/data/';
export const dataURL = filename => new URL(filename, base).href;

function element(tag, text) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  return node;
}

function link(url, label) {
  const node = element('a', label);
  node.href = url;
  return node;
}

function tagURL(search, tag) {
  const url = new URL(search, location.href);
  url.searchParams.set('tag', tag);
  return url.href;
}

function addTags(list, records) {
  const tags = [...new Set(records.flatMap(record => record.tags))];
  for (const tag of tags.sort((a, b) => a.localeCompare(b))) {
    const item = element('li');
    const anchor = link(tagURL(list.dataset.searchUrl, tag), tag);
    anchor.dataset.tag = tag;
    item.append(anchor);
    list.append(item);
  }
}

function showSubjects(container, records) {
  const subjects = new Map();
  for (const record of records) {
    if (!subjects.has(record.subject)) subjects.set(record.subject, []);
    subjects.get(record.subject).push(record);
  }
  for (const subject of [...subjects.keys()].sort()) {
    const list = element('ul');
    for (const record of subjects.get(subject)) {
      const item = element('li');
      item.append(link(container.dataset.modelUrl + encodeURIComponent(record.id) + '.html', record.name));
      list.append(item);
    }
    container.append(element('h3', subject), list);
  }
}

function showModel(container, record) {
  if (!record) {
    container.textContent = 'Model unavailable.';
    return;
  }
  document.title = record.name;
  document.querySelector('main h1').textContent = record.name;
  if (record.description) container.append(element('p', record.description));
  if (record.download) {
    const links = element('p');
    links.append(link(record.repo_folder, 'Model folder on GitHub'), ' · ',
      link(record.download, 'Download ' + record.file.split('.').at(-1).toUpperCase() + ' CAD model'),
      ' · ', link(record.companion, 'Companion'));
    container.append(links);
  } else if (record.state) {
    container.append(element('p', record.state));
  }
  if (record.gallery.length) {
    const gallery = element('div');
    gallery.className = 'gallery';
    for (const view of record.gallery) {
      const figure = element('figure');
      const anchor = link(view.url);
      const image = element('img');
      image.src = view.url;
      image.alt = view.alt;
      image.loading = 'lazy';
      anchor.append(image);
      figure.append(anchor, element('figcaption', view.view));
      gallery.append(figure);
    }
    container.append(element('h2', 'Preview views'), gallery);
  }
  for (const field of ['tags', 'materials', 'standards', 'dimensions']) {
    if (!record[field]?.length) continue;
    const list = element('ul');
    for (const value of record[field]) {
      const item = element('li');
      if (field === 'tags') item.append(link(tagURL(container.dataset.searchUrl, value), value));
      else item.textContent = Object.values(value).join(' · ');
      list.append(item);
    }
    container.append(element('h2', field[0].toUpperCase() + field.slice(1)), list);
  }
}

if (typeof document !== 'undefined') {
  const tags = document.querySelectorAll('[data-catalogue-tags]');
  const subjects = document.querySelector('#catalogue-subjects');
  const model = document.querySelector('#catalogue-model');
  if (tags.length || subjects || model) {
    fetch(dataURL('catalogue.json')).then(response => {
      if (!response.ok) throw new Error('Catalogue download failed');
      return response.json();
    }).then(records => {
      for (const list of tags) addTags(list, records);
      if (subjects) showSubjects(subjects, records);
      if (model) showModel(model, records.find(record => record.id === model.dataset.id));
    }).catch(() => {
      for (const list of tags) list.append(element('li', 'Catalogue tags unavailable.'));
      if (subjects) subjects.textContent = 'Catalogue subjects unavailable.';
      if (model) model.textContent = 'Catalogue record unavailable.';
    });
  }
}
