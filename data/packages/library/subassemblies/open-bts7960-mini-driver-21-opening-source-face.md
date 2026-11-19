# Open BTS7960 Mini driver with Mini360 mounting slots

1. **Library number** 312.
2. **Native drawing** [Open BTS7960 Mini driver](<open-bts7960-mini-driver-21-opening-source-face.dwg>).
3. **DWG SHA-256:** `88cbee0a4a3df39fc11ff2cb7d22cd0e01e367c356c29db145b028f9801fd808`. DWG 2018, 296,971 bytes.
4. **State** SAVED AND SOURCE GEOMETRY CHECKED. The drawing contains a zero-thickness source board face and five connector occurrences.
5. **Execution model** Actual identity unavailable.

## Technical specification

1. **Board frame and outline** Original library 286 frame in millimetres, board face Z = 0. The retained source outline is 70.104 × 39.243 mm.
2. **Openings** The source-derived board face contains 21 openings, including the 17 original holes and four plated slots for U8, the underside Mini360 module. Each U8 slot is 0.9144 mm wide and 0.91948 mm long in Y, calculated from EasyEDA revision `d2e022f694a84285a6e31ba5a6f05354` at 0.254 mm per source unit. Source slot centres are at X = 28.702 and 38.354 mm, and Y = 13.970 and 29.464 mm.
3. **Source mesh and placements** 989 vertices, 1,029 triangles. The five terminals and all seven root placements match the [17-opening stage, library 286](<open-bts7960-source-connector-board-face-stage.md>). The two XH connector housings cross the source board plane in the retained placements. Their overlapping cross-sections are 44.66 mm² for the four-pin housing and 17.34 mm² for the three-pin housing at Z = 0.

## Verification

1. Native vertex and face arrays match the checked 21-opening source profile. The saved input library drawing retains its original SHA-256. Current records confirm that only the board-face geometry and its source metadata changed in the new assembly.
2. Verified SAVE confirmed the path, byte count and hash with zero dropped entities. Owned-document closure passed after inspecting the [XY view](<../images/open-bts7960-mini-driver-21-opening-source-face-XY.png>), [XZ view](<../images/open-bts7960-mini-driver-21-opening-source-face-XZ.png>) and [isometric view](<../images/open-bts7960-mini-driver-21-opening-source-face-isometric.png>).

## Sources — online

1. Original Open BTS7960 EasyEDA document, revision `d2e022f694a84285a6e31ba5a6f05354`.
2. Sowbot hardware table, source link for the first Mini driver.
