# Brain hardware reference placement proposal

1. **Plan identity:** assembly 4, Brain electronics; partial hardware placement proposal.
2. **Native drawing:** [Brain hardware reference proposal](<brain-hardware-reference-placement-proposal.dwg>).
3. **DWG SHA-256:** `1021a217fb9f37804f89155c6f98dd5040d6359e12e1cd8d9d9434b1064f221c`.
4. **State:** PARTIAL_HARDWARE_PLACEMENT_PROPOSAL_SAVED_CURRENT_GEOMETRY_CHECKED.
5. **Frame:** millimetres; existing five-board layout X/Y axes, Z up. All root rotations are identity and scale is one.
6. **Actual execution model:** unavailable.

## Installed occurrences

The translations are CAD placement proposal coordinates under plan assembly 4. Source component geometry, local interfaces and connector directions are retained.

| Root | Library / assembly | Readable hardware or reference | Quantity | Source DWG SHA-256 | Translation X, Y, Z (mm) |
|---|---|---|---:|---|---|
| 1 | assembly | Brain five-board partial layout | 1 | `2926eb40290bbc7d26854aa85d2e5d96c074346098dcb3759d3000ca7f3ab6c6` | `[0.0, 0.0, 0.0]` |
| 2 | 285 | Brain ORP mounting plate source open face | 1 | `c5e100633abca40daf5bd5f4f0e6346bd021a1cb82b60a79aeaccc36f4ee5ae0` | `[50.0, 50.0, -10.0]` |
| 3 | 281 | Beitian BT-560 raster exterior stage | 1 | `275dbde0fe8fddeeff433ececf528a00f3fac30455867fff927c497d6436f986` | `[-40.0, 180.0, 0.0]` |
| 4 | 281 | Beitian BT-560 raster exterior stage | 1 | `275dbde0fe8fddeeff433ececf528a00f3fac30455867fff927c497d6436f986` | `[160.0, 180.0, 0.0]` |
| 5 | 257 | Physical emergency-stop 22 mm panel interface reference | 1 | `d745139922913b67695e11de6e4cadc03109c8fc233f967aeb381aeac5ffd5a7` | `[-40.0, -40.0, 0.0]` |

## Technical specification and checks

1. **Represented hardware:** the reused five-board source layout contains two Yuzuki Avaota-A1 v1.7 computer exteriors, one LEVIA-H7 control-board exterior and two SparkFun NEO-F9P carrier/module stages. Added references are the ORP open plate face, two Beitian BT-560 raster exterior stages and one 22 mm switch panel-interface circle.
2. **Current geometry:** five root occurrences contain 910 Solid3D occurrences, seven Mesh occurrences and one Circle. Complete noncommon source properties and all composed nested matrices PASS. The panel circle separately matches source centre (0, 0, 0), radius 11 mm, source plane and proposed root matrix.
3. **Plate reference:** its open face lies at Z = −10 mm. Sampled plate-to-board Z gap is 6.535 mm. Board-layout projected bounds are X = −4.524116…209.985977 mm and Y = 2.983913…143.18 mm; plate-face bounds are X/Y = 0…100 mm. The represented board layout projects beyond the plate face. Mounting-hole/retention correspondence remains a source-interface placement input.
4. **Antenna proposal:** roots (−40, 180, 0) and (160, 180, 0) mm retain +Z connector-to-tip axes and 58.6 mm source axial extent. Sampled antenna X separation is 172.744361 mm. Full axial profiles, rounded tips and collar steps are visible in current-record Mesh-edge views.
5. **Switch reference:** the circle at (−40, −40, 0) mm represents the source 22 mm panel interface. The visible collar/body source-section correspondence retains its component 35 pause.
6. **Source limits:** enclosure body/lid title-to-feature attribution retains the measured 9.6095% axis-scale contradiction. The exact power-board source page retains its application-shell and metric-scale error. The open plate retains its zero-thickness source representation. These component results preserve the assembly's partial scope.
7. **Persistence:** immediate and per-source insertion/placement/provenance saves completed. Current root matrices, millimetre units and source hashes were inspected before canonical SAVE. Completed original SAVE response, correct path, file existence/size, SHA-256, save audit and zero dropped entities PASS; final geometry revision is unchanged. Verification uses the current owned records.
8. **Appearance:** XY and isometric views from actual current document 776 inspected PASS. The views include all unique Mesh face edges, 3D-solid boundary samples and the source circle, with actual nested transforms. The retained boundary-only source projections have their separate limited appearance scope.
9. **Cleanup:** owned document 776 guarded closed after source-geometry, visual and persistence checks. Unrelated Start 1 preserved.

## Sources — online

1. Sowbot hardware and Brain component quantities.
2. Exact ORP source document, open-face source curves and revision.
3. Beitian BT-560 manufacturer page.
4. Beitian BT-560 technical drawing, revision 5.53.
5. Exact stop-switch source listing, source switch photographs; source panel nominal size is retained in the Sowbot hardware table.

## References

1. [Original five-board proposal](<brain-board-layout-proposal.md>), preserved.
2. [ORP open face](<../../../../library/parts/mechanical/brain-mounting-plate-source-open-face.md>), library 285.
3. [BT-560 exterior stage](<../../../../library/parts/electrical/beitian-bt560-raster-exterior-stage.md>), library 281.
4. [22 mm panel interface](<../../../../library/standards/physical-estop-22mm-panel-interface-reference.md>), library 257.
5. [Top current-record view](<../../../../images/sowbot/brain-hardware-reference-placement-proposal-XY.png>).
6. [Isometric current-record view](<../../../../images/sowbot/brain-hardware-reference-placement-proposal-isometric.png>).
7. Exact source pins and proposed matrices.
8. Current source geometry and nested-matrix checks.
9. Plate-reference projection check.
10. Completed SAVE receipt.
11. Mesh-edge-inclusive view receipt.
12. Guarded cleanup.
