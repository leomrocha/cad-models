# Pico frame, drives and lower suspension

1. **Library number** 301.
2. **Plan use** Assembly 2, steps 2–5 and 7.
3. **Native drawing** [Pico frame, drives and lower suspension](<pico-frame-drives-lower-suspension-source-group.dwg>).
4. **DWG SHA-256:** `f2d1d4da4481c1d58fd01e76eb5f6926c8491d1944336b4a73325df6c8f98487`. DWG 2018, 5,581,348 bytes.
5. **State** SAVED_CURRENT_SOURCE_GEOMETRY_CHECKED.
6. **Actual execution model** gpt-6.2-sol.

## Technical specification

The drawing places the fixed frame and both drive groups from library 300 with eight lower suspension groups. Each suspension group contains one arm and one lower roller. Four left groups reuse library 294 and four right groups reuse library 296. The drawing uses the manufacturer STEP coordinate frame in millimetres.

Thirteen Model Space block references expand to 62 solid occurrences. The original five frame and drive references retain 46 solids. The eight suspension references add 16 occurrences using four stored solids. All 62 placed vertex sets match their corresponding manufacturer bodies within 1.53e-13 mm. Face counts and closed coedge pairs passed for 4,741 source faces. The original frame and drive solid payloads and all eight suspension placement matrices passed native comparison.

## Persistence and views

1. SAVE verified the drawing path, byte size and hash. The native save audit recorded 50 stored 3D solids, 19 total block references and zero dropped entities.
2. Four views derived from the current native records were inspected. The views show 2,722 trim edges by their endpoints.
3. The two suspension source tabs and the owned frame construction tab were closed after save and checks.

## References

1. [Fixed frame and drives, library 300](<../pico-fixed-frame-and-drive-source-group/pico-fixed-frame-and-drive-source-group.md>).
2. [Left suspension arm and lower roller, library 294](<../pico-left-suspension-arm-roller-source-group/pico-left-suspension-arm-roller-source-group.md>).
3. [Right suspension arm and lower roller, library 296](<../pico-right-suspension-arm-roller-source-group/pico-right-suspension-arm-roller-source-group.md>).
4. [XY view](<pico-frame-drives-lower-suspension-source-group-XY.png>).
5. [XZ view](<pico-frame-drives-lower-suspension-source-group-XZ.png>).
6. [YZ view](<pico-frame-drives-lower-suspension-source-group-YZ.png>).
7. [Isometric view](<pico-frame-drives-lower-suspension-source-group-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP. Source SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.

## Related model documentation

[Pico suspension pivots and roller axes](pico-suspension-pivot-registration.md).
