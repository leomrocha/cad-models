"""Refresh generated Jekyll data, model entries and static assets from dist."""
import json
import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[1]
dist = root / "dist"
docs = root / "docs"
records = json.loads((dist / "data/catalogue.json").read_text())
for name in ("data", "vendor", "downloads", "previews"):
    source, target = dist / name, docs / name
    if target.exists():
        shutil.rmtree(target)
    if source.is_dir():
        shutil.copytree(source, target)
for name in ("app.mjs", "sqlite-worker.mjs", "engine.mjs", "style.css"):
    shutil.copyfile(dist / name, docs / name)
model_dir = docs / "models"
model_dir.mkdir(exist_ok=True)
ids = {record["id"] for record in records}
for stale in model_dir.glob("*.md"):
    if stale.stem not in ids and stale.read_text().startswith("---\n# Generated catalogue entry\n"):
        stale.unlink()
for record in records:
    model_id = record["id"]
    gallery = []
    for preview in record.get("previews") or []:
        path = Path("previews") / preview["file"]
        if (dist / path).is_file():
            gallery.append(dict(preview, url="/" + path.as_posix()))
    record["gallery"] = sorted(gallery, key=lambda view: view["view"].casefold() != "isometric")
    if record.get("file"):
        path = Path("downloads") / record["file"]
        if (dist / path).is_file():
            record["download"] = "/" + path.as_posix()
            companion = path.with_suffix(".md")
            if (dist / companion).is_file():
                record["companion"] = "/" + companion.as_posix()
    title = json.dumps(record["name"], ensure_ascii=False)
    entry = model_dir / f"{model_id}.md"
    entry.write_text(
        f"---\n# Generated catalogue entry\nlayout: model\ntitle: {title}\n"
        f"model_id: {model_id}\npermalink: /models/{model_id}.html\n---\n"
    )

metadata = docs / "_data"
metadata.mkdir(exist_ok=True)
(metadata / "catalogue.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
guide = (root / "CONTRIBUTING.md").read_text()
(docs / "contributing.md").write_text(
    "---\nlayout: default\ntitle: Contribute to CAD Models\npermalink: /contributing.html\n---\n\n"
    + guide.removeprefix("# Contribute to CAD Models\n\n")
)
