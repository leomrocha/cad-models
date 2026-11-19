# Hiwonder Pico manufacturer plate support spacer

1. **Library number:** 276.
2. **Plan component:** model 20; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer plate support spacer](<pico-spacer-manufacturer-source.dwg>).
4. **DWG SHA-256:** `801ab8dc8b90cacce5fed870c9bac05f3e06478ddf5f6ac13805567f3984aba3`.
5. **Representation:** source-native solid geometry; 1 selected source solid definitions representing complete source hex support spacer including exposed end-interface geometry.
6. **Frame:** mm; X = source Y, Y = −source X, Z up along post; local origin on source post axis at lower hex support plane. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, 89.3791368860226], [-1.0, 0.0, 0.0, 43.1379916963854], [0.0, 0.0, 1.0, -98.105432476082], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[-0.0, -1.0, -0.0, 43.1379916963854], [1.0, 0.0, 0.0, -89.3791368860226], [0.0, 0.0, 1.0, 98.105432476082], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3032:** 77 faces; reachable vertex bounds X/Y/Z = `[[39.9884105942676, 46.2875727985032], [-92.8278884606204, -85.9303853114248], [90.6213645619075, 123.105432476082]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Source hex support planes span 25 mm; original source assembly placements retained. Source post upper support plane and expansion-plate underside retain their original approximately 0.124 mm separation rather than forced contact. Existing raster cylinder hypothesis library 256 remains preserved.

## Dimensioned source drawing

1. [Dimensioned hex spacer source drawing](<pico-spacer-manufacturer-source-dimensioned.png>): 4800 × 3200 PNG; XY, XZ, ZY and isometric boundary projections of source body 3032. One CAD solid represents one spacer definition; installed quantity is four whole spacers.
2. **Supported hex dimensions:** lower/upper cap planes Z = **0.000/25.000 mm**, spacing **25.000 mm**. Each outer cap profile has six straight edges; all six axis-to-flat distances are **3.000 mm**, establishing **6.000 mm across flats**. Original angular orientation gives X/Y coordinate spans **6.898/6.299 mm** (unrounded 6.8975031491956/6.2991622042356 mm).
3. **Source cap sections:** complete centred circular mouths at each Z = 0.000/25.000 mm cap measure Ø**4.300 mm**.
4. **Separate whole-source vertex measurement:** local Z interval **−7.484…25.000 mm**, span **32.484 mm** (unrounded 32.4840679141745 mm). This topological-vertex measurement retains the unsupported exterior-trim scope; the supported hex cap spacing is independently 25.000 mm.
5. **Boundary representation:** 101 supported edges and 111 unsupported trim curves; unsupported curves appear only as isolated endpoint markers. Original numeric frame, geometry and assembly poses remain unchanged, including the recorded approximately 0.124 mm upper-support-plane/plate-underside separation.
6. Dimensions use original millimetre source geometry; three decimal places are displayed.

## References — library

1. [Isometric boundary view](<pico-spacer-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<pico-spacer-manufacturer-source-local-XY.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `85981a6792734d7803167bc5270e28029f7aa7e2ef3a452b3921f48b4eeba203`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.
