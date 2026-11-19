# Brain five-board layout proposal

1. **Plan assembly:** 4 — Brain electronics assembly; saved partial board layout proposal.
2. **Native file:** [Brain board layout proposal](<brain-board-layout-proposal.dwg>).
3. **DWG SHA-256:** `2926eb40290bbc7d26854aa85d2e5d96c074346098dcb3759d3000ca7f3ab6c6`.
4. **Representation:** five placed board-stage occurrences, containing 910 nested construction-solid occurrences.
5. **Coordinate frame:** millimetres; X/Y are the proposed horizontal layout axes; Z is up. Every root has unit scale and zero additional rotation. Original board geometry, source placements and connector directions are retained.
6. **Placement status:** PROPOSAL — job-supplied two-row board arrangement.
7. **Actual execution model:** unavailable.

## Installed components

Every matrix has the form `[[1,0,0,X],[0,1,0,Y],[0,0,1,Z],[0,0,0,1]]`; X, Y and Z below are millimetres.

| Occurrence | Library number / readable component | Quantity | Source DWG SHA-256 | Proposed root X, Y, Z (mm) | Root handle |
|---|---|---:|---|---|---|
| Avaota-A | 252 / Yuzuki Avaota-A1 v1.7 computer exterior | 1 | `88808616d5568ab9ef5deb1eca41fcf4bc9b5f62cb4adf3bc2025b7775b79b3f` | [0, 0, 0] | `25E` |
| Avaota-B | 252 / Yuzuki Avaota-A1 v1.7 computer exterior | 1 | `88808616d5568ab9ef5deb1eca41fcf4bc9b5f62cb4adf3bc2025b7775b79b3f` | [110, 0, 0] | `43B` |
| LEVIA | 249 / LEVIA-H7 control board exterior | 1 | `fa1cc46d5326ef9edf11cdc8d5b4454032bc9b467fc6bd8b1c5537bb983aa8c7` | [0, 100, 0] | `596` |
| F9P-A | 250 / SparkFun NEO-F9P carrier/module | 1 | `62b8861d041d8f51f2eda30518132d4666447606141520acbe2cb8ff37552672` | [70, 100, 0] | `5C1` |
| F9P-B | 250 / SparkFun NEO-F9P carrier/module | 1 | `62b8861d041d8f51f2eda30518132d4666447606141520acbe2cb8ff37552672` | [125, 100, 0] | `5EC` |

## Automated checks and inspected views

1. **Source/native geometry:** PASS — complete noncommon native solid properties and original nested placement matrices match all five source occurrences after reopening. Quantities: 2 × 288 Avaota solids, 272 LEVIA solids and 2 × 31 F9P solids.
2. **Root metadata:** PASS — five readable identities, source hashes, proposal status and proposed root positions match job inputs after reopening.
3. **Persistence:** PASS — save/reopen audit has 834 unique solid definitions and 147 block references; zero dropped entities; saved SHA-256 verified.
4. **Native view:** captured and inspected on owned reopened document 682, geometry revision 37964.
5. **Boundary views:** XY and isometric inspected. Native edge samples and unsupported-trim endpoint points provide display geometry. The original source surfaces remain in the DWG.
6. **Cleanup:** owned documents 682 and 681 closed; Start document preserved.

## References — project and library

1. [Avaota-A1 exterior — library 252](<../../../../library/subassemblies/avaota-a1-computer-exterior-stage.md>), quantity 2.
2. [LEVIA-H7 exterior — library 249](<../../../../library/parts/electrical/levia-h7-board-exterior-stage.md>), quantity 1.
3. [SparkFun receiver carrier/module — library 250](<../../../../library/parts/electrical/sparkfun-neo-f9p-carrier-module-stage.md>), quantity 2.
4. [XY boundary view](<../../../../images/sowbot/brain-board-layout-proposal-grouped-XY.png>).
5. [Isometric boundary view](<../../../../images/sowbot/brain-board-layout-proposal-grouped-isometric.png>).
6. [Native viewport](<../../../../images/sowbot/brain-board-layout-proposal-native.png>).
7. [Grouped native-boundary renderer](<../../../../scripts/sowbot/render_native_boundary_views.py>); caller supplies native records, skill scripts, output folder, stem and title. Acquisition, checkpoints, failed request and geometry receipts reside under ignored `local/work/sowbot/assembly-04-brain/`.

## Sources — online

1. Avaota-A1 manufacturer v1.7 3D archive.
2. LEVIA-H7 source repository, retained Rev0_1 KiCad and STEP sources.
3. SparkFun GPS-23288 receiver, retained v1.1 board.
4. u-blox NEO-F9P manufacturer STEP.
