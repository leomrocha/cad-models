# Hiwonder Pico manufacturer suspension arm

1. **Library number:** 274.
2. **Plan component:** model 18; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer suspension arm](<pico-suspension-arm-manufacturer-source.dwg>).
4. **DWG SHA-256:** `b8a567745e7b3a466bc91307b994bd0681ca4c24baa7d6374d70a3a6a6159a23`.
5. **Representation:** source-native solid geometry; 1 selected source solid definitions representing one whole purchased component or one named exterior definition.
6. **Frame:** mm; local Z = source X pivot-axis direction, X = source Y, Y = source Z; carrier pivot axis and sheet midplane at origin. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, -76.3061736612362], [0.0, 0.0, 1.0, -35.3946521582783], [1.0, 0.0, 0.0, 58.0989075047825], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[0.0, 0.0, 1.0, -58.0989075047825], [1.0, 0.0, 0.0, 76.3061736612362], [0.0, 1.0, 0.0, 35.3946521582783], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3186:** 19 faces; reachable vertex bounds X/Y/Z = `[[-59.0989075048626, -57.0989075046048], [60.7467106542007, 88.4254233934921], [19.8351891512315, 42.3946521583045]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Source carrier pivot axis Y = 76.3061736612362 mm, Z = 35.3946521582783 mm; roller axle Y = 65.6964581225066 mm, Z = 24.7849366195488 mm. Source pivot-to-axle distance is 15.004404 mm. Sheet thickness 2 mm.

## Dimensioned source drawing

1. [Dimensioned suspension-arm source drawing](<../../images/pico-suspension-arm-manufacturer-source-dimensioned.png>): 4800 × 3200 PNG; XY, XZ, ZY and isometric boundary projections of one source CAD solid 3186. Installed quantity: eight suspension arms.
2. **Supported Z = +1 mm face profile:** analytic X/Y spans **32.463 × 24.610 mm** (unrounded 32.462624053604586 × 24.609715538744226 mm). The complete 18-edge outer loop uses supported straight and ellipse curves; exact stationary coordinate parameters within actual trim intervals give these profile extrema.
3. **Main cap planes:** Z = −1.000/+1.000 mm; spacing **2.000 mm**. Both caps have complete pivot circular mouths Ø**7.200 mm**, centred at X/Y = **0.000/0.000 mm**, and roller-axle circular mouths Ø**5.200 mm**, centred at X/Y = **−10.610/−10.610 mm** (unrounded −10.609715538729915/−10.609715538718241 mm). Pivot-to-roller-axle centre distance: **15.004 mm** (unrounded 15.00440360778416 mm).
4. **Curve scope:** 55 supported boundary edges and one unsupported opposite-face trim. The Z = −1 mm outer loop contains 13 edges including that trim; the drawing shows its isolated endpoint markers. The analytic profile dimensions above apply to the complete supported Z = +1 mm face loop.
5. Source geometry, numeric frame and DWG are unchanged. Measurements use source face planes and complete cap circles; three decimal places are displayed.

## References — library

1. [Isometric boundary view](<../../images/pico-suspension-arm-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<../../images/pico-suspension-arm-manufacturer-source-local-XY.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `c706cef119a82f08cfe0bc2844aacb7fd1dd52410e6814b6ad8292308db9d1be`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.
