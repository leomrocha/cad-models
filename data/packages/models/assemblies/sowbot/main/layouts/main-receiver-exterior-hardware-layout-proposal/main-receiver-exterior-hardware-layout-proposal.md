# Main receiver-exterior hardware layout proposal

1. **Plan identity:** existing assembly 5, Main; partial hardware placement proposal.
2. **Native drawing:** [Main proposal](<main-receiver-exterior-hardware-layout-proposal.dwg>).
3. **State:** PARTIAL_RECEIVER_EXTERIOR_PROPOSAL_SAVED_CURRENT_GEOMETRY_CHECKED.
4. **DWG SHA-256:** `1f7b3e112dca1dcef175ea719e5582b99abee115a3b31b24c39c23f865bacb75`.
5. **Actual execution model:** unavailable.

## Technical specification

CAD placement proposal coordinates and represented geometry checks are retained with each occurrence matrix.

1. **Arrangement:** ten roots contain the source-visible track patches, six VariCore photo-exterior battery occurrences, two ODrive v3.6 planar controller references and the updated shared Brain proposal. All ten parent matrices are retained from the preceding compact proposal, including Brain coordinates (250, 726, 250) mm.
2. **Represented separation:** all six positive-Z battery-removal projections remain clear of the represented Brain and controller geometry. The proposed projected gap beyond the last battery row remains 5 mm. The updated Brain union bounds retain the antenna and panel extents of the preceding source proposal.
3. **Source scope:** the track patches use the conditional straight-tread reference plane Z = 0. The battery geometry is a source-photo exterior reconstruction and the controller geometry is a 135 × 50 mm source dimensional reference. Their source/camera qualifications remain attributed to their component companions.
4. **Current source geometry:** 10 roots contain 1139 geometry occurrences: {'Mesh': 228, 'Solid3D': 910, 'Circle': 1}. Source DWG hashes, complete noncommon-property fingerprints and composed nested matrices PASS. Prepared source bounds and clearance checks are bound to the exact current source definitions and root matrices.
5. **Shared receiver representation:** the F9P source stage retains the carrier/module and open drawing-reconstructed connector surfaces. USB-C nominal overall height differs by 0.01 mm from the sum of its source callouts. SMA axis height 2.205 mm remains a registration proposal with 0.125 mm and 0.035 mm ground-foot gaps. The consuming robot component stages retain their individual partial scopes.
6. **Persistence:** immediate and per-step checkpoints completed. Current owned geometry and millimetre units were checked before final SAVE. Original SAVE completion, exact path, file existence/size/SHA-256, save audit and zero dropped entities PASS. Verification uses retained current records.
7. **Appearance and cleanup:** actual current-record XY and isometric views inspected PASS; native Solid3D boundary samples, all unique Mesh face edges and source planar curves retain actual nested transforms. Owned document 790 guarded closed. Unrelated Start 1 preserved.

## Controller outline clearance

1. **Saved references:** the two 135 × 50 mm ODrive v3.6 outlines have 115 mm between them. Their minimum calculated plan-view distance to the represented battery bounds is 35 mm. Their distances to the visible track meshes are 4.505 mm at root 7 and 8.101 mm at root 8. ODrive v3.6 comparison table.
2. **Conditional 140.50 × 50 mm outline:** the separate ODrive figure gives this larger outline with revision unresolved. The check allows its extra 5.50 mm to extend from either end of either saved outline or to be split between the ends. The union of these possible outlines leaves at least 104 mm between the controllers. Minimum gaps to the battery bounds and visible track meshes are unchanged in the calculation. ODrive mechanical figure.
3. **Check basis:** battery distances are to the saved photo-exterior bounding boxes. Track distances are to the projected finite triangles in the saved track patch reference. These are XY distances for the represented layout. Actual calculation model unavailable. Source pins and results.

## Installed occurrences

| Root | Source library / assembly | Readable component | Quantity | Source DWG SHA-256 | Root matrix, row-major |
|---|---|---|---:|---|---|
| 0 | assembly | Main chassis two source-visible track patches | 1 | `6b0f9d08fcc85a779fe1ef1ae908d22d8a697df18c962107c38d8b38d1ba6c77` | `1.0, 0.0, 0.0, 0.0; 0.0, 1.0, 0.0, 0.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 1 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `1.0, 0.0, 0.0, 80.0; 0.0, 1.0, 0.0, 100.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 2 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `1.0, 0.0, 0.0, 80.0; 0.0, 1.0, 0.0, 300.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 3 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `1.0, 0.0, 0.0, 80.0; 0.0, 1.0, 0.0, 500.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 4 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `1.0, 0.0, 0.0, 430.0; 0.0, 1.0, 0.0, 100.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 5 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `1.0, 0.0, 0.0, 430.0; 0.0, 1.0, 0.0, 300.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 6 | 282 | VariCore VC-1280NA battery photo exterior PROPOSAL | 1 | `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e` | `1.0, 0.0, 0.0, 430.0; 0.0, 1.0, 0.0, 500.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 7 | 283 | ODrive v3.6 135 by 50 mm planar reference PROPOSAL | 1 | `ea06fee77de0dc0e196a6521bb397a76531db4418699aafdcf6cc8eeac35547a` | `1.0, 0.0, 0.0, 200.0; 0.0, 1.0, 0.0, 40.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 8 | 283 | ODrive v3.6 135 by 50 mm planar reference PROPOSAL | 1 | `ea06fee77de0dc0e196a6521bb397a76531db4418699aafdcf6cc8eeac35547a` | `1.0, 0.0, 0.0, 450.0; 0.0, 1.0, 0.0, 40.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 9 | assembly | Shared compact three-tier Brain partial layout PROPOSAL | 1 | `55918aff4e8a49fd5405aad7a1c5a7d807654d3f6527c742075b83523532b747` | `1.0, 0.0, 0.0, 250.0; 0.0, 1.0, 0.0, 726.0; 0.0, 0.0, 1.0, 250.0; 0.0, 0.0, 0.0, 1.0` |

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
10. Retained component technical source 10.
11. Retained component technical source 11.
12. Retained component technical source 12.

## Views

1. [XY current-record view](<main-receiver-exterior-hardware-layout-proposal-XY.png>).
2. [XZ current-record view](<main-receiver-exterior-hardware-layout-proposal-XZ.png>).
3. [YZ current-record view](<main-receiver-exterior-hardware-layout-proposal-YZ.png>).
4. [isometric current-record view](<main-receiver-exterior-hardware-layout-proposal-isometric.png>).

## References

1. Main chassis two source-visible track patches companion.
2. [VariCore VC-1280NA battery photo exterior PROPOSAL companion](<../../../../../electronics/batteries/varicore-vc1280na-photo-exterior-stage/varicore-vc1280na-photo-exterior-stage.md>).
3. [VariCore VC-1280NA battery photo exterior PROPOSAL companion](<../../../../../electronics/batteries/varicore-vc1280na-photo-exterior-stage/varicore-vc1280na-photo-exterior-stage.md>).
4. [VariCore VC-1280NA battery photo exterior PROPOSAL companion](<../../../../../electronics/batteries/varicore-vc1280na-photo-exterior-stage/varicore-vc1280na-photo-exterior-stage.md>).
5. [VariCore VC-1280NA battery photo exterior PROPOSAL companion](<../../../../../electronics/batteries/varicore-vc1280na-photo-exterior-stage/varicore-vc1280na-photo-exterior-stage.md>).
6. [VariCore VC-1280NA battery photo exterior PROPOSAL companion](<../../../../../electronics/batteries/varicore-vc1280na-photo-exterior-stage/varicore-vc1280na-photo-exterior-stage.md>).
7. [VariCore VC-1280NA battery photo exterior PROPOSAL companion](<../../../../../electronics/batteries/varicore-vc1280na-photo-exterior-stage/varicore-vc1280na-photo-exterior-stage.md>).
8. [ODrive v3.6 135 by 50 mm planar reference PROPOSAL companion](<../../../../../electronics/components/odrive-v36-135x50-source-dimension-reference/odrive-v36-135x50-source-dimension-reference.md>).
9. [ODrive v3.6 135 by 50 mm planar reference PROPOSAL companion](<../../../../../electronics/components/odrive-v36-135x50-source-dimension-reference/odrive-v36-135x50-source-dimension-reference.md>).
10. [Shared compact three-tier Brain partial layout PROPOSAL companion](<../../../brain/layouts/brain-receiver-exterior-layout-proposal/brain-receiver-exterior-layout-proposal.md>).
11. Project execution evidence: exact source pins, proposed matrices, preparation bounds, SAVE/current geometry, render and cleanup receipts are retained at ``.
