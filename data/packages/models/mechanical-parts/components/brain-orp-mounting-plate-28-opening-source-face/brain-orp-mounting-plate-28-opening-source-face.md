# Brain Rosmo ORP mounting plate with complete opening pattern

1. **Library number** 314.
2. **Native drawing** [28-opening source face](<brain-orp-mounting-plate-28-opening-source-face.dwg>).
3. **DWG SHA-256:** `be5094170d968f885e75cd99a29e4fb02fc9afda9323c30fabfc9181be6afb38`. DWG 2018, 72,837 bytes.
4. **State** SAVED AND SOURCE CHECKED. Native planar face at Z = 0 mm.
5. **Execution model** Actual identity unavailable.

## Technical specification

1. **Outline** 99.9998 × 99.9998 mm in the original plate-centred XY frame. Source corner radius is 3.499993 mm.
2. **Openings** The union of 70 source records forms 28 connected opening regions. The records include 39 explicit holes within the ORP footprint, five board-level holes, 24 layer-10 circles and two non-plated cutout contours. The native face preserves the earlier perimeter and includes 18 more distinct openings than the earlier face, library 285 (earlier revision `model-285`; [current catalogue revision](<brain-orp-mounting-plate-28-opening-source-face.md>)).
3. **Material face** One connected Mesh, 2,051 vertices, 2,105 triangles, 28 inner loops and Euler characteristic −27. Arc profiles use a maximum chord error of 0.002 mm. The face represents the mounting pattern at zero thickness.

## Verification

1. Native Mesh arrays match the prepared union and triangulation. The source revision, prior library drawing and model frame are retained.
2. Verified SAVE confirmed path, bytes, SHA-256 and zero dropped entities. The [native XY projection](<brain-orp-mounting-plate-28-opening-source-face-XY.png>) was inspected before guarded closure.

## Sources — online

1. Original Rosmo ORP EasyEDA document, revision `1ff7250ebd4c4571b7af0292bb667b55`.
2. Sowbot hardware table, Brain plate and its nominal 100 × 100 mm size.
