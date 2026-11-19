# Sowbot Mini footprint and Brain board layout proposal

1. **Plan assembly:** 6 — saved partial footprint and board layout proposal.
2. **Native file:** [Mini footprint and board layout proposal](<mini-board-footprint-layout-proposal.dwg>).
3. **DWG SHA-256:** `60f4d2ed0294c15485a4799f5284876de4eaf7b7d573d26d71edfb693a15548d`.
4. **Representation:** one closed 450 × 490 mm planar source footprint and one placed partial Brain board-layout occurrence containing five board occurrences and 910 nested construction-solid occurrences.
5. **Coordinate frame:** millimetres; footprint centre is [0, 0, 0] mm; X represents the first source dimension, Y the second, and Z is up.
6. **Placement status:** PROPOSAL — partial Brain board-layout root at [0, 0, 0] mm with original local board placements retained.
7. **Actual execution model:** unavailable.

## Installed occurrences

Each proposed root matrix is `[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]` in the millimetre frame.

| Occurrence | Library number / readable component | Quantity | Source DWG SHA-256 | Root handle |
|---|---|---:|---|---|
| Planar footprint | 245 / Sowbot Mini chassis footprint reference | 1 | `d890c11303d90da0a029a2d23cf11c64a82e084c68e4411910c0921f7ff66b3d` | `85` |
| Partial Brain layout | Project assembly 4 / five-board layout proposal | 1 | `2926eb40290bbc7d26854aa85d2e5d96c074346098dcb3759d3000ca7f3ab6c6` | `5F5` |

The Brain occurrence contains library 252 Yuzuki Avaota-A1 v1.7 computer exterior, quantity 2; library 249 LEVIA-H7 control board exterior, quantity 1; and library 250 SparkFun NEO-F9P carrier/module, quantity 2. Their exact source hashes and local root matrices are listed in [the Brain layout companion](<brain-board-layout-proposal.md>).

## Automated checks and inspected views

1. **Source footprint:** PASS — one closed polyline with exact source points [−225, −245], [225, −245], [225, 245], [−225, 245] mm and identity root transform.
2. **Board geometry:** PASS — all 910 nested solid occurrences retain their complete source-native noncommon geometry and nested matrices after reopening.
3. **Root metadata:** PASS — names, source hashes and proposal placements retained for both installed occurrences.
4. **Projected placement check:** PASS — native board boundary samples span X = −4.524116…209.985976632 mm and Y = 2.983912571…143.18 mm, inside the source footprint X = −225…225 mm and Y = −245…245 mm. This check uses displayed boundary samples and trim endpoints projected into the footprint plane.
5. **Persistence:** PASS — verified save/reopen, exact saved-file hash and zero dropped entities. Final reopened checkpoint retained.
6. **Views:** XY boundary drawing and native top viewport inspected. Four boundary projections rendered from 89956 native edges; 10186 unsupported trim edges are displayed using endpoint points.
7. **Cleanup:** owned construction document 683 and reopened document 684 closed; Start preserved.

## References — project and library

1. [Mini planar footprint — library 245](<../../../../library/standards/sowbot-mini-chassis-footprint-reference.md>).
2. [Brain five-board proposal](<brain-board-layout-proposal.md>).
3. [XY boundary drawing](<../../../../images/sowbot/mini-board-footprint-layout-proposal-XY.png>).
4. [Isometric boundary drawing](<../../../../images/sowbot/mini-board-footprint-layout-proposal-isometric.png>).
5. [Native top viewport](<../../../../images/sowbot/mini-board-footprint-layout-proposal-native.png>).
6. Grouped native-boundary renderer. Job inputs, geometry checks, footprint projection check, source pins, native records and incremental checkpoints are retained in ignored `local/work/sowbot/assembly-06-mini/`.

## Sources — online

1. Sowbot hardware page, retained 45 × 49 cm Mini chassis footprint.
2. First source-linked Mini chassis.
3. Board source URLs and retained variants are listed in [the Brain layout companion](<brain-board-layout-proposal.md>).
