THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Mast-seat brace, unclipped

1. **Library number:** 151.
2. **Type:** part.
3. **CAD file:** [p08brms0-attachment-mast-seat-brace-unclipped.dwg](<p08brms0-attachment-mast-seat-brace-unclipped.dwg>).
4. **DWG SHA-256:** `a266d883f0009ed9c8f56039a05ef21081a9d2305bd24761c0acca7fa9e2b47f`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Mast-seat brace, unclipped — P08BRMS0.

**Design status:** Discussion construction proposal.

## Technical specification

1. **Status:** Separately identified discussion construction proposal. Source geometry preserved. Actual analysis model: unavailable.
2. **Units/frame:** mm; Structural S front source frame, X forward/Y left/Z up. Proposed steel plate 6 mm thick, retaining the source plate-stock family. Evaluate plate and weld loads with the attachment joint calculation.
3. **Quantity:** Two instances per interface when this alternative is used. The unclipped and relieved alternatives occupy the same use; construct separate comparison assemblies. Front/rear reuse this manufactured profile; source P08BR/P09BR originals remain separate records.
4. **Exact left profile:** XZ polygon vertices, in boundary order: [(308, 283), (368, 283), (308, 363)]. Extrude along +Y from Y20 to Y26. No holes. Closed area 2400 mm²; nominal solid volume 14400 mm³.
5. **Right instance:** Reflect only the manufactured instance across Y0, giving Y-26…-20; retain its own occurrence identity. Both plate profiles retain the stated XZ coordinates. The resulting left/right brace pair is not fused to either host.
6. **Raised installation:** Front J: (X,Y,Z)=(x+25,y,z+267). Rear J: (X,Y,Z)=(-x-25,-y,z+267), a proper 180° Z rotation then translation. Rear Structural S uses (-x,-y,z). Minimum front/rear J Z is 550 mm. Apply the group transform once, including the original host group.
7. **Host contact:** Bottom contact on seat top Z283 is 60 mm. The saved mast uses outer R6/inner R3 nominal corners. Its planar side at Y20 spans X314…342; side-face contact area is 1493.333333 mm². The brace has a gap to the rounded mast surface over X308…314 and X342…348, reaching 6 mm at X308/348; X348…368 extends beyond the mast onto the seat. Do not report the full plate area as mast contact. The distance from lower pivot (368,323) to the sloping brace edge is 24 mm, leaving 12.75 mm to its Ø22.5 bore projection.
8. **Pin/service check:** Reuse C063 — Category 1 lower linkage pin, Ø22×100 mm reference at (X,Z)=(368,323), axis Y, transformed with the interface. Sweep the complete 100 mm reference shank along the removal direction. The calculated bore-to-brace gap covers the circular bore projection. Use the source pin, shoulder, arm, ball and keeper geometry for the complete removal check.
9. **Weld construction:** Fixture brace and host with broad-face/edge contacts above. Record weld beads separately from plate solids, including any root relief. A 10×10 root cut applies only to the explicit relieved profile; its lost area is 50 mm². Check welding access at both faces and preserve source base-seat/doubler geometry.
10. **Next native operations:** Make a new owned document and save its partial checkpoint immediately. Reuse bounded planar-profile construction from `complete_model_plate_batch.py`; encode the XZ frame and normal +Y explicitly. Construct this one closed polygon, extrude 6 mm, save a checkpoint, measure all vertices/thickness/area or volume, verify one closed solid, save/reopen and verify file/source hashes. Close every finished or temporary owned document with the installed cleanup helper and verify disappearance; preserve active, unsaved and other-agent documents. Repeat as a separate new file for each alternative.
11. **Proposed output:** ``. Assembly proposal outputs should distinguish `unclipped` and `root-relief` and retain the existing seven-solid host assembly plus four separate brace occurrences. Save/check the S assembly first, then place source front/rear J variants with the exact matrices above.

1. **Status:** Separately identified discussion construction proposal. Source geometry preserved. Actual analysis model: unavailable.
2. **Units/frame:** mm; Structural S front source frame, X forward/Y left/Z up. Proposed steel plate 6 mm thick, retaining the source plate-stock family. Evaluate plate and weld loads with the attachment joint calculation.
3. **Quantity:** Two instances per interface when this alternative is used. The unclipped and relieved alternatives occupy the same use; construct separate comparison assemblies. Front/rear reuse this manufactured profile; source P08BR/P09BR originals remain separate records.
4. **Exact left profile:** XZ polygon vertices, in boundary order: [(308, 283), (368, 283), (308, 363)]. Extrude along +Y from Y20 to Y26. No holes. Closed area 2400 mm²; nominal solid volume 14400 mm³.
5. **Right instance:** Reflect only the manufactured instance across Y0, giving Y-26…-20; retain its own occurrence identity. Both plate profiles retain the stated XZ coordinates. The resulting left/right brace pair is not fused to either host.
6. **Raised installation:** Front J: (X,Y,Z)=(x+25,y,z+267). Rear J: (X,Y,Z)=(-x-25,-y,z+267), a proper 180° Z rotation then translation. Rear Structural S uses (-x,-y,z). Minimum front/rear J Z is 550 mm. Apply the group transform once, including the original host group.
7. **Host contact:** Bottom contact on seat top Z283 is 60 mm. The saved mast uses outer R6/inner R3 nominal corners. Its planar side at Y20 spans X314…342; side-face contact area is 1493.333333 mm². The brace has a gap to the rounded mast surface over X308…314 and X342…348, reaching 6 mm at X308/348; X348…368 extends beyond the mast onto the seat. Do not report the full plate area as mast contact. The distance from lower pivot (368,323) to the sloping brace edge is 24 mm, leaving 12.75 mm to its Ø22.5 bore projection.
8. **Pin/service check:** Reuse C063 — Category 1 lower linkage pin, Ø22×100 mm reference at (X,Z)=(368,323), axis Y, transformed with the interface. Sweep the complete 100 mm reference shank along the removal direction. The calculated bore-to-brace gap covers the circular bore projection. Use the source pin, shoulder, arm, ball and keeper geometry for the complete removal check.
9. **Weld construction:** Fixture brace and host with broad-face/edge contacts above. Record weld beads separately from plate solids, including any root relief. A 10×10 root cut applies only to the explicit relieved profile; its lost area is 50 mm². Check welding access at both faces and preserve source base-seat/doubler geometry.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Mast-seat brace, unclipped | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[308.0, 368.0], [20.000000000000018, 26.00000000000002], [283.0, 363.0]] | mm |
| Every source polygon vertex on both thickness faces | PASS | [1, 1, 1, 1, 1, 1] | count |

## Sources — online

1. Weldable steel plate stock family — supplier reference.

## References — local

153. [Front/rear S attachment mast base seat](<p08bs-front-attachment-mast-base-seat.md>) — library entry 153.
157. [S attachment mast tube](<p08ms-front-attachment-mast.md>) — library entry 157.
