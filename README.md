# CAD Models

CAD Models is a searchable catalogue of CAD parts, assemblies, and reference
drawings. Each entry describes the model and links to available CAD files, preview
images, and technical companions.

The current index contains 320 entries, including 319 reusable CAD model records
and the original tube-profile DXF. Each entry lists its available downloads.

**[Search the catalogue](https://leomrocha.github.io/cad-models/)**
· [Browse subjects](https://leomrocha.github.io/cad-models/browse.html)
· [User guide](https://leomrocha.github.io/cad-models/manual.html)
· [Agent guide](https://leomrocha.github.io/cad-models/agents.html)

## Find and download a model

1. Search by name, part number, standard designation, or keyword. Try
   `LS-PS310K` or `ISO 4017`.
2. Select **SQLite** or **DuckDB with Parquet**. Both search the same catalogue.
   Use a filter to narrow results, or browse by subject.
3. Open a result to inspect its geometry scope and available files.
   Download the CAD file and read its companion when listed. Entries can
   describe a model even when a CAD download is unavailable.

## Contribute

[Open an issue](https://github.com/leomrocha/cad-models/issues/new) to report a
broken download, correct a model record, suggest a search improvement, or
propose a model or subject. Include the affected entry or search query and any
supporting evidence. See the [contribution guide](CONTRIBUTING.md) for model
sources, redistribution, preview images, and proposed changes.

## Search from an agent or script

Run these commands from the repository root. SQLite uses Python's standard
library and searches the database already included in the checkout.

```sh
python scripts/search.py --data docs/data 'LS-PS310K'
python scripts/search.py --data docs/data --filter tags caster --limit 10
```

For DuckDB, use an interpreter with the dependencies from `requirements.txt`
and pass `--engine duckdb`. Both engines return JSON. The
[catalogue search skill](skills/cad-catalogue-search/SKILL.md) covers how to
interpret results and share findings.

## Build and maintain the site

The Jekyll source and published catalogue assets are in `docs/`.
Build and preview the site locally with Jekyll and Node.js.

```sh
jekyll build --safe --source docs --destination _site
CATALOGUE_ROOT=_site node scripts/serve.mjs
```

Open <http://127.0.0.1:8339>. Edit the user-facing Markdown in `docs/`.
Edit the root `CONTRIBUTING.md` for changes to the published contribution guide.

For changes to catalogue data or browser assets, refresh the generated files
from the repository root, then run the Jekyll build again.

```sh
npm ci
python -m venv .venv
.venv/bin/pip install -r requirements.txt
node scripts/export.mjs
.venv/bin/python scripts/build.py
python scripts/sync-docs.py
```

The model metadata starts in `data/pilot.json`. The sync command updates
the Jekyll model entries, search assets, and contribution guide.
