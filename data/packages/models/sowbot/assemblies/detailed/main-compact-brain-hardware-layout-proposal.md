# Main compact Brain hardware layout proposal

1. **Plan identity:** assembly 5, Main robot; partial hardware placement proposal.
2. **Native drawing:** [Main proposal](<main-compact-brain-hardware-layout-proposal.dwg>).
3. **DWG SHA-256:** `343eeb6daf42a9bbfd11b4dd55cfef051e633b0a74b9ece9b7e324cefb709c35`.
4. **State:** PARTIAL_COMPACT_BRAIN_PROPOSAL_SAVED_CURRENT_GEOMETRY_CHECKED.
5. **Frame:** millimetres; inherited conditional track Xtravel,Ytransverse,Zup; Z0 is straight-tread reference plane, not ground contact.
6. **Actual execution model:** unavailable.

## Installed occurrences

Translations are CAD placement proposal coordinates. Identity rotations and unit scales retain each source definition's geometry. Full source hashes and 4 × 4 matrices are retained in the execution job.

| Root | Library / assembly | Readable component or reference | Quantity | Source DWG SHA-256 | Translation X, Y, Z (mm) |
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
| 10 | assembly | Shared compact three-tier Brain partial layout PROPOSAL | 1 | `ca59f3dc8b93adc71737fd3096e1f8f1ab4f58458f5b71c4de81a4ac2adee01b` | `[250.0, 726.0, 250.0]` |

## Technical specification

1. **Arrangement:** ten roots contain the two source-visible track references, six VariCore photo-exterior battery occurrences, two ODrive v3.6 planar controller references and the compact Brain proposal. The Brain root is (250, 726, 250) mm; its Y coordinate increases 36 mm from the previous proposal. The other nine root coordinates are retained.
2. **Projection checks:** the revised Brain position supplies a 5 mm proposed projected gap beyond the last battery row. All six +Z battery-removal projection checks PASS against represented Brain/controller geometry. Track geometry uses the conditional straight-tread reference plane Z = 0. The visible track patches, conditional battery exterior and planar controller references retain their component representations.
3. **Source geometry:** 10 root occurrences contain 1015 geometry occurrences: {'Mesh': 104, 'Solid3D': 910, 'Circle': 1}. Complete noncommon source-property fingerprints, all composed nested matrices and exact source DWG hashes PASS. Planar curves and circles are compared through their original native properties.
4. **Shared Brain scope:** the reused three-tier stage has five sampled board projections inside the open plate projection and 5 mm proposed represented gaps. Avaota sampled X-edge inset is 0.012499695 mm. Plate supports, enclosure dimensions, source connector representation and power-board source inputs retain the shared Brain companion's partial scope.
5. **Persistence:** initial and per-step checkpoint saves completed. Current owned geometry and millimetre units were checked before final SAVE. Completed original SAVE response, exact target path, file existence/size/hash, save audit and zero dropped entities PASS. Current geometry revision remained unchanged through SAVE. Verification uses retained current records.
6. **Appearance:** actual current-record XY, XZ and isometric views inspected PASS; native solid-boundary samples, every unique Mesh face edge and source planar curves use their actual nested transforms. Unsupported trim endpoints retain the renderer's recorded scope.
7. **Cleanup:** finished owned document 778 guarded closed after persistence, geometry and visual checks. Unrelated documents preserved.

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
8. Previous proposal, preserved.
9. Main chassis two source-visible track patches source companion.
10. [VariCore VC-1280NA battery photo exterior PROPOSAL source companion](<../../../../library/parts/electrical/varicore-vc1280na-photo-exterior-stage.md>).
11. [VariCore VC-1280NA battery photo exterior PROPOSAL source companion](<../../../../library/parts/electrical/varicore-vc1280na-photo-exterior-stage.md>).
12. [VariCore VC-1280NA battery photo exterior PROPOSAL source companion](<../../../../library/parts/electrical/varicore-vc1280na-photo-exterior-stage.md>).
13. [VariCore VC-1280NA battery photo exterior PROPOSAL source companion](<../../../../library/parts/electrical/varicore-vc1280na-photo-exterior-stage.md>).
14. [VariCore VC-1280NA battery photo exterior PROPOSAL source companion](<../../../../library/parts/electrical/varicore-vc1280na-photo-exterior-stage.md>).
15. [VariCore VC-1280NA battery photo exterior PROPOSAL source companion](<../../../../library/parts/electrical/varicore-vc1280na-photo-exterior-stage.md>).
16. [ODrive v3.6 135 by 50 mm planar reference PROPOSAL source companion](<../../../../library/parts/electrical/odrive-v36-135x50-source-dimension-reference.md>).
17. [ODrive v3.6 135 by 50 mm planar reference PROPOSAL source companion](<../../../../library/parts/electrical/odrive-v36-135x50-source-dimension-reference.md>).
18. [Shared compact three-tier Brain partial layout PROPOSAL source companion](<brain-stacked-hardware-layout-proposal.md>).
