THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# frame core raised foot passages j3f

1. **Library number:** 26.
2. **Type:** group.
3. **CAD file:** [frame-core-raised-foot-passages-j3f.dwg](<frame-core-raised-foot-passages-j3f.dwg>).
4. **DWG SHA-256:** `5ab966631d0bc4bb9df46d19f1e42100e8b2c55c59a63114b3dd25a7c023ac9f`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

1. **Status:** Discussion machined-stock variant of P01J650 — raised J frame rail. Units: mm. Quantity: two identical rails per eight-foot installation.
2. **Stock geometry:** Retain the 40 × 40 × 3 mm nominal hollow section and 650 mm cut from P01J650 — stock rail. The existing native stock reference uses outside radius 6 mm and inside radius 3 mm. This variant retains those nominal modeling radii.
3. **Part datum:** Local section coordinates (u,v) occupy −20…20 mm; cut station w occupies 0…650 mm. Assembly rotation about Y by +90° and translation (−325,150,520) mm gives global X = w − 325 mm, Y = v + 150 mm, Z = 520 − u mm. The right rail uses Y translation −150 mm.
4. **Proposed machining:** Eight Ø11 mm passages along local v, at u = 0 mm and w = 60, 90, 130, 160, 490, 520, 560, 590 mm. Each passage cuts both sidewalls. The global axes are Y-directed at X = −265, −235, −195, −165, 165, 195, 235, 265 mm and Z = 520 mm. These correspond to the two axes Xc ±15 mm on each of four foot centres Xc = −250, −180, 180, 250 mm, as specified in P04JFTV — foot vertical leg.

### Nominal mating geometry and construction

1. **Wall intervals:** At the stated axis the straight outer walls lie at v = ±20 mm and the inner walls at v = ±17 mm. Proposed bounded Boolean cutters cover v = −21…−16 mm and 16…21 mm. The radius-5.5 mm bore disks stay within the straight-wall region u = −14…14 mm, so the omitted central interval contains cavity at every bore-disk point.
2. **Sleeve contact:** P04JCT34 — compression sleeve has outside diameter 14 mm, bore diameter 11 mm and length 34 mm. Its ends contact the retained inner walls v = ±17 mm. At global Z = 520 mm its end circle occupies Z = 513…527 mm inside the source nominal straight-wall interval Z = 506…534 mm. The proposed Ø11 mm rail passage leaves an annular sleeve contact area π(14²−11²)/4 = 58.904862 mm² per end, before edge deburring.
3. **External stack:** Positive-Y nominal installation retains inner washer Y = 128…130 mm, rail Y = 130…170 mm, leg Y = 170…178 mm, outer washer Y = 178…180 mm, nut Y = 180…190 mm and M10×70 screw shoulder Y = 128 mm. The right side has the corresponding proper rotated poses. Supplied hardware limits and the inboard assembly/tool sequence are retained in the foot source sheet.
4. **Manufacturing proposal:** Mark the eight source axes, drill the two walls on a controlled common axis, deburr the holes, inspect actual wall separation and fit the source sleeves before final joint assembly. Preserve the separate stock-rail model and its original frame group.
5. **Native checks:** One closed tube body; local stock bounds; nominal radius-3/radius-6 mm corners; eight projected Ø11 mm axes; sixteen actual cylindrical wall patches connecting outer ±20 mm to inner ±17 mm wall surfaces; source metadata; incremental saves; final save/reopen/hash; verified owned-document closure.
6. **Assembly scope:** Substitute this separately identified rail at the two original frame-rail transforms. Retain every other frame and deck/lifting child. Add exactly one existing eighty-occurrence foot-hardware subassembly. The hardware-only subassembly retains its separate identity and counts.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P01J650F — Left raised longitudinal rail | 1 | [Raised rail with two-hole foot passages](<../parts/mechanical/p01j650f-raised-rail-two-hole-foot-passages.md>) — 113 | `0cb6cca426a4c6f583069f166405e0c80af4bab7cbdcaabd6e3f67b06cc72d81` | `{"position_mm":[150.0,520.0,-324.99999999999994],"scale":[1.0,0.9999999999999999,0.9999999999999999],"rotation_radians":-1.5707963267948966,"normal":[1.0,0.0,6.123233995736766e-17]}` |
| P01J650F — Right raised longitudinal rail | 1 | [Raised rail with two-hole foot passages](<../parts/mechanical/p01j650f-raised-rail-two-hole-foot-passages.md>) — 113 | `0cb6cca426a4c6f583069f166405e0c80af4bab7cbdcaabd6e3f67b06cc72d81` | `{"position_mm":[-150.0,520.0,-324.99999999999994],"scale":[1.0,0.9999999999999999,0.9999999999999999],"rotation_radians":-1.5707963267948966,"normal":[1.0,0.0,6.123233995736766e-17]}` |
| P02 — Rear crossmember | 1 | [Main frame crossmember](<../parts/mechanical/p02-main-frame-crossmember-reference.md>) — 114 | `f2cd4fdf0b6f1c7b2ddc58fbbe1f9680c92ecac4fee7365acececf92c55104c2` | `{"position_mm":[305.0,520.0,-129.99999999999997],"scale":[0.9999999999999999,1.0,0.9999999999999999],"rotation_radians":3.141592653589793,"normal":[0.0,1.0,6.123233995736766e-17]}` |
| P02 — Middle crossmember | 1 | [Main frame crossmember](<../parts/mechanical/p02-main-frame-crossmember-reference.md>) — 114 | `f2cd4fdf0b6f1c7b2ddc58fbbe1f9680c92ecac4fee7365acececf92c55104c2` | `{"position_mm":[200.0,520.0,-129.99999999999997],"scale":[0.9999999999999999,1.0,0.9999999999999999],"rotation_radians":3.141592653589793,"normal":[0.0,1.0,6.123233995736766e-17]}` |
| P02JF — Narrow front crossmember | 1 | [J front narrow crossmember](<../parts/mechanical/p02jf-j-front-narrow-crossmember.md>) — 115 | `cb2075536d1391cbae7ffd5a4b1cd9ac47f711adad08933f1a2d14a025140e0e` | `{"position_mm":[-315.0,520.0,-129.99999999999997],"scale":[0.9999999999999999,1.0,0.9999999999999999],"rotation_radians":3.141592653589793,"normal":[0.0,1.0,6.123233995736766e-17]}` |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.
3. Westfield Fasteners ISO 7089 washer dimensions and tolerances.

## References — local

113. [Raised rail with two-hole foot passages](<../parts/mechanical/p01j650f-raised-rail-two-hole-foot-passages.md>) — library entry 113.
114. [Main frame crossmember](<../parts/mechanical/p02-main-frame-crossmember-reference.md>) — library entry 114.
115. [J front narrow crossmember](<../parts/mechanical/p02jf-j-front-narrow-crossmember.md>) — library entry 115.

## Views

1. [frame core raised foot passages j3f isometric](<../images/frame-core-raised-foot-passages-j3f-isometric.png>).

1. [frame core raised foot passages j3f orthographic](<../images/frame-core-raised-foot-passages-j3f-orthographic.png>).

1. [frame core raised foot passages j3f orthographic](<../images/frame-core-raised-foot-passages-j3f-orthographic.svg>).
