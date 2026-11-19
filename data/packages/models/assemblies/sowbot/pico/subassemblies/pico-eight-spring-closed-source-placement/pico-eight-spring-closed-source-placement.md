# Pico eight-spring exterior subassembly

1. **Library number** 309.
2. **Plan use** Assembly 2, step 6. Eight source spring exteriors in the checked Pico chassis frame.
3. **Native drawing** [Eight-spring exterior subassembly](<pico-eight-spring-closed-source-placement.dwg>).
4. **DWG SHA-256:** `bf2efdc77afedd13cc5a36030fff6a11d587e4702f2a3d1e792ac4c59da4229d`. DWG 2018, 7,842,046 bytes.
5. **Execution models** Construction and source-checking identities unavailable.

## Technical specification

1. **Left side:** Four occurrences share the twelve-face source body 3182 exterior from library 308. Their source body IDs are 3182, 3238, 3235 and 3236.
2. **Right side:** Four occurrences share the twelve-face source body 3316 exterior from library 303. Their source body IDs are 3316, 3369, 3370 and 3372.
3. **Frame and placements:** X forward, Y left, Z up, ground at Z = 0. Units are millimetres. All eight poses match the checked chassis. Each occurrence carries the installed source body ID and its chassis root handle.
4. **Geometry:** Two mesh definitions contain 24 native face meshes and 369,824 stored triangles. Eight block references expand to 96 face meshes and **1,479,296 placed triangles**. The left surface-sampling and winding checks are recorded in the library 308 companion.

## Verification

1. Each spring's native placement matrix passed against its checked chassis pose. Across the eight springs, the largest distance from an original STEP topological vertex to the nearest placed mesh vertex is **2.11 × 10⁻¹⁰ mm**. This is the checked vertex-location residual.
2. The 24 native mesh records match their checked coordinate arrays, triangle indices and subdivision level. The completed SAVE passed filename, size, SHA-256 and audit checks, with zero dropped entities.
3. The [XY and isometric view from native records](<pico-eight-spring-closed-source-placement.png>) was inspected. Owned document 29 passed guarded closure.
4. The twelve right spring mesh records join at identical vertices to form one outward shell with 60,750 triangles, zero open edges and zero nonmanifold edges. Its sampled geometric volume is 423.062 mm³. The closed manufacturer STEP body has a calculated geometric volume of 429.815 mm³. The sampled volume is 1.571% lower. All eight placement rotations are orthonormal and have determinant +1.

## References

1. [Left spring exterior, library 308](<../../parts/pico-left-spring-closed-source-exterior/pico-left-spring-closed-source-exterior.md>).
2. Right spring definition and earlier eight placements, library 303 (earlier revision `model-303`; [current catalogue revision](<pico-eight-spring-closed-source-placement.md>)).

## Sources — online

1. Hiwonder Pico chassis STEP, original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, exterior and tension-spring installation images.
