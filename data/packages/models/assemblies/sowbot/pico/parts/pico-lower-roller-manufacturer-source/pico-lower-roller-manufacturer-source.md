# Hiwonder Pico manufacturer lower load roller

1. **Library number:** 273.
2. **Plan component:** model 16; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer lower load roller](<pico-lower-roller-manufacturer-source.dwg>).
4. **DWG SHA-256:** `8df447938dfbf5e1877cb22d6a613b97cf8c011da6c89a7f12143168ba4c07a7`.
5. **Representation:** source-native solid geometry; 1 selected source solid definitions representing one whole purchased component or one named exterior definition.
6. **Frame:** mm; local Z = source X axle direction, X = source Y, Y = source Z; bore axis and roller midplane at origin. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, -65.6964581225068], [0.0, 0.0, 1.0, -24.7849366195963], [1.0, 0.0, 0.0, 67.09890750466116], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[0.0, 0.0, 1.0, -67.09890750466116], [1.0, 0.0, 0.0, 65.6964581225068], [0.0, 1.0, 0.0, 24.7849366195963], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3180:** 24 faces; reachable vertex bounds X/Y/Z = `[[-72.0989075046612, -62.0989075046611], [53.6539965443718, 77.7389197006417], [24.784936619384, 24.7849366195078]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Source lower roller axial width 10 mm; bore cylindrical support radius 7.5 mm. Upper source roller 3170 matches lower 3180 topological vertices under translation to 0.000000000000111 mm; analytic and trim correspondence is checked separately before shared-definition reuse.

## Dimensioned shared-roller source drawing

1. [Dimensioned shared roller source drawing](<pico-roller-manufacturer-source-dimensioned.png>): 4800 × 3200 PNG; XY, XZ, ZY and isometric boundary projections of source solid 3180. One shared roller definition is used by **eight lower rollers (model 16)** and **two upper rollers (model 17)**.
2. **Analytic source dimensions:** local X/Y/Z = **24.085 × 24.085 × 10.000 mm** (unrounded 24.084923156269895 × 24.08492315632835 × 10.000000000226564 mm). All 48 boundary curves (26 ellipse, 22 straight) are supported; exact stationary coordinate parameters within actual ellipse trim intervals and straight-edge endpoints establish these extrema. The original profiled outer surface is retained.
3. **Axial cap sections:** at Z = −5.000/+5.000 mm the outer/inner circular boundaries measure Ø**19.826/15.400 mm**. The native cylindrical bore supports measure radius **7.500 mm**, diameter **15.000 mm**. The Ø15.400 cap mouth and Ø15.000 bore support retain their separate source meanings.
4. **Upper/lower definition reuse:** source upper roller 3170 and lower roller 3180 share the same recursively compared source geometry: **828 paired entities**, matching translated graph after numerical normalization to 0.0000001 mm, with an empty paired graph-differences list. Their original source occurrence poses and separate installed counts are retained.
5. Numeric source frame, geometry, component identities and DWG remain unchanged. The drawing uses millimetres and displays three decimal places.

## References — library

1. [Isometric boundary view](<pico-lower-roller-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<pico-lower-roller-manufacturer-source-local-XY.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `dd1958da72e2d07b6db7f1923b799f550795dd45c9be68cf1b18d0db044bc089`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.

## Upper roller source reuse

Plan model 17 upper carrier roller reuses library 273. Source body 3170 and lower body 3180 have matching translated recursive source graphs across 828 entities at 0.0000001 mm numeric precision, including topology, analytic supports, spline controls, knots and weights. The upper source axle is Y = 86.0490427672882 mm, Z = 76.1522823948006 mm; its source axial midplane is X = −66.99088181147835 mm. Exact inverse placement and comparison receipts are retained with model 17 execution evidence.
