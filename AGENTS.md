# CAD Models contribution instructions

Work within the assigned catalogue issue. Use the same intake and build commands
as human contributors. Submit drafts with the affected catalogue IDs, evidence,
and checks. A maintainer assigns final IDs and authorizes publication.

Keep the catalogue independent of source projects. Record original evidence
for individual records and use null for unknown facts. Keep supplier and sales
listing URLs out of public catalogue records and companions.

Each model folder under `data/packages/models/` owns its CAD file, matching
Markdown companion, gallery images, and thumbnail. Record the files in that
model's `package_assets` and `previews`. Use one file for identical asset bytes.
The site generates indexes and pages. It loads every image and links to every
model asset through `raw.githubusercontent.com` using the repository path.
Run the export, build, and sync checks before delivery. Check both search
engines, the model's raw links, and zero asset copies in the site output.

For catalogue questions, use `python scripts/search.py --data docs/data QUERY`.
Read [the catalogue search skill](skills/cad-catalogue-search/SKILL.md) for
search and result reporting. Use [CONTRIBUTING.md](CONTRIBUTING.md) for
catalogue corrections, proposals, and submission checks.
