# Pico HRB 3S 6,000 mAh regular-wrap battery clearance reference

1. **Library number** 320.
2. **Native drawing** [HRB regular-wrap envelope](<hrb-3s-6000mah-regular-wrap-pico-clearance.dwg>).
3. **DWG SHA-256:** `edebde5b438531997e8420e02dfc040ca4b026bedd661f34fe28086091836e47`. DWG 2018, 30,332 bytes.
4. **State** Saved and geometry checked. Case clearance reference at the compared Pico position.
5. **Actual execution model** Unavailable.

## Technical specification

1. **Seller chart** HRB regular-wrap 3S, 11.1 V, 6,000 mAh, 50C and 419 g. Rectangular case envelope **155 × 48 × 27 mm**.
2. **CAD frame** Pico chassis frame. X forward, Y left, Z up from track ground. The pack length follows +X. The bottom centre is at (19.287945, 0.078085, 33.842676) mm.
3. **CAD bounds** X −58.212055 to 96.787945 mm, Y −23.921915 to 24.078085 mm and Z 33.842676 to 60.842676 mm. One closed case-clearance solid with a volume of 200,880 mm³.
4. **Fit result at the modeled position** The rigid envelope intersects seven Hiwonder source bodies. The intersection with lower formed plate 3108 is 772.92 mm³.

## Checks

1. The eight native corners match the transformed chassis-frame corners within 0.000001 mm. The solid has six planar faces and reciprocal closed topology.
2. Verified SAVE confirmed the path, size, SHA-256 and zero dropped entities. The [isometric view](<hrb-3s-6000mah-regular-wrap-pico-clearance-isometric.png>) was inspected and guarded closure passed.

## Sources — online

1. HRB seller dimensional chart, 3S regular-wrap row.
2. Hiwonder manufacturer chassis STEP, original battery case location and compared source bodies.
