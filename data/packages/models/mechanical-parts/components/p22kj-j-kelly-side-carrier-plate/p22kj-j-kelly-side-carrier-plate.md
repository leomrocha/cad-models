THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# J Kelly side carrier plate

1. **Library number:** 188.
2. **Type:** part.
3. **CAD file:** [p22kj-j-kelly-side-carrier-plate.dwg](<p22kj-j-kelly-side-carrier-plate.dwg>).
4. **DWG SHA-256:** `52824c27923ef18b3b6e9d57cced5588d012be3ea1485cb6c4e9df7ebb561fdf`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** J Kelly side carrier plate — P22KJ.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 2 per J controller pair. Assembly/reference family:P22Kelly. Repeated identical pieces use instances.

### Geometry, datum and interfaces

Proposed full 3 mm Kelly frame carrier 234 X×188 Z, centre X−30,Z 574: X−147…87,Z 480…668. Left Y 197…200, right mirrored. Four independent frame holesØ6.6 at X−137/77,Z 490/658. Source controller 174×128 mounting pitch gives source axes X−117/57,Z 510/638; preserve sourceØ10 openings and exact bolt stack. Source controller body 194×148 at X−127…67,Z 500…648, thermal face Y 200; carrier lowest 480 exceeds expanded tyre crown 471 by 9. Post/contact plane Y 197 supports carrier inner face. All frame holes are 20 mm from nearest source hole along X and 20 in Z where corners differ; actual socket/washer sweeps remain source parts.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

### Through-rail attachment — access-hole correction proposal

1. **Carrier openings:** add two Ø6.6 mm holes at assembly (X,Z) = (−137,520) and (77,520) mm, axes along Y. These align with the existing rail-gap-post axes. Retain the four carrier-end holes at Z = 490/658 mm and the separate controller source pattern. Both side carriers retain X centre −30 mm; the right installation mirrors Y.
2. **Clamp path:** the left bolt passes rail Y = 130…170 mm, P22SP7 gap spacer 170…177 mm, P22KJR post 177…197 mm and this carrier 197…200 mm. Total external grip is 40+7+20+3 = 70 mm. P22CT34 spans rail inner walls 133…167 mm; P22CT14 spans post inner walls 179…195 mm. Both sleeves contact the inside walls and transmit clamp force through the hollow sections.
3. **Proposed hardware:** M6×85 ISO 4017 class 8.8 bolt, two M6 plain washers and one M6 nylon-insert nut per rail/post/carrier axis. There are two axes per controller and four across both controllers. The audit assumes 1.6 mm washer thickness, 4 mm head height, 6 mm nut height and 1 mm thread pitch. Minimum under-head length with two exposed pitches is 70+2×1.6+6+2 = 81.2 mm. The 85 mm candidate leaves 5.8 mm beyond the assumed nut. Source dimensions and offered lengths are being checked separately.
4. **Nominal left axial bounds:** head Y = 124.4…128.4 mm, inner washer 128.4…130 mm, grip 130…200 mm, outer washer 200…201.6 mm, nut 201.6…207.6 mm and bolt tip 213.4 mm. The retained 12 mm assumed washer diameter gives 4 mm lateral gap from each frame-hole washer to the controller body. Motor end Y = 115 mm to head start gives 9.4 mm. These are static nominal component screens; actual tools use their source dimensions and an insertion path.
5. **Installation sequence:** fit the internal rail sleeves before rail-end closure. Align the post, gap spacer and carrier; insert the inboard bolts and tighten the outboard nuts before installing the controller on its separate source holes. The bolt heads remain accessible during this sequence. For service, remove the controller first when its body obstructs the required tool sweep. Record actual socket outside diameter/depth and positive insertion clearance for both mirrored installations.
6. **Basis:** the existing carrier, P22KJR — frame upright, P22SP7 — gap spacer, P22CT14 — post sleeve and P22CT34 — rail sleeve. Custom holes and the hardware stack are discussion proposals. The closed clamp path replaces the earlier unperforated carrier at the rail-bolt exit.


### Source-limit 70 mm clamp proposal

Use C132 — ISO 4017 M6×85 screw, proposed class 8.8, two C146 — ISO 7089 M6 plain washer, proposed 200 HV and one C152 — DIN 985 M6 nylon-insert nut, proposed class 8 at each rail/post/carrier axis. Four axes across the controller pair give4 bolts,8 washers and4 nuts. Westfield WF40730 lists the M6×85 fully threaded class8.8 product; Böllhoff's separate M6 grid ends at60 mm. The two source-independent carrier access holes at Z520 close the existing70 mm clamp path.

The JC ISO 7089 M6 reference has OD≤12 mm and thickness1.4–1.8 mm; HBS DIN 985 M6 h≤6 mm; ISO 4017:2022 M6 k≤4.15 mm. Length acceptance for the two-pitch projection screen is L_actual≥70+2×1.8+6+2=81.6 mm. Nominal85 mm has3.4 mm margin. With the inboard head, minimum head Y=130−1.8−4.15=124.05 mm gives9.05 mm to motor end115. Nominal bolt tip is Y213.2…213.6 mm; the outer washer/nut end reaches207.8 mm. Actual supply length/runout and tool insertion remain assembly inspection fields. Both carriers retain X centre−30 and mirrored Y poses. Washer OD12 leaves4 mm from the controller body edge at the frame axes; this concrete clearance remains below the5 mm planning margin and is checked with actual controller corners/tooling. Fit the rail/post clamp before installing the controller on its separate source pattern.

### Carrier-end washer corner clearance — source body-box screen

1. **Inputs:** the existing controller body rectangle is X = −127…67 mm, Z = 500…648 mm. Four carrier-end axes are X = −137/77 mm, Z = 490/658 mm. Each axis is 10 mm outside the body in both X and Z. The paired controllers share these coordinates and mirror Y.
2. **Calculated corner distance:** the distance from each fixing axis to its nearest body-box corner is √(10²+10²) = 14.1421 mm. For the sourced 12 mm maximum outside-diameter M6 washer, the circle-to-body-box gap is 14.1421−6 = 8.1421 mm. This calculation covers the four carrier-end joints at Z = 490/658 mm.
3. **Tool-radius bound:** preserving the existing 5 mm planning gap to this body box permits a circular tool envelope of radius at most 14.1421−5 = 9.1421 mm, equivalent to 18.2843 mm diameter. The actual socket profile and axial insertion path supply the installed tool check.
4. **Rail-joint distinction:** the two rail joints at Z = 520 mm lie inside the body's Z band. Their 10 mm lateral axis offset and 6 mm washer radius give the separately recorded 4 mm body-box gap. The carrier-end calculation and rail-joint calculation use their own fixing coordinates.
5. **Source basis:** body and fixing coordinates are the existing source/template transfer in this sheet. Washer outside-diameter maximum is recorded in C146 — M6 ISO 7089 plain washer, proposed 200 HV, using the source table in standard fastener geometry. Distances above are calculated nominal assembly screens for the named body rectangle.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed J Kelly side carrier plate | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-147.0, 87.0], [197.0, 200.0], [480.0, 668.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-137.0, 490.0], [-137.0, 520.0], [-137.0, 658.0], [77.0, 490.0], [77.0, 520.0], [77.0, 658.0]] | mm |
| Source-sheet hole group 2 | PASS | [[-117.0, 510.0], [-117.0, 638.0], [57.0, 510.0], [57.0, 638.0]] | mm |

## Sources — online

1. Kelly KLS-N wiring diagram, §3.2.2, p.14.
2. source review r02.
3. source review r02.
4. Square steel tube stock family — supplier reference.
5. Weldable steel plate stock family — supplier reference.
6. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.
7. HBS Fasteners DIN 985 dimensions and product information.
8. standard fastener geometry sources.
9. standard fastener geometry sources.
10. standard fastener geometry sources.
