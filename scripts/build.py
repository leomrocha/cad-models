"""Build both browser datasets from the same JSON export."""
import hashlib
import json
import re
import sqlite3
from pathlib import Path

import duckdb

from catalogue_urls import FOLDER_BASE, RAW_BASE, repository_path

data = Path("data")
records = json.loads((data / "pilot.json").read_text())
for record in records:
    record.pop("sources", None)
    record["text"] = " ".join([record["name"], record["description"], *record["tags"], *record["aliases"]])
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
site = Path("docs")
for retired in ("downloads", "previews", "data", "_data"):
    if (site / retired).exists():
        raise ValueError(f"Remove the retired site tree: {site / retired}")
for copied in site.rglob("*"):
    if copied.is_file() and copied.suffix.lower() in (cad_formats | image_formats | {".sqlite", ".parquet"}):
        raise ValueError(f"Catalogue asset in site source: {copied}")

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
