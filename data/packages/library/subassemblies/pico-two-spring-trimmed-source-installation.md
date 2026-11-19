# Pico two-spring source-trimmed installation

1. **Library number:** 299.
2. **Plan use:** Assembly 2, step 6, model 19.
3. **Native drawing:** [Pico two-spring source-trimmed installation](<pico-two-spring-trimmed-source-installation.dwg>).
4. **DWG SHA-256:** `b2978840ee8511fcdd0ded3d22f1de29fc17e18b7eb0124117632e0c6c0ffc69`. DWG 2018, 6,495,782 bytes.
5. **State:** SAVED_CURRENT_SOURCE_GEOMETRY_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Geometry:** Two block references share one definition derived from library 292. It stores 12 open source-face meshes, 162,592 vertices and 311,646 triangles. The two references expand to 24 mesh occurrences and 623,292 triangles. The open meshes represent the source-trimmed spring exterior.
2. **Frame:** Pico chassis XYZ, millimetres. X is longitudinal, Y is transverse and Z is up. Both insertions use identity rotation and unit scale.
3. **Placement:** Source body 3182 uses translation `[53.32638370333214, 63.7077772627037, 37.39273304545219]` mm. Source body 3238 uses `[-66.67158396619236, 63.887777262704205, 37.39273304545038]` mm. The ordered source graph comparison binds the second pose as a translated repeat.
4. **Geometry verification:** All 12 stored vertex and triangle arrays and their source-face metadata match library 292 exactly. Both native insertion matrices and source-body labels match the installation contract. Twelve erased handles appear in the current Model Space membership table. The live entity records and final save audit contain 12 meshes and two block references.
5. **Persistence and closure:** The original library 292 DWG served as the source for a byte-identical construction copy. The completed final SAVE passed its path, byte size, SHA-256 and audit checks with zero drops. Persistence verification uses SAVE only. Guarded closure of owned document 8 passed and preserved Start document 1.
6. **Views:** XY, XZ, YZ and isometric projections use the 24 expanded current-record mesh occurrences. The YZ projection overlaps both springs. All four views were inspected.

## References

1. [Original source-trimmed spring exterior, library 292](<../parts/mechanical/pico-tension-spring-source-trimmed-exterior-stage.md>).
2. [XY view](<../images/pico-two-spring-trimmed-source-installation-XY.png>).
3. [XZ view](<../images/pico-two-spring-trimmed-source-installation-XZ.png>).
4. [YZ view](<../images/pico-two-spring-trimmed-source-installation-YZ.png>).
5. [Isometric view](<../images/pico-two-spring-trimmed-source-installation-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP. Source bodies 3182 and 3238. Original STEP SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
