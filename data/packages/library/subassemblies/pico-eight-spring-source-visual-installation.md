# Pico eight-spring source visual installation

1. **Library number** 303.
2. **Plan use** Assembly 2, step 6.
3. **Native drawing** [Eight spring visual placements](<pico-eight-spring-source-visual-installation.dwg>).
4. **DWG SHA-256:** `c3acd10cb1e40dd9addfea17d45b076c38d582b6c1478454c516679089773455`. DWG 2018, 7,797,915 bytes.
5. **State** SAVED_SOURCE_VISUALS_AND_PLACEMENTS_CHECKED.
6. **Execution models** gpt-6.2-sol for independent array and placement checks. The model that built the native group is unavailable.

## Technical specification

Eight Pico tension spring visuals use their manufacturer placements in the library 299 chassis frame, in millimetres. A visual mesh definition stores the sampled exterior surfaces. Four left spring positions share the 12-mesh definition from library 292. Four right positions share a second 12-mesh definition from manufacturer STEP body 3316. The body 3316 definition uses 60,750 triangles with maximum sampled surface deviation 0.023128 mm.

1. **Left source positions** 3182, 3238, 3235 and 3236.
2. **Right source positions** 3316, 3369, 3370 and 3372.
3. **Native geometry** 24 stored meshes, 96 placed mesh occurrences and 1,489,584 placed triangles.

## Verification

1. All eight placement matrices match their checked source placements. The native mesh coordinates, triangle indices and winding, and source metadata match the two saved source definitions.
2. The completed SAVE passed path, byte size, SHA-256 and native audit checks. The audit reported zero dropped entities. The two owned construction tabs passed guarded closure.
3. The isometric view was generated from the checked current native meshes and inspected.

## References

1. [Left spring mesh definition, library 292](<../parts/mechanical/pico-tension-spring-source-trimmed-exterior-stage.md>).
2. [Initial two-position spring group, library 299](<pico-two-spring-trimmed-source-installation.md>).
3. [Isometric view of all eight positions](<../images/pico-eight-spring-source-visual-installation-isometric.png>).

## Sources — online

1. Manufacturer-linked Pico chassis STEP. Source SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
