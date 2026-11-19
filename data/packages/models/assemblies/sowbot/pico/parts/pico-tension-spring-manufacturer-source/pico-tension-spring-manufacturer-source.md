# Hiwonder Pico manufacturer tension spring exterior

1. **Library number:** 275.
2. **Plan component:** model 19; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer tension spring exterior](<pico-tension-spring-manufacturer-source.dwg>).
4. **DWG SHA-256:** `340a38bdc1ff933e5d799803a8856cebbed786beb941b7bf67bacace5b29d949`.
5. **Representation:** source-native solid geometry; 1 selected source solid definitions representing complete source wire spring body 3182, coil and exposed end-wire geometry.
6. **Frame:** mm; X travel = source Y, Y transverse = −source X, Z up; source body XY vertex-bounds centre at zero, lowest source wire vertex Z = 0; inverse preserves installed source pose. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, -67.45145966994615], [-1.0, 0.0, 0.0, -54.680151364355], [0.0, 0.0, 1.0, -43.2323659374299], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[-0.0, -1.0, -0.0, -54.680151364355], [1.0, 0.0, 0.0, 67.45145966994615], [0.0, 0.0, 1.0, 43.2323659374299], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SAVED_REOPENED_GEOMETRY_CHECKED_NATIVE_COIL_DISPLAY_FAILED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3182:** 12 faces; reachable vertex bounds X/Y/Z = `[[-56.6042912947952, -52.7560114339148], [55.291803869713, 79.6111154701793], [43.2323659374299, 67.8957560460182]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** native boundary projections retain the two end sections; 14 of 28 trim edges use endpoint points. Source B-spline projections display the coil and wire loops. Native viewport capture also displays the separated end sections.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Manufacturer documentation names a carbon-steel tension spring with miniature bearings in the suspension. Source spring body 3182 is retained as one wire-surface solid with 12 faces; source mounting pose is preserved by the inverse transform.

## References — library

1. [Isometric boundary view](<pico-tension-spring-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<pico-tension-spring-manufacturer-source-local-XY.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `4c3f3f99822ccfda56ce05f49f6cd0188497ca8c14328207438f27c233c9e630`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.

## Curved surface checks

All six saved native exact NURBS surfaces match source control-point/weight multisets, degrees and unique knot values within 0.0000001 mm numeric precision. Five surfaces contain 2,450 controls each and one contains 3,430 controls. Surface trimming and knot multiplicities retain separate checking scope.

[Supplemental source STEP B-spline coil view](<pico-tension-spring-manufacturer-source-source-spline-isometric.png>).

**Native visual check: FAIL.** The saved exact NURBS coil is absent from native viewport rendering; only end sections appear. Source-derived coil projections are supplemental.

The bounded shaded native check used Gouraud Shaded, Front and ZOOM EXTENTS; its capture displays shaded end sections while the intervening coil remains absent. Owned inspection document 729 was checkpointed and closed. Native visual state remains FAIL.

## Partial coil display recovery

[Library 277 source-sampled partial coil exterior](<../pico-tension-spring-source-sampled-coil-patch/pico-tension-spring-source-sampled-coil-patch.md>) displays the sampled interior of source face 18547 in the native viewport. This separate open faceted stage retains measured trim-inversion and sampled approximation errors. The original source-native DWG and its failed exact-coil display evidence remain preserved.
