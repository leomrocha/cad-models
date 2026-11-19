# Hiwonder Pico spring twelve source-face interior stage

1. **Library number:** 287.
2. **Plan component:** model 19, existing Hiwonder Pico tension spring; open source exterior recovery stage.
3. **Native drawing:** [Twelve source-face interior patches](<pico-tension-spring-source-twelve-face-interior-stage.dwg>).
4. **DWG SHA-256:** `9a5b45f392cde4e48a86dd097e5cca03a841731eb2c3a8a92afe2e9a4d59d986`.
5. **State:** SOURCE_TWELVE_FACE_INTERIORS_SAVED_CURRENT_GEOMETRY_CHECKED_PARTIAL.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Representation:** twelve open, zero-thickness native Mesh occurrences sample all twelve rational source-face interiors of manufacturer spring body 3182, closed shell 3593. They contain 149,126 vertices and 288,552 triangles. Cells intersecting trim boundaries remain omitted. Eleven newly recovered patches are separate Mesh entities; the existing library 277 definition supplies face 18547/support 1752 through an identity Insert.
2. **Source topology method:** each shared STEP VERTEX_POINT supplies one cached UV corner to its adjacent oriented edge curves. Original curve-interior samples are retained. This gives valid source UV polygons for faces 18544…18555 and supports 1749…1760. Complete parameter-grid cells contained inside each polygon generate the open patches. The method preserves the original oriented source trim topology.
3. **Source approximation:** the eleven new patches have maximum sampled rational-surface-to-facet deviation 0.0031901128444954178 mm. The reused library 277 patch retains its prior sampled deviation 0.027199143389474167 mm. The declared CAD sampling-check input is 0.03 mm; these sampled comparisons have their own scope. Maximum sampled curve-to-surface inverse residual is 0.001195302656587621 mm.
4. **Frame:** millimetres; identical to libraries 275 and 277. X = source Y − 67.45145966994615; Y = −source X − 54.680151364355; Z = source Z − 43.2323659374299. The inverse frame preserves the exact manufacturer assembly placement. Root scales are one; library 277 is inserted at identity.
5. **Native checks:** each new Mesh has exact prepared vertex coordinates, triangle indices/winding and subdivision level zero. The reused 277 Mesh has exact prior source arrays and identity composed placement. All twelve source face/surface identities, source-job hashes, source derivative, units and aggregate counts PASS against the current owned document. Original library 275 and 277 hashes remain unchanged.
6. **Persistence:** source import was saved immediately. Each source-face provenance step and recovered 277 insertion was checkpointed. Final original SAVE completion, intended path, file existence/size/hash, audit and zero dropped entities PASS. The current geometry revision remained unchanged through canonical SAVE. Verification uses the retained current document records.
7. **Appearance:** current-record XY, XZ and isometric Mesh-edge views inspected PASS. They display the repeated coil exterior and both source attachment loops. All 437,666 unique Mesh face edges are included with actual nested transforms. Finished owned document 782 guarded closed after checks.
8. **Preserved source stages:** library 275 contains the original imported source solid and its failed coil-display result. Library 277 contains its original single source-face partial patch. This stage adds the recovered source-face interiors under the same planned component identity.

## Source face patches

| Source face | Rational support | Vertices | Triangles | Sampled maximum facet deviation (mm) |
|---:|---:|---:|---:|---:|
| 18544 | 1749 | 289 | 478 | 0.0003940564611197595 |
| 18545 | 1750 | 3500 | 6730 | 0.003132336596421828 |
| 18546 | 1751 | 1228 | 2314 | 0.0003902576020893146 |
| 18547 | 1752 | 18343 | 34630 | 0.027199143389474167 |
| 18548 | 1753 | 1509 | 2856 | 0.0003988783417449984 |
| 18549 | 1754 | 3445 | 6632 | 0.003026553638696322 |
| 18550 | 1755 | 289 | 480 | 0.0003940564611058942 |
| 18551 | 1756 | 3412 | 6568 | 0.0027589262580739737 |
| 18552 | 1757 | 1231 | 2316 | 0.0003902576020838547 |
| 18553 | 1758 | 110819 | 215868 | 0.0031901128444954178 |
| 18554 | 1759 | 1511 | 2860 | 0.0003988783417324634 |
| 18555 | 1760 | 3550 | 6820 | 0.00315592760030726 |

## Sources — online

1. Manufacturer-linked chassis STEP, original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`. Selected source-closed derivative SHA-256 `4c3f3f99822ccfda56ce05f49f6cd0188497ca8c14328207438f27c233c9e630`.
2. Hiwonder suspended tracked chassis, source product and geometry context.

## References — library

1. [Original source-native spring](<pico-tension-spring-manufacturer-source.md>), library 275, preserved.
2. [Reused single-face coil patch](<pico-tension-spring-source-sampled-coil-patch.md>), library 277, identity placement.
3. [Current XY view](<../../images/pico-tension-spring-source-twelve-face-interior-stage-XY.png>).
4. [Current XZ view](<../../images/pico-tension-spring-source-twelve-face-interior-stage-XZ.png>).
5. [Current isometric view](<../../images/pico-tension-spring-source-twelve-face-interior-stage-isometric.png>).
