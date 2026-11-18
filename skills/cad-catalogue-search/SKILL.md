---
name: cad-catalogue-search
description: Search the local CAD Models catalogue for existing parts, assemblies, identifiers, tags, materials, standards, and dimensions.
---

# Search the CAD catalogue

Run the repository's read-only Python command. It returns JSON. SQLite uses
Python's standard library. For DuckDB, use the interpreter with the catalogue's
DuckDB dependency installed.

```sh
python scripts/search.py 'LS-PS310K'
python scripts/search.py --filter tags caster --limit 15
python scripts/search.py --engine duckdb --data /path/to/data 'ISO 730'
```

Use `--data` to target a specific built catalogue snapshot. Search the exact
identifier first, then try keywords or filter values. A null field means the
catalogue lacks that detail. Review the model page and companion for the source
and geometry scope. Report which snapshot and catalogue IDs the search returned.
