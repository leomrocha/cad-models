# Pico geared motor — primary exterior stage

1. **Library number:** 247.
2. **Plan component:** model 13, Hiwonder Pico geared motor.
3. **CAD file:** [Partial motor exterior](<pico-gearmotor-primary-exterior-stage.dwg>).
4. **DWG SHA-256:** `573358626fe24c7795faa954ea38b876d38b29e33945fb53eca2fbf1444d7240`.
5. **Status:** PARTIAL_SAVED_REOPENED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Represented geometry:** five separate closed solids: rear motor can, front motor can, rounded gearbox case, output-bearing boss and nominal circular output shaft.
2. **Printed dimensions from the RoboDoo motor drawing:** rear can diameter 34.00 mm; rear and front can axial lengths 12.40 and 22.75 mm; gearbox front face 64.40 × 38.00 mm; gearbox depth 12.01 mm; boss diameter 12.00 mm and projection 2.50 mm; output-axis offset 12.93 mm from the left face edge.
3. **Raster estimates measured from that same motor drawing:** front motor-can diameter 32.7561 mm from a 158-pixel span against the rear can's 164 pixels / 34 mm. Gearbox corner radius 9.7617 mm from a 47-pixel corner and 310 × 183 pixel face spans. Pixel-pick uncertainty: ±2 pixels. These are raster estimates.
4. **Frame:** drawing millimetres; gearbox front face Z=0; +Z points toward the output shaft; motor axis X=Y=0; output axis X=−19.27 mm, Y=0.
5. **Saved-stage checks:** five closed-body topology checks, source-bound axial spans, cylinder radii/axes and gearbox bounds PASS. Native save/reopen and retained file hash PASS. Four boundary views inspected. Both owned OCS tabs closed.
6. **Output shaft stage:** Hiwonder identifies motor JGB3865-520R45-12 and a 6 mm D-shaped eccentric shaft. This saved stage uses a nominal circular shaft of diameter 6 mm from Z=2.50 to Z=13.10 mm, using the boss and tip dimensions printed in the RoboDoo drawing.
7. **Required exterior features:** shaft flat and mounting interfaces.

## References — library

1. [Isometric stage view](<../../images/pico-gearmotor-round-shaft-stage-isometric.png>).
2. [Front profile view](<../../images/pico-gearmotor-round-shaft-stage-XY.png>).
3. [Longitudinal view](<../../images/pico-gearmotor-round-shaft-stage-XZ.png>).

## Sources — online

1. Hiwonder suspended tracked chassis.
2. RoboDoo dimensioned motor drawing.
