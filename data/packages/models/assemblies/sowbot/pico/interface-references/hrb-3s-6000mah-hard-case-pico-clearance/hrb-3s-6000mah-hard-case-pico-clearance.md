# Pico HRB 3S 6,000 mAh hard-case battery clearance proposal

1. **Library number** 313.
2. **Native drawing** [HRB hard-case clearance solid](<hrb-3s-6000mah-hard-case-pico-clearance.dwg>).
3. **DWG SHA-256:** `f78aebc41ff25fd707143ef87b2652d1d5dcab2eb86edfa93542ee1004075329`. DWG 2018, 30,300 bytes.
4. **State** SAVED AND SOURCE POSITION CHECKED. Rectangular clearance envelope for the tested static placement.
5. **Execution model** Actual identity unavailable.

## Technical specification

1. **Seller chart** HRB hard case, 11.1 V, 3S, 6,000 mAh, 50C, 425 g. The listed case is 138 × 46 × 39 mm.
2. **Model frame** Saved Pico chassis coordinates in millimetres. X points forward, Y left and Z up from track ground. Pack length follows +X. The centre of its bottom face is at X = 19.287945 mm, Y = 0.078085 mm and Z = 33.842676 mm.
3. **Bounds** X = −49.712055 to 88.287945 mm, Y = −22.921915 to 23.078085 mm, and Z = 33.842676 to 72.842676 mm. The geometric envelope volume is 247,572 mm³.
4. **Scope** One rigid case-clearance solid at the tested proposal position. Terminals, leads and retention surfaces belong to the separate installed-pack source geometry.

## Verification

1. All eight native corners match the transformed source-clearance corners at the recorded precision. The solid has six planar faces, one shell and 24 reciprocal coedges.
2. Verified SAVE confirmed the path, byte count, hash and zero dropped entities. The [isometric view](<hrb-3s-6000mah-hard-case-pico-clearance-isometric.png>) was inspected before guarded closure.

## Sources — online

1. HRB seller dimensional chart, the hard-case 11.1 V, 6,000 mAh and 50C row.
2. Hiwonder manufacturer chassis STEP, source case location and chassis frame.
