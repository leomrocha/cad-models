"""Read-only search of the generated CAD catalogue, with JSON output for agents."""
import argparse
import json
import re
import sqlite3
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("query", nargs="?", default="")
parser.add_argument("--engine", choices=("sqlite", "duckdb"), default="sqlite")
parser.add_argument("--data", type=Path, default=Path(__file__).resolve().parents[1] / "data")
parser.add_argument("--filter", nargs=2, metavar=("FIELD", "VALUE"), action="append", default=[])
parser.add_argument("--needs-information", action="store_true")
parser.add_argument("--limit", type=int, default=20)
args = parser.parse_args()
fields = {"subject", "kind", "tags", "materials", "standards", "dimensions"}
if not 1 <= args.limit <= 1000 or any(field not in fields for field, _ in args.filter):
    parser.error("limit must be 1–1000 and filters must use " + ", ".join(sorted(fields)))

if args.engine == "sqlite":
    conn = sqlite3.connect((args.data / "catalogue.sqlite").resolve().as_uri() + "?mode=ro", uri=True)
    models, facets = "models", "facets"
    source_values = []
else:
    import duckdb
    conn = duckdb.connect()
    models, facets = "read_parquet(?)", "read_parquet(?)"
    source_values = [str(args.data / f"{name}.parquet") for name in ("catalogue", "facets")]

q = args.query.strip().lower()
words = re.findall(r"[^\W_]+", q)
exact = "FALSE"
exact_values = []
if q:
    exact = "(lower(m.id)=? OR lower(m.name)=? OR EXISTS (SELECT 1 FROM f WHERE f.model=m.id AND f.field='aliases' AND f.value=?))"
    exact_values = [q] * 3
conditions, values = [], []
if q:
    if not words:
        keyword, keywords = "FALSE", []
    elif args.engine == "sqlite":
        keyword = "m.id IN (SELECT id FROM keyword WHERE keyword MATCH ?)"
        keywords = [" AND ".join(f'"{word}"' for word in words)]
    else:
        keyword = " AND ".join("regexp_matches(lower(m.text), ?)" for _ in words)
        keywords = [r"(^|[^\p{L}\p{N}])" + re.escape(word) + r"($|[^\p{L}\p{N}])" for word in words]
    conditions.append(f"({exact} OR ({keyword}))")
    values.extend(exact_values + keywords)
for field, value in args.filter:
    conditions.append("EXISTS (SELECT 1 FROM f WHERE f.model=m.id AND f.field=? AND f.value=?)")
    values.extend((field, value.strip().casefold()))
if args.needs_information:
    conditions.append("m.needs_information")
where = "WHERE " + " AND ".join(conditions) if conditions else ""
query = f"""
WITH m AS (SELECT * FROM {models}),
     f AS (SELECT * FROM {facets})
SELECT m.id, m.name, m.subject, m.description, m.tags, m.materials, m.standards, m.dimensions,
       m.needs_information, {exact} AS exact
FROM m {where}
ORDER BY exact DESC, m.id LIMIT ?
"""
with conn:
    cursor = conn.execute(query, source_values + exact_values + values + [args.limit])
    names = [item[0] for item in cursor.description]
    result = [dict(zip(names, row)) for row in cursor.fetchall()]
for row in result:
    for name in ("tags", "materials", "standards", "dimensions"):
        if row[name] is not None:
            row[name] = json.loads(row[name])
    for name in ("exact", "needs_information"):
        row[name] = bool(row[name])
print(json.dumps(result, ensure_ascii=False, indent=2))
