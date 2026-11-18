"""Generate and reopen an analytic nominal plain ring from explicit millimetre dimensions."""
import hashlib
import json
import math
from pathlib import Path
import sys

import cadquery as cq

BASE = Path(__file__).resolve().parent
TARGET = BASE/"models/plain-washer-10p5-20-2.step"
if "--build" in sys.argv:
    if TARGET.exists():
        raise FileExistsError(TARGET)
    ring=cq.Workplane("XY").circle(10).circle(5.25).extrude(2)
    assembly=cq.Assembly(name="Plain_washer")
    assembly.add(ring,name="Washer_10p5_20_2")
    assembly.export(str(TARGET),exportType="STEP",mode="default")
shape=cq.importers.importStep(str(TARGET)).val()
assert len(shape.Solids())==1
box=shape.BoundingBox()
assert all(math.isclose(x,y,abs_tol=1e-6) for x,y in zip(
    (box.xmin,box.xmax,box.ymin,box.ymax,box.zmin,box.zmax),(-10,10,-10,10,0,2)))
radii=sorted(f._geomAdaptor().Cylinder().Radius() for f in shape.Faces() if f.geomType()=="CYLINDER")
assert radii==[5.25,10]
assert math.isclose(shape.Volume(),math.pi*(10**2-5.25**2)*2,rel_tol=1e-9)
print(json.dumps({"id":"plain-washer-10p5-20-2","sha256":hashlib.sha256(TARGET.read_bytes()).hexdigest(),
   "file":TARGET.name,"axis":"Z","outside_mm":20,"inside_mm":10.5,"thickness_mm":2,
   "z_bounds_mm":[box.zmin,box.zmax],"volume_mm3":shape.Volume(),"solid_count":1,"result":"PASS"},indent=2))
