# Pico source chassis with twelve-face spring interior supplements

1. **State:** HISTORICAL_PARTIAL_SOURCE_GEOMETRY_AND_PLACEMENTS_CHECKED.
3. **Historical DWG SHA-256:** `c55bb14553f847cec0bd9c480902931c42b77e7cae04c300101dd0fcd1c3cb61`.
4. **Plan identity:** existing Pico chassis assembly; 42 planned whole-unit occurrences, represented by 26 top-level roots, 192 solid occurrences and 24 supplemental open source-face Mesh occurrences in two spring groups.
5. **Actual execution model:** unavailable.

6. **Working-tree drawing:** [Pico chassis source stage](<pico-chassis-source-twelve-face-spring-partial-stage.dwg>), SHA-256 `18d63b2d59b4120ebbf2dea76c142d51287ffc188f0977162bc37ebd804905cc`. The [current Pico mechanical chassis](<../../layouts/pico-chassis/pico-chassis.md>) is the active plan model.

## Technical specification

1. **Frame:** millimetres; X = source Y − 14.125075966614006; Y = −source X + 9.027625898348703; Z = source Z − 5.83963289197771. X follows travel, Y is transverse and Z is up. The lower-run source-vertex plane is Z = 0.
2. **Placement:** one common source-to-assembly transform composes with each saved component local-to-source transform and each independently checked source occurrence. The source-direct group retains its exact manufacturer coordinates under the common transform.
3. **Measured aggregate topological-vertex span:** 279.939117 × 193.430113 × 119.389892 mm. Native/source bound difference is 1.4211e−14 mm. These values round to the retained drawing labels 279.94 × 193.43 × 119.39 mm. Curved support extrema have separate sample scope. Manufacturer PDF claims 273 × 193 × 94 mm for the single-layer chassis and 270 × 143 mm for the elevated plate. Source dimensions are retained without rescaling.
4. **Partial scope:** distinct reflected formed source plate 3037 remains in the original source. The existing planned source members are represented in this stage. Library 275 retains its full imported source spring with native coil display FAIL; library 287 supplies two separately labelled groups, each containing all twelve source-face interior patches at checked source poses 3182/3238.
5. **Source-direct group:** 94 exact-source solids represent 19 additional occurrences of the existing planned track, motor, sprocket, guide wheel, roller, arm and spring identities. Reparameterized opposite-side surfaces retain their own source geometry; the stage makes no unproved mirrored-reuse claim.

## Installed native roots

| Root | Library number / readable component | Quantity | Source DWG SHA-256 | Root matrix, row-major |
| --- | --- | --- | --- | --- |
| 0 | 265 — Hiwonder Pico manufacturer upper expansion plate | 1 | `0ff45ae07b45fe084dfadb6aea9d2ff4e0f069cc5a4c2714808833393d0724ee` | `1, 0, 0, -10.1600499383; 0, 1, 0, 0.0698212216813; 0, 0, 1, 117.38989202; 0, 0, 0, 1` |
| 1 | 266 — Hiwonder Pico manufacturer lower formed plate | 1 | `ec03b07b05d9108416acfb45da3d34a92fc8f4598275db3df010a42f1df4f203` | `1, 0, 0, -16.2770011371; 0, 1, 0, 0.0707915030146; 0, 0, 1, 31.7455749674; 0, 0, 0, 1` |
| 2 | 267 — Hiwonder Pico manufacturer left side carrier | 1 | `8d91f98c371a0b70af86fc883d86125e61664d64ee09e7693900e392bef0cbc8` | `1, 0, 0, -104.07473906; 0, 1, 0, 59.9465334033; 0, 0, 1, 58.7962686648; 0, 0, 0, 1` |
| 3 | 268 — Hiwonder Pico manufacturer right side carrier | 1 | `b55047906c7c29f992ffd9669131222345b098e29ca09ddd7d920d2bbc8db044` | `1, 0, 0, -104.07473906; 0, 1, 0, -59.9200985566; 0, 0, 1, 58.7962686648; 0, 0, 0, 1` |
| 4 | 269 — Hiwonder Pico manufacturer whole left track loop | 1 | `2b306f31d783490a4dc99245b5714674dd793de51e4a16b5c4ff6f389ce6f2a4` | `1, 0, 0, 0; 0, 1, 0, 76.2150565272; 0, 0, 1, 0; 0, 0, 0, 1` |
| 5 | 270 — Hiwonder Pico manufacturer geared motor exterior | 1 | `57c35c58ad8e9e6358623fd9d209e0a5da75f30483ad80e9b8bbaaca4d2eb692` | `1, 0, 0, -104.07473906; 0, 0, 1, 51.3103149423; 0, -1, 0, 58.7962686648; 0, 0, 0, 1` |
| 6 | 271 — Hiwonder Pico manufacturer drive sprocket assembly | 1 | `fdd5bd5a71ca2c9aded8dce9e0d13d1039962df10344ba949d4d4035b838c9ba` | `1, 0, 0, -104.07473906; 0, 0, -1, 77.4103149423; 0, 1, 0, 58.7962686648; 0, 0, 0, 1` |
| 7 | 272 — Hiwonder Pico manufacturer guide end wheel | 1 | `ae4adbc3f49fc3901378be6fc989b332d508223e1e5f76a290b21563389c1a99` | `1, 0, 0, 108.160124396; 0, 0, -1, 76.4465334033; 0, 1, 0, 42.8520136367; 0, 0, 0, 1` |
| 8 | 273 — Hiwonder Pico manufacturer lower load roller — source body 3170 | 1 | `8df447938dfbf5e1877cb22d6a613b97cf8c011da6c89a7f12143168ba4c07a7` | `1, 0, 0, 71.9239668007; 0, 0, -1, 76.0185077098; 0, 1, 0, 70.3126495028; 0, 0, 0, 1` |
| 9 | 273 — Hiwonder Pico manufacturer lower load roller — source body 3180 | 1 | `8df447938dfbf5e1877cb22d6a613b97cf8c011da6c89a7f12143168ba4c07a7` | `1, 0, 0, 51.5713821559; 0, 0, -1, 76.126533403; 0, 1, 0, 18.9453037276; 0, 0, 0, 1` |
| 10 | 273 — Hiwonder Pico manufacturer lower load roller — source body 3205 | 1 | `8df447938dfbf5e1877cb22d6a613b97cf8c011da6c89a7f12143168ba4c07a7` | `1, 0, 0, 11.5734144864; 0, 0, -1, 76.126533403; 0, 1, 0, 18.9453037276; 0, 0, 0, 1` |
| 11 | 273 — Hiwonder Pico manufacturer lower load roller — source body 3219 | 1 | `8df447938dfbf5e1877cb22d6a613b97cf8c011da6c89a7f12143168ba4c07a7` | `1, 0, 0, -28.4265855136; 0, 0, -1, 76.126533403; 0, 1, 0, 18.9453037276; 0, 0, 0, 1` |
| 12 | 273 — Hiwonder Pico manufacturer lower load roller — source body 3233 | 1 | `8df447938dfbf5e1877cb22d6a613b97cf8c011da6c89a7f12143168ba4c07a7` | `1, 0, 0, -68.4265855136; 0, 0, -1, 76.126533403; 0, 1, 0, 18.9453037276; 0, 0, 0, 1` |
| 13 | 274 — Hiwonder Pico manufacturer suspension arm — source body 3186 | 1 | `b8a567745e7b3a466bc91307b994bd0681ca4c24baa7d6374d70a3a6a6159a23` | `1, 0, 0, 62.1810976946; 0, 0, -1, 67.1265334031; 0, 1, 0, 29.5550192663; 0, 0, 0, 1` |
| 14 | 274 — Hiwonder Pico manufacturer suspension arm — source body 3206 | 1 | `b8a567745e7b3a466bc91307b994bd0681ca4c24baa7d6374d70a3a6a6159a23` | `1, 0, 0, 22.1831300251; 0, 0, -1, 67.1265334031; 0, 1, 0, 29.5550192663; 0, 0, 0, 1` |
| 15 | 274 — Hiwonder Pico manufacturer suspension arm — source body 3220 | 1 | `b8a567745e7b3a466bc91307b994bd0681ca4c24baa7d6374d70a3a6a6159a23` | `1, 0, 0, -17.8168699749; 0, 0, -1, 67.1265334031; 0, 1, 0, 29.5550192663; 0, 0, 0, 1` |
| 16 | 274 — Hiwonder Pico manufacturer suspension arm — source body 3237 | 1 | `b8a567745e7b3a466bc91307b994bd0681ca4c24baa7d6374d70a3a6a6159a23` | `1, 0, 0, -57.8168699749; 0, 0, -1, 67.1265334031; 0, 1, 0, 29.5550192663; 0, 0, 0, 1` |
| 17 | 275 — Hiwonder Pico manufacturer tension spring exterior — source body 3182 | 1 | `340a38bdc1ff933e5d799803a8856cebbed786beb941b7bf67bacace5b29d949` | `1, 0, 0, 53.3263837033; 0, 1, 0, 63.7077772627; 0, 0, 1, 37.3927330455; 0, 0, 0, 1` |
| 18 | 275 — Hiwonder Pico manufacturer tension spring exterior — source body 3238 | 1 | `340a38bdc1ff933e5d799803a8856cebbed786beb941b7bf67bacace5b29d949` | `1, 0, 0, -66.6715839662; 0, 1, 0, 63.8877772627; 0, 0, 1, 37.3927330455; 0, 0, 0, 1` |
| 19 | 276 — Hiwonder Pico manufacturer plate support spacer — source body 3032 | 1 | `801ab8dc8b90cacce5fed870c9bac05f3e06478ddf5f6ac13805567f3984aba3` | `1, 0, 0, -103.504212853; 0, 1, 0, -34.110365798; 0, 0, 1, 92.2657995841; 0, 0, 0, 1` |
| 20 | 276 — Hiwonder Pico manufacturer plate support spacer — source body 3033 | 1 | `801ab8dc8b90cacce5fed870c9bac05f3e06478ddf5f6ac13805567f3984aba3` | `1, 0, 0, 83.3093576953; 0, 1, 0, 31.4216827905; 0, 0, 1, 92.2657995841; 0, 0, 0, 1` |
| 21 | 276 — Hiwonder Pico manufacturer plate support spacer — source body 3034 | 1 | `801ab8dc8b90cacce5fed870c9bac05f3e06478ddf5f6ac13805567f3984aba3` | `1, 0, 0, 83.3093576953; 0, 1, 0, -31.3257307837; 0, 0, 1, 92.2657995841; 0, 0, 0, 1` |
| 22 | 276 — Hiwonder Pico manufacturer plate support spacer — source body 3035 | 1 | `801ab8dc8b90cacce5fed870c9bac05f3e06478ddf5f6ac13805567f3984aba3` | `1, 0, 0, -103.504212853; 0, 1, 0, 34.2063178049; 0, 0, 1, 92.2657995841; 0, 0, 0, 1` |
| 23 | 269–275 planned unit identities; source-direct occurrence geometry — Manufacturer source-direct remaining planned component occurrences | 19 whole units | `8904798b2bed983ab1298d9fb9a2fb95eeb18c8da1821c0dd70a5c4f3db24c92` | `0, 1, 0, -14.1250759666; -1, 0, 0, 9.02762589835; 0, 0, 1, -5.83963289198; 0, 0, 0, 1` |
| 24 | 287 — Supplemental twelve source-face interior patches — source spring 3182 | 1 | `9a5b45f392cde4e48a86dd097e5cca03a841731eb2c3a8a92afe2e9a4d59d986` | `1, 0, 0, 53.3263837033; 0, 1, 0, 63.7077772627; 0, 0, 1, 37.3927330455; 0, 0, 0, 1` |
| 25 | 287 — Supplemental twelve source-face interior patches — source spring 3238 | 1 | `9a5b45f392cde4e48a86dd097e5cca03a841731eb2c3a8a92afe2e9a4d59d986` | `1, 0, 0, -66.6715839662; 0, 1, 0, 63.8877772627; 0, 0, 1, 37.3927330455; 0, 0, 0, 1` |

## Source-direct physical unit grouping

| Existing plan job | Readable component | Source body IDs | Quantity |
| --- | --- | --- | --- |
| 12 | right whole track loop | 3377, 3378, 3379, 3380, 3381, 3382, 3383, 3384, 3385, 3386, 3387, 3388, 3389, 3390, 3391, 3392, 3393, 3394, 3395, 3396, 3397, 3398, 3399, 3400, 3401, 3402, 3403, 3404, 3405, 3406, 3407, 3408, 3409, 3410, 3411, 3412, 3413, 3414, 3415, 3416, 3417, 3418, 3419, 3420, 3421, 3422, 3423, 3424, 3425, 3426, 3427, 3428, 3429, 3430, 3431, 3432, 3433, 3434, 3435 | 1 |
| 13 | right geared motor exterior | 3269, 3271, 3273, 3275, 3276, 3283 | 1 |
| 14 | right drive sprocket whole unit | 3244, 3245, 3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255, 3256 | 1 |
| 15 | right guide end wheel | 3310 | 1 |
| 17 | right upper return roller | 3304 | 1 |
| 16 | right lower load rollers | 3314, 3339, 3353, 3367 | 4 |
| 18 | right suspension arms | 3320, 3340, 3354, 3371 | 4 |
| 19 | right spring exteriors | 3316, 3369, 3370, 3372 | 4 |
| 19 | two remaining left spring exteriors | 3235, 3236 | 2 |

## Checks

1. All 26 roots and 216 nested geometry occurrences match exact source-property fingerprints and composed matrices: {'Solid3D': 192, 'Mesh': 24}. Source hashes and millimetre units PASS. The 42 physical units retain the previous source grouping.
2. Original SAVE completion, exact path, file existence/size/SHA-256, zero dropped data and save audit PASS. Current owned records were captured before final SAVE. Verification uses retained current records.
3. Library 287 contributes twelve open source-face interiors at each unchanged source spring pose. Boundary-crossing cells are omitted. The original 275 NURBS solids and all other source definitions and poses remain represented.
4. Actual current-record views include all unique Mesh face edges and native Solid3D boundaries. Unsupported trims retain their endpoint display scope. XY and isometric inspection PASS.
5. Owned document 783 guarded closed after persistence, geometry and view checks. Start 1 preserved.

## Views

1. XY current-record view.
2. XZ current-record view.
3. YZ current-record view.
4. isometric current-record view.

## Sources — online

1. [Manufacturer-linked chassis STEP](https://drive.google.com/file/d/118zHyaMR6LU_DeXndFg6-FFH070BZfYu/view), SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis.

## References

3. Earlier plate/spacer hypothesis assembly: [preserved partial stage](<../pico-expansion-plate-spacer-partial-stage/pico-expansion-plate-spacer-partial-stage.md>).

4. Source twelve-face spring stage (earlier revision `model-287`; [current catalogue revision](<../../parts/pico-tension-spring-source-trimmed-exterior-stage/pico-tension-spring-source-trimmed-exterior-stage.md>)).
5. Preserved previous source chassis (earlier revision `assembly-pico-chassis-manufacturer-source-partial-stage`; [current catalogue revision](<../../layouts/pico-chassis/pico-chassis.md>)).
