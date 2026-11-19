---
name: cad-catalogue-search
description: Search the local CAD Models catalogue for existing parts, assemblies, identifiers, tags, materials, standards, and dimensions.
---

# Search the CAD catalogue

Run the repository's read-only Python command. It returns JSON. SQLite uses
Python's standard library. For DuckDB, use the interpreter with the catalogue's
DuckDB dependency installed.

```sh
python scripts/search.py --data data 'LS-PS310K'
python scripts/search.py --data data --filter tags caster --limit 15
python scripts/search.py --engine duckdb --data data 'ISO 730'
```

Use `data` for the catalogue included in the checkout. Use another `--data` path to target a different snapshot. Search the exact
identifier first, then try keywords or filter values. A null field means the
catalogue lacks that detail. Review the model page and companion for the source
and geometry scope. Report which snapshot and catalogue IDs the search returned.

Use the catalogue record in `data/catalogue.json` to check asset links.
The CAD file, companion, thumbnails, and views are stored together under
`data/packages/models/`. Site links and browser image requests must use the
exact file URLs on `raw.githubusercontent.com`. For delivery, run the build and sync commands, then verify ID and tag parity in both indexes and
confirm the site output contains zero CAD or image copies.
