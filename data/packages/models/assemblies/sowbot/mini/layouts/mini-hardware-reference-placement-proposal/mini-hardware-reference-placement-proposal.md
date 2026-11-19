# Mini hardware reference placement proposal

1. **Plan identity:** assembly 6, Mini Sowbot; partial reference-placement proposal.
2. **Native drawing:** [Mini hardware reference proposal](<mini-hardware-reference-placement-proposal.dwg>).
3. **DWG SHA-256:** `30c1bc3b7957a43c476706cd241401cb2390edfc7a8f356466082c001843f3dd`.
4. **State:** PARTIAL_REFERENCE_PLACEMENT_PROPOSAL_SAVED_CHECKED.
5. **Frame:** millimetres; X and Y follow the centred 450 × 490 mm Mini installation footprint, Z points up; installation-reference plane Z = 0.
6. **Actual execution model:** unavailable.

## Installed occurrences

The root rotations are identity and scale is one. Coordinates are CAD placement proposal inputs under plan assembly 6.

| Root | Library / assembly | Readable reference | Quantity | Source DWG SHA-256 | Translation X, Y, Z (mm) |
|---|---|---|---:|---|---|
| 1 | assembly | Mini footprint and Brain five-board partial proposal | 1 | `60f4d2ed0294c15485a4799f5284876de4eaf7b7d573d26d71edfb693a15548d` | `[0.0, 0.0, 0.0]` |
| 2 | 253 | Open BTS7960 source planar interface reference | 1 | `b26130af1423c3312823ecabf596941ae4f672ccb3e12b93e4bba856b3986ffb` | `[-200.0, 100.0, 0.0]` |
| 3 | 255 selected XY derivative | Propow CPN24050 selected306 by174 mm XY footprint reference | 1 | `6ea66c78b9794098d7f3a085c23c4661ee428afdfe9b2e71e161e48cebf48923` | `[-153.0, -210.0, 0.0]` |

## Technical specification and checks

1. **Existing geometry reuse:** the first root contains the checked Mini footprint and Brain five-board proposal. The driver root preserves all 36 exact source planar features from library 253: six closed polylines and 30 circles. The battery root contains the 306 × 174 mm XY reference selected from library 255's existing dimension-field source.
2. **Battery source selection:** library 255 also contains two independent height-field drafting rectangles. The selected local derivative retains the first XY rectangle as a zero-thickness triangulated face. The original 255 drawing and literal 200/220 mm height alternatives remain unchanged. This source selection serves existing component job 29.
3. **Saved geometry:** three root occurrences; 910 solid occurrences, seven polylines, 30 circles and one Mesh. All noncommon native source properties and composed root/nested matrices PASS. Source file hashes match their pinned definitions.
4. **Projected fit:** represented Brain, driver and battery XY references lie inside the 450 × 490 mm source footprint. Minimum represented margins are 15.014023 mm for the Brain boundary sample, 25 mm for the driver reference and 35 mm for the battery footprint.
5. **Removal projection:** battery-to-Brain projected Y gap is 38.983912571 mm. The battery's +Z projection clears the represented driver and Brain bounds. Battery case height and driver physical height retain their source attribution limits; this check covers the retained planar references and Brain boundary sample.
6. **Persistence:** immediate and per-insertion/placement saves, canonical verified save, path/hash and audit PASS. A fresh reopen completed as document 774 before the instruction to omit verification reopen; this history is retained. Current geometry uses the saved stable records. No further verification OPEN is part of this method.
7. **Appearance and cleanup:** saved-record XY and isometric views inspected PASS. Owned construction 773 and completed inspection 774 guarded closed. Source driver inspection 772 and battery staging documents 769–771 were previously closed after their checks. Unrelated Start 1 preserved.

## Sources — online

1. Sowbot hardware, first Mini 450 × 490 mm source footprint and component identities.
2. Open BTS7960 exact source document, driver interface geometry and source revision.
3. Propow CPN24050 source, retained manufacturer dimension field; exact retained source attribution is linked in the battery companion.

## References

1. [Existing Mini footprint and Brain proposal](<../mini-board-footprint-layout-proposal/mini-board-footprint-layout-proposal.md>).
2. [Driver source reference](<../../../../../interface-references/mechanical/open-bts7960-mini-source-interface-reference/open-bts7960-mini-source-interface-reference.md>), library 253.
3. [Battery dimension-field reference](<../../../../../interface-references/mechanical/propow-cpn24050-dimension-field-reference/propow-cpn24050-dimension-field-reference.md>), library 255.
4. [Top saved-record view](<mini-hardware-reference-placement-proposal-XY.png>).
5. [Isometric saved-record view](<mini-hardware-reference-placement-proposal-isometric.png>).
6. Source pins and root proposal matrices.
7. Battery source-selection conversion.
8. Exact source properties and nested matrices.
9. Projected fit and removal checks.
10. Guarded document cleanup.
