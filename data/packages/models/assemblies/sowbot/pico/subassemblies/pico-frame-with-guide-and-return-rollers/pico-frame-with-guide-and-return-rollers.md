# Pico frame with guide wheels and upper return rollers

1. **Library number** 302.
2. **Plan use** Assembly 2, steps 4 and 6.
3. **Native drawing** [Pico frame with guide wheels and upper return rollers](<pico-frame-with-guide-and-return-rollers.dwg>).
4. **DWG SHA-256:** `e9b04ba43a2c67f71a3cf21fae83f4202e8759f5771db69b9410d127fcb78feb`. DWG 2018, 5,617,847 bytes.
5. **State** SAVED_SOURCE_GEOMETRY_CHECKED.
6. **Execution models** gpt-6.2-sol for the assembly write and saved-file checks. The model that built the four-body guide group is unavailable.

## Technical specification

The drawing combines library 301 with two guide end wheels and two upper return rollers in manufacturer XYZ coordinates, in millimetres. It carries the original frame, both drive groups and the eight lower suspension positions.

1. **Left guide end wheel** source body 3176, library 272, 36 faces.
2. **Left upper return roller** source body 3170, matches library 273's template body 3180, 24 faces.
3. **Right guide end wheel** source body 3310, 36 faces.
4. **Right upper return roller** source body 3304, 24 faces.

## Verification

1. OpenCADStudio wrote the guide group into a new DWG using library 301 as the WBLOCK template. The completed write, path, file size and SHA-256 passed. The input library 301 hash remained the same.
2. An OpenCADStudio 2018 DXF diagnostic readback of the native drawing retained 16 Model Space inserts, 54 stored solids, 66 placed solids, 4,861 faces and the expected body groups. Closes on paired coedges passed for every solid. All installed vertex sets matched the manufacturer STEP within 1.53e-13 mm.
3. Four boundary views from the saved drawing's diagnostic records were inspected. The views show 2,722 trim edges by their endpoints. The owned guide staging tab and both temporary left source tabs passed guarded closure.

## References

1. [Frame and lower suspension, library 301](<../pico-frame-drives-lower-suspension-source-group/pico-frame-drives-lower-suspension-source-group.md>).
2. [Guide end wheel, library 272](<../../parts/pico-end-wheel-manufacturer-source/pico-end-wheel-manufacturer-source.md>).
3. [Roller definition, library 273](<../../parts/pico-lower-roller-manufacturer-source/pico-lower-roller-manufacturer-source.md>).
4. [XY view](<pico-frame-with-guide-and-return-rollers-XY.png>).
5. [XZ view](<pico-frame-with-guide-and-return-rollers-XZ.png>).
6. [YZ view](<pico-frame-with-guide-and-return-rollers-YZ.png>).
7. [Isometric view](<pico-frame-with-guide-and-return-rollers-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP. Original STEP SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
