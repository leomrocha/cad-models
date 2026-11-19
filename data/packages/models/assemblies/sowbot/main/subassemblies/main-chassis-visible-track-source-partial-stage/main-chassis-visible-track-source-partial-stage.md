# Main chassis source-visible track partial stage

1. **Plan identity:** assembly 1, Main tracked chassis; component job 03 supplies two source-visible track occurrence patches.
2. **State:** PARTIAL_SAVED_REOPENED_SOURCE_MESHES_CHECKED.
3. **Native drawing:** [Two-track visible-surface stage](<main-chassis-visible-track-source-partial-stage.dwg>).
4. **DWG SHA-256:** `6b0f9d08fcc85a779fe1ef1ae908d22d8a697df18c962107c38d8b38d1ba6c77`.
5. **Actual execution model:** unavailable.

## Technical specification

1. **Geometry:** five open Mesh surfaces, 20 vertices and 10 triangles. The near-track occurrence contains the retained straight-tread patch and three source-projected cleat-band overlays. The far-track occurrence contains one separately traced visible interior patch.
2. **Frame:** millimetres; X follows travel toward the distant end, Y points across the track pair toward image-left, Z points up. Z = 0 is the common straight-tread reference plane. The ground-contact datum retains the full-track side-silhouette pause.
3. **Source calibration:** retained conditional perspective camera, square pixels, principal point (218, 125) px and equal 150 mm source-claimed track widths. Training direction residual 2.187019 px; independent held-out direction residual 3.471280 px, within the retained ±4 px pick interval.
4. **Far-track source picks:** (124, 30), (188, 9), (205, 13), (137, 37) px in the unchanged 436 × 250 px photograph. Positive camera depth PASS; backprojection/reprojection error 0.00000000000003553 px is a construction check. The per-vertex intervals propagate ±4 px at the fixed camera and plane; camera uncertainty and physical tread relief remain separate.
5. **Source reuse:** library 280 near-track arrays are unchanged. The far-track patch uses its own source pixels and resulting common-frame coordinates. All five layer names retain the near/far occurrence roles in the reopened native records.
6. **Persistence:** source DXF opened and immediately saved; DWG context, provenance, shaded view and extents checkpointed separately. Canonical save/reopen, exact vertices/triangles, millimetre units and source SHA-256 checks PASS.
7. **Appearance:** reopened-record XY and isometric views inspected PASS. The earlier native viewport shows the near-track patch and three cleat bands. The separate viewport retry returned the Start screen. All five mesh arrays and their layers match the saved drawing. Delivered views derive from the five saved native records.
8. **Partial scope:** carrier material correspondence, crossmember plane height, reducer face datum and full track side/return contour retain their individual Sol/Astra pause evidence. These open visible-source surfaces contain no inferred carrier or hidden belt geometry.
9. **Cleanup:** owned documents 764, 765 and 766 guarded closed after verified save/reopen and geometry checks; unrelated Start 1 preserved.

## Sources — online

1. [Sowbot hardware source](https://sowbot.co.uk/hardware/), original main-chassis photo SHA-256 `3897d5debeae511473cf8432be790d350d4d252ac97db0883011e7018a74b392`; source claim 150 mm tread width.

## References

1. [Existing near-track component](<../../parts/main-chassis-visible-tread-photo-reference/main-chassis-visible-tread-photo-reference.md>), library 280; canonical component preserved.
2. [Top saved-record view](<view-2.png>).
3. [Isometric saved-record view](<view-1.png>).
4. Source-calibrated construction recipe and arrays.
5. Original-pixel pick overlay.
6. Native array/unit/source checks.
7. Calibrated camera and independent direction test.

The conversion uses the existing Python 3.12 runtime with `PYTHONPATH=/tmp/3dmodeling-native-reader` for numpy and ezdxf. It back-projects selected photo pixels to open planar Mesh surfaces in a DXF2018 millimetre construction intermediate, then imports those exact arrays into OCS DWG. The source photograph, camera receipt, existing component DWG and prior failed side hypotheses remain unchanged.
