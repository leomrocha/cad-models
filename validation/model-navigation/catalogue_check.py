"""Build and search a draft dataset in a new owner-local build directory."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
entries=[]
for path in sorted((BASE/"drafts").glob("*.json")):
    d=json.loads(path.read_text())
    subprocess.run([sys.executable,"scripts/intake.py","check",str(path)],cwd=ROOT,check=True)
    assert hashlib.sha256((ROOT/d["model_file"]).read_bytes()).hexdigest()==d["sha256"]
    for dependency in d.get("dependencies",[]):
        part=json.loads((BASE/"drafts"/(dependency["draft"]+".json")).read_text())
        assert dependency["sha256"]==part["sha256"]
    entries.append(dict(id=d.get("draft_id","draft-"+path.stem),name=d["title"],
       subject=d["subject"],kind="Assembly" if path.stem=="joint" else "Part",
       description=d["description"],tags=d["tags"],aliases=[],materials=None,standards=None,
       dimensions=None,needs_information=True,state="Local draft",previews=d["previews"]))
with tempfile.TemporaryDirectory(dir=ROOT/"_local") as tmp:
    build=Path(tmp)
    data=build/"data"
    data.mkdir()
    (data/"pilot.json").write_text(json.dumps(entries))
    (data/"previews").symlink_to(ROOT/"data/previews",target_is_directory=True)
    for item in ("src","node_modules","CONTRIBUTING.md"):
        (build/item).symlink_to(ROOT/item)
    subprocess.run(["node",str(ROOT/"scripts/export.mjs")],cwd=build,check=True)
    subprocess.run([sys.executable,str(ROOT/"scripts/build.py")],cwd=build,check=True)
    queries={}
    for engine in ("sqlite","duckdb"):
        for query,expected in (("draft-body","draft-body"),("draft-joint","draft-joint"),
                               ("plain-washer-10p5-20-2","plain-washer-10p5-20-2")):
            cmd=[sys.executable,str(ROOT/"scripts/search.py"),"--engine",engine,
                 "--data",str(build/"dist/data"),query]
            hits=json.loads(subprocess.check_output(cmd,cwd=ROOT))
            assert any(r["id"]==expected for r in hits),(engine,query,hits)
            queries[engine+" "+query]=[r["id"] for r in hits]
        material_cmd=[sys.executable,str(ROOT/"scripts/search.py"),"--engine",engine,
                      "--data",str(build/"dist/data"),"--filter","materials","steel"]
        assert json.loads(subprocess.check_output(material_cmd,cwd=ROOT)) == []
        queries[engine+" material=steel"]=[]
    (BASE/"results/catalogue.json").write_text(json.dumps(queries,indent=2)+"\n")
