# Pico upper plate perforated planar stage

1. **Library number:** 262.
2. **Plan component:** model 08, Hiwonder Pico upper plate.
3. **CAD file:** [Native planar plate mesh](<pico-upper-plate-planar-perforated-faceted-stage.dwg>).
4. **DWG SHA-256:** `a71716d3e800d15b3f4414fff8746e11f9bc29bf6b2444a2888c3ffa4371fb3c`.
5. **State:** PARTIAL_PLANAR_PERFORATED_FACETED_STAGE_SAVED_REOPENED_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Representation:** closed faceted mesh of the planar upper-plate stage, with 24 slot openings and 41 circular openings. Perimeter and opening contours reuse the corrected source-profile drawing.
2. **Source dimensions:** plate outline 270 × 143 mm from the RoboDoo plate drawing; thickness 2 mm from Hiwonder's product specification. This drawing variant retains its own perimeter and hole pattern.
3. **Frame:** millimetres; X longitudinal, Y transverse, original profile centre at X = Y = 0 mm; bottom Z = 0 mm, top Z = 2 mm.
4. **Raster reconstruction:** opening coordinates and radii retain the source trace's recorded pixel uncertainty; smallest coordinate uncertainty 1.354794 mm. Circular curves are represented by inscribed chords with maximum measured deviation 0.001977135 mm.
5. **Mesh:** 8,792 vertices and 17,840 triangles; one connected closed surface, every edge shared by two oppositely oriented faces, 65 through-openings. Faceted planar area 30,049.341627098 mm²; calculated volume 60,098.683254195 mm³. Faceting changes the analytic traced area by 0.899064094 mm².
6. **Checks:** all original profile coordinates/bulges matched; cap coverage and through-opening checks PASS. Reopened native vertex/face arrays and source metadata match the prepared mesh exactly. Subdivision 0, millimetre units and zero dropped entities checked. Save/reopen PASS; top/isometric views inspected. Finished owned documents 676–678 closed.

## Sources — online

1. RoboDoo dimensioned Hiwonder plate drawing, 270 × 143 mm plate-view dimensions and raster linework; source SHA-256 `6619b6941f7c22c137efb661b2924ac5dc5d314c6c5f105cc9d9a3922253f1b4`.
2. Hiwonder suspended tracked chassis, retained product variant specification: 2 mm plate thickness.

## References — library

1. [Original corrected source-profile drawing](<../../interface-references/hiwonder-pico-plate-source-profile/hiwonder-pico-plate-source-profile.md>).
2. [Native-mesh isometric view](<pico-upper-plate-planar-perforated-faceted-stage-isometric.png>).
3. [Native-mesh top view](<pico-upper-plate-planar-perforated-faceted-stage-XY.png>).
