# Beitian BT-560 traced exterior stage

1. **Library number:** 281.
2. **Plan job:** 24; partial reference stage.
3. **Native drawing:** [Beitian BT-560 traced exterior stage](<beitian-bt560-raster-exterior-stage.dwg>).
4. **DWG SHA-256:** `275dbde0fe8fddeeff433ececf528a00f3fac30455867fff927c497d6436f986`.
5. **State:** PARTIAL_REFERENCE_SAVED_REOPENED_NATIVE_ARRAYS_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. Manufacturer BT-560 drawing revision 5.53, January 2023: overall length 58.6 ± 0.3 mm; barrel Ø25.0 ± 0.3 mm; collar Ø27.3 ± 0.3 mm; collar span 16.10 ± 0.3 mm.
2. The outer meridian uses eight original raster stations and 128 angular segments. The rounded or bevelled far tip and collar steps retain their traced profile. Axial calibration uses the source collar span 16.1 mm and remaining barrel span 42.5 mm. Raster pick uncertainty is ±1.5 px, separate from manufacturing tolerances.
3. Model axial extent: 58.6 mm. Traced maximum diameter: 27.255639 mm, within the source 27.3 ± 0.3 mm interval. Main barrel radius: 12.5 mm. Collar and tip profiles are raster estimates.
4. The far tip face and separate SMA end-face annular reference use the source end views. Estimated opening radius: 3.791667 mm, from the 20/72 pixel radius ratio. The source seal callout is 0.4 mm; axial endpoint attribution remains separate.
5. Frame: Z follows the connector axis from the collar rear plane at 0 mm toward the far tip at 58.6 mm; X and Y are radial. Existing library 278 dimensional envelopes are preserved.

## Checks

1. Immediate source import save, DWG-context save, metadata/view checkpoints, final save and fresh reopen PASS. Zero dropped entities.
2. Reopened native Mesh vertices, faces and subdivision 0 match the prepared arrays exactly; millimetre header and source hashes PASS.
3. Actual native viewport inspected for the represented reference geometry; four retained views use the reopened native records.
4. Owned document cleanup is recorded in the execution recipe after saved/reopened checks.

## Views

1. [XY](<beitian-bt560-raster-exterior-stage-XY.png>).
1. [XZ](<beitian-bt560-raster-exterior-stage-XZ.png>).
1. [YZ](<beitian-bt560-raster-exterior-stage-YZ.png>).
1. [isometric](<beitian-bt560-raster-exterior-stage-isometric.png>).
1. [Native viewport](<beitian-bt560-raster-exterior-stage-native.png>).

## Sources — online

1. Beitian BT-560 traced exterior stage source.

## References

1. Construction, source pins, native arrays, checkpoints, readback and cleanup recipe: ``.
2. Existing runtime: `PYTHONPATH=/tmp/3dmodeling-native-reader`; native helpers from the installed cad-ocs-engineering skill. Python numpy/ezdxf build the source-pinned DXF intermediate. Conversion changes are retained in `job.json`; source originals remain unchanged.
