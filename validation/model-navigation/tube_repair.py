"""Repair the existing public tube profile in a distinct DXF and compare its entities."""
import hashlib
from collections import Counter
from pathlib import Path
import sys

import ezdxf
from PIL import Image, ImageDraw

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parents[1] / 'data/packages/models/mechanical-parts/profiles/rectangular-tubes/tube-profile/tube-profile.dxf'
TARGET = BASE / "models/tube-profile-organised.dxf"
APP = "PROFILE_NAV"
SCHEDULE = {
    (40, 20): ("outer", "Outer profile", "outside", "Outer profile", 5),
    (36, 16): ("bore", "Internal opening", "opening", "Internal opening", 2),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def geometry(document):
    return [(e.dxftype(), e.closed, tuple(e.get_points("xyseb")),
             tuple(e.dxf.extrusion), e.dxf.elevation) for e in document.modelspace()]


def proposal(document):
    entities = list(document.modelspace())
    plans = []
    for e in entities:
        if e.dxftype() != "LWPOLYLINE" or not e.closed:
            raise ValueError("Unknown contour type")
        xs, ys = zip(*e.vertices())
        size = max(xs)-min(xs), max(ys)-min(ys)
        if size not in SCHEDULE:
            raise ValueError("Unknown contour size")
        plans.append((e,SCHEDULE[size]))
    if Counter(p[0] for _,p in plans) != Counter(p[0] for p in SCHEDULE.values()):
        raise ValueError("Ambiguous contour occurrence; identify the intended contour")
    return plans


def apply(document):
    plans = proposal(document)
    if APP not in document.appids:
        document.appids.new(APP)
    for entity, (identity, label, role, layer, colour) in plans:
        if layer not in document.layers:
            document.layers.new(layer, dxfattribs={"color": colour})
        entity.dxf.layer = layer
        entity.set_xdata(APP, [(1000,s) for s in (identity,label,role)])


def inventory(document):
    rows = []
    for e in document.modelspace():
        identity,label,role = [record.value for record in e.get_xdata(APP)]
        rows.append(dict(id=identity,label=label,definition=identity,parent=None,
            role=role,layer=e.dxf.layer,display_colour=document.layers.get(e.dxf.layer).color,
            physical_material=None))
    return {"objects": rows}


def preview(document, name):
    image = Image.new("RGB",(640,420),(247,247,244))
    draw = ImageDraw.Draw(image)
    for e in document.modelspace():
        pts=[(40+14*x,345-14*y) for x,y in e.vertices()]
        colour={"0":"#363c42","Outer profile":"#285f91","Internal opening":"#a06400"}[e.dxf.layer]
        draw.line(pts+[pts[0]],fill=colour,width=5)
    image.save(BASE/"models"/(name+".png"))


def run():
    original_hash = digest(SOURCE)
    original = ezdxf.readfile(SOURCE)
    assert len(original.modelspace().query('LWPOLYLINE[layer=="0"]')) == 2
    assert not any(e.has_xdata(APP) for e in original.modelspace())
    old = geometry(original)
    if "--build" in sys.argv:
        if TARGET.exists():
            raise FileExistsError(TARGET)
        derived = ezdxf.readfile(SOURCE)
        apply(derived)
        derived.saveas(TARGET)
    reopened = ezdxf.readfile(TARGET)
    assert not reopened.audit().errors
    assert geometry(reopened)==old and reopened.units==original.units==4
    rows = inventory(reopened)
    expected = [{"id":v[0],"definition":v[0],"parent":None,"label":v[1],"role":v[2],
                 "layer":v[3],"display_colour":v[4],"physical_material":None} for v in SCHEDULE.values()]
    assert rows["objects"]==expected
    for row in expected:
        matches = list(reopened.modelspace().query(f'LWPOLYLINE[layer=="{row["layer"]}"]'))
        assert len(matches)==1 and matches[0].get_xdata(APP)[0].value==row['id']
    apply(reopened)
    assert inventory(reopened)==rows and geometry(reopened)==old
    negative = ezdxf.readfile(SOURCE)
    e = list(negative.modelspace())[0]
    negative.modelspace().add_lwpolyline(list(e.vertices()),close=True)
    try:
        apply(negative)
    except ValueError as exc:
        assert "Ambiguous" in str(exc)
    else:
        raise AssertionError("Duplicate contour must require clarification")
    assert all(o.dxf.layer=="0" and not o.has_xdata(APP) for o in negative.modelspace())
    assert digest(SOURCE)==original_hash
    preview(original,"tube-before")
    preview(reopened,"tube-after")
    print("PASS: real original two contours both on layer 0; separately selectable named layers after repair; all vertices/widths/bulges/closed flags/normals/elevations/units unchanged; ambiguous duplicate refused; repeat semantic equality; original SHA-256",original_hash)


if __name__=="__main__":
    run()
