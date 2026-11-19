# Pico left suspension arm and lower roller source group

1. **Library number:** 294.
2. **Plan use:** Assembly 2 step 5, models 18 and 16; reusable left suspension pair.
3. **Native drawing:** [Suspension arm and roller group](<pico-left-suspension-arm-roller-source-group.dwg>).
4. **DWG SHA-256:** `6e6aa4273cb8048fd62662061f1525eb44685028acf7219bb83a51421882eaa0`; 45,702 bytes.
5. **State:** SAVED_CURRENT_SOURCE_GEOMETRY_CHECKED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Geometry:** two root occurrences and two Solid3D leaves. One suspension arm reuses library 274, source body 3186. One lower roller reuses library 273, source body 3180.
2. **Frame:** millimetres; library 274 arm frame. Local Z follows the source X pivot axis; local X follows source Y; local Y follows source Z. Origin is the carrier pivot axis at the arm sheet midplane. Arm placement is identity.
3. **Roller placement:** identity rotation and translation `[-10.609715538729404, -10.609715538681996, -8.999999999878654]` mm in the arm frame. This is inverse arm installation pose multiplied by roller installation pose from the checked manufacturer-source chassis. Four left source pairs retain this relative pose within 0.000000001 mm numerical comparison tolerance.
4. **Checks:** exact non-common Solid3D property fingerprints and nested occurrence matrices match both retained source records. Two roots and two solid occurrences PASS. Original completed SAVE, path, byte size, SHA-256, audit and zero dropped entities PASS. Persistence uses SAVE only. Owned construction document 3 closed with guards; Start document 1 preserved.
5. **Views:** XY, XZ, YZ and isometric current-record boundary projections inspected. Supported curves use sampled boundaries; unsupported trim curves use endpoint markers.

## References — local geometry

1. [Suspension arm](<../parts/mechanical/pico-suspension-arm-manufacturer-source.md>), library 274, quantity one; DWG SHA-256 `b8a567745e7b3a466bc91307b994bd0681ca4c24baa7d6374d70a3a6a6159a23`.
2. [Lower load roller](<../parts/mechanical/pico-lower-roller-manufacturer-source.md>), library 273, quantity one; DWG SHA-256 `8df447938dfbf5e1877cb22d6a613b97cf8c011da6c89a7f12143168ba4c07a7`.
3. [XY view](<../images/pico-left-suspension-arm-roller-source-group-XY.png>).
4. [XZ view](<../images/pico-left-suspension-arm-roller-source-group-XZ.png>).
5. [YZ view](<../images/pico-left-suspension-arm-roller-source-group-YZ.png>).
6. [Isometric view](<../images/pico-left-suspension-arm-roller-source-group-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP, retained source arm 3186 and roller 3180 with recorded installation occurrences.
