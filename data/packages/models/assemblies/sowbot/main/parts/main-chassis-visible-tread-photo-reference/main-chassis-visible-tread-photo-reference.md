# GD DG Shengtian main track visible photo reference

1. **Library number:** 280.
2. **Plan job:** 3; partial reference stage.
3. **Native drawing:** [GD DG Shengtian main track visible photo reference](<main-chassis-visible-tread-photo-reference.dwg>).
4. **DWG SHA-256:** `3ba7d97170ea1a796287ef143ac014aee1cb5d1edb9c02737a6932ceebb6f1eb`.
5. **State:** PARTIAL_REFERENCE_SAVED_REOPENED_NATIVE_ARRAYS_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. Conditional open straight-tread reference plus three coplanar projected visible cleat-band overlays;side-plane silhouette hypothesis failed separately
2. X along travel,Y image-left,Zup;origin at first selected source pixel on conditional straight-tread reference planeZ0
3. Conditional representative perspective camera: training maximum 2.187019 px; held-out cleat direction maximum 3.471280 px, within ±4 px picks. Source track width 150 mm calibrates equal tread strips.
4. Four open Mesh references: one four-vertex straight-tread patch and three four-vertex projected visible cleat-band overlays, 16 vertices and eight triangles total. Cleat bands use inspected source direction segments with ±2 pixel band offsets; physical relief is excluded.
5. The attempted constant-Y side silhouette produced a 3116.783 mm contour Z span and one negative camera depth, failing the source height/ray sanity check. The recorded 2037.239 mm value is its top-plane shift, calculated from minimum silhouette Z, rather than the full contour span. Its failed native stage is preserved separately; this supported stage contains zero side-silhouette lines.

## Checks

1. Immediate source import save, DWG-context save, metadata/view checkpoints, final save and fresh reopen PASS. Zero dropped entities.
2. Reopened native Mesh vertices, faces and subdivision 0 match the prepared arrays exactly; millimetre header and source hashes PASS.
3. Actual native viewport inspected for the represented reference geometry; four retained views use the reopened native records.
4. Guarded owned-document cleanup PASS: 749, 748, 747 closed; unrelated Start 1 preserved.

## Views

1. [XY](<main-chassis-visible-tread-photo-reference-XY.png>).
1. [XZ](<main-chassis-visible-tread-photo-reference-XZ.png>).
1. [YZ](<main-chassis-visible-tread-photo-reference-YZ.png>).
1. [isometric](<main-chassis-visible-tread-photo-reference-isometric.png>).
1. [Native viewport](<main-chassis-visible-tread-photo-reference-native.png>).

## Sources — online

1. GD DG Shengtian main track visible photo reference source.

## References

1. Construction, source pins, native arrays, checkpoints, readback and cleanup recipe: ``.
2. Existing runtime: `PYTHONPATH=/tmp/3dmodeling-native-reader`; native helpers from the installed cad-ocs-engineering skill. Python numpy/ezdxf build the source-pinned DXF intermediate. Conversion changes are retained in `job.json`; source originals remain unchanged.

## Bounded side recovery

1. The calibrated camera centre has Y = −126.328915 mm; the assumed outboard plane has Y = −145.826614 mm, a separation of 19.497699 mm. Selected contour rays cross the plane projection singularity. Changing the constant plane datum alone cannot repair the opposite ray-depth signs.
2. Three independently selected visible front-tread spans were tested with common transverse edges 150 mm apart and Z between −550 and 0 mm. Maximum endpoint residuals were 6.236769, 6.188717 and 8.179740 px, exceeding the ±4 px pick interval. These are failed representative-camera hypotheses; they add no native geometry.
3. Side recovery state: PAUSED_SIDE_SILHOUETTE_ONLY. Supported four-Mesh stage and hash above are preserved. Evidence and local method: ``.
