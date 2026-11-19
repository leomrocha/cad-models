# Brain layout proposal with updated Avaota source connectors

1. **Plan identity** Assembly 4, Brain electronics, partial hardware layout proposal.
2. **Native drawing** [Brain assembly with updated Avaota boards](<brain-avaota-source-connectors-layout-proposal.dwg>).
3. **DWG SHA-256:** `46652f78828a449f8f435809add298a3d2727fa5ad77caa4ae3b6ec51b3e2c25`. DWG 2018, 7,440,102 bytes.
4. **Execution model** Actual identity unavailable.

## Technical specification

1. **Computer placements** Two Yuzuki Avaota-A1 v1.7 boards from library 311. Each has 309 placed solids, including the RF1 antenna connector, CN2 audio jack and DC1 barrel power jack. Both use identity rotation and X = 0.001424 mm, Y = 6.626946 mm. The lower board is at Z = −2.383202 mm, and the upper at Z = 22.731787 mm. These are proposal placements in the previous Brain frame.
2. **Other placed hardware** The existing LEVIA-H7 control board, two SparkFun receivers, ORP mounting-plate face, two Beitian antenna exteriors and circular panel-switch reference retain their geometry and positions.
3. **Live assembly structure** Nine root occurrences expand to 1,084 geometry occurrences: 952 solids, 131 meshes and one circle.
4. **Projected installation geometry** At the saved positions the sampled board-root boxes retain a 5 mm minimum separation. The lowest added DC1 feature is 5.800 mm above the ORP face. These checks use sampled bounds and the source connector geometry.

## Verification

1. OpenCADStudio saved both library 311 occurrences at the existing placements. The live root handles are `6AD` for the lower board and `6AE` for the upper board. Exact entity queries confirmed the two previous board handles were erased.
2. Independent checks matched all 618 Avaota solid payloads and placements against library 311 and all seven other live roots against the previous layout, including the geometry and placement of their descendants.
3. Incremental and final SAVE receipts confirmed the DWG path, byte count, hash and zero dropped entities. The [top-isometric view](<../../../../images/sowbot/brain-avaota-source-connectors-layout-proposal-isometric.png>) was inspected before guarded closure.

## References

1. [Nine-root occurrence BOM](<../../../../docs/sowbot/bom/brain-avaota-source-connectors-occurrences.csv>).
2. [Library 311 Avaota-A1 board](<../../../../library/subassemblies/avaota-a1-v17-board-source-connectors.md>).
3. [Previous Brain proposal](<brain-receiver-exterior-layout-proposal.md>).
4. Saved-model and geometry evidence.
5. Source-supported placement projection.

## Sources — online

1. Sowbot Brain hardware description.
2. Yuzuki Avaota-A1 v1.7 manufacturer STEP archive.
