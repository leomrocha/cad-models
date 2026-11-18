const quote = value => "'" + value.replaceAll("'", "''") + "'";
const tokens = text => text.toLowerCase().match(/[\p{L}\p{N}]+/gu) || [];
const esc = text => text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const choices = new Set(['subject', 'kind', 'tags', 'materials', 'standards', 'dimensions']);

async function sqliteEngine() {
  const {default: init} = await import('./vendor/sqlite/index.mjs');
  const sqlite = await init();
  const response = await fetch('./data/catalogue.sqlite');
  if (!response.ok) throw new Error('SQLite download failed');
  const bytes = new Uint8Array(await response.arrayBuffer());
  const db = new sqlite.oo1.DB();
  const ptr = sqlite.wasm.allocFromTypedArray(bytes);
  db.checkRc(sqlite.capi.sqlite3_deserialize(db.pointer, 'main', ptr, bytes.length, bytes.length, 5));
  return sql => db.exec({sql, returnValue: 'resultRows', rowMode: 'object'});
}

async function duckEngine() {
  const duck = await import('./vendor/duckdb/duckdb-browser.mjs');
  const worker = new Worker(new URL('./vendor/duckdb/duckdb-browser-eh.worker.js', location.href));
  const db = new duck.AsyncDuckDB(new duck.VoidLogger(), worker);
  await db.instantiate(new URL('./vendor/duckdb/duckdb-eh.wasm', location.href).href);
  for (const name of ['catalogue', 'facets']) {
    await db.registerFileURL(name + '.parquet', new URL('./data/' + name + '.parquet', location.href).href, duck.DuckDBDataProtocol.HTTP, false);
  }
  const conn = await db.connect();
  await conn.query("CREATE VIEW models AS SELECT * FROM read_parquet('catalogue.parquet')");
  await conn.query("CREATE VIEW facets AS SELECT * FROM read_parquet('facets.parquet')");
  return async sql => (await conn.query(sql)).toArray().map(row => row.toJSON());
}

const engines = new Map();
export const pageSize = 100;

export async function search(engine, query, field, value, page = 1) {
  if (!Number.isSafeInteger(page) || page < 1 || page > 1_000_000) {
    throw new RangeError('Invalid search page');
  }
  if (!engines.has(engine)) {
    const promise = engine === 'duckdb' ? duckEngine() : sqliteEngine();
    engines.set(engine, promise);
    promise.catch(() => engines.delete(engine));
  }
  const run = await engines.get(engine);
  const q = query.trim().toLowerCase();
  const words = tokens(q);
  const exact = q ? `(lower(m.id) = ${quote(q)} OR lower(m.name) = ${quote(q)} OR EXISTS (SELECT 1 FROM facets fa WHERE fa.model=m.id AND fa.field='aliases' AND fa.value=${quote(q)}))` : 'FALSE';
  const constraints = [];
  if (choices.has(field) && value.trim()) {
    constraints.push(`EXISTS (SELECT 1 FROM facets f WHERE f.model=m.id AND f.field=${quote(field)} AND f.value=${quote(value.trim().toLowerCase())})`);
  } else if (field === 'needs') {
    constraints.push('m.needs_information');
  }
  if (q) {
    let keyword = 'FALSE';
    if (words.length) {
      if (engine === 'sqlite') {
        keyword = `m.id IN (SELECT id FROM keyword WHERE keyword MATCH ${quote(words.map(word => '"' + word + '"').join(' AND '))})`;
      } else {
        keyword = words.map(word => `regexp_matches(lower(m.text), ${quote('(^|[^\\p{L}\\p{N}])' + esc(word) + '($|[^\\p{L}\\p{N}])')})`).join(' AND ');
      }
    }
    constraints.push(`(${exact} OR (${keyword}))`);
  }
  const rows = await run(`SELECT m.id, m.name, m.subject, m.description, m.needs_information, m.preview, ${exact} AS exact FROM models m ${constraints.length ? 'WHERE ' + constraints.join(' AND ') : ''} ORDER BY exact DESC, m.id LIMIT ${pageSize + 1} OFFSET ${(page - 1) * pageSize}`);
  return {rows: rows.slice(0, pageSize), hasNext: rows.length > pageSize};
}
