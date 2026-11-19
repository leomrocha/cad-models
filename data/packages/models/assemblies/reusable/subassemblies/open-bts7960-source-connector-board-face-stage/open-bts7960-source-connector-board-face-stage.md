# Open BTS7960 source connector and board-face stage

1. **Library number:** 286.
2. **Plan identity:** model 27, first-choice Open BTS7960 Mini driver; partial source exterior.
3. **Native drawing:** [Source connector and board-face stage](<open-bts7960-source-connector-board-face-stage.dwg>).
4. **DWG SHA-256:** `a14019a8c2ca9594064ebcc3da95a081b097c01a830a7afbbd4357be6f5ae021`.
5. **State:** PARTIAL_SOURCE_CONNECTORS_AND_OPEN_BOARD_FACE_SAVED_CURRENT_GEOMETRY_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Representation:** five source connector instances reuse three saved Mesh definitions: three two-pin terminals, one XH four-pin connector and one XH three-pin connector. One open board-top reference face and the original planar installation drawing complete seven root occurrences. There are 16 Mesh, six closed LwPolyline and 30 Circle geometry occurrences. The 52 geometry occurrences include material partitions and reference curves.
2. **Source board:** EasyEDA document `7e53d61c870a4bf4afbabc508e75e327`, revision `d2e022f694a84285a6e31ba5a6f05354`. Board reference spans X = 70.104 mm, Y = 39.243 mm. Four source mounting apertures have calculated diameter 2.1999956 mm and pitch 63.246 × 31.75 mm.
3. **Frame:** millimetres; X = 0.254 × (EasyEDA X − 4057), Y = 0.254 × (3256.5 − EasyEDA Y), Z normal to the source top face. The open top-face reference lies at Z = 0 mm. OBJ files carry no unit declaration; their millimetre interpretation is corroborated by the retained independent source XY-span comparisons.
4. **Transform derivation:** the retained EasyEDA parser reads model origin, width, height, rotation and signed Z as numeric source fields. Its exporter first subtracts raw OBJ bounding-box X/Y centre and minimum Z, then applies source rotation, uniform width/height scale, signed Z and source origin. The exporter's fixed substrate-height input is 10 native units, calculated as 2.54 mm at the retained source scale. Rebasing the exported top face to Z = 0 removes that common offset from both face and top-side connector placements. Authored connector Z offsets remain −3.7999924 mm for terminals and −3.499993 mm for XH connectors.
5. **Source scale:** all five connector roots retain the exporter-derived uniform scale 0.999998. Original connector definition coordinates and triangle arrays remain embedded unchanged. The three terminal rotations are 180°, 180° and 0°; four-pin XH rotation is 180° and three-pin XH rotation is 0°.
6. **Board-face construction:** the source perimeter and 17 mounting/drill aperture circles define one open planar Mesh with 725 vertices and 757 triangles. Circular chord error is at most 0.001997755343 mm. Polygon coverage error is zero; triangle overlap residual is −1.3642420526593924 × 10⁻¹² mm². Board thickness and the remaining heatsink/exterior source geometry retain their separate source prerequisites.
7. **Independent projected source comparison:** maximum full projected-outline Hausdorff difference is 0.005777605119 mm between the source OBJ projection and retained source SVG outline. This is a measured source-representation difference. The earlier source XY-span calibration remains a separate check.
8. **Current native checks:** complete source Mesh/curve properties and all composed source occurrence matrices PASS with absolute matrix tolerance 0.0000001 and zero relative tolerance. Current units, root quantities and source hashes PASS. The source-scale correction is retained in the FERME caller recipe and original checkpoint history.
9. **Persistence and appearance:** initial and per-step checkpoints completed. Original final SAVE response, intended path, file existence/size/hash, save audit and zero dropped entities PASS. Current-record XY, XZ and isometric views inspected PASS. Finished owned documents 780 and 781 guarded closed. Verification uses current records.

## Source connector placements

The table lists source global XY centres after conversion and source signed Z before bounding-box normalization. Full root matrices follow the transform derivation above.

| Source occurrence | Library | Source asset | Quantity | Source XY centre (mm) | Signed source Z (mm) | Source rotation |
|---|---:|---|---:|---|---:|---:|
| gge534 | 261 | `b19afe431503404b987e4f77cf7908a2` | 1 | `[14.169999600000041, 35.014027000000006]` | -3.7999924 | 180° |
| gge621 | 261 | `b19afe431503404b987e4f77cf7908a2` | 1 | `[55.57199960000004, 34.887027]` | -3.7999924 | 180° |
| gge708 | 261 | `b19afe431503404b987e4f77cf7908a2` | 1 | `[34.87099960000004, 35.089973]` | -3.7999924 | 0° |
| gge2919 | 259 | `e3b4308fa1f642b986d418566713cf3c` | 1 | `[29.73275740000005, 4.707001000000013]` | -3.4999930000000004 | 180° |
| gge3084 | 260 | `94b3e8f777e240f4a4a022a0a96d0235` | 1 | `[41.783, 4.707001000000013]` | -3.4999930000000004 | 0° |

## Sources — online

1. Original Open BTS7960 EasyEDA source document.
2. Two-pin terminal OBJ source.
3. XH four-pin OBJ source.
4. XH three-pin OBJ source.
5. Sowbot hardware table, original Mini driver identity and design link.
6. Retained EasyEDA 6.5.61 parser/exporter source, inspected as text; SHA-256 `627a35eeaeb76af75b6d42cf957ca22db14effd321f40bc2527109efda4b41ee`.

## References — library

1. [Original source installation drawing](<../../../../interface-references/mechanical/open-bts7960-mini-source-interface-reference/open-bts7960-mini-source-interface-reference.md>), library 253, preserved.
2. [Four-pin connector source definition](<../../../../electronics/components/open-bts7960-xh-four-pin-source-mesh/open-bts7960-xh-four-pin-source-mesh.md>), library 259, quantity one.
3. [Three-pin connector source definition](<../../../../electronics/components/open-bts7960-xh-three-pin-source-mesh/open-bts7960-xh-three-pin-source-mesh.md>), library 260, quantity one.
4. [Two-pin terminal source definition](<../../../../electronics/components/open-bts7960-two-pin-terminal-source-mesh/open-bts7960-two-pin-terminal-source-mesh.md>), library 261, quantity three.
5. [Top current-record view](<open-bts7960-source-connector-board-face-stage-XY.png>).
6. [Side current-record view](<open-bts7960-source-connector-board-face-stage-XZ.png>).
7. [Isometric current-record view](<open-bts7960-source-connector-board-face-stage-isometric.png>).
