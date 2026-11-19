# Hiwonder Pico manufacturer lower formed plate

1. **Library number:** 266.
2. **Plan component:** model 9; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer lower formed plate](<pico-lower-plate-manufacturer-source.dwg>).
4. **DWG SHA-256:** `ec03b07b05d9108416acfb45da3d34a92fc8f4598275db3df010a42f1df4f203`.
5. **Representation:** source-native solid geometry; 1 selected source solid definitions representing one whole purchased component or one named exterior definition.
6. **Frame:** mm; X longitudinal = source Y, Y transverse = −source X, Z up; source XY bounds centre at 0, lower support plane Z = 0. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, 2.151925170529502], [-1.0, 0.0, 0.0, 8.956834395334152], [0.0, 0.0, 1.0, -37.5852078594164], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[-0.0, -1.0, -0.0, 8.956834395334152], [1.0, 0.0, 0.0, -2.151925170529502], [0.0, 0.0, 1.0, 37.5852078594164], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3108:** 215 faces; reachable vertex bounds X/Y/Z = `[[-41.7779606823829, 59.6916294730512], [-123.92061822436, 119.616767883301], [37.5852078594164, 54.0774804312808]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Source lower plate has 2 mm main sheet and upward end flanges; source width 101.47 mm retains comparison with drawing body width 101.58 mm. Source body 3037 is retained separately with a Z-reflected vertex correspondence.

7. **Dimensioned formed-plate drawing:** [Native lower plate measurement drawing](<pico-lower-plate-manufacturer-source-dimensioned.png>) shows XY, XZ, YZ and isometric projections of the saved formed geometry. Analytic boundary extents are X = 243.537386107661 mm, Y = 101.4695901554341 mm and Z = 16.49227257186446 mm (displayed as 243.537 × 101.470 × 16.492 mm). The calculation uses all retained native straight-edge endpoints and stationary coordinate parameters on the actual trimmed ellipse arcs under the saved canonical transform. Analytic boundary extents and the topological-vertex spans above retain their separate measurement methods. The drawing labels one plate, source body 3108, XY centre origin and the Z = 0 lower support datum. All boundary edges are projected with the end flanges in their saved formed positions.

## References — library

1. [Isometric boundary view](<pico-lower-plate-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<pico-lower-plate-manufacturer-source-local-XY.png>).
3. [Dimensioned formed-plate drawing](<pico-lower-plate-manufacturer-source-dimensioned.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `675e9522eab1152641b9ba44b0490b64ec724d3bf3b343d264b5f811e2eb028d`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.
