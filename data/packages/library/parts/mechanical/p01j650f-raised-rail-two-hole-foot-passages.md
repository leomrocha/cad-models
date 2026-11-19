THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Raised rail with two-hole foot passages

1. **Library number:** 113.
2. **Type:** part.
3. **CAD file:** [p01j650f-raised-rail-two-hole-foot-passages.dwg](<p01j650f-raised-rail-two-hole-foot-passages.dwg>).
4. **DWG SHA-256:** `0cb6cca426a4c6f583069f166405e0c80af4bab7cbdcaabd6e3f67b06cc72d81`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Raised rail with two-hole foot passages — P01J650F.

**Design status:** Discussion nominal hollow-section reference.

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

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed hollow tube body | PASS | [1, 1, 1, 1] | count |
| Section and cut-length vertex bounds | PASS | [[-20.0, 20.0], [-20.0, 20.0], [0.0, 650.0]] | mm |
| Nominal inner and outer corner radii | PASS | [3.0, 6.0] | mm |
| Source transverse bore axes | PASS | [[0.0, 60.0], [0.0, 90.0], [0.0, 130.0], [0.0, 160.0], [0.0, 490.0], [0.0, 520.0], [0.0, 560.0], [0.0, 590.0]] | mm |
| Actual rail wall bore [0, 60] side -1 | PASS | "" | mm |
| Actual rail wall bore [0, 60] side 1 | PASS | "" | mm |
| Actual rail wall bore [0, 90] side -1 | PASS | "" | mm |
| Actual rail wall bore [0, 90] side 1 | PASS | "" | mm |
| Actual rail wall bore [0, 130] side -1 | PASS | "" | mm |
| Actual rail wall bore [0, 130] side 1 | PASS | "" | mm |
| Actual rail wall bore [0, 160] side -1 | PASS | "" | mm |
| Actual rail wall bore [0, 160] side 1 | PASS | "" | mm |
| Actual rail wall bore [0, 490] side -1 | PASS | "" | mm |
| Actual rail wall bore [0, 490] side 1 | PASS | "" | mm |
| Actual rail wall bore [0, 520] side -1 | PASS | "" | mm |
| Actual rail wall bore [0, 520] side 1 | PASS | "" | mm |
| Actual rail wall bore [0, 560] side -1 | PASS | "" | mm |
| Actual rail wall bore [0, 560] side 1 | PASS | "" | mm |
| Actual rail wall bore [0, 590] side -1 | PASS | "" | mm |
| Actual rail wall bore [0, 590] side 1 | PASS | "" | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.
3. Westfield Fasteners ISO 7089 washer dimensions and tolerances.
4. standard fastener geometry sources.

## References — local

112. [Raised J frame longitudinal rail](<p01j650-raised-j-frame-longitudinal-rail.md>) — library entry 112.
121. [M10 deck/lift foot compression sleeve](<p04jct34-j-foot-m10-rail-compression-sleeve.md>) — library entry 121.
123. [Raised deck two-hole outrigger vertical leg](<p04jftv-j-outboard-foot-vertical-leg.md>) — library entry 123.
