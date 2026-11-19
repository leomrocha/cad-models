# VariCore VC-1280NA photo exterior stage

1. **Library number:** 282.
2. **Plan job:** 28; partial reference stage.
3. **Native drawing:** [VariCore VC-1280NA photo exterior stage](<varicore-vc1280na-photo-exterior-stage.dwg>).
4. **DWG SHA-256:** `07b7a363a9d1eaeb1da39c246c406602f95ca2ee44262107be233cffdd898f3e`.
5. **State:** PARTIAL_REFERENCE_SAVED_REOPENED_NATIVE_ARRAYS_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. Manufacturer VC-1280Na+ source states 12 V, 80 Ah and ordered size 330 × 170 × 220 mm. Listing photo identifies VC-1280NA / 80 Ah. Library 279 source-size/front reference is preserved.
2. Representative metric perspective camera assigns the first two size values to the photographed lid extents and the 220 mm value to the front base-to-positive-cap height. These endpoint assignments are CAD inputs. Top-corner coordinates vary within ±3 px per coordinate. Positive-terminal direction is calibration; independent negative-terminal direction residual is 0.315136 px.
3. Source case/lid/front contours, lid top and visible display faces are inverse-projected under that camera. Display height 4.75 mm and terminal bracket top height 6.2 mm above the lid are photographic estimates. Raster feature uncertainty is ±3 px; camera and height-assignment uncertainty are separate.
4. Both terminal knobs and two exposed studs use their own source pixel profiles with three axial radius stations and 64 angular segments. Visible cap faces and bracket top faces are retained; fine thread/knurl relief is represented by the outer raster profile.
5. The camera-calibrated front case height is 192.992124143043 mm. All surfaces remain a conditional photo exterior stage; the manufacturer ordered dimensions retain their own source status. Frame: X across lid width, Y from front toward rear, Z up, front base plane at Z = 0.
6. Seller photo 1 shows the right case wall, two lid seam lines and the right carrying-strap passage on the labelled VC-1280NA pack. The photo identifies these features in image coordinates. Metric construction needs a shared side-plane or depth datum.

## Checks

1. Immediate source import save, DWG-context save, metadata/view checkpoints, final save and fresh reopen PASS. Zero dropped entities.
2. Reopened native Mesh vertices, faces and subdivision 0 match the prepared arrays exactly; millimetre header and source hashes PASS.
3. Native capture identity FAIL: OpenAEC home UI was returned. The failed image remains local. Four delivered views use actual reopened native Mesh records.
4. Owned document cleanup is recorded in the execution recipe after saved/reopened checks.
5. **Cross-view registration:** Each terminal cap centre was taken from the vertex shared by all 64 cap triangles. The best of 98 photo-1 camera fits that matched the lid picks had a maximum held-out coordinate residual of 17.576 px. No fit matched more than two of seven terminal, seam and base landmarks within their assigned ±5 to ±6 px pick intervals. The eight nominal photo-2 fits had a smallest maximum held-out coordinate residual of 20.976 px. The retained photographs support the visible right-wall trace in pixels. Actual checking model unavailable.

## Views

1. [XY](<varicore-vc1280na-photo-exterior-stage-XY.png>).
1. [XZ](<varicore-vc1280na-photo-exterior-stage-XZ.png>).
1. [YZ](<varicore-vc1280na-photo-exterior-stage-YZ.png>).
1. [isometric](<varicore-vc1280na-photo-exterior-stage-isometric.png>).
1. Native-record boundary views are delivered; failed viewport capture is retained locally.

## Sources — online

1. Exact VC-1280NA listing and photo 3 supplies the photographed case, lid, display and terminal exterior.
1. VariCore VC-1280NA photo exterior stage source.

## References

1. Construction, source pins, native arrays, checkpoints, readback and cleanup recipe: ``.
2. Existing runtime: `PYTHONPATH=/tmp/3dmodeling-native-reader`; native helpers from the installed cad-ocs-engineering skill. Python numpy/ezdxf build the source-pinned DXF intermediate. Conversion changes are retained in `job.json`; source originals remain unchanged.

1. [Top-facing isometric saved-record view](<varicore-vc1280na-photo-exterior-stage-top-isometric.png>).
