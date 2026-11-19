# Brain ORP mounting plate source open face

1. **Library number:** 285.
2. **Plan component:** model 32, Brain mounting plate; source open-face stage.
3. **Native drawing:** [Source open face](<brain-mounting-plate-source-open-face.dwg>).
4. **DWG SHA-256:** `c5e100633abca40daf5bd5f4f0e6346bd021a1cb82b60a79aeaccc36f4ee5ae0`.
5. **Representation:** one open planar Mesh surface, Z = 0 mm; 816 vertices and 834 triangles.
6. **State:** PARTIAL_SOURCE_OPEN_FACE_SAVED_CURRENT_GEOMETRY_CHECKED.
7. **Actual execution model:** unavailable.

## Technical specification

1. **Source:** exact ORP EasyEDA revision `1ff7250ebd4c4571b7af0292bb667b55`, original JSON SHA-256 `7dc2d170ca2def020656b6bb60a6307799179b3edb62a37369aa6b53ac3b949b`.
2. **Coordinates:** millimetres; X = 0.254 × (source X − 4216.85), Y = 0.254 × (3177.15 − source Y), Z = 0. The source-linked 100 mm plate claim calibrates 393.7 native units to 99.9998 mm. Source quarter-circle corner radius is 3.499993 mm.
3. **Source face:** 17 unique circle records and two original overlapping npth polygons form 10 connected opening regions. The original analytic curves, duplicate source-record history and three nonjoining tracks remain in library 254. The open-face stage uses the union of the opening regions as the material-face boundaries.
4. **Faceting:** analytic circles and perimeter quarter-arcs sampled with a 0.002 mm chord-error limit; maximum observed bound 0.001988858923 mm. Constrained Delaunay triangulation covers the sampled face with zero symmetric-difference area; triangle overlap magnitude is below 0.00000001 mm². Face area is 9619.406702876 mm².
5. **Topology:** one connected open surface, 10 inner boundary loops, Euler characteristic −9; every triangle edge has incidence one or two. Native arrays exactly match the source-bound prepared vertices and triangles; subdivision is zero.
6. **Persistence:** source DXF loaded for construction and immediately saved. Provenance checkpoint and canonical save completed; correct target path, file existence, 41,366-byte size, SHA-256, save audit and zero dropped entities PASS. Current owned Mesh arrays, units and source hashes were checked before the final save. The final save retains the same geometry revision.
7. **Appearance and cleanup:** current-record top boundary view inspected PASS. Owned document 775 guarded closed after verified persistence. Unrelated Start 1 preserved.
8. **Partial geometry scope:** the open source face has zero thickness. Source plate thickness and its mating elevation remain separate component and assembly inputs.

## Sources — online

1. Original EasyEDA ORP document, source curves and revision.
2. Sowbot hardware table, mounting-plate identity and 100 × 100 mm claim.

## References — library

1. [Original analytic pattern reference](<../../interface-references/brain-mounting-plate-source-pattern-reference/brain-mounting-plate-source-pattern-reference.md>), library 254, preserved.
2. [Top current-record boundary view](<brain-mounting-plate-source-open-face-XY.png>).
3. [Isometric current-record boundary view](<brain-mounting-plate-source-open-face-isometric.png>).

The consuming project's retained recipe reuses the constrained Delaunay cap method for a single open face. Python 3.12, numpy, ezdxf and Shapely create a bounded faceted DXF2018 Mesh in millimetres from the existing source curves. OCS loads that construction intermediate and saves the native DWG. Original source bytes and library 254 remain unchanged; the conversion adds the triangulated face representation. Source pins, exact-array checks, original standalone-audit extension error, corrected save-audit method and cleanup receipts remain in the caller's execution storage.
