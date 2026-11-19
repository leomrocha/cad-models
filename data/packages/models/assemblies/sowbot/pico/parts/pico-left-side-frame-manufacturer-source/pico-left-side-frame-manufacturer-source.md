# Hiwonder Pico manufacturer left side carrier

1. **Library number:** 267.
2. **Plan component:** model 10; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer left side carrier](<pico-left-side-frame-manufacturer-source.dwg>).
4. **DWG SHA-256:** `8d91f98c371a0b70af86fc883d86125e61664d64ee09e7693900e392bef0cbc8`.
5. **Representation:** source-native solid geometry; 1 selected source solid definitions representing one whole purchased component or one named exterior definition.
6. **Frame:** mm; X travel = source Y, Y transverse = −source X, Z up; sheet midplane Y = 0; X/Z origin on source motor output-shaft axis. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, 89.9496630935861], [-1.0, 0.0, 0.0, -50.91890750497305], [0.0, 0.0, 1.0, -64.6359015567724], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[-0.0, -1.0, -0.0, -50.91890750497305], [1.0, 0.0, 0.0, -89.9496630935861], [0.0, 0.0, 1.0, 64.6359015567724], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3234:** 175 faces; reachable vertex bounds X/Y/Z = `[[-51.9189075053311, -49.918907504615], [-86.8406633698312, 126.616533934377], [20.7849366196194, 83.4439234603994]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Source output shaft body 3142 cylinder axis: source Y = −89.9496630935861 mm and Z = 64.6359015567724 mm; source radius 3 mm. Carrier source body 3234 is retained separately from right body 3368; source placements and holes are unchanged.

7. **Dimensioned carrier drawing:** [Native left carrier measurement drawing](<pico-left-side-frame-manufacturer-source-dimensioned.png>) shows XZ, XY, YZ and isometric projections. The complete 59-edge supported outer profile measures X = 218.84580936872808 mm and Z = 62.658986840757194 mm (displayed as 218.846 × 62.659 mm). Native circular-arc stationary points establish the rounded-end X maximum; the existing X topological-vertex span is 213.4571973042082 mm. The analytic profile span exceeds that vertex span by 5.3886120645199 mm. Main planar faces at Y = −1 and +1 mm have measured separation 2.000 mm. The drawing labels source body 3234, one carrier, the retained source motor-axis reference datum and twelve complete circular-opening centres/diameters.
8. **Drawing curve scope:** 409 supported native edges supply linework. The 112 unsupported internal trim curves are shown only as isolated orange endpoint markers, with an explicit legend. Dimensions use the complete supported profile, measured main-face planes and complete analytic circular openings. Original source geometry and earlier boundary views remain preserved.

## References — library

1. [Isometric boundary view](<pico-left-side-frame-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<pico-left-side-frame-manufacturer-source-local-XY.png>).
3. [Dimensioned side-carrier drawing and circular-opening table](<pico-left-side-frame-manufacturer-source-dimensioned.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `5606fb61b2350fdb7c59e5274a70bd41354d0c8441e15c43aca0b59c4655d6e6`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.
