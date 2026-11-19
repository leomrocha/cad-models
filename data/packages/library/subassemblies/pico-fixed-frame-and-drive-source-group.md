# Pico fixed frame and drive source group

1. **Library number:** 300.
2. **Plan use:** Assembly 2, steps 2, 3, 4 and 7.
3. **Native drawing:** [Pico fixed frame and drive source group](<pico-fixed-frame-and-drive-source-group.dwg>).
4. **DWG SHA-256:** `042760c7919ef6f16e00136b79f4fb5d25626756911c164b3e7b1c5815310440`. DWG 2018, 5,548,046 bytes.
5. **State:** SAVED_CURRENT_SOURCE_GEOMETRY_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

The group contains a lower formed plate, two handed side carriers, an upper expansion plate, four hex spacers, two gearmotors and two whole drive sprockets. The drawing preserves their manufacturer STEP positions in XYZ and millimetres.

| Source library | Model Space roots | Original source solids | Placement |
| --- | ---: | ---: | --- |
| 293, left motor and drive sprocket | 2 | 19 | The original motor and sprocket roots are individually placed in manufacturer XYZ from the saved chassis transforms. |
| 295, right motor and drive sprocket | 1 | 19 | Identity. |
| 297, upper expansion plate and four hex spacers | 1 | 5 | Identity. |
| 298, lower formed plate and two handed side carriers | 1 | 3 | Identity. |

The left motor origin is `[−42.2826890439483, −89.9496630935861, 64.6359015567724]` mm, with local axes mapped to manufacturer +Y, −Z and −X. The left sprocket origin is `[−68.3826890439483, −89.9496630935861, 64.6359015567724]` mm, with local axes mapped to manufacturer +Y, +Z and +X.

## Verification

1. Five Model Space roots retain 46 distinct source solids and 4,397 source faces. All 46 placed vertex sets match the manufacturer STEP. The largest bidirectional vertex error is 1.65 × 10⁻¹⁴ mm. All face counts and reciprocal closed coedge checks passed. Solid payload fingerprints matched across the native transfers from the opened source copies. The original source-stage records and final drawing can use different ACIS encodings.
2. The original lower-frame paste completed under its original request identity and was checkpointed before the final save. The final save verified the expected path, byte size, SHA-256 and audit with zero dropped entities. Persistence verification uses SAVE only. Guarded closure of the four owned construction documents passed. Start document 1 was preserved.
3. Four views represent all 46 placed solids using 12,123 recorded edges. The views show 2,714 trim edges by their endpoints. XY, XZ, YZ and isometric pixels were inspected.

## References

1. [Left gearmotor and sprocket, library 293](<pico-left-gearmotor-sprocket-source-group.md>).
2. [Right gearmotor and sprocket, library 295](<pico-right-gearmotor-sprocket-source-group.md>).
3. [Upper expansion plate and four hex spacers, library 297](<pico-upper-plate-four-spacers-source-group.md>).
4. [Lower formed plate and side carriers, library 298](<pico-lower-plate-carriers-source-group.md>).
5. [XY view](<../images/pico-fixed-frame-and-drive-source-group-XY.png>).
6. [XZ view](<../images/pico-fixed-frame-and-drive-source-group-XZ.png>).
7. [YZ view](<../images/pico-fixed-frame-and-drive-source-group-YZ.png>).
8. [Isometric view](<../images/pico-fixed-frame-and-drive-source-group-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP. Original STEP SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
