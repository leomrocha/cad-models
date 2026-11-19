# Mini Sowbot layout with updated Brain, driver and battery clearance

1. **Plan identity** Assembly 6, Mini Sowbot, hardware layout proposal.
2. **Native drawing** [Mini assembly with updated Brain](<mini-battery-driver-and-brain-layout-proposal.dwg>).
3. **DWG SHA-256:** `cfec381db8b5e347857d57d84b831a3eb2f841a90fe79de6fbc8ed98899891ba`. DWG 2018, 9,583,180 bytes.
4. **Execution model** Actual identity unavailable.

## Technical specification

1. **Brain placement** The updated Brain is installed at root `8E0`, with identity rotation and X = 0 mm, Y = +20 mm, Z = 0 mm. It contains both 309-solid Avaota-A1 boards and their RF1, CN2 and DC1 connectors.
2. **Other roots** The base footprint, library 312 Open BTS7960 driver and 306 × 174 × 220 mm Propow CPN24050 clearance solid retain their geometry and placements. The driver has 21 openings and five connector occurrences. The projected battery lift gap to the driver remains 136 mm.
3. **Live geometry** Four roots expand to 1,138 geometry occurrences: 953 solids, 147 meshes, 31 circles and seven lightweight polylines.

## Verification

1. Independent native-record checks matched all 1,084 Brain geometry occurrences and composed placement matrices to the updated Brain source. The previous Brain handle `46F` is erased.
2. The retained base, all 52 driver geometry occurrences and the six-face battery solid matched their previous records.
3. Final SAVE verified the drawing hash, bytes, zero dropped entities and geometry epoch. The [isometric view](<../../../../images/sowbot/mini-battery-driver-and-brain-layout-proposal-isometric.png>) was inspected before guarded closure.

## References

1. [Updated Brain source](<brain-avaota-source-connectors-layout-proposal.md>).
2. [Previous Mini battery and driver layout](<mini-battery-and-driver-layout-proposal.md>).
3. [Four-root occurrence BOM](<../../../../docs/sowbot/bom/mini-updated-brain-occurrences.csv>).
4. Independent saved drawing check.

## Sources — online

1. Sowbot Mini hardware table.
2. Open BTS7960 EasyEDA PCB.
3. Propow CPN24050 clearance dimensions.
