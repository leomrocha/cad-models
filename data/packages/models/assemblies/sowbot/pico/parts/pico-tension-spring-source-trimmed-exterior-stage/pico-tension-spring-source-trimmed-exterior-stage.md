# Hiwonder Pico spring source-trimmed exterior stage

1. **Library number:** 292.
2. **Plan component:** model 19, Hiwonder Pico tension spring.
3. **Native drawing:** [Source-trimmed exterior](<pico-tension-spring-source-trimmed-exterior-stage.dwg>).
4. **DWG SHA-256:** `451013b0572f278849aba86f863157f07857b77e5188070941f7583e691c2bd4`.
5. **State:** SAVED_CURRENT_GEOMETRY_AND_VIEWS_CHECKED_PARTIAL.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Representation:** twelve open, zero-thickness Mesh entities sample source faces 18544–18555, rational supports 1749–1760 of spring body 3182, shell 3593. Aggregate counts: 162,592 vertices and 311,646 triangles. This face-dependent exterior retains the sampled source trim polygons.
2. **Source method:** shared STEP vertex topology supplies UV corners; source edge interiors and rational surface data are retained. Boundary cells are clipped against the valid source UV polygons. Eleven previous interior arrays remain exact. Face 18547/support 1752 retains 17,313 of 17,315 original nominal 21 × 1001 grid cells; cells (0, 30) and (0, 31) use clipped coverage.
3. **Numerical recovery:** 124 new boundary vertices use rational evaluation at 65 and 100 decimal digits followed by one float64 rounding. Maximum 65-versus-100-digit coordinate difference is 6.95216578432157e-64 mm. Maximum final rounding error against the 100-digit reference is 2.36229130272844e-15 mm. These values describe numerical evaluation. All final and DXF-readback triangles have positive area; minimum recorded area is 3.1554436208840472e-30 mm².
4. **Sampled approximation:** maximum retained/new sampled facet deviation is 0.027199143389474167 mm against the assumed 0.03 mm CAD sampling-check input. This sampled comparison has its measured scope. Independently inverted neighboring-face boundaries retain source residuals and disagreements; the stage is an open numerical derivative.
5. **Frame:** millimetres; X = source Y − 67.45145966994615; Y = −source X − 54.680151364355; Z = source Z − 43.2323659374299. The frame is identical to libraries 275, 277 and 287, preserving their inverse manufacturer placements.
6. **Native checks:** all twelve current native Mesh vertex arrays, triangle indices/winding and subdivision zero match the checked source jobs exactly. Millimetre units and counts PASS. Source import and every provenance step were saved. Canonical original SAVE completion, exact path/file size/hash, audit and zero dropped entities PASS. Verification uses the current document records. Finished owned document 792 guarded closed.
7. **Appearance:** current-record XY and isometric Mesh-edge views inspected PASS; coil turns and both attachment loops are visible. All 475,453 unique Mesh face edges are included.
8. **Preserved stages:** libraries 275, 277 and 287 remain their existing source-solid, single-face and twelve-interior stages.

## Source face patches

| Source face | Vertices | Triangles |
|---:|---:|---:|
| 18544 | 470 | 757 |
| 18545 | 3957 | 7453 |
| 18546 | 1429 | 2655 |
| 18547 | 21671 | 40008 |
| 18548 | 1749 | 3256 |
| 18549 | 3795 | 7225 |
| 18550 | 473 | 760 |
| 18551 | 3782 | 7192 |
| 18552 | 1434 | 2663 |
| 18553 | 118141 | 228958 |
| 18554 | 1750 | 3258 |
| 18555 | 3941 | 7461 |

## Sources — online

1. Manufacturer-linked chassis STEP, original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis.

## References — library

1. [Original source-native spring](<../pico-tension-spring-manufacturer-source/pico-tension-spring-manufacturer-source.md>), library 275.
2. Single source-face patch (earlier revision `model-277`; [current catalogue revision](<../pico-left-spring-closed-source-exterior/pico-left-spring-closed-source-exterior.md>)), library 277.
3. Twelve source-face interiors (earlier revision `model-287`; [current catalogue revision](<pico-tension-spring-source-trimmed-exterior-stage.md>)), library 287.

## Project execution evidence


## Current-record views

1. [YZ view](<pico-tension-spring-source-trimmed-exterior-stage-YZ.png>).
2. [XY view](<pico-tension-spring-source-trimmed-exterior-stage-XY.png>).
3. [XZ view](<pico-tension-spring-source-trimmed-exterior-stage-XZ.png>).
4. [isometric view](<pico-tension-spring-source-trimmed-exterior-stage-isometric.png>).
