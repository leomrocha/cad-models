# Pico expansion plate and four spacer hypotheses — partial stage

1. **Plan assembly:** 2 — Pico tracked chassis partial exterior stage.
2. **Native file:** [Registered plate and spacer stage](<pico-expansion-plate-spacer-partial-stage.dwg>).
3. **DWG SHA-256:** `dcf05df4076ba4fef6a4b9ed4100e9f03d1414150baa972ea7160e92fe74a892`.
4. **Representation:** one existing perforated plate mesh and four existing cylindrical spacer exterior hypotheses.
5. **Frame:** millimetres; original plate X longitudinal, Y transverse, Z up. Plate underside Z = 0 mm; plate top Z = 2 mm. Spacer upper exposed end planes seat at Z = 0 mm.
6. **Actual execution model:** unavailable.

## Installed components

All occurrence matrices are `[[1,0,0,X],[0,1,0,Y],[0,0,1,Z],[0,0,0,1]]`; translations below use millimetres.

| Library number / readable component | Quantity | Source DWG SHA-256 | Root X, Y, Z (mm) |
|---|---:|---|---|
| 262 / Pico 270 × 143 mm planar perforated expansion plate | 1 | `a71716d3e800d15b3f4414fff8746e11f9bc29bf6b2444a2888c3ffa4371fb3c` | [0, 0, 0] |
| 256 / Pico spacer hypothesis 1 — cylindrical exterior estimate | 1 | `550bc29c109ab4e0ee0485d77668d4ed92d75612bd6aaac62f920bd0d39cdfa7` | [-93.70588235294117, 31.16666666666667, -25.4643007] |
| 256 / Pico spacer hypothesis 2 — cylindrical exterior estimate | 1 | `550bc29c109ab4e0ee0485d77668d4ed92d75612bd6aaac62f920bd0d39cdfa7` | [-93.70588235294117, -30.904761904761905, -25.4643007] |
| 256 / Pico spacer hypothesis 3 — cylindrical exterior estimate | 1 | `550bc29c109ab4e0ee0485d77668d4ed92d75612bd6aaac62f920bd0d39cdfa7` | [93.1764705882353, 34.30952380952381, -25.4643007] |
| 256 / Pico spacer hypothesis 4 — cylindrical exterior estimate | 1 | `550bc29c109ab4e0ee0485d77668d4ed92d75612bd6aaac62f920bd0d39cdfa7` | [93.1764705882353, -33.785714285714285, -25.4643007] |

## Source registration and placement

1. **Plate identity:** 65 existing openings registered against the elevated expansion plate in the manufacturer orthographic drawing: 24 slots and 41 circular openings. Eight independently picked outline corners determine scale/translation. Features 3, 6, 43 and 64 select mirror orientation; the other 61 features validate the registration independently.
2. **Raster mapping:** image u = 344.25 − 2.41773905548 Y; image v = 612.846292276 + 2.38947993517 X. Image coordinates use pixels and plate coordinates use millimetres. Outline RMS residual = 1.628736 px; maximum = 2.947609 px. Across all opening boundary samples, 99.6126% lie within 2 px of source ink. The existing trace retains its original coordinate uncertainty.
3. **Opening visibility:** four openings are covered by fastener heads. Their fastener axes are measured separately; hole radius is retained from the dimensioned source profile. Other contours retain individual closed-component or underdrawing boundary-support evidence.
4. **Post axes:** source openings 30, 45, 25 and 46 identify four post positions. Independent inverse-registration centre differences are at most 0.632105 mm longitudinal and 0.426163 mm transverse. The photograph shows three gold post bodies and an occluded fourth position; plate silhouette and opening-group overlay inspected.
5. **Spacer section:** existing library 256 remains the original estimated Ø8.76639860 mm cylindrical exterior with exposed length 25.46430070 mm. Four-axis front-projection diagnostic gives RMS edge residual 3.485170 px for that diameter; an illustrative Ø6 mm cylindrical diagnostic gives 1.083400 px. The diameter diagnostics retain hypothesis status. This saved stage preserves the existing spacer geometry and source uncertainty.

## Automated checks and views

1. **Native source profiles:** all 65 native polyline centres and arc radii match the corrected source recipe.
2. **Saved geometry:** reopened plate Mesh properties match all 8,792 vertices and 17,840 faces exactly. All 28 original spacer geometry/topology SAB records and analytic features match after accounting for INSERT's added explicit identity transform. Each spacer has closed reciprocal topology.
3. **Placement and metadata:** five occurrence matrices, readable component identities, source pins and source metadata PASS after reopening.
4. **Persistence:** final DWG save/reopen and SHA-256 PASS; zero dropped entities. Incremental checkpoints retained after each insertion/metadata step.
5. **Views:** four model boundary projections saved; isometric inspected. Native capture completed through same-ID recovery; pixel identity review failed because the image contained a non-model application surface. Boundary views supply the delivered geometry images.
6. **Cleanup:** owned assembly documents 685/686 and source-read document 687 closed; unrelated documents preserved.

## References — library and project

1. [Planar perforated plate — library 262](<../../parts/pico-upper-plate-planar-perforated-faceted-stage/pico-upper-plate-planar-perforated-faceted-stage.md>).
2. [Spacer exterior hypothesis — library 256](<../../parts/pico-plate-support-spacer-raster-exterior/pico-plate-support-spacer-raster-exterior.md>).
3. [Isometric boundary view](<view-1.png>).
4. 65-opening drawing overlay.
5. Photograph registration overlay.

## Sources — online

1. Manufacturer hiwonder-21030156-image-1_2.jpg, retained original and SHA-256 recorded in registration evidence.
1. Manufacturer hiwonder-21030156-image-3.jpg, retained original and SHA-256 recorded in registration evidence.
1. Dimensioned plate drawing, 270 × 143 mm silhouette and opening profiles.
1. Hiwonder tracked chassis, retained 2 mm plate-thickness specification.
