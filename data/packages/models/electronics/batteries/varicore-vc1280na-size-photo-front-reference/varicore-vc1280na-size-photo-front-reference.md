# VariCore VC-1280NA80Ah battery

1. **Library number:** 279.
2. **Plan job:** 28; partial reference stage.
3. **Native drawing:** [VariCore VC-1280NA80Ah battery](<varicore-vc1280na-size-photo-front-reference.dwg>).
4. **DWG SHA-256:** `b2e2eb4e789d91cc21750a9c338d66df1a5c6f49c14b6c4fff54e22c8889496c`.
5. **State:** PARTIAL_REFERENCE_SAVED_REOPENED_NATIVE_ARRAYS_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. Manufacturer VC-1280Na+ source: 12 V, 80 Ah, ordered size tuple 330 × 170 × 220 mm and mass 12.5 kg. Listing photo labels VC-1280NA / 80 Ah.
2. Twelve native lines represent the separate 330 × 170 × 220 mm size reference; the ordered tuple maps to X/Y/Z as a CAD input.
3. Two open photographed front patches share the observed y = 500 px seam. Case pixels y = 500–773; lid pixels y = 475–500. Their common boundary has zero overlapping area.
4. Photo calibration assumes the 330 mm first size value spans the 738 px top-front edge and equal X/Z pixel scale. Calculated scale 0.447154 mm/px gives combined front height 133.252033 mm. These photo estimates retain perspective foreshortening; the 220 mm overall size reference stays separately represented.

## Checks

1. Immediate source import save, DWG-context save, metadata/view checkpoints, final save and fresh reopen PASS. Zero dropped entities.
2. Reopened native Mesh vertices, faces and subdivision 0 match the prepared arrays exactly; millimetre header and source hashes PASS.
3. Actual native viewport inspected for the represented reference geometry; four retained views use the reopened native records.
4. Guarded owned-document cleanup PASS: 743, 742, 741 closed; unrelated Start 1 preserved.

## Views

1. [XY](<varicore-vc1280na-size-photo-front-reference-XY.png>).
1. [XZ](<varicore-vc1280na-size-photo-front-reference-XZ.png>).
1. [YZ](<varicore-vc1280na-size-photo-front-reference-YZ.png>).
1. [isometric](<varicore-vc1280na-size-photo-front-reference-isometric.png>).
1. [Native viewport](<varicore-vc1280na-size-photo-front-reference-native.png>).

## Sources — online

1. VariCore VC-1280NA80Ah battery source.

## References

1. Construction, source pins, native arrays, checkpoints, readback and cleanup recipe: ``.
2. Existing runtime: `PYTHONPATH=/tmp/3dmodeling-native-reader`; native helpers from the installed cad-ocs-engineering skill. Python numpy/ezdxf build the source-pinned DXF intermediate. Conversion changes are retained in `job.json`; source originals remain unchanged.
