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
               description="TEXT", needs_information="BOOLEAN", text="TEXT", preview="TEXT",
               aliases="TEXT", tags="TEXT", materials="TEXT", standards="TEXT", dimensions="TEXT")
json_fields = {"preview", "aliases", "tags", "materials", "standards", "dimensions"}
preview_source = Path("data/previews").resolve()
preview_dist = dist / "previews"
if preview_dist.exists():
    shutil.rmtree(preview_dist)
for record in records:
    views = []
    for preview in record.get("previews") or []:
        relative = Path(preview["file"])
        source = (preview_source / relative).resolve()
        if not source.is_relative_to(preview_source) or source.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            raise ValueError(f"Invalid preview path for {record['id']}: {relative}")
        if not source.is_file():
            continue
        destination = preview_dist / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            shutil.copyfile(source, destination)
        views.append(dict(url="/" + destination.relative_to(dist).as_posix(), alt=preview["alt"], view=preview["view"]))
    views.sort(key=lambda entry: entry["view"].casefold() != "isometric")
    record["gallery"] = views
    record["preview"] = views[0] if views else None

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

def make_dxf():
    pairs = [(0, "SECTION"), (2, "HEADER"), (9, "$ACADVER"), (1, "AC1015"),
             (9, "$INSUNITS"), (70, 4), (0, "ENDSEC"), (0, "SECTION"), (2, "ENTITIES")]
    for points in [[(0,0),(40,0),(40,20),(0,20)], [(2,2),(38,2),(38,18),(2,18)]]:
        pairs.extend([(0,"LWPOLYLINE"), (100,"AcDbEntity"), (8,"0"), (100,"AcDbPolyline"), (90,4), (70,1)])
        for x, y in points:
            pairs.extend([(10,x),(20,y)])
    pairs.extend([(0,"ENDSEC"),(0,"EOF")])
    return "".join(f"{code}\n{value}\n" for code,value in pairs)

model_dir = dist / "models"
model_dir.mkdir(exist_ok=True)
for stale in model_dir.glob("*.html"):
    if stale.stem not in id_set:
        stale.unlink()
downloads = dist / "downloads"
downloads.mkdir(exist_ok=True)
dxf = downloads / "tube-profile.dxf"
dxf.write_text(make_dxf())
companion = dxf.with_suffix(".md")
companion.write_text(f"# Rectangular tube profile fixture\n\n2D DXF, mm. Outer profile 40 × 20 mm, wall 2 mm.\n\nSHA-256: {hashlib.sha256(dxf.read_bytes()).hexdigest()}\n\nOriginal pilot geometry. The file is a section profile. A tube length belongs to a separate extrusion.\n")

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
    for source in record.get("sources", []):
        detail.append(f'<p><a href="{html.escape(source["url"], quote=True)}">{html.escape(source["title"])}</a></p>')
    if record.get("file") == dxf.name:
        detail.append(f'<p><a href="/downloads/{dxf.name}" download>Download DXF</a> · <a href="/downloads/{companion.name}">Companion</a></p>')
    (model_dir / f'{record["id"]}.html').write_text(page(record["name"], "".join(detail)))
    subjects.setdefault(record["subject"], []).append(record)
body = []
for subject, members in sorted(subjects.items()):
    body.append(f'<h2>{html.escape(subject)}</h2><ul>')
    for record in members:
        body.append(f'<li><a href="/models/{record["id"]}.html">{html.escape(record["name"])}</a></li>')
    body.append('</ul>')
(dist / "browse.html").write_text(page("Browse CAD models", "<h2>Browse by tag</h2>" + tag_list + "<h2>Browse by subject</h2>" + "".join(body)))
