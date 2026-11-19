# Mini compact Brain hardware layout proposal

1. **Plan identity:** assembly 6, Mini robot; partial hardware placement proposal.
2. **Native drawing:** [Mini proposal](<mini-compact-brain-hardware-layout-proposal.dwg>).
3. **DWG SHA-256:** `ca1f7673b296c5db112226f735611092e3d092c9031dfe3de1c2f708860d613e`.
4. **State:** PARTIAL_COMPACT_BRAIN_PROPOSAL_SAVED_CURRENT_GEOMETRY_CHECKED.
5. **Frame:** mm; inherited450 ×490 mm footprint-centredX/Y,Zup; planar installation referenceZ0.
6. **Actual execution model:** unavailable.

## Installed occurrences

Translations are CAD placement proposal coordinates. Identity rotations and unit scales retain each source definition's geometry. Full source hashes and 4 × 4 matrices are retained in the execution job.

| Root | Library / assembly | Readable component or reference | Quantity | Source DWG SHA-256 | Translation X, Y, Z (mm) |
|---|---|---|---:|---|---|
| 1 | 245 | Mini 450 × 490 mm planar footprint | 1 | `d890c11303d90da0a029a2d23cf11c64a82e084c68e4411910c0921f7ff66b3d` | `[0.0, 0.0, 0.0]` |
| 2 | assembly | Shared compact three-tier Brain partial layout PROPOSAL | 1 | `ca59f3dc8b93adc71737fd3096e1f8f1ab4f58458f5b71c4de81a4ac2adee01b` | `[0.0, 20.0, 0.0]` |
| 3 | 253 | Open BTS7960 source planar interface reference | 1 | `b26130af1423c3312823ecabf596941ae4f672ccb3e12b93e4bba856b3986ffb` | `[-200.0, 100.0, 0.0]` |
| 4 | 255 selected XY derivative | Propow CPN24050 selected306 by174 mm XY footprint reference | 1 | `6ea66c78b9794098d7f3a085c23c4661ee428afdfe9b2e71e161e48cebf48923` | `[-153.0, -210.0, 0.0]` |

## Technical specification

1. **Arrangement:** the 450 × 490 mm planar base reference, compact Brain proposal at (0, 20, 0) mm, Open BTS7960 planar interface and selected 306 × 174 mm battery XY footprint occupy four source-pinned roots. The Brain source contains its nine existing hardware/reference roots. The selected battery face reuses the original library 255 source; its 200/220 mm height attribution remains in the battery source companion.
2. **Projection checks:** represented hardware projections lie within the planar base reference. The Brain Y translation supplies the proposed 5 mm projected gap to the battery footprint reference. Current sampled source bounds, planar references and pairwise separation scope are retained in layout-checks.json. Mounting interfaces and full battery-height geometry retain their source inputs.
3. **Source geometry:** 4 root occurrences contain 956 geometry occurrences: {'LwPolyline': 7, 'Solid3D': 910, 'Mesh': 8, 'Circle': 31}. Complete noncommon source-property fingerprints, all composed nested matrices and exact source DWG hashes PASS. Planar curves and circles are compared through their original native properties.
4. **Shared Brain scope:** the reused three-tier stage has five sampled board projections inside the open plate projection and 5 mm proposed represented gaps. Avaota sampled X-edge inset is 0.012499695 mm. Plate supports, enclosure dimensions, source connector representation and power-board source inputs retain the shared Brain companion's partial scope.
5. **Persistence:** initial and per-step checkpoint saves completed. Current owned geometry and millimetre units were checked before final SAVE. Completed original SAVE response, exact target path, file existence/size/hash, save audit and zero dropped entities PASS. Current geometry revision remained unchanged through SAVE. Verification uses retained current records.
6. **Appearance:** actual current-record XY, XZ and isometric views inspected PASS; native solid-boundary samples, every unique Mesh face edge and source planar curves use their actual nested transforms. Unsupported trim endpoints retain the renderer's recorded scope.
7. **Cleanup:** finished owned document 779 guarded closed after persistence, geometry and visual checks. Unrelated documents preserved.

## Sources — online

1. Sowbot hardware and installed quantities.
2. Beitian BT-560 manufacturer page.
3. Exact ORP plate source.

## References

1. [Shared compact Brain component attribution and source limits](<brain-stacked-hardware-layout-proposal.md>).
2. Execution job and occurrence matrices.
3. Current source geometry and nested transforms.
4. Current-bound sampled layout checks.
5. Completed SAVE receipt.
6. Actual current-record views.
7. Guarded cleanup.
8. [Previous proposal](<mini-hardware-reference-placement-proposal.md>), preserved.
9. [Mini 450 × 490 mm planar footprint source companion](<../../../../library/standards/sowbot-mini-chassis-footprint-reference.md>).
10. [Shared compact three-tier Brain partial layout PROPOSAL source companion](<brain-stacked-hardware-layout-proposal.md>).
11. [Open BTS7960 source planar interface reference source companion](<../../../../library/standards/open-bts7960-mini-source-interface-reference.md>).
