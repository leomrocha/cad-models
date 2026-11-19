# Mini Sowbot battery and driver layout proposal

1. **Plan identity** Assembly 6, Mini Sowbot.
2. **Native drawing** [Mini battery and driver layout](<mini-battery-and-driver-layout-proposal.dwg>).
3. **DWG SHA-256:** `95a949908ec10e389784a8476de106beafe48d2360405893c9571f77a1a806da`. DWG 2018, 4,732,886 bytes.
4. **Execution model** Actual identity unavailable.

## Technical specification

1. **Installed driver** Library 312, Open BTS7960 Mini driver with the 21-opening source face. The driver retains its placement at X = −200 mm, Y = +100 mm and Z = 0. All five connector occurrences retain their previous positions.
2. **Battery reference** One Propow CPN24050 24 V 50 Ah clearance solid, 306 × 174 × 220 mm. Its original root and position are retained. Both source height cases use the same footprint.
3. **Other placements** Original Mini planar base reference and existing shared Brain proposal. Current CAD has four live assembly roots, identified in the occurrence BOM.
4. **Service clearance** The driver retains 136 mm projected gap from the straight +Z battery lift. Its lowest terminal remains Z = −3.7999924 mm relative to the planar base datum.

## Verification

1. One checked native mesh now represents the 21 openings, with its 989 vertices and 1,029 triangles matching the library arrays. Its path is driver root `4BA`, board insert `4B3`, mesh `4AF`.
2. All four root placements, the driver block definitions, and the driver geometry records outside that face matched the current baseline. Source metadata was updated on the driver root and face.
3. Incremental and final SAVE receipts confirmed the path, bytes, file hash and zero dropped entities. The [top-isometric view](<../../../../images/sowbot/mini-battery-and-driver-layout-proposal-isometric.png>) was inspected before guarded closure.

## References

1. [Previous battery clearance proposal](<mini-hardware-battery-envelope-layout-proposal.md>).
2. [Library 312 Mini motor driver](<../../../../library/subassemblies/open-bts7960-mini-driver-21-opening-source-face.md>).
3. Four-root occurrence BOM.
4. Native placement and geometry checks.

## Sources — online

1. Sowbot Mini hardware table.
2. Open BTS7960 EasyEDA PCB.
3. Propow CPN24050 clearance dimensions.
