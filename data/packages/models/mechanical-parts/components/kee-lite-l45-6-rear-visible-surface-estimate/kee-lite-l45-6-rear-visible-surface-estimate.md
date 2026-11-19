# Kee Lite L45-6 rear visible surface estimate

1. **Library number:** 264.
2. **Plan component:** model 36 — Kee Lite L45-6 crossover fitting; partial exterior stage.
3. **Native model:** [Rear visible surface estimate](<kee-lite-l45-6-rear-visible-surface-estimate.dwg>).
4. **DWG SHA-256:** `50f04e795c8fc51ccc4eeea4caa41af504b8d683421a6dc17c72dadac0e66063`.
5. **Representation:** photo-reconstructed exposed cylindrical side strip, open zero-thickness Mesh; separate nominal Ø33.7 mm tube-section Circle reference.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Exposed strip:** reconstructed outer radius 21.56228814 mm, axial span 8.36134576 mm, 66 vertices and 64 triangles. Angular range is 150.175132°…180° in the local rear-tube frame. The small angular patch follows the photograph's exposed left side and ends at its visible occlusion boundary.
2. **Frame:** millimetres; rear tube axis +Z, local X image-right at the tangent and +Y towards the visible front. Z = 0 is the selected upper strip point. The strip extends towards negative Z. The nominal tube-section reference has radius 16.85 mm at Z = 0.
3. **Photographic scale:** nominal tube Ø33.7 mm divided by its 118 px lateral span gives 0.28559322 mm/px. The exposed outer collar span is 151 px, producing estimated diameter 43.12457627 mm. With ±1 px per selected endpoint for both spans, the diameter reconstruction interval is 41.84416667…44.44913793 mm.
4. **Axial estimate:** exposed source strip from [120,151] to [120,179] px. A seven-point visible rim-arc ellipse fit has axes 119.26463318 × 34.84087753 px and projected axial factor 0.95637836 under the circular-section/weak-perspective reconstruction. This gives 8.36134576 mm. A recorded 2,000-sample ±1 px ellipse-pick sensitivity calculation gives axial range 7.49391945…10.09607549 mm including strip/calibration endpoint variation; this is a sampled reconstruction range.
5. **Nominal tube reference:** Ø33.7 mm identifies the supported tube. The separate Circle represents that nominal tube section. The photograph's dark lip span is retained as an image observation in the reconstruction recipe.
6. **Manufacturer dimensions:** D = 44 mm is the front collar axial span; E = 40 mm is projected tube-axis offset. Both remain dimensional metadata and are preserved in library 258.
7. **Family-drawing calibration:** D-based and E-based scales are 0.24581006 and 0.23529412 mm/px, differing by 4.469274%. Applying them to the drawing circle yields diameters 37.36312849 and 35.29411765 mm. The surface radius above uses the photograph with its own nominal-tube calibration.
8. **Reconstruction assumptions:** circular rear-collar section and weak-perspective photographic scale. The delivered geometry represents the exposed surface strip; the nominal tube section remains a separate reference entity.

## Checks and views

1. **Native geometry:** exact prepared vertex and triangle arrays, Mesh subdivision 0, millimetre units and all source metadata PASS after reopening.
2. **Surface topology:** connected open disk; every edge has incidence 1 or 2; Euler characteristic 1. The Mesh has zero thickness.
3. **Persistence:** incremental checkpoint immediately after import, verified DWG-context checkpoint and final save/reopen PASS; zero dropped entities; original source images and library 258 hash unchanged.
4. **Views:** four boundary projections saved; isometric inspected from reopened Mesh records.
5. **Cleanup:** owned documents 688, 689 and 690 closed; unrelated documents preserved.

## References — library

1. [Supplier dimensional reference — library 258](<../../../interface-references/mechanical/kee-lite-l45-6-supplier-dimension-reference/kee-lite-l45-6-supplier-dimension-reference.md>).
2. [Isometric surface/reference view](<kee-lite-l45-6-rear-visible-surface-estimate-isometric.png>).
3. [Photographic measurement overlay](<kee-lite-l45-6-photo-measurement-overlay.png>).

## Sources — online

1. Exact L45-6 supplier listing, retained product photograph, nominal tube diameter and family dimension diagram.
2. Kee Safety catalogue, printed page 28, exact L45-6 row: tube reference 6, D = 44 mm, E = 40 mm.
3. Retained family dimension figure.
