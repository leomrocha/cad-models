# Pico tracked running gear

1. **Library number** 305.
2. **Plan use** Assembly 2, steps 2–8.
3. **Native drawing** [Pico tracked running gear](<pico-tracked-running-gear-source-group.dwg>).
4. **DWG SHA-256:** `92e79a296a5884f952f1955b9eece64454cf78f88f66109e7fa7ec49362ef6ff`. DWG 2018, 7,098,159 bytes.
5. **State** SAVED_SOURCE_GEOMETRY_AND_TRACK_PLACEMENTS_CHECKED.
6. **Execution models** gpt-6.2-sol for saved-file readback and views. The model that wrote the native assembly is unavailable.

## Technical specification

The group combines the Pico fixed frame, both gearmotors and sprockets, eight lower suspension arm–roller pairs, two guide end wheels, two upper return rollers and two track loops. The drawing retains the manufacturer XYZ frame in millimetres.

1. **Frame and wheels** 16 roots and 66 installed solids from library 302.
2. **Track placement** two roots share the 59-link definition from library 304. The saved right root retains the X reflection and the 18.05525179669725 mm source translation.
3. **Drawing totals** 18 Model Space roots, 113 stored solids, 184 installed solids and 14,537 installed source faces.

## Verification

1. OpenCADStudio wrote the two track references into a new DWG using library 302 as the WBLOCK template. The completed write, path, file size and SHA-256 passed. Library 302 retained its source hash.
2. The OpenCADStudio 2018 DXF diagnostic readback confirmed the original 16 source groups, two track placements, one shared track definition, and the signed right scale. All closed coedge checks passed. The maximum installed source vertex error was 6.54e-13 mm.
3. Four saved-file boundary views were inspected, including track alignment around the sprockets and rollers at the manufacturer source positions. The views show 2,722 trim edges by their endpoints. The owned track staging tab passed guarded closure.

## References

1. [Frame and guide wheels, library 302](<../pico-frame-with-guide-and-return-rollers/pico-frame-with-guide-and-return-rollers.md>).
2. [Shared track loops, library 304](<../pico-two-track-loops-shared-source-installation/pico-two-track-loops-shared-source-installation.md>).
3. [XY view](<pico-tracked-running-gear-source-group-XY.png>).
4. [XZ view](<pico-tracked-running-gear-source-group-XZ.png>).
5. [YZ view](<pico-tracked-running-gear-source-group-YZ.png>).
6. [Isometric view](<pico-tracked-running-gear-source-group-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP. Source SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
