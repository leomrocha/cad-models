# Hiwonder Pico manufacturer right side carrier

1. **Library number:** 268.
2. **Plan component:** model 11; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer right side carrier](<pico-right-side-frame-manufacturer-source.dwg>).
4. **DWG SHA-256:** `b55047906c7c29f992ffd9669131222345b098e29ca09ddd7d920d2bbc8db044`.
5. **Representation:** source-native solid geometry; 1 selected source solid definitions representing one whole purchased component or one named exterior definition.
6. **Frame:** mm; X travel = source Y, Y transverse = −source X, Z up; carrier sheet midplane Y = 0; shared source drive-axis Y/Z datum. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, 89.9496630935861], [-1.0, 0.0, 0.0, 68.94772445498324], [0.0, 0.0, 1.0, -64.6359015567724], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[-0.0, -1.0, -0.0, 68.94772445498324], [1.0, 0.0, 0.0, -89.9496630935861], [0.0, 0.0, 1.0, 64.6359015567724], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3368:** 175 faces; reachable vertex bounds X/Y/Z = `[[67.9477244546252, 69.9477244553413], [-86.8406633698312, 126.616533934377], [20.7849366196194, 83.4439234603994]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Right carrier source body 3368 retains its own holes and source orientation. Left and right source carrier profiles share the four lower suspension positions and upper return-wheel positions; separate manufacturer bodies are preserved.

7. **Dimensioned right carrier drawing:** [Native right carrier measurement drawing](<../../images/pico-right-side-frame-manufacturer-source-dimensioned.png>) uses this body 3368 and its retained right-side transform for XZ, XY, YZ and isometric projections. The complete 59-edge supported outer profile measures X = 218.84580936872808 mm and Z = 62.658986840757194 mm (displayed as 218.846 × 62.659 mm). The rounded-end analytic X extremum gives a profile span 5.3886120645199 mm greater than the existing 213.4571973042082 mm topological-vertex span. Main planar faces at Y = −1 and +1 mm have measured separation 2.000 mm. The drawing labels one right carrier, its source drive-axis reference datum and twelve complete circular-opening centres/diameters measured on the selected Y = −1.000 mm cap.
8. **Drawing curve scope:** 409 supported native edges supply linework. The 112 unsupported internal trim curves are shown only as isolated orange endpoint markers, with an explicit legend. Dimensions use the complete supported profile, measured main-face planes and complete analytic circular openings. Original source geometry, source pose and earlier boundary views remain preserved.

## References — library

1. [Isometric boundary view](<../../images/pico-right-side-frame-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<../../images/pico-right-side-frame-manufacturer-source-local-XY.png>).
3. [Dimensioned right carrier drawing and circular-opening table](<../../images/pico-right-side-frame-manufacturer-source-dimensioned.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `eb774318e3c3c5631345425f97c38b605dc19033787bf8572fadb5256528a5f3`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.
