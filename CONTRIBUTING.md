# Contribute to CAD Models

## Catalogue tickets

Use a bug report for a wrong result, a broken download, or a catalogue error.
Use an improvement ticket for a proposed search, classification, or catalogue
change. A catalogue-wide ticket can identify a page or query.

1. Run `python scripts/intake.py new bug > bug.json` or replace `bug` with `improvement`.
2. Fill in the title, affected URL or query, and expected and observed results for a bug. Include the model ID and revision when relevant.
3. Check the draft with `python scripts/intake.py check bug.json` and give it to the maintainer for triage.

## Models, revisions, and subjects

1. Search for existing models and variants. Generate a draft with `python scripts/intake.py new model` or `python scripts/intake.py new subject`.
2. Describe the supplied geometry and its best-known subject and tags. Use JSON null for unavailable facts. Attach source citations to standards and material claims. List internal CAD references with their exact revisions and use roles.
3. Share metadata and citations at intake. Maintain clearance for each native file, embedded resource, derivative and preview before public submission.
4. Include available, redistribution-cleared preview images for the supplied CAD revision. Use a small isometric thumbnail when available. Additional front, side, top, or detail views can help. Use PNG, JPEG, or WebP and label each view with `view`, `file`, and `alt`. Store images under `data/previews/` and list their relative paths in the model's `previews` array. Entries without images remain listed.
5. Run the same draft check and catalogue build used by maintainers. Maintainers resolve duplicate IDs, review evidence and rights, and decide when a model can be released.
