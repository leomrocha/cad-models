# Hiwonder Pico manufacturer guide end wheel

1. **Library number:** 272.
2. **Plan component:** model 15; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer guide end wheel](<pico-end-wheel-manufacturer-source.dwg>).
4. **DWG SHA-256:** `ae4adbc3f49fc3901378be6fc989b332d508223e1e5f76a290b21563389c1a99`.
5. **Representation:** source-native solid geometry; 1 selected source solid definitions representing one whole purchased component or one named exterior definition.
6. **Frame:** mm; local Z = source X axle direction, X = source Y, Y = source Z; axle and wheel midplane at origin. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, -122.285200362186], [0.0, 0.0, 1.0, -48.6916465286565], [1.0, 0.0, 0.0, 67.4189075049339], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[0.0, 0.0, 1.0, -67.4189075049339], [1.0, 0.0, 0.0, 122.285200362186], [0.0, 1.0, 0.0, 48.6916465286565], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3176:** 36 faces; reachable vertex bounds X/Y/Z = `[[-72.418907504934, -62.4189075049338], [102.285200362186, 142.285200362186], [48.6916465285596, 48.6916465287535]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Source guide wheel cylindrical rim radius 20 mm, axial width 10 mm. Analytic cylindrical supports establish the 40 mm radial diameter even though source circular seam vertices have near-zero source Z span.

## Dimensioned source drawing

1. [Dimensioned guide end-wheel source drawing](<../../images/pico-end-wheel-manufacturer-source-dimensioned.png>): 4800 × 3200 PNG; XY, XZ, ZY and isometric boundary projections. One source CAD solid 3176 represents one wheel definition; installed quantity is two whole guide end wheels.
2. **Analytic source dimensions:** overall local X/Y/Z = **40.000 × 40.000 × 10.000 mm**; outer rim diameter **40.000 mm**, axial width **10.000 mm**. All 72 native boundary curves (60 ellipse, 12 straight) are supported. Exact stationary coordinate parameters within the actual ellipse trim intervals and straight-edge endpoints give these extrema. Source seam-vertex bounds remain separately recorded above.
3. **Axial source sections:** at each Z = −5.000/+5.000 mm face, outer annular boundaries are Ø**39.000/33.000 mm** and inner annular boundaries are Ø**21.000/19.000 mm**. Values describe complete circular source face boundaries at their stated planes.
4. **Asymmetric source recesses:** at Z = +3.500 mm the annular boundaries are Ø**32.000/22.000 mm**; at Z = −3.500 mm they are Ø**31.000/22.000 mm**. The original source asymmetry is retained.
5. Original numeric frame, source geometry and DWG remain unchanged. The drawing uses millimetres and displays three decimal places.

## References — library

1. [Isometric boundary view](<../../images/pico-end-wheel-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<../../images/pico-end-wheel-manufacturer-source-local-XY.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `152b70823e1840cf8bc539350fa4eb9ced51a30df04583014876272419a24c3d`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.
