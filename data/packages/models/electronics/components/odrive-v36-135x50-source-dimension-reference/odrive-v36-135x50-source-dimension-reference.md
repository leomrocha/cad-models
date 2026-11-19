# ODrive v3.6 manufacturer size reference

1. **Library number:** 283.
2. **Plan job:** 26; partial reference stage.
3. **Native drawing:** [ODrive v3.6 manufacturer size reference](<odrive-v36-135x50-source-dimension-reference.dwg>).
4. **DWG SHA-256:** `ea06fee77de0dc0e196a6521bb397a76531db4418699aafdcf6cc8eeac35547a`.
5. **State:** PARTIAL_REFERENCE_SAVED_REOPENED_NATIVE_ARRAYS_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. The manufacturer Mechanical Specifications comparison table assigns 135 × 50 mm and 80 g to ODrive v3.6 (NRND). The exact shop variant is ODv36-56V.
2. One open, zero-thickness 135 × 50 mm size-reference plane is centred at X = Y = 0 and Z = 0. X is the first size value and Y is the second size value.
3. The separately retained unrevisioned mechanical figure labels outer edges 140.50 × 50.00 mm and corner-hole pitch 135.50 mm. Those dimensions retain their source identity and supply no holes in this exact-v3.6 reference.
   The same figure places the corner-hole centres at X = 2.50 and 138.00 mm and Y = 4.00 and 47.50 mm from its lower-left corner. Its 135.50 mm centre pitch exceeds the 135 mm v3.6 footprint length by 0.50 mm. The artwork and the v3.6 outline therefore require separate references. Actual checking model unavailable. Source figure.
4. The exact v3.6 listing states its photos show older versions. Connector, heatsink and board-thickness geometry therefore retain their existing exact-variant source pause. The v3.5 STEP remains a separately identified source.

## Checks

1. Immediate source import save, DWG-context save, metadata/view checkpoints, final save and fresh reopen PASS. Zero dropped entities.
2. Reopened native Mesh vertices, faces and subdivision 0 match the prepared arrays exactly; millimetre header and source hashes PASS.
3. Native capture identity FAIL: a stale battery scene was returned. The failed image remains local. Four delivered views use actual reopened native Mesh records.
4. Owned document cleanup is recorded in the execution recipe after saved/reopened checks.

## Views

1. [XY](<odrive-v36-135x50-source-dimension-reference-XY.png>).
1. [XZ](<odrive-v36-135x50-source-dimension-reference-XZ.png>).
1. [YZ](<odrive-v36-135x50-source-dimension-reference-YZ.png>).
1. [isometric](<odrive-v36-135x50-source-dimension-reference-isometric.png>).
1. Native-record boundary views are delivered; failed viewport capture is retained locally.

## Sources — online

1. ODrive v3.6 manufacturer size reference source.

## References

1. Construction, source pins, native arrays, checkpoints, readback and cleanup recipe: ``.
2. Existing runtime: `PYTHONPATH=/tmp/3dmodeling-native-reader`; native helpers from the installed cad-ocs-engineering skill. Python numpy/ezdxf build the source-pinned DXF intermediate. Conversion changes are retained in `job.json`; source originals remain unchanged.
