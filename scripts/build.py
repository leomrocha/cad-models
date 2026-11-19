"""Build both browser datasets from the same JSON export."""
import hashlib
import html
import json
import re
import shutil
import sqlite3
import subprocess
from pathlib import Path
from urllib.parse import quote_plus

import duckdb

from catalogue_urls import FOLDER_BASE, RAW_BASE, repository_path

dist = Path("dist")
data = dist / "data"
records = json.loads((data / "catalogue.json").read_text())
ids = [record["id"] for record in records]
id_set = set(ids)
assert len(ids) == len(set(ids))
assert all(re.fullmatch(r"[a-z0-9-]+", model_id) for model_id in ids)
assert all(isinstance(record["tags"], list) and record["name"] and record["subject"] for record in records)
for column in ("materials", "standards", "dimensions"):
    assert all(record[column] is None or isinstance(record[column], list) for record in records)

columns = dict(id="TEXT PRIMARY KEY", name="TEXT", subject="TEXT", kind="TEXT",
               description="TEXT", category_path="TEXT", needs_information="BOOLEAN", text="TEXT", preview="TEXT",
               aliases="TEXT", tags="TEXT", materials="TEXT", standards="TEXT", dimensions="TEXT")
json_fields = {"preview", "aliases", "tags", "materials", "standards", "dimensions"}
package_source = Path("data/packages").resolve()
cad_formats = {".dwg", ".dxf", ".step", ".stp", ".iges", ".igs", ".stl", ".obj",
               ".3mf", ".blend", ".fcstd", ".brep", ".ifc", ".glb", ".gltf"}
image_formats = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif", ".ico", ".bmp"}
asset_paths = set()
hashes = {}

def prepare_assets(record):
    model = record["id"]
    assets = [Path(asset) for asset in record.get("package_assets", [])]
    views = record.get("previews") or []
    record.update(download=None, companion=None, repo_folder=None, gallery=[], preview=None)
    if not record.get("file"):
        if assets or views:
            raise ValueError(f"Assets require a CAD file for {model}")
        return
    native = Path(record["file"])
    companion = native.with_suffix(".md")
    if (native.suffix.lower() not in cad_formats or native not in assets or
            companion not in assets or not native.is_relative_to("models")):
        raise ValueError(f"Expected a CAD file and same-basename companion for {model}")
    for asset in assets:
        source = package_source / asset
        if (asset.parent != native.parent or asset.is_absolute() or ".." in asset.parts or
                source.resolve() != source or not source.is_file() or
                (asset != native and asset.suffix.lower() not in (image_formats | {".md"}))):
            raise ValueError(f"Invalid asset path for {model}: {asset}")
        if asset in asset_paths:
            raise ValueError(f"Asset listed more than once: {asset}")
        with source.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").digest()
        if digest in hashes:
            raise ValueError(f"Duplicate asset bytes: {hashes[digest]} and {asset} ({model})")
        hashes[digest] = asset
        asset_paths.add(asset)

    def image_url(value):
        path = Path(value)
        if path not in assets or path.suffix.lower() not in image_formats:
            raise ValueError(f"Invalid image for {model}: {path}")
        return RAW_BASE + repository_path(path)

    record["download"] = RAW_BASE + repository_path(native)
    record["companion"] = RAW_BASE + repository_path(companion)
    record["repo_folder"] = FOLDER_BASE + repository_path(native.parent)
    for view in sorted(views, key=lambda entry: entry["view"].casefold() != "isometric"):
        gallery_entry = dict(url=image_url(view["file"]), alt=view["alt"], view=view["view"])
        record["gallery"].append(gallery_entry)
        thumbnail = view.get("thumbnail_file")
        thumbnail_url = image_url(thumbnail) if thumbnail else gallery_entry["url"]
        if record["preview"] is None:
            record["preview"] = dict(gallery_entry, url=thumbnail_url)

for record in records:
    record.setdefault("category_path", None)
    prepare_assets(record)

actual_paths = {path.relative_to(package_source) for path in package_source.rglob("*")
                if path.is_file() or path.is_symlink()}
if actual_paths != asset_paths:
    raise ValueError(f"Unlisted model assets: {sorted(actual_paths - asset_paths)}")
for output in (dist, Path("docs")):
    for retired in ("downloads", "previews"):
        if (output / retired).exists():
            raise ValueError(f"Remove the retired asset tree: {output / retired}")
    for copied in output.rglob("*"):
        if copied.is_file() and copied.suffix.lower() in (cad_formats | image_formats):
            raise ValueError(f"Model or image in site output: {copied}")

(data / "catalogue.json").write_text(json.dumps(records, ensure_ascii=False))

values = [
    tuple(json.dumps(record[column], ensure_ascii=False) if column in json_fields and record[column] is not None
          else record[column] for column in columns)
    for record in records
]
schema = ", ".join(f"{name} {kind}" for name, kind in columns.items())
insert = "INSERT INTO models VALUES (" + ", ".join("?" for _ in columns) + ")"
facets = []
for record in records:
    model = record["id"]
    for field in ("subject", "kind"):
        facets.append((model, field, record[field].casefold()))
    for field in ("aliases", "tags"):
        facets.extend((model, field, value.casefold()) for value in record[field])
    for field, key in (("materials", "name"), ("standards", "designation"), ("dimensions", "value")):
        if record[field] is not None:
            facets.extend((model, field, entry[key].casefold()) for entry in record[field])
facet_schema = "CREATE TABLE facets (model TEXT, field TEXT, value TEXT)"
facet_insert = "INSERT INTO facets VALUES (?, ?, ?)"
(data / "catalogue.sqlite").unlink(missing_ok=True)
with sqlite3.connect(data / "catalogue.sqlite") as db:
    db.execute(f"CREATE TABLE models ({schema})")
    db.executemany(insert, values)
    db.execute(facet_schema)
    db.executemany(facet_insert, facets)
    db.execute("CREATE VIRTUAL TABLE keyword USING fts5(id UNINDEXED, text)")
    db.execute("INSERT INTO keyword SELECT id, text FROM models")
    assert db.execute("SELECT count(*) FROM keyword").fetchone()[0] == len(records)

with duckdb.connect() as db:
    db.execute(f"CREATE TABLE models ({schema})")
    db.executemany(insert, values)
    db.execute(facet_schema)
    db.executemany(facet_insert, facets)
    db.execute(f"COPY models TO '{(data / 'catalogue.parquet').as_posix()}' (FORMAT PARQUET)")
    db.execute(f"COPY facets TO '{(data / 'facets.parquet').as_posix()}' (FORMAT PARQUET)")
    assert db.execute("SELECT count(*) FROM models").fetchone()[0] == len(records)

for source, files, target in [
    ("@sqlite.org/sqlite-wasm", ["index.mjs", "sqlite3.wasm"], "sqlite"),
    ("@duckdb/duckdb-wasm", ["duckdb-browser.mjs", "duckdb-browser-eh.worker.js", "duckdb-eh.wasm"], "duckdb"),
]:
    folder = dist / "vendor" / target
    folder.mkdir(parents=True, exist_ok=True)
    for file in files:
        shutil.copy(Path("node_modules") / source / "dist" / file, folder)
    for license_file in (Path("node_modules") / source).glob("LICENSE*"):
        shutil.copy(license_file, folder)

# Preserve notices for dependencies bundled into the browser module.
for package, filename in (
    ("apache-arrow", "LICENSE.txt"),
    ("apache-arrow", "NOTICE.txt"),
    ("flatbuffers", "LICENSE"),
    ("tslib", "LICENSE.txt"),
):
    shutil.copyfile(
        Path("node_modules") / package / filename,
        dist / "vendor" / "duckdb" / f"{package}-{filename}",
    )

subprocess.run(["node_modules/.bin/esbuild", "node_modules/@duckdb/duckdb-wasm/dist/duckdb-browser.mjs", "--bundle", "--format=esm", "--platform=browser", "--minify", "--legal-comments=inline", "--outfile=dist/vendor/duckdb/duckdb-browser.mjs"], check=True)

shutil.copyfile("CONTRIBUTING.md", dist / "contributing.md")

for file in Path("src").iterdir():
    shutil.copy(file, dist)

tags = sorted({tag for record in records for tag in record["tags"]}, key=str.casefold)
tag_list = '<ul class="tag-list" aria-label="Catalogue tags">' + "".join(
    f'<li><a href="./?tag={quote_plus(tag)}" data-tag="{html.escape(tag, quote=True)}">{html.escape(tag)}</a></li>'
    for tag in tags
) + '</ul>'
home = dist / "index.html"
home.write_text(home.read_text().replace("<!-- catalogue-tags -->", tag_list))

def page(title, body):
    return f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>{html.escape(title)}</title><link rel="stylesheet" href="/style.css"><main><nav><a href="/">Search</a> · <a href="/browse.html">Browse</a> · <a href="/manual.html">Manual</a></nav><h1>{html.escape(title)}</h1>{body}</main></html>'

model_dir = dist / "models"
model_dir.mkdir(exist_ok=True)
for stale in model_dir.glob("*.html"):
    if stale.stem not in id_set:
        stale.unlink()

subjects = {}
for record in records:
    get = lambda key: html.escape(str(record[key]))
    detail = [f'<p>{get("description")}</p><p>{get("state")}</p>']
    if record["gallery"]:
        detail.append('<h2>Preview views</h2><div class="gallery">')
        for preview in record["gallery"]:
            url = html.escape(preview["url"], quote=True)
            alt = html.escape(preview["alt"], quote=True)
            view = html.escape(preview["view"])
            detail.append(f'<figure><a href="{url}"><img src="{url}" alt="{alt}" loading="lazy"></a><figcaption>{view}</figcaption></figure>')
        detail.append('</div>')
    for key in ("tags","materials","standards","dimensions"):
        if record[key] is not None:
            detail.append(f'<h2>{key.title()}</h2><ul>')
            for value in record[key]:
                text = " · ".join(value.values()) if isinstance(value, dict) else value
                detail.append(f'<li>{html.escape(text)}</li>')
            detail.append('</ul>')
    if record["download"]:
        folder, native, companion = (get(key) for key in ("repo_folder", "download", "companion"))
        detail.append(f'<p><a href="{folder}">Model folder on GitHub</a> · '
                      f'<a href="{native}">Download CAD file</a> · <a href="{companion}">Companion</a></p>')
    (model_dir / f'{record["id"]}.html').write_text(page(record["name"], "".join(detail)))
    subjects.setdefault(record["subject"], []).append(record)
body = []
for subject, members in sorted(subjects.items()):
    body.append(f'<h2>{html.escape(subject)}</h2><ul>')
    for record in members:
        body.append(f'<li><a href="/models/{record["id"]}.html">{html.escape(record["name"])}</a></li>')
    body.append('</ul>')
(dist / "browse.html").write_text(page("Browse CAD models", "<h2>Browse by tag</h2>" + tag_list + "<h2>Browse by subject</h2>" + "".join(body)))
