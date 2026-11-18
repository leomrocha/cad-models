"""Blender background runner: blender -b -P clevis.py -- build|check|views."""
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

BASE = Path(__file__).resolve().parent
MODELS = BASE / "models"
RESULTS = BASE / "results"
IMAGES = BASE.parents[1] / "data/previews/model-navigation"
ROOT_ID = "clevis-joint"
SPECS = {
    "body": ("Fork body", "yoke", "Structure", (0.18, 0.48, 0.70), (30, 20, 22)),
    "pin": ("Plain pin", "pivot", "Pivot", (0.72, 0.57, 0.28), (6, 24, 6)),
    "spacer": ("Spacing ring", "spacer", "Spacers", (0.68, 0.76, 0.79), (10, 2, 10)),
}


def clear():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.001
    scene.unit_settings.length_unit = "MILLIMETERS"


def box(dims, center):
    bpy.ops.mesh.primitive_cube_add(size=1, location=center)
    obj = bpy.context.object
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return obj


def cylinder(diameter, depth, center=(0, 0, 0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=diameter / 2,
        depth=depth, location=center, rotation=(math.pi/2, 0, 0))
    obj = bpy.context.object
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    return obj


def boolean(obj, tool, operation):
    mod = obj.modifiers.new(operation, "BOOLEAN")
    mod.operation = operation
    mod.object = tool
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(tool, do_unlink=True)


def part(key):
    if key == "body":
        obj = box((30, 20, 4), (0, 0, 2))
        for y in (-8, 8):
            lug = box((16, 4, 19), (0, y, 12.5))
            boolean(obj, lug, "UNION")
        boolean(obj, cylinder(6.4, 30, (0, 0, 15)), "DIFFERENCE")
        bpy.context.scene.cursor.location = (0, 0, 0)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.select_all(action="DESELECT")
        obj.select_set(True)
        bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    elif key == "pin":
        obj = cylinder(6, 24)
    else:
        obj = cylinder(10, 2)
        boolean(obj, cylinder(6.4, 4), "DIFFERENCE")
    obj.data.name = SPECS[key][0] + " geometry"
    return obj


def collection(name):
    group = bpy.data.collections.get(name)
    if group is None:
        group = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(group)
    return group


def assign(obj, key, identity, label, parent=None):
    _, role, layer, rgb, _ = SPECS[key]
    obj.name = label
    obj["id"] = identity
    obj["definition"] = key
    obj["role"] = role
    obj["tags"] = [role, "mechanical"]
    obj.color = (*rgb, 1)
    obj.parent = parent
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    collection(layer).objects.link(obj)


def save(name):
    path = MODELS / (name + ".blend")
    if path.exists():
        raise FileExistsError(path)
    bpy.ops.wm.save_as_mainfile(filepath=str(path), compress=True)


def build():
    for key in SPECS:
        clear()
        assign(part(key), key, key, SPECS[key][0])
        save(key)
    clear()
    root = bpy.data.objects.new("Clevis joint", None)
    collection("Assembly").objects.link(root)
    root["id"], root["definition"], root["role"] = ROOT_ID, ROOT_ID, "assembly"
    for key in SPECS:
        # Import the actual standalone definition; both ring occurrences share mesh data.
        with bpy.data.libraries.load(str(MODELS/(key + ".blend")), link=False) as (src, dst):
            dst.objects = [SPECS[key][0]]
        obj = dst.objects[0]
        assign(obj, key, key if key != "spacer" else "spacer-left",
               SPECS[key][0] if key != "spacer" else "Left spacing ring", root)
        if key != "body":
            obj.location = (0, -5 if key == "spacer" else 0, 15)
        if key == "spacer":
            other = obj.copy()
            assign(other, key, "spacer-right", "Right spacing ring", root)
            other.location = (0, 5, 15)
    save("joint")


def inventory():
    rows = []
    for o in bpy.context.scene.objects:
        rows.append(dict(id=o["id"], definition=o["definition"],
            parent=o.parent["id"] if o.parent else None,
            label=o.name, role=o["role"], layer=o.users_collection[0].name,
            position=[round(v, 6) for v in o.location],
            display_colour=[round(v, 3) for v in o.color][:3],
            tags=list(o.get("tags", [])), physical_material=o.get("physical_material")))
    return {"objects": sorted(rows, key=lambda r: r["id"])}


def check():
    for key, spec in SPECS.items():
        bpy.ops.wm.open_mainfile(filepath=str(MODELS/(key+".blend")), use_scripts=False)
        obj, = [o for o in bpy.context.scene.objects if o["role"]==spec[1]]
        assert obj["id"] == key and obj.name == spec[0]
        assert all(abs(x-y)<1e-4 for x,y in zip(obj.dimensions,spec[4]))
        assert abs(bpy.context.scene.unit_settings.scale_length-.001)<1e-9
    bpy.ops.wm.open_mainfile(filepath=str(MODELS/"joint.blend"), use_scripts=False)
    data = inventory()
    by_id = {o["id"]: o for o in bpy.context.scene.objects}
    left, right = (by_id[k] for k in ("spacer-left", "spacer-right"))
    assert left.data == right.data and left.parent == right.parent
    assert not bpy.data.libraries and not any(i.filepath for i in bpy.data.images)
    bpy.ops.object.select_all(action="DESELECT")
    right.select_set(True)
    assert list(bpy.context.selected_objects) == [right]
    right.hide_set(True)
    assert left.visible_get() and not right.visible_get()
    right.hide_set(False)
    assert right.visible_get()
    expected=json.loads((BASE/"joint-expected.json").read_text())
    assert len(expected["objects"]) == len(data["objects"])
    for row in expected["objects"]:
        actual=next(r for r in data["objects"] if r["id"] == row["id"])
        assert all(v==actual[k] for k,v in row.items()), (row,actual)
    (RESULTS/"joint-reopened.json").write_text(json.dumps(data,indent=2)+"\n")
    print("PASS: dimensions, units, embedded definitions, parentage, four placements, native selection and visibility")


def render(name, direction, center, size):
    scene = bpy.context.scene
    cam = bpy.data.cameras.new("Validation view")
    obj = bpy.data.objects.new("Validation view", cam)
    scene.collection.objects.link(obj)
    scene.camera = obj
    position = Vector(direction).normalized()*90 + Vector(center)
    obj.location = position
    obj.rotation_euler = (Vector(center)-position).to_track_quat("-Z","Y").to_euler()
    cam.type = "ORTHO"
    cam.ortho_scale = size
    scene.render.engine="BLENDER_WORKBENCH"
    shading=scene.display.shading
    shading.light="STUDIO"
    shading.color_type="OBJECT"
    shading.show_shadows=True
    shading.show_cavity=True
    shading.background_type="WORLD"
    scene.world=bpy.data.worlds.new("Neutral background")
    scene.world.color=(.08,.09,.10)
    scene.render.resolution_x=640
    scene.render.resolution_y=480
    scene.render.resolution_percentage=100
    scene.render.filepath=str(IMAGES/(name+".png"))
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(obj,do_unlink=True)


def views():
    for key in SPECS:
        bpy.ops.wm.open_mainfile(filepath=str(MODELS/(key+".blend")), use_scripts=False)
        center=(0,0,11) if key=="body" else (0,0,0)
        for suffix,direction in [("iso",(1,-1,.7)),("face",(0,-1,0))]:
            render(key+"-"+suffix,direction,center,1.65*max(SPECS[key][4]))
    bpy.ops.wm.open_mainfile(filepath=str(MODELS/"joint.blend"), use_scripts=False)
    render("joint-iso",(1,-1,.7),(0,0,10),50)
    render("joint-top",(0,-.001,1),(0,0,10),50)
    bpy.data.collections["Structure"].hide_render=True
    render("joint-pivot-spacers",(1,-1,.7),(0,0,10),50)


def damaged_revisions():
    import tempfile
    import os
    output = Path(os.environ["NEGATIVE_EVIDENCE_DIR"])
    mutations = {
        "duplicate occurrence": lambda o: o.__setitem__("id","spacer-right"),
        "wrong layer": lambda o: move_layer(o),
        "wrong physical material": lambda o: o.__setitem__("physical_material","steel"),
        "moved occurrence": lambda o: setattr(o,"location",(0,-3,15)),
        "broken definition": lambda o: o.__setitem__("definition","missing"),
        "swapped appearance": lambda o: setattr(o,"color",(*SPECS["body"][3],1)),
        "incorrect label": lambda o: setattr(o,"name","Wrong ring label"),
    }
    def move_layer(o):
        for c in list(o.users_collection):
            c.objects.unlink(o)
        collection("Structure").objects.link(o)
    with tempfile.TemporaryDirectory(dir=output) as tmp:
        for name, mutate in mutations.items():
            bpy.ops.wm.open_mainfile(filepath=str(MODELS/"joint.blend"),use_scripts=False)
            mutate(bpy.data.objects["Left spacing ring"])
            path=Path(tmp)/(name+".blend")
            bpy.ops.wm.save_as_mainfile(filepath=str(path),compress=True)
            bpy.ops.wm.open_mainfile(filepath=str(path),use_scripts=False)
            (output/(name+".json")).write_text(json.dumps(inventory(),indent=2)+"\n")


if __name__ == "__main__":
    {"build": build, "check": check, "views": views, "adversarial": damaged_revisions}[sys.argv[-1]]()
