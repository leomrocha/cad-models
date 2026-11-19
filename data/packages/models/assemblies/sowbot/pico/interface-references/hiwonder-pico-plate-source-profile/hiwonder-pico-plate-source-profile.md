# Hiwonder Pico plate source-profile drawing

1. **Library number:** 246.
2. **CAD drawing:** [Hiwonder Pico plate source-profile drawing](<hiwonder-pico-plate-source-profile.dwg>).
3. **DWG SHA-256:** `739ad33b2bd3aa9ee2bd96880938786840562d882fe01a5f0e3e4ec67fbf1936`.
4. **Representation:** two-dimensional source-profile reference.
5. **Actual execution model:** unavailable.

## Technical specification

1. **Geometry:** 66 closed polylines: one 270 × 143 mm perimeter, 24 slots and 41 circular openings. Perimeter dimensions follow the drawing labels; opening positions and radii are raster reconstructions with recorded pixel uncertainty. Units mm; origin at the outline centre.
2. **Checks:** native save/reopen, profile count, closed profiles, millimetre units and XY extents PASS.
3. **Drawing review:** model-derived profile image inspected.
4. **Document closure:** both owned drawing documents closed; pre-existing documents preserved.
5. **Plan role:** These corrected profiles supply the [saved perforated planar 3D mesh](<../../parts/pico-upper-plate-planar-perforated-faceted-stage/pico-upper-plate-planar-perforated-faceted-stage.md>). Earlier native cutting attempts returned “the selected object no longer exists” and “the selected topology could not be cut safely”; their plate blank, cutter solids and failed-state DWG remain retained in the execution records.

## References — library

1. [Native profile image](<hiwonder-pico-plate-source-profile.png>).
2. [Vector drawing](<hiwonder-pico-plate-source-profile.svg>).

## Sources — online

1. Source hardware page.
2. RoboDoo dimensioned plate drawing.
