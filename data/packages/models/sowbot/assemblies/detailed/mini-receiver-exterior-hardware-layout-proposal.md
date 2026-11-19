# Mini receiver-exterior hardware layout proposal

1. **Plan identity:** existing assembly 6, Mini; partial hardware placement proposal.
2. **Native drawing:** [Mini proposal](<mini-receiver-exterior-hardware-layout-proposal.dwg>).
3. **State:** PARTIAL_RECEIVER_EXTERIOR_PROPOSAL_SAVED_CURRENT_GEOMETRY_CHECKED.
4. **DWG SHA-256:** `52ada16de56c1f5fb988618072c722d0d4e1f1f02cebf694ad99dee0a0ece38c`.
5. **Actual execution model:** unavailable.

## Technical specification

CAD placement proposal coordinates and represented geometry checks are retained with each occurrence matrix.

1. **Arrangement:** four roots contain the 450 × 490 mm planar base reference, updated shared Brain proposal, Open BTS7960 source connector/board-face stage and selected 306 × 174 mm battery XY footprint. All four parent matrices retain the reviewed proposal positions; Brain coordinates are (0, 20, 0) mm.
2. **Represented separation:** hardware projections lie within the base reference. The Brain-to-battery footprint projected gap remains 5 mm. Source driver bounds are (−200, 100, −3.7999924) to (−129.896, 139.243, 9.99998) mm; represented driver-to-Brain X separation is 76.268180451 mm and driver-to-battery Y separation is 136 mm.
3. **Source driver:** library 286 retains the source-authored connector poses and positive uniform scale 0.999998. Its exporter display translation is rebased onto the source board-top face; it supplies an open board face and existing planar reference. The selected battery XY face retains library 255 source dimensions and its separate 200/220 mm height attribution.
4. **Current source geometry:** 4 roots contain 1096 geometry occurrences: {'LwPolyline': 7, 'Solid3D': 910, 'Mesh': 148, 'Circle': 31}. Source DWG hashes, complete noncommon-property fingerprints and composed nested matrices PASS. Prepared source bounds and clearance checks are bound to the exact current source definitions and root matrices.
5. **Shared receiver representation:** the F9P source stage retains the carrier/module and open drawing-reconstructed connector surfaces. USB-C nominal overall height differs by 0.01 mm from the sum of its source callouts. SMA axis height 2.205 mm remains a registration proposal with 0.125 mm and 0.035 mm ground-foot gaps. The consuming robot component stages retain their individual partial scopes.
6. **Persistence:** immediate and per-step checkpoints completed. Current owned geometry and millimetre units were checked before final SAVE. Original SAVE completion, exact path, file existence/size/SHA-256, save audit and zero dropped entities PASS. Verification uses retained current records.
7. **Appearance and cleanup:** actual current-record XY and isometric views inspected PASS; native Solid3D boundary samples, all unique Mesh face edges and source planar curves retain actual nested transforms. Owned document 791 guarded closed. Unrelated Start 1 preserved.

8. **Service and mounting checks:** The proposed vertical battery lift has 5 mm projected clearance to the Brain and 136 mm to the driver. All five proposed board paths clear the represented driver and battery footprint. The driver terminal and Brain mounting plate reach Z = −3.7999924 mm and −10 mm relative to the footprint plane, respectively. [Service and mounting report](<../../../../docs/sowbot/mini-layout-service-clearance.md>).

## Installed occurrences

| Root | Source library / assembly | Readable component | Quantity | Source DWG SHA-256 | Root matrix, row-major |
|---|---|---|---:|---|---|
| 0 | 245 | Mini 450 × 490 mm planar footprint | 1 | `d890c11303d90da0a029a2d23cf11c64a82e084c68e4411910c0921f7ff66b3d` | `1.0, 0.0, 0.0, 0.0; 0.0, 1.0, 0.0, 0.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 1 | assembly | Shared compact three-tier Brain partial layout PROPOSAL | 1 | `55918aff4e8a49fd5405aad7a1c5a7d807654d3f6527c742075b83523532b747` | `1.0, 0.0, 0.0, 0.0; 0.0, 1.0, 0.0, 20.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 2 | 286 | Open BTS7960 source connector and board-face stage | 1 | `a14019a8c2ca9594064ebcc3da95a081b097c01a830a7afbbd4357be6f5ae021` | `1.0, 0.0, 0.0, -200.0; 0.0, 1.0, 0.0, 100.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| 3 | 255 selected XY derivative | Propow CPN24050 selected306 by174 mm XY footprint reference | 1 | `6ea66c78b9794098d7f3a085c23c4661ee428afdfe9b2e71e161e48cebf48923` | `1.0, 0.0, 0.0, -153.0; 0.0, 1.0, 0.0, -210.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |

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
13. Retained component technical source 13.
14. Retained component technical source 14.
15. Retained component technical source 15.

## Views

1. [XY current-record view](<../../../../images/sowbot/mini-receiver-exterior-hardware-layout-proposal-XY.png>).
2. [XZ current-record view](<../../../../images/sowbot/mini-receiver-exterior-hardware-layout-proposal-XZ.png>).
3. [YZ current-record view](<../../../../images/sowbot/mini-receiver-exterior-hardware-layout-proposal-YZ.png>).
4. [isometric current-record view](<../../../../images/sowbot/mini-receiver-exterior-hardware-layout-proposal-isometric.png>).

## References

1. [Mini 450 × 490 mm planar footprint companion](<../../../../library/standards/sowbot-mini-chassis-footprint-reference.md>).
2. [Shared compact three-tier Brain partial layout PROPOSAL companion](<brain-receiver-exterior-layout-proposal.md>).
3. [OpenBTS7960sourceconnectorandboardfacestage companion](<../../../../library/subassemblies/open-bts7960-source-connector-board-face-stage.md>).
4. Project execution evidence: exact source pins, proposed matrices, preparation bounds, SAVE/current geometry, render and cleanup receipts are retained at ``.
