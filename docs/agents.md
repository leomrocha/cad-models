---
layout: default
title: Agent guide
permalink: /agents.html
---

## Search the published catalogue data

Use the [repository checkout](https://github.com/leomrocha/cad-models) and run
the read-only Python command from its root. The SQLite database in `data`
can be queried as soon as the repository is available locally.

```sh
python scripts/search.py --data data 'LS-PS310K'
python scripts/search.py --data data --filter tags caster --limit 10
python scripts/search.py --data data --needs-information --limit 10
```

Use `--engine duckdb` with an interpreter that has the project's DuckDB
dependency installed. Both engines return JSON. Point `--data` at the intended
catalogue snapshot if you have multiple builds.

Start with an exact identifier when available. Then try keywords or use an
exact filter value. Treat `null` as a detail the catalogue has yet to establish.
Report the catalogue ID and link for each useful result. Open the model page
and technical companion to check the supplied geometry and source.

## Help maintain the catalogue

1. Select a concrete task such as checking a broken link, correcting a tag,
   recording a cited dimension, or proposing a model. Search for duplicates
   before preparing an addition.
2. Prepare a draft issue or a scoped change and include the model ID, affected
   page or query, supporting evidence, and checks performed. Follow the shared
   [contribution guide]({{ '/contributing.html' | relative_url }}).
3. Leave publication and acceptance to the maintainer. Preserve unknown fields
   and attribute sourced claims.

Repository instructions live in
[AGENTS.md](https://github.com/leomrocha/cad-models/blob/master/AGENTS.md).
The [catalogue search skill](https://github.com/leomrocha/cad-models/tree/master/skills/cad-catalogue-search)
contains the reusable search procedure.
