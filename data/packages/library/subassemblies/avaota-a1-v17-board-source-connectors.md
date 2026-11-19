# Yuzuki Avaota-A1 v1.7 board with source connectors

1. **Library number** 311.
2. **Native drawing** [Avaota-A1 v1.7 board and source connectors](<avaota-a1-v17-board-source-connectors.dwg>).
3. **DWG SHA-256:** `99627762af6f0a796268cf33389a5ffd8ce8f6dfbcd0a1c155ae735ff3f28911`. DWG 2018, 3,032,756 bytes.
4. **State** SAVED AND SOURCE PLACEMENTS CHECKED. The installation exterior contains the source board and connectors. The TFT1 display exterior requires separate source geometry.
5. **Execution model** Actual identity unavailable.

## Technical specification

1. **Frame** Original v1.7 manufacturer STEP axes and origin, in millimetres. The substrate bottom is Z = 0 and top is Z = 1.183202 mm.
2. **Base** The 288 placed solids from the [earlier board stage, library 252](<avaota-a1-computer-exterior-stage.md>) supply the board and the earlier interfaces.
3. **RF1 antenna connector** BAT WIRELESS BWIPX-1-001E, STEP product 711544, 14 solids.
4. **CN2 audio jack** XKB Connectivity PJ-327A0-SMT, STEP product 724472, one solid.
5. **DC1 barrel power jack** XUNPU DC-044A-A200, STEP product 142254, six solids. The five original imported body IDs are 151757, 152917, 155111, 155779 and 156401. The recovered housing is body 142283.

## Verification

1. The 303 input solid instances retain their geometry payloads and placement matrices. The six added DC1 instances match their independently checked vertex sets with a recorded maximum residual of 0.0 mm in the board frame. The saved drawing contains 309 placed solid instances.
2. The DC1 housing retains the original source trims and occurrence position. Its 73 extrusion support surfaces use equivalent B-spline surfaces. Native readback matched all 278 faces, placed vertices and reciprocal coedges.
3. Incremental and final SAVE receipts confirmed the file path, byte count, SHA-256 and zero dropped entities. Inspection used current-document geometry records. Guarded closure passed.
4. [Isometric view](<../images/avaota-a1-v17-board-source-connectors-isometric.png>) and [XY view](<../images/avaota-a1-v17-board-source-connectors-XY.png>) show the checked native boundaries.

## Sources — online

1. Avaota-A1 manufacturer v1.7 STEP archive, member `3D_PCB1_2024-08-17.step`, SHA-256 `80560b3471ae01130e5d671fd85837e824fd1c22fbfe5bae4b5f4bbc36f9ac41`.
2. Avaota-A1 v1.7 manufacturer BOM, rows RF1, CN2 and DC1.
