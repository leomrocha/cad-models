"""Refresh stable Jekyll model routes from the standalone catalogue."""
import json
from pathlib import Path

from catalogue_urls import FOLDER_BASE, RAW_BASE, repository_path

root = Path(__file__).resolve().parents[1]
docs = root / "docs"
records = json.loads((root / "data/catalogue.json").read_text())
for record in records:
    if not record.get("file"):
        continue
    cad = Path(record["file"])
    if (record.get("download") != RAW_BASE + repository_path(cad) or
            record.get("companion") != RAW_BASE + repository_path(cad.with_suffix(".md")) or
            record.get("repo_folder") != FOLDER_BASE + repository_path(cad.parent)):
        raise ValueError(f"Invalid repository links for {record['id']}; run the catalogue build")
    images = {RAW_BASE + repository_path(Path(asset)) for asset in record["package_assets"]
              if Path(asset).suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif", ".ico", ".bmp"}}
    for view in [*record["gallery"], record["preview"]]:
        if view and view["url"] not in images:
            raise ValueError(f"Invalid repository image for {record['id']}")

model_dir = docs / "models"
model_dir.mkdir(exist_ok=True)
ids = {record["id"] for record in records}
for stale in model_dir.glob("*.md"):
    if stale.stem not in ids and stale.read_text().startswith("---\n# Generated catalogue entry\n"):
        stale.unlink()
for record in records:
    model_id = record["id"]
    entry = model_dir / f"{model_id}.md"
    entry.write_text(
        f"---\n# Generated catalogue entry\nlayout: model\ntitle: CAD model\n"
        f"model_id: {model_id}\npermalink: /models/{model_id}.html\n---\n"
    )
