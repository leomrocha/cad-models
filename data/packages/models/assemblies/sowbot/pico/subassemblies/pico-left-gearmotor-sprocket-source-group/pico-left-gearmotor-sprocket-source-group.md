# Pico left gearmotor and sprocket source group

1. **Library number:** 293.
2. **Plan use:** Assembly 2, steps 3–4; reusable left geared motor and drive sprocket group.
3. **Native drawing:** [Pico left gearmotor and sprocket source group](<pico-left-gearmotor-sprocket-source-group.dwg>).
4. **DWG SHA-256:** `42017d3ac39f719c5a6a94662285c0d7e0b36d0dd903a4e1b1af35256de40017`; 2,153,728 bytes.
5. **State:** SAVED_CURRENT_SOURCE_GEOMETRY_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Geometry:** two root occurrences; 19 Solid3D leaves. One geared motor reuses library 270 with six source solids; one drive sprocket reuses library 271 with thirteen source solids.
2. **Frame:** millimetres; library 270 output-shaft frame, +Z toward the shaft output and Z = 0 at the boss front. Motor placement is identity. Sprocket placement rotates 180° about local X and translates +26.1 mm along local Z.
3. **Source placement:** inverse motor installation matrix multiplied by the sprocket installation matrix from the checked manufacturer-source chassis job. Relative matrix rows are `[1,0,0,0]`, `[0,-1,0,0]`, `[0,0,-1,26.1]`, `[0,0,0,1]`.
4. **Checks:** exact non-common Solid3D property fingerprints and all nested occurrence matrices match the retained source records. Two roots and nineteen solid occurrences PASS. Completed SAVE, intended path, byte size, SHA-256, audit and zero dropped entities PASS. Persistence verification uses SAVE only. Guarded closure of owned document 2 PASS; Start document 1 preserved.
5. **Views:** current-document native boundary samples and trim endpoints, retaining all nineteen placed solids. XY, XZ, YZ and isometric pixels inspected.

## References — local geometry

1. [Pico manufacturer geared motor exterior](<../../parts/pico-gearmotor-manufacturer-source/pico-gearmotor-manufacturer-source.md>), library 270, quantity one; source DWG SHA-256 `57c35c58ad8e9e6358623fd9d209e0a5da75f30483ad80e9b8bbaaca4d2eb692`.
2. [Pico manufacturer drive sprocket assembly](<../../parts/pico-drive-sprocket-manufacturer-source/pico-drive-sprocket-manufacturer-source.md>), library 271, quantity one; source DWG SHA-256 `fdd5bd5a71ca2c9aded8dce9e0d13d1039962df10344ba949d4d4035b838c9ba`.
3. [XY view](<pico-left-gearmotor-sprocket-source-group-XY.png>).
4. [XZ view](<pico-left-gearmotor-sprocket-source-group-XZ.png>).
5. [YZ view](<pico-left-gearmotor-sprocket-source-group-YZ.png>).
6. [Isometric view](<pico-left-gearmotor-sprocket-source-group-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP, motor bodies 3135, 3137, 3139, 3141, 3142 and 3149; drive sprocket bodies 3110–3122.
