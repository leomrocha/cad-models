# Pico source chassis with twelve-face spring and central battery-case stage

1. **Plan identity:** existing assembly 7, Pico Sowbot; partial source-backed hardware stage.
2. **Native drawing:** [Pico source stage](<pico-hardware-source-twelve-face-spring-battery-layout-proposal.dwg>).
3. **State:** PARTIAL_SAVED_CURRENT_SOURCE_GEOMETRY_AND_PLACEMENTS_CHECKED.
4. **DWG SHA-256:** `3cc572d59df62c38acca764f2c2bef71df0ad7a76a10d1d2792f6fb9100a666e`.
5. **Actual execution model:** unavailable.

## Technical specification

1. **Frame:** mm; X travel = source Y, Y transverse = −source X, Z up; common origin at combined track XY vertex-bounds centre and lowest lower-run source vertex plane.
2. **Chassis:** the source stage retains its 42 planned physical unit occurrences, 192 source solid occurrences and two supplemental groups of twelve open source-face interior Mesh patches. The original 275 NURBS geometry and its native coil display failure remain attributed beside the 287 display representation. Boundary-crossing cells are omitted from the supplemental meshes. Source plate 3037 retains its scope finding in the chassis companion.
3. **Central case:** library 284 retains exact manufacturer source solid 3036, measured 76.8 × 66.8 × 24 mm. The role is manufacturer source central battery-case geometry, interpreted from the exploded illustration. Library 248 retains the separate supplier 86 × 60 × 21 mm reference.

## Installed occurrences

| Component | Quantity | Source DWG SHA-256 | Root matrix, row-major |
|---|---:|---|---|
| Manufacturer source Pico chassis partial stage | 1 | `c55bb14553f847cec0bd9c480902931c42b77e7cae04c300101dd0fcd1c3cb61` | `1.0, 0.0, 0.0, 0.0; 0.0, 1.0, 0.0, 0.0; 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 1.0` |
| Hiwonder manufacturer central battery-case geometry — exploded-view interpretation | 1 | `306b0bea34286d402fdd2add377ef0c95253f852d83397929358ac04606ac66d` | `0.0, 1.0, 0.0, 19.287944944981604; -1.0, 0.0, 0.0, 0.07808514033535374; 0.0, 0.0, 1.0, 33.84267639045569; 0.0, 0.0, 0.0, 1.0` |

The chassis member above uses Git object `7d903f045ff594681c09ff26116361ede089d6ea:models/sowbot/assemblies/detailed/pico-chassis-source-twelve-face-spring-partial-stage.dwg`. This is the chassis revision embedded in the held layout.

## Checks

1. Two roots contain {'Solid3D': 193, 'Mesh': 24}, 217 geometry occurrences. Complete noncommon source fingerprints, source DWG hashes and all composed nested matrices PASS.
2. Empty document and each meaningful construction step were saved separately. Current owned geometry and millimetre units were checked before final SAVE. Original SAVE completion, correct path, file existence/size/SHA-256, save audit and zero dropped data PASS. Verification uses retained current records.
3. Current-record XY and isometric views inspected PASS. Every unique Mesh face edge and source Solid3D boundary uses its actual composed placement. Unsupported trim curves retain endpoint display scope.
4. Finished owned document 784 guarded closed; unrelated Start 1 preserved.

5. **Central case lift:** With XY fixed and the upper plate installed, the manufacturer source case meets the upper plate by **59.547216 mm** of vertical travel. The source check confirms material on both faces at chassis XY (30, 24) mm. [Upper plate access calculation](<../../../../docs/sowbot/pico-battery-case-upper-plate-access.md>).

## Sources — online

1. Manufacturer-linked chassis STEP, original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder tracked chassis and product-structure illustration.

## Views

1. [XY current-record view](<../../../../images/sowbot/pico-hardware-source-twelve-face-spring-battery-layout-proposal-XY.png>).
2. [XZ current-record view](<../../../../images/sowbot/pico-hardware-source-twelve-face-spring-battery-layout-proposal-XZ.png>).
3. [YZ current-record view](<../../../../images/sowbot/pico-hardware-source-twelve-face-spring-battery-layout-proposal-YZ.png>).
4. [isometric current-record view](<../../../../images/sowbot/pico-hardware-source-twelve-face-spring-battery-layout-proposal-isometric.png>).

## References

1. Manufacturer source Pico chassis partial stage companion.
2. [Hiwonder manufacturer central battery-case geometry — exploded-view interpretation companion](<../../../../library/parts/electrical/hiwonder-manufacturer-central-battery-case-source-stage.md>).
3. Current source/SAVE/geometry/cleanup recipe.
4. [Preserved earlier Pico source stage](<pico-hardware-source-backed-battery-layout-proposal.md>).
