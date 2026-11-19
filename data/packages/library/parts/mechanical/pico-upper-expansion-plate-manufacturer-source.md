# Hiwonder Pico manufacturer upper expansion plate

1. **Library number:** 265.
2. **Plan component:** model 8; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer upper expansion plate](<pico-upper-expansion-plate-manufacturer-source.dwg>).
4. **DWG SHA-256:** `0ff45ae07b45fe084dfadb6aea9d2ff4e0f069cc5a4c2714808833393d0724ee`.
5. **Representation:** source-native solid geometry; 1 selected source solid definition representing one planned component.
6. **Frame:** mm; X longitudinal = source Y, Y transverse = −source X, Z up; plate XY bounds centre at 0, underside Z = 0. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, -3.965026028327003], [-1.0, 0.0, 0.0, 8.957804676667397], [0.0, 0.0, 1.0, -123.229524911704], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[-0.0, -1.0, -0.0, 8.957804676667397], [1.0, 0.0, 0.0, 3.965026028327003], [0.0, 0.0, 1.0, 123.229524911704], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3026:** 206 faces; reachable vertex bounds X/Y/Z = `[[-62.8726760601837, 80.7882854135185], [-131.003868873496, 138.93392093015], [123.229524911704, 125.229524911801]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Manufacturer source has 66 opening loops: 24 slots and 42 circles. Existing raster stage 262 has 65: 24 slots and 41 circles. All 65 raster opening centres match within recorded raster uncertainty under the explicitly tested mirrored/opposite-face view mapping (raster X reversed, Y retained); maximum centre residual 0.898656 mm. Rejected pure 180 degree rotation leaves four asymmetric holes displaced about 20 mm.
7. **Independent source comparison:** Extra CAD circle projects near original plate-drawing pixel [534, 129]; a small circular opening is visible there in the original raster. This is an omitted trace feature; no design-revision claim is made.
8. **Independent source comparison:** Source vertex spans are X = 143.660961 mm, Y = 269.937790 mm and Z = 2 mm. Source dimensions and nominal 270 × 143 mm drawing remain separately attributed; source geometry unchanged and no rescaling applied.

9. **Dimensioned top drawing:** [Native upper plate measurement drawing](<../../images/pico-upper-expansion-plate-manufacturer-source-dimensioned.png>) records analytic upper-cap boundary extents X = 269.937789803646 mm and Y = 143.66096147370058 mm (displayed as 269.938 × 143.661 mm). The calculation uses retained native straight-edge endpoints and circular-arc stationary points under the saved canonical transform. This analytic boundary measurement is recorded separately from the topological-vertex spans above. The drawing labels one plate, source body 3026, centre origin and all 66 opening centres/sizes: 42 circles, 22 capsule slots and two rounded rectangles. The rounded rectangles are included in the existing 24-slot source grouping. Displayed dimensions use three decimal places.

## References — library

1. [Isometric boundary view](<../../images/pico-upper-expansion-plate-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<../../images/pico-upper-expansion-plate-manufacturer-source-local-XY.png>).
3. [Dimensioned top drawing and opening coordinate table](<../../images/pico-upper-expansion-plate-manufacturer-source-dimensioned.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `461c844132fac00a2ea1433d1d6c000c5fefd5fefe16d41dbc75ce6ac14d25d7`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.
