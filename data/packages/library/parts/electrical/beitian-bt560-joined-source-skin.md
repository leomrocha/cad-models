# Beitian BT-560 joined source skin

1. **Library number:** 315.
2. **Plan model:** 24, Beitian BT-560 GNSS antenna exterior.
3. **Native drawing:** [Beitian BT-560 joined source skin](<beitian-bt560-joined-source-skin.dwg>).
4. **DWG SHA-256:** `706883046cce97218936e9ff91febc324dd6ef67157e8d3e7568aa561d98fac1`.
5. **State:** Partial source-traced exterior with open connector recess.
6. **Actual execution model:** unavailable.

## Technical specification

1. The Beitian revision 5.53 dimensioned drawing, dated January 2023, specifies 58.6 ± 0.3 mm overall length, Ø25.0 ± 0.3 mm barrel, Ø27.3 ± 0.3 mm collar and 16.10 ± 0.3 mm collar span.
2. The source-traced model uses the library 281 frame. Z follows the antenna axis from the rear collar plane at Z = 0 toward the tip at Z = 58.6 mm. X and Y are radial. The model retains the measured traced diameter of 27.255639 mm. The open SMA-J rim radius is a calibrated raster estimate of 3.791667 mm.
3. The joined exterior is a single native mesh with 1,153 vertices, 2,176 triangles and one 128-edge open rim. Welding 256 coincident seam edges preserves every original triangle's vertex positions and winding. The rear mounting-interface datums remain in library 306.

## Checks

1. The native mesh matches the checked source-derived arrays and original oriented triangles. The connector rim is the sole open boundary.
2. OpenCADStudio verified the final SAVE at 50,366 bytes with one Mesh, zero dropped entities and a passing audit. The saved file and geometry-derived inspection image were checked by SHA-256. Guarded closure of the owned construction document passed.
3. [Joined exterior and rear rim inspection view](<../../images/beitian-bt560-joined-source-skin.png>).

## Sources — online

1. Beitian BT-560 manufacturer product page.
2. Beitian revision 5.53 dimensioned drawing.

## References

1. [Library 281 original traced exterior and calibration](<beitian-bt560-raster-exterior-stage.md>).
2. [Library 306 rear mounting-interface datums](<../../standards/beitian-bt560-rear-mounting-interface-reference.md>).
