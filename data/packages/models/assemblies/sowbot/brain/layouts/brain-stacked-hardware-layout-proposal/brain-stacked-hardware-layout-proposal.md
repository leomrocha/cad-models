# Brain three-tier hardware layout proposal

1. **Plan identity:** assembly 4, Brain electronics; partial hardware placement proposal.
2. **Native drawing:** [Brain three-tier proposal](<brain-stacked-hardware-layout-proposal.dwg>).
3. **DWG SHA-256:** `ca59f3dc8b93adc71737fd3096e1f8f1ab4f58458f5b71c4de81a4ac2adee01b`.
4. **State:** PARTIAL_THREE_TIER_PROPOSAL_SAVED_CURRENT_GEOMETRY_CHECKED.
5. **Frame:** millimetres; X/Y plate layout axes, Z up; identity root rotations and unit scales.
6. **Actual execution model:** unavailable.

## Installed occurrences

Positions are CAD placement proposal coordinates. Each table row specifies one root; its full 4 × 4 matrix is retained in the execution job.

| Root | Library | Readable component or reference | Quantity | Source DWG SHA-256 | Translation X, Y, Z (mm) |
|---|---|---|---:|---|---|
| 1 | 252 | Yuzuki Avaota-A1 v1.7 computer exterior | 1 | `88808616d5568ab9ef5deb1eca41fcf4bc9b5f62cb4adf3bc2025b7775b79b3f` | `[0.0014236728473591143, 6.6269464799470015, -2.3832022476698658]` |
| 2 | 252 | Yuzuki Avaota-A1 v1.7 computer exterior | 1 | `88808616d5568ab9ef5deb1eca41fcf4bc9b5f62cb4adf3bc2025b7775b79b3f` | `[0.0014236728473591143, 6.6269464799470015, 22.73178660419927]` |
| 3 | 249 | LEVIA-H7 control board exterior | 1 | `fa1cc46d5326ef9edf11cdc8d5b4454032bc9b467fc6bd8b1c5537bb983aa8c7` | `[34.75893699999987, 58.8440895, 48.694977703738274]` |
| 4 | 250 | SparkFun NEO-F9P carrier/module | 1 | `62b8861d041d8f51f2eda30518132d4666447606141520acbe2cb8ff37552672` | `[4.319999999999872, 6.144798499999993, 45.22997770373827]` |
| 5 | 250 | SparkFun NEO-F9P carrier/module | 1 | `62b8861d041d8f51f2eda30518132d4666447606141520acbe2cb8ff37552672` | `[52.49999999999987, 6.144798499999993, 45.22997770373827]` |
| 6 | 285 | ORP mounting plate source open face | 1 | `c5e100633abca40daf5bd5f4f0e6346bd021a1cb82b60a79aeaccc36f4ee5ae0` | `[50.0, 50.0, -10.0]` |
| 7 | 281 | Beitian BT-560 raster exterior | 1 | `275dbde0fe8fddeeff433ececf528a00f3fac30455867fff927c497d6436f986` | `[-40.0, 180.0, 0.0]` |
| 8 | 281 | Beitian BT-560 raster exterior | 1 | `275dbde0fe8fddeeff433ececf528a00f3fac30455867fff927c497d6436f986` | `[160.0, 180.0, 0.0]` |
| 9 | 257 | 22 mm emergency-stop panel interface reference | 1 | `d745139922913b67695e11de6e4cadc03109c8fc233f967aeb381aeac5ffd5a7` | `[-40.0, -40.0, 0.0]` |

## Technical specification

1. **Arrangement:** two Avaota computers occupy separate lower tiers. Two SparkFun boards share a row on the upper tier; the LEVIA board occupies the second row. Their upper-tier combined sampled footprint is 91.36 × 87.710403 mm. Two antenna exterior stages and the panel-interface reference retain their previous proposal positions.
2. **Vertical coordinates:** the plate open face lies at Z = −10 mm. The two Avaota sampled ranges are −5…15.114988852 mm and 20.114988852…40.229977704 mm. The upper-board tier begins at 45.229977704 mm and ends at 53.669977704 mm. Proposed represented air gaps are 5 mm.
3. **Plate projection:** all five sampled board projections lie within the source plate projection, X/Y = 0.0001…99.9999 mm. Each Avaota sampled X-edge inset is 0.012499695 mm. This value describes sampled projection containment. Plate-hole correspondence, supports, cable mating envelopes and enclosure geometry retain their component/interface inputs.
4. **Separation:** all 36 represented root pairs have sampled axis-aligned bounding-box separation of at least 5 mm. Each board has a clear outward translation ray through the other eight represented root bounds. These checks cover the currently represented geometry and proposal coordinates.
5. **Current geometry:** nine roots contain 910 Solid3D occurrences, seven Mesh occurrences and one Circle, totalling 918 geometry occurrences. Complete noncommon source-property fingerprints and all composed nested matrices PASS. The panel circle independently matches centre (0, 0, 0), radius 11 mm and its proposal matrix.
6. **Source scope:** Avaota exterior stages retain the TFT-source finding; SparkFun stages retain their carrier/module representation and connector-source findings. The plate is an open zero-thickness face. The antenna shape is raster-estimated exterior geometry. The switch uses its 22 mm panel circle. Enclosure body/lid attribution retains its measured 9.6095% axis-scale contradiction; power-board geometry retains its source application-shell/metric-scale finding.
7. **Persistence:** initial, insertion, placement and provenance checkpoints completed. Current geometry, root matrices, source hashes and millimetre units were inspected before the canonical SAVE. Completed original SAVE response, exact path, file existence/size/hash, save audit and zero dropped entities PASS. Geometry revision remained unchanged through SAVE. Verification uses retained current records.
8. **Appearance:** current-document XY, XZ and isometric views inspected PASS. Views include all unique Mesh face edges, native solid-boundary samples and the source circle with actual nested matrices. Unsupported trim endpoints retain their renderer scope.
9. **Cleanup:** owned document 777 guarded closed after persistence, geometry and visual checks. Unrelated Start 1 preserved.

## Sources — online

1. Sowbot hardware quantities.
2. Exact ORP source document.
3. Beitian BT-560 manufacturer page.
4. Beitian BT-560 technical drawing, revision 5.53.
5. Stop-switch source listing.

## References

1. [Previous flat hardware proposal](<../brain-hardware-reference-placement-proposal/brain-hardware-reference-placement-proposal.md>), preserved with its board-projection finding.
2. [Original five-board proposal](<../brain-board-layout-proposal/brain-board-layout-proposal.md>), preserved.
3. Current execution inputs and matrices.
4. Source geometry and nested matrices.
5. Current-bound layout checks.
6. Completed SAVE receipt.
7. Current-record views.
8. Guarded cleanup.
9. [Top view](<brain-stacked-hardware-layout-proposal-XY.png>).
10. [Tier side view](<brain-stacked-hardware-layout-proposal-XZ.png>).
11. [Isometric view](<brain-stacked-hardware-layout-proposal-isometric.png>).
