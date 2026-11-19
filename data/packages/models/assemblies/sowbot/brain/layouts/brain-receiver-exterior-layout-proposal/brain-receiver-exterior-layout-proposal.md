# Brain receiver-exterior hardware layout proposal

1. **Plan identity:** existing assembly 4, Brain; partial hardware placement proposal.
2. **Native drawing:** [Brain proposal](<brain-receiver-exterior-layout-proposal.dwg>).
3. **State:** PARTIAL_RECEIVER_EXTERIOR_PROPOSAL_SAVED_CURRENT_GEOMETRY_CHECKED.
4. **DWG SHA-256:** `55918aff4e8a49fd5405aad7a1c5a7d807654d3f6527c742075b83523532b747`.
5. **Actual execution model:** unavailable.

## Technical specification

CAD placement proposal coordinates and represented geometry checks are retained with each occurrence matrix.

1. **Arrangement:** nine source-pinned roots contain two Avaota computer exteriors, one LEVIA control-board exterior, two updated F9P receiver exteriors, the open ORP plate face, two BT560 antenna exteriors and the existing panel-switch circular reference. Five boards occupy three proposed tiers.
2. **Receiver coordinates:** receiver A is (0.6122, 6.1447985, 47.06497770373827) mm and receiver B is (56.2078, 6.1447985, 47.06497770373827) mm, with identity rotations. The other seven root matrices are retained from the preceding compact proposal.
3. **Represented separation:** all 36 source-derived root AABB pairs have at least 5 mm proposed separation; each board has a checked outward translation ray against the other eight represented roots. This scope uses represented component geometry and source-sampled solid bounds.
4. **Projection:** the two F9P PCB substrates lie within the actual plate projection, with 0.6121 mm outer X-edge inset. Connector exteriors extend 0.7329 mm beyond the negative X edge and 5.4585 mm beyond the positive X edge. Avaota sampled X-edge inset remains 0.012499695 mm. These are projection measurements; physical supports and enclosure surfaces retain their component source scope.
5. **Current source geometry:** 9 roots contain 1042 geometry occurrences: {'Solid3D': 910, 'Mesh': 131, 'Circle': 1}. Source DWG hashes, complete noncommon-property fingerprints and composed nested matrices PASS. Prepared source bounds and clearance checks are bound to the exact current source definitions and root matrices.
6. **Shared receiver representation:** the F9P source stage retains the carrier/module and open drawing-reconstructed connector surfaces. USB-C nominal overall height differs by 0.01 mm from the sum of its source callouts. SMA axis height 2.205 mm remains a registration proposal with 0.125 mm and 0.035 mm ground-foot gaps. The consuming robot component stages retain their individual partial scopes.
7. **Persistence:** immediate and per-step checkpoints completed. Current owned geometry and millimetre units were checked before final SAVE. Original SAVE completion, exact path, file existence/size/SHA-256, save audit and zero dropped entities PASS. Verification uses retained current records.
8. **Appearance and cleanup:** actual current-record XY and isometric views inspected PASS; native Solid3D boundary samples, all unique Mesh face edges and source planar curves retain actual nested transforms. Owned document 789 guarded closed. Unrelated Start 1 preserved.

**Board and plate registration:** The saved board apertures and LEVIA drill references lie clear of the ten existing plate openings in XY. [Source dimensions and checked mounting projection](<../brain-orp-and-antenna-layout-proposal/brain-board-to-plate-registration.md>).

## Enclosure space required by the represented stack

1. **Represented internal bounds:** **106.191 × 100.000 × 63.670 mm** along the saved X, Y and Z axes, using the five board exteriors and the open ORP plate. The receiver connector exteriors set the X span. The ORP face sets the Y span and the lower Z datum. The panel switch and two antenna occurrences sit outside this internal-stack comparison.
2. **Height:** The ORP mounting face sits at Z = **−10.000 mm**. A separate read of the saved geometry reproduced the highest represented point at Z = **53.670 mm** on the LEVIA-H7 control board's connector geometry, including the U11 Megastar ZX-SH1.0-3PWT connector.
3. **Conditional case comparison:** If **68 mm** from the enclosure listing denotes its exterior height, the represented stack leaves **4.330 mm** total for the enclosure floor, lid, any fins included in that exterior height, mounting plate thickness below its datum and assembly clearance. The enclosed cavity height must be measured between its floor and lowest lid feature.
4. **Evidence:** Saved proposal and source DWG checksums, occurrence transforms and the checked source-sampled bounds were used. Construction geometry is retained in the existing proposal. Calculation model identities unavailable. [Height comparison plot](<brain-enclosure-stack-envelope.png>) · Calculation · Saved geometry extrema · Sowbot-linked enclosure listing.

## Installed occurrences

| Root | Source library / assembly | Readable component | Quantity | Source DWG SHA-256 | Root matrix, row-major |
|---|---|---|---:|---|---|
| 0 | 252 | Yuzuki Avaota-A1 v1.7 computer exterior | 1 | `88808616d5568ab9ef5deb1eca41fcf4bc9b5f62cb4adf3bc2025b7775b79b3f` | `1.0, 0.0, 0.0, 0.0014236728473591143; 0.0, 1.0, 0.0, 6.6269464799470015; 0.0, 0.0, 1.0, -2.3832022476698658; 0.0, 0.0, 0.0, 1.0` |
| 1 | 252 | Yuzuki Avaota-A1 v1.7 computer exterior | 1 | `88808616d5568ab9ef5deb1eca41fcf4bc9b5f62cb4adf3bc2025b7775b79b3f` | `1.0, 0.0, 0.0, 0.0014236728473591143; 0.0, 1.0, 0.0, 6.6269464799470015; 0.0, 0.0, 1.0, 22.73178660419927; 0.0, 0.0, 0.0, 1.0` |
| 2 | 249 | LEVIA-H7 control board exterior | 1 | `fa1cc46d5326ef9edf11cdc8d5b4454032bc9b467fc6bd8b1c5537bb983aa8c7` | `1.0, 0.0, 0.0, 34.75893699999987; 0.0, 1.0, 0.0, 58.8440895; 0.0, 0.0, 1.0, 48.694977703738274; 0.0, 0.0, 0.0, 1.0` |
| 3 | 291 | SparkFun NEO-F9P receiver and source connector exterior | 1 | `f76f6d8de63f91dc101b36226b1d3973e737cd48b7669bfe2037b8d162c7747e` | `1.0, 0.0, 0.0, 0.6121999999998735; 0.0, 1.0, 0.0, 6.144798499999993; 0.0, 0.0, 1.0, 47.06497770373827; 0.0, 0.0, 0.0, 1.0` |
| 4 | 291 | SparkFun NEO-F9P receiver and source connector exterior | 1 | `f76f6d8de63f91dc101b36226b1d3973e737cd48b7669bfe2037b8d162c7747e` | `1.0, 0.0, 0.0, 56.20779999999987; 0.0, 1.0, 0.0, 6.144798499999993; 0.0, 0.0, 1.0, 47.06497770373827; 0.0, 0.0, 0.0, 1.0` |
| 5 | 285 | ORP mounting-plate source open face | 1 | `c5e100633abca40daf5bd5f4f0e6346bd021a1cb82b60a79aeaccc36f4ee5ae0` | `1.0, 0.0, 0.0, 50.0; 0.0, 1.0, 0.0, 50.0; 0.0, 0.0, 1.0, -10.0; 0.0, 0.0, 0.0, 1.0` |
| 6 | 281 | BT560 antenna source exterior | 1 | `275dbde0fe8fddeeff433ececf528a00f3fac30455867fff927c497d6436f986` | `1.0, 0.0, 0.0, -40.0; 0.0, 1.0, 0.0, 180.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 7 | 281 | BT560 antenna source exterior | 1 | `275dbde0fe8fddeeff433ececf528a00f3fac30455867fff927c497d6436f986` | `1.0, 0.0, 0.0, 160.0; 0.0, 1.0, 0.0, 180.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 8 | 257 | Panel-switch circular interface reference | 1 | `d745139922913b67695e11de6e4cadc03109c8fc233f967aeb381aeac5ffd5a7` | `1.0, 0.0, 0.0, -40.0; 0.0, 1.0, 0.0, -40.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |

## Sources — online

1. Retained component technical source 1.
2. Retained component technical source 2.
3. Retained component technical source 3.
4. Retained component technical source 4.
5. Retained component technical source 5.
6. Retained component technical source 6.
7. Retained component technical source 7.
8. Retained component technical source 8.
9. Retained component technical source 9.

## Views

1. [XY current-record view](<brain-receiver-exterior-layout-proposal-XY.png>).
2. [XZ current-record view](<brain-receiver-exterior-layout-proposal-XZ.png>).
3. [YZ current-record view](<brain-receiver-exterior-layout-proposal-YZ.png>).
4. [isometric current-record view](<brain-receiver-exterior-layout-proposal-isometric.png>).

## References

1. [Avaota-A companion](<../../../../reusable/subassemblies/avaota-a1-computer-exterior-stage/avaota-a1-computer-exterior-stage.md>).
2. [Avaota-B companion](<../../../../reusable/subassemblies/avaota-a1-computer-exterior-stage/avaota-a1-computer-exterior-stage.md>).
3. [LEVIA companion](<../../../../../electronics/components/levia-h7-board-exterior-stage/levia-h7-board-exterior-stage.md>).
4. [F9P-A companion](<../../../../reusable/subassemblies/sparkfun-neo-f9p-source-connector-exterior-stage/sparkfun-neo-f9p-source-connector-exterior-stage.md>).
5. [F9P-B companion](<../../../../reusable/subassemblies/sparkfun-neo-f9p-source-connector-exterior-stage/sparkfun-neo-f9p-source-connector-exterior-stage.md>).
6. [Brain ORP mounting plate source open face companion](<../../parts/brain-mounting-plate-source-open-face/brain-mounting-plate-source-open-face.md>).
7. [Beitian BT-560 raster exterior stage companion](<../../../../../electronics/components/beitian-bt560-raster-exterior-stage/beitian-bt560-raster-exterior-stage.md>).
8. [Beitian BT-560 raster exterior stage companion](<../../../../../electronics/components/beitian-bt560-raster-exterior-stage/beitian-bt560-raster-exterior-stage.md>).
9. [Physical emergency-stop22 mm panel interface reference companion](<../../../../../interface-references/mechanical/physical-estop-22mm-panel-interface-reference/physical-estop-22mm-panel-interface-reference.md>).
10. Project execution evidence: exact source pins, proposed matrices, preparation bounds, SAVE/current geometry, render and cleanup receipts are retained at ``.
