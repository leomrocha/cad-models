# Open BTS7960 Mini motor driver screw-tool entry openings

1. **Library number** 322.
2. **Native drawing** [Six screw-tool entry openings](<open-bts7960-terminal-tool-entry-reference.dwg>).
3. **DWG SHA-256:** `e089830b6136b8c31b5c8d4cf564762df64adfcdf5835b413ec6a3cdbe4a95be`. DWG 2018, 30,398 bytes.
4. **Execution and checking models** Actual identities unavailable.

## Technical specification

1. Three source two-pin screw terminals on the Open BTS7960 Mini driver have two tool openings each. The drawing retains all six native positions in the library 312 board frame. Z = **9.999980 mm** above the reference board face. The six opening axes point along +Z.
2. Each contour reproduces 40 original mesh vertices. The radius to the vertices is **1.799996 mm** and the minimum centre-to-facet distance is **1.794447 mm**. The drawing supplies the opening contours and axes for a future tool fit check.
3. **Board XY centres** in millimetres.
   - **P1 pin 1, OUT1** (16.470495, 35.814025) mm.
   - **P1 pin 2, OUT2** (11.470505, 35.814025) mm.
   - **P2 pin 1, OUT3** (57.872495, 35.687025) mm.
   - **P2 pin 2, OUT4** (52.872505, 35.687025) mm.
   - **P3 pin 1, GND** (32.570504, 34.289975) mm.
   - **P3 pin 2, VCC** (37.570494, 34.289975) mm.

## Verification

1. Checked the exact source mesh, source PCB revision and three connector matrices against saved native library 312 records. The 240 native points match the source loops within 0.000001 mm.
2. Incremental verified SAVE, final path and hash, zero dropped entities and owned-tab closure passed. The [view from saved native records](<open-bts7960-terminal-tool-entry-reference.png>) was inspected.

## Sources — online

1. Original EasyEDA Open BTS7960 board, revision `d2e022f694a84285a6e31ba5a6f05354`.
2. Original two-pin terminal source mesh.

## References

1. [Open BTS7960 Mini driver, library 312](<../../../assemblies/reusable/subassemblies/open-bts7960-mini-driver-21-opening-source-face/open-bts7960-mini-driver-21-opening-source-face.md>).
