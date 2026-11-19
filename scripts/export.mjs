import {readFileSync, writeFileSync, mkdirSync} from 'node:fs';

const rows = JSON.parse(readFileSync('data/pilot.json', 'utf8'));
const scale = Number(process.env.CATALOGUE_SCALE ?? 1);
const records = Array.from({length: scale}, (_, index) => rows.map(row => {
  const record = {...row};
  delete record.sources;
  if (index) Object.assign(record, {id: `${row.id}-scale-${index}`, aliases: [], file: undefined, package_assets: [], previews: []});
  const text = [record.name, record.description, ...record.tags, ...record.aliases].join(' ');
  return {...record, text};
})).flat();
mkdirSync('dist/data', {recursive: true});
writeFileSync('dist/data/catalogue.json', JSON.stringify(records));
