# Hiwonder Pico source-sampled partial coil exterior

1. **Library number:** 277.
2. **Plan component:** model 19, the existing Hiwonder Pico tension spring; partial exterior recovery stage.
3. **Native model:** [Source-sampled coil patch](<pico-tension-spring-source-sampled-coil-patch.dwg>).
4. **DWG SHA-256:** `185ac91638f5ca59b8a32691585d68e6ececd13115b2914ef54fcaebdc48fc8e`.
5. **State:** SOURCE_SAMPLED_PARTIAL_COIL_SAVED_REOPENED_NATIVE_DISPLAY_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Representation:** one open, zero-thickness faceted Mesh with 18,343 vertices and 34,630 triangles. The mesh samples the interior of manufacturer STEP face 18547 on rational NURBS support 1752, belonging to spring body 3182. It displays a portion of the source wire's exterior around the coil. Other faces and cells crossing the trim boundary are omitted.
2. **Source trim:** actual oriented STEP edge-loop curves are evaluated and inverted onto the surface. The resulting UV polygon is valid; maximum sampled curve-to-surface inversion residual is 0.0010064125 mm. Only complete grid cells contained in that reconstructed polygon are retained. Grid resolution is 20 × 1,000 cells across the full support parameter domain; 17,315 cells are retained.
3. **Approximation check:** independent rational-surface evaluations at two barycentric points per triangle give maximum sampled deviation 0.0271991434 mm. This is a sampled comparison, not a certified global error bound. The source rational control grid, weights, expanded knot multiplicities and source-to-local transform generate the mesh coordinates.
4. **Frame:** millimetres; identical source-to-local frame to library 275. X = source Y − 67.45145966994615; Y = −source X − 54.680151364355; Z = source Z − 43.2323659374299. The inverse transformation preserves the original source assembly pose.
5. **Original geometry:** library 275 retains the complete imported source solid and its original bytes. This mesh is a separately labelled partial faceted stage. Source surface 1758's inverted trim polygon failed validity; its data and failed attempt remain preserved in execution evidence.

## Checks

1. Immediate import checkpoint, subsequent geometry/view checkpoints and final save/reopen PASS. Zero dropped entities; original library 275 SHA-256 unchanged.
2. Reopened native mesh vertices and triangles match the prepared arrays exactly. Subdivision 0 and millimetre units checked.
3. Actual native viewport pixels show the repeated coil surface along its length. The reopened capture shows the TOP view cube. [Native viewport capture](<../../images/pico-tension-spring-source-sampled-coil-patch-native.png>).
4. Owned documents 730, 731 and 732 closed after persistence checks; unrelated Start document preserved.

## References — library

1. [Preserved source-native spring, library 275](<pico-tension-spring-manufacturer-source.md>).

## Sources — online

1. Manufacturer-linked STEP model, original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`. Selected source-closed derivative SHA-256 `4c3f3f99822ccfda56ce05f49f6cd0188497ca8c14328207438f27c233c9e630`.
2. Hiwonder suspended tracked chassis, manufacturer product and model-source context.
