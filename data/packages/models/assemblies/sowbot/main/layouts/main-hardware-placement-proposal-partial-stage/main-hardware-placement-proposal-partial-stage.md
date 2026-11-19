# Main Sowbot hardware placement proposal — partial source stage

1. **Plan identity:** assembly 5, complete main Sowbot; partial placement proposal.
2. **Native drawing:** [Main hardware placement proposal](<main-hardware-placement-proposal-partial-stage.dwg>).
3. **DWG SHA-256:** `75f7aba3e7d8d996f19745be583c3243fb040bfa25f9b9c29c26707091dadecf`.
4. **State:** PARTIAL_PLACEMENT_PROPOSAL_SAVED_REOPENED_CHECKED.
5. **Frame:** millimetres; X follows conditional track travel, Y crosses the track pair, Z points up. Z = 0 is the straight-tread reference plane.
6. **Actual execution model:** unavailable.

## Installed occurrences and proposal inputs

All root rotations are identity and scale is one. The translation coordinates below are CAD placement proposal coordinates under plan assembly 5. The source definitions and their internal connector directions are retained.

| Occurrence | Library / assembly | Readable component | Quantity at this root | Source DWG SHA-256 | Proposed translation X, Y, Z (mm) |
|---|---|---|---:|---|---|
| 1 | assembly | Main chassis two source-visible track patches | 1 | `6b0f9d08fcc85a779fe1ef1ae908d22d8a697df18c962107c38d8b38d1ba6c77` | `[0.0, 0.0, 0.0]` |
| 2 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `[80.0, 100.0, 0.0]` |
| 3 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `[80.0, 300.0, 0.0]` |
| 4 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `[80.0, 500.0, 0.0]` |
| 5 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `[430.0, 100.0, 0.0]` |
| 6 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `[430.0, 300.0, 0.0]` |
| 7 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `[430.0, 500.0, 0.0]` |
| 8 | 283 | ODrive v3.6 135 by 50 mm planar reference PROPOSAL | 1 | `ea06fee77de0dc0e196a6521bb397a76531db4418699aafdcf6cc8eeac35547a` | `[200.0, 40.0, 0.0]` |
| 9 | 283 | ODrive v3.6 135 by 50 mm planar reference PROPOSAL | 1 | `ea06fee77de0dc0e196a6521bb397a76531db4418699aafdcf6cc8eeac35547a` | `[450.0, 40.0, 0.0]` |
| 10 | assembly | Brain five-board partial layout PROPOSAL | 1 | `2926eb40290bbc7d26854aa85d2e5d96c074346098dcb3759d3000ca7f3ab6c6` | `[250.0, 690.0, 250.0]` |

## Technical specification and checks

1. **Installed source units:** one two-track source-visible chassis partial, six VariCore VC-1280NA photo-exterior stages, two ODrive v3.6 135 × 50 mm planar references and one existing five-board Brain proposal. The Brain supplies two Yuzuki Avaota-A1 computers, one LEVIA-H7 control board and two SparkFun NEO-F9P carrier/module stages.
2. **Reopened geometry:** 10 root occurrences, 910 solid occurrences and 97 Mesh occurrences. Complete noncommon source properties and all composed nested placement matrices PASS. Source DWG hashes match the checked definitions.
3. **Battery arrangement:** two longitudinal columns at X = 80 and 430 mm, three rows at Y = 100, 300 and 500 mm, base reference Z = 0 mm. Positive terminal directions remain +Z. The minimum pairwise represented battery-exterior AABB distance is 16.441139033 mm; adjacent transverse rows have 30 mm reference gaps.
4. **Removal-reference check:** +Z removal projections for all six represented battery exteriors have no XY overlap with the translated Brain boundary-sample AABB or either controller reference. Other battery reference AABBs are mutually separated. This check covers the represented exterior surfaces and references.
5. **Brain and controller proposals:** Brain root (250, 690, 250) mm; controller roots (200, 40, 0) and (450, 40, 0) mm. The controller geometry remains a planar dimensional reference. Physical support and enclosure seating retain their source-interface dependencies.
6. **Source scope:** the main carrier material correspondence, crossmember height, reducer face datum and full track side geometry retain their recorded individual source pauses. The D6374 motor definition remains reusable when its reducer/mount pose is established. Kee Lite fitting placement retains the source-visible tube-joint correspondence dependency. The six battery stages retain their conditional photographic camera and source dimension attribution.
7. **Persistence and appearance:** new document saved immediately; every source insertion, placement and provenance step checkpointed. Canonical verified save, zero dropped entities and fresh reopen PASS. Reopened-record XY and isometric views inspected PASS; 94,760 sampled boundary edges.
8. **Cleanup:** owned documents 767 and 768 guarded closed after persistence and geometry checks. Unrelated Start 1 preserved.

## Sources — online

1. [Sowbot hardware and component quantities](https://sowbot.co.uk/hardware/).
2. VariCore VC-1280Na+ manufacturer size source.
3. Exact VariCore listing photo source.
4. [ODrive official hardware comparison](https://docs.odriverobotics.com/v/latest/hardware/odrive-comparison.html), v3.6 135 × 50 mm reference.

## References

1. [Main source-visible chassis stage](<../../subassemblies/main-chassis-visible-track-source-partial-stage/main-chassis-visible-track-source-partial-stage.md>).
2. [Brain five-board proposal](<../../../../../sowbot/assemblies/detailed/brain-board-layout-proposal.md>).
3. [VariCore exterior stage](<../../../../../../library/parts/electrical/varicore-vc1280na-photo-exterior-stage.md>), library 282.
4. [ODrive v3.6 dimensional reference](<../../../../../../library/parts/electrical/odrive-v36-135x50-source-dimension-reference.md>), library 283.
5. [Top saved-record view](<main-hardware-placement-proposal-partial-stage-XY.png>).
6. [Isometric saved-record view](<main-hardware-placement-proposal-partial-stage-isometric.png>).
7. Proposed root matrices and source pins.
8. Exact nested geometry checks.
9. Represented-exterior clearance and removal checks.
10. Guarded cleanup.
