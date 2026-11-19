"""Read a skill directory supplied at execution. Persist corruptions only in disposable local files."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

import ezdxf

BASE = Path(__file__).resolve().parent
REPO = BASE.parents[1]


def invoke(*args, check=True):
    return subprocess.run(args,check=check,capture_output=True,text=True)


def style_case(tool, scratch):
    path = scratch/"styles.dxf"
    doc=ezdxf.new()
    doc.layers.new("Blue",dxfattribs={"color":5})
    doc.layers.new("Red",dxfattribs={"color":1})
    hidden=doc.layers.new("Hidden",dxfattribs={"color":2})
    hidden.off()
    b=doc.blocks.new("Plug")
    for color in (256,0,3):
        b.add_line((0,0),(5,0),dxfattribs={"color":color})
    inner=doc.blocks.new("Holder")
    inner.add_blockref("Plug",(0,0),dxfattribs={"color":0})
    for layer in ("Blue","Red","Hidden"):
        doc.modelspace().add_blockref("Holder",(0,0),dxfattribs={"layer":layer,"color":6})
    doc.saveas(path)
    report=json.loads(invoke(sys.executable, str(tool), str(path)).stdout)
    lines=[e for e in report["entities"] if e["type"]=="LINE"]
    for layer,colour,visible in [("Blue","#0000ff",True),("Red","#ff0000",True),("Hidden","#ffff00",False)]:
        group=[e for e in lines if e["effective_layer"]==layer]
        assert len(group)==3,(layer,group)
        got = {e["aci"]:e["display_colour"].lower() for e in group}
        assert got=={256:colour,0:"#ff00ff",3:"#00ff00"},(layer,got)
        assert all(bool(e["visible"])==visible for e in group),(layer,group)
    return {"nested_layers":3,"observed_lines":len(lines),"overrides":"PASS","hidden_inheritance":"PASS"}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("skill",type=Path)
    parser.add_argument("format_skill",type=Path)
    opt=parser.parse_args()
    tool=opt.skill.resolve()/"scripts/verify_navigation.py"
    expected=BASE/"joint-expected.json"
    with tempfile.TemporaryDirectory(dir=REPO/"_local") as folder:
        tmp=Path(folder)
        checks={}
        env=dict(os.environ,NEGATIVE_EVIDENCE_DIR=str(tmp))
        subprocess.run(["blender","-b","-t","1","--factory-startup","--disable-autoexec",
                        "--python-exit-code","1","--python",str(BASE/"clevis.py"),"--","adversarial"],
                       env=env,check=True,capture_output=True,text=True)
        for path in sorted(tmp.glob("*.json")):
            name=path.stem
            result=invoke(sys.executable,str(tool),str(expected),str(path),check=False)
            receipt=json.loads(result.stdout)
            assert result.returncode and receipt["result"]=="FAIL",(name,receipt)
            assert "spacer" in json.dumps(receipt),(name,receipt)
            checks[name]=receipt
        assert len(checks)==7
        positive=json.loads(invoke(sys.executable,str(tool),str(expected),str(BASE/"results/joint-reopened.json")).stdout)
        from tube_repair import TARGET, inventory
        import ezdxf
        tube_observed = tmp / "tube-reopened.json"
        tube_observed.write_text(json.dumps(inventory(ezdxf.readfile(TARGET))))
        repair=json.loads(invoke(sys.executable,str(tool),str(BASE/"results/tube-expected.json"),str(tube_observed)).stdout)
        fixture=opt.format_skill/"fixtures/inventory.json"
        planner=opt.format_skill/"scripts/routes.py"
        args=[sys.executable,str(planner),str(fixture),"--connection","workshop-fixture",
              "--source","step-solid","--target","stl-mesh"]
        route=json.loads(invoke(*args,"--require","physical_material").stdout)
        assert route["status"]=="GAP" and not route["routes"]
        assert any("physical_material" in reason for reason in route["reasons"])
        assert json.loads(invoke(*args,"--require","shape").stdout)["status"]=="CANDIDATE"
        styles=style_case(opt.skill/"scripts/dxf_styles.py",tmp)
    result={"assembly":positive,"repaired_tube":repair,"adversarial_readback_cases":checks,
            "drawing_inheritance":styles,"stl_material_route":route,
            "tool_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (tool,opt.skill/"scripts/dxf_styles.py")}}
    (BASE/"results/verification.json").write_text(json.dumps(result,indent=2)+"\n")


if __name__=="__main__":
    main()
