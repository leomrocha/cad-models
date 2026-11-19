# Pico two track loops with a shared source definition

1. **Library number** 304.
2. **Plan use** Assembly 2, step 8.
3. **Native drawing** [Pico shared track loops](<pico-two-track-loops-shared-source-installation.dwg>).
4. **DWG SHA-256:** `d1e5540143c5156ce2f24a6ea31e0fcd6c76cc144d5623a6fd3cc75f710b0fbd`. DWG 2018, 1,510,034 bytes.
5. **State** SAVED_SOURCE_GEOMETRY_AND_SIGNED_PLACEMENTS_CHECKED.
6. **Execution models** gpt-6.2-sol for saved-file readback. The model that built the two-track drawing is unavailable.

## Technical specification

Two Pico track loops share one stored block from library 269. Each installed loop has 59 solid links. The drawing uses manufacturer XYZ coordinates, in millimetres.

1. **Left placement** identity.
2. **Right placement** X reflection at the source chassis centre plane. The right reference has X scale −1, Y and Z scale 1, and X translation 18.05525179669725 mm. This value comes from the manufacturer STEP coordinate comparison.
3. **Geometry count** 59 stored solids, 118 installed solids and 9,676 installed source faces.

## Verification

1. The source STEP comparison found that all 59 mirrored links match the right loop's support surfaces, spline edges and oriented trim boundaries.
2. The native SAVE audit recorded zero dropped entities. OpenCADStudio read the saved drawing through a DXF 2018 diagnostic and retained the common block definition, both placements, and the signed right scale. The 118 installed source vertex sets match within 6.54e-13 mm.
3. Four views from the checked current records were inspected. The owned construction tab passed guarded closure.

## References

1. [Shared track geometry, library 269](<../parts/mechanical/pico-track-manufacturer-source.md>).
2. [XY view](<../images/pico-two-track-loops-shared-source-installation-XY.png>).
3. [XZ view](<../images/pico-two-track-loops-shared-source-installation-XZ.png>).
4. [YZ view](<../images/pico-two-track-loops-shared-source-installation-YZ.png>).
5. [Isometric view](<../images/pico-two-track-loops-shared-source-installation-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP. Source SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
