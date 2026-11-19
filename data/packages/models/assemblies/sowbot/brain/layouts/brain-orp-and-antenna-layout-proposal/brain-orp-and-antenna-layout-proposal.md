# Brain layout proposal with corrected ORP plate and joined BT-560 antennas

1. **Plan identity:** Assembly 4, Brain electronics, partial hardware layout proposal.
2. **Native drawing:** [Brain ORP and antenna layout](<brain-orp-and-antenna-layout-proposal.dwg>).
3. **DWG SHA-256:** `a3e174ab293d61fd81580ed1701b708320e9a28550ddfb44bca14a7cd3afbd7f`.
4. **Actual execution model:** unavailable.

## Technical specification

1. The library 314 Rosmo ORP face retains the saved translation (50, 50, −10) mm. The face represents all 28 source openings at the original plane and outer perimeter. Library 314 models a planar mounting reference.
2. The two library 315 Beitian BT-560 antenna skins retain translations (−40, 180, 0) mm and (160, 180, 0) mm. Both have identity rotation and unit scale. Each occurrence retains all 2,176 oriented world-coordinate triangles and the open SMA-J rim.
3. The Avaota-A1 computers, LEVIA-H7 control board, two SparkFun receivers and panel switch reference retain their saved geometry and placement. Nine live roots expand to 1,080 geometry occurrences: 952 solids, 127 meshes and one circle.

## Verification

1. Exact live root and nested records, plate arrays and antenna triangle winding passed. The [mounting projection checks](<brain-board-to-plate-registration.md>) report all 22 aperture projections clear at the retained board positions, with the nearest 1.069 mm separation at LEVIA H4.
2. Incremental verified SAVE, final audit, inspected [ORP plate and antenna isometric detail](<brain-orp-and-antenna-layout-isometric.png>) and guarded closure passed. The occurrence BOM records the actual placed model paths, matrices and hashes.
3. **Lower Avaota-A1 removal:** A straight vertical lift at the saved XY position is obstructed by the upper Avaota-A1. Both occurrences use the same native block, rotation and scale. The represented solids coincide after **25.114989 mm** of upward travel. This is a confirmed interference position. The resting vertical gap between the sampled vertex envelopes is **5.000 mm**. Actual calculation model unavailable. Native placement check.
4. **SparkFun SMA straight approach:** Both connectors point toward +X. From the receiver at lower X, a straight Ø2 mm probe intersects the other SMA mesh. The witness is **48.096 mm** outward from the entry plane and **0.634809 mm** from the connector axis. The same probe from the receiver at higher X has zero hits among the **127** checked mesh occurrences. The calculation covers the saved meshes. Full physical access also depends on the other solid occurrences, the mating plug and enclosure entry. Actual calculation model unavailable. Saved placement and face witness.

5. **Lower Avaota-A1 horizontal extraction:** A straight +X path at the saved height and orientation clears all eight stationary roots over **174.615 mm**. The conservative clearance to the upper Avaota-A1 is **3.141 mm**. The moving board bound includes all original source STEP solids apart from the identified detached TFT proxy. In the saved Main and Mini layouts the same motion also clears their represented surroundings. The path models released hardware and uses the existing layout coordinates. The physical enclosure and cables require separate checks. Actual calculation model unavailable. Brain source result · Installed layout checks.

## References

1. [Library 314 Rosmo ORP plate](<../../../../../mechanical-parts/components/brain-orp-mounting-plate-28-opening-source-face/brain-orp-mounting-plate-28-opening-source-face.md>).
2. [Library 315 Beitian BT-560](<../../../../../electronics/components/beitian-bt560-joined-source-skin/beitian-bt560-joined-source-skin.md>).
3. [Previous Brain proposal](<../brain-avaota-source-connectors-layout-proposal/brain-avaota-source-connectors-layout-proposal.md>).
4. Native assembly and save checks.

## Sources — online

1. Sowbot Brain hardware.
2. Beitian BT-560 manufacturer data.
