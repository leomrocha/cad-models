# Beitian BT-560 antenna

1. **Library number:** 278.
2. **Plan job:** 24; partial reference stage.
3. **Native drawing:** [Beitian BT-560 antenna](<beitian-bt560-dimensional-exterior-reference.dwg>).
4. **DWG SHA-256:** `6f23d10077e553d85e283619dfc06b46c4f369dff1192d6fe59ca25978e376c4`.
5. **State:** PARTIAL_REFERENCE_SAVED_REOPENED_NATIVE_ARRAYS_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. Source BT-560 manufacturer revision 5.53, January 2023: overall 58.6 ± 0.3 mm; barrel Ø25.0 ± 0.3 mm; collar Ø27.3 ± 0.3 mm; collar length 16.10 ± 0.3 mm; SMA-J connector label.
2. Two open faceted cylindrical dimensional envelopes, 256 triangles each, 128 angular segments. The rounded tip and collar recesses remain source-shape features beyond this envelope stage.
3. Z follows connector axis from the collar rear plane at 0 toward the 58.6 mm barrel end; X/Y are radial. Maximum nominal radial chord deviations: 0.003765 mm barrel, 0.004111 mm collar.

## Checks

1. Immediate source import save, DWG-context save, metadata/view checkpoints, final save and fresh reopen PASS. Zero dropped entities.
2. Reopened native Mesh vertices, faces and subdivision 0 match the prepared arrays exactly; millimetre header and source hashes PASS.
3. Actual native viewport inspected for the represented reference geometry; four retained views use the reopened native records.
4. Guarded owned-document cleanup PASS: 740, 739, 738 closed; unrelated Start 1 preserved.

## Views

1. [XY](<../../images/beitian-bt560-dimensional-exterior-reference-XY.png>).
1. [XZ](<../../images/beitian-bt560-dimensional-exterior-reference-XZ.png>).
1. [YZ](<../../images/beitian-bt560-dimensional-exterior-reference-YZ.png>).
1. [isometric](<../../images/beitian-bt560-dimensional-exterior-reference-isometric.png>).
1. [Native viewport](<../../images/beitian-bt560-dimensional-exterior-reference-native.png>).

## Sources — online

1. Beitian BT-560 antenna source.

## References

1. Construction, source pins, native arrays, checkpoints, readback and cleanup recipe: ``.
2. Existing runtime: `PYTHONPATH=/tmp/3dmodeling-native-reader`; native helpers from the installed cad-ocs-engineering skill. Python numpy/ezdxf build the source-pinned DXF intermediate. Conversion changes are retained in `job.json`; source originals remain unchanged.
