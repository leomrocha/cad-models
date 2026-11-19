# Hiwonder Pico manufacturer geared motor exterior

1. **Library number:** 270.
2. **Plan component:** model 13; manufacturer source geometry stage.
3. **Native model:** [Hiwonder Pico manufacturer geared motor exterior](<pico-gearmotor-manufacturer-source.dwg>).
4. **DWG SHA-256:** `57c35c58ad8e9e6358623fd9d209e0a5da75f30483ad80e9b8bbaaca4d2eb692`.
5. **Representation:** source-native solid geometry; 6 selected source solid definitions representing geared motor visible exterior group: motor can, two gearbox exterior pieces, rear cover, output shaft and exposed connector.
6. **Frame:** mm; local Z = output-shaft direction (−source X), X = source Y, Y = −source Z; origin at shaft axis on the boss-front plane Z = 0 mm; the broad gearbox front mounting plane is Z = −2.500 mm. Unit scale retained. Source-to-local matrix `[[0.0, 1.0, 0.0, 89.9496630935861], [0.0, 0.0, -1.0, 64.6359015567724], [-1.0, 0.0, 0.0, -42.2826890439483], [0.0, 0.0, 0.0, 1.0]]`; inverse manufacturer placement `[[-0.0, -0.0, -1.0, -42.2826890439483], [1.0, 0.0, 0.0, -89.9496630935861], [-0.0, -1.0, -0.0, 64.6359015567724], [0.0, 0.0, 0.0, 1.0]]`.
7. **State:** SOURCE_STAGE_SAVED_REOPENED_CHECKED.
8. **Actual execution model:** unavailable.

## Technical specification

1. **Source body 3135:** 41 faces; reachable vertex bounds X/Y/Z = `[[-36.9826890439484, 1.56731095605166], [-75.3996630935862, -42.4996630935862], [48.1859015567724, 81.0859015567724]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
1. **Source body 3137:** 194 faces; reachable vertex bounds X/Y/Z = `[[-42.2826890439483, -33.7826890439483], [-102.849663093586, -38.4496630935866], [45.6359015567749, 83.6359015567749]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
1. **Source body 3139:** 200 faces; reachable vertex bounds X/Y/Z = `[[-34.7826890439483, -25.0826890439483], [-102.849663093586, -38.4496630935866], [45.6359015567749, 83.6359015567749]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
1. **Source body 3141:** 229 faces; reachable vertex bounds X/Y/Z = `[[-5.03268904394837, 7.36731095605167], [-75.1046101326514, -43.8082438910233], [47.6359015567723, 81.6359015567725]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
1. **Source body 3142:** 17 faces; reachable vertex bounds X/Y/Z = `[[-55.3826890439483, -25.4826890439483], [-92.9896630935861, -86.9096630935861], [62.8359015567724, 66.4359015567724]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
1. **Source body 3149:** 31 faces; reachable vertex bounds X/Y/Z = `[[-2.03268904394837, 3.56731095605163], [-52.8456062135863, -45.3005242135862], [56.6839365531187, 72.6839045531187]]` mm. These bounds cover topological vertices; circular seam vertices retain their own analytic-extrema scope.
2. **Source/native comparison:** selected source bodies matched bijectively to reopened native instances by bidirectional topological vertex-set distance below 0.000001 mm, source/native face counts and reciprocal closed native topology. Analytic support and trim coverage retain their own checking scope.
3. **Persistence:** imported geometry checkpointed immediately, verified in DWG context, saved/reopened; file SHA-256 and zero dropped entities PASS.
4. **Views:** four native boundary projections retained; isometric inspected. Supported boundary curves are sampled and unsupported trim curves use endpoint points.
5. **Cleanup:** owned source-import, checkpoint and reopened documents closed; unrelated documents preserved.
6. **Independent source comparison:** Output shaft source cylindrical support radius 3 mm matches manufacturer eccentric 6 mm D shaft specification. Source motor can cylindrical radius 16.45 mm; output shaft axis is offset 31 mm from motor-can axis. Source geometry remains unscaled.


## Dimensioned source drawing

1. [Dimensioned geared-motor source drawing](<../../images/pico-gearmotor-manufacturer-source-dimensioned.png>): 4800 × 3200 PNG; XY, XZ, ZY and isometric native boundary projections of the six selected source CAD bodies. Supported edges are sampled; the 200 unsupported internal trim curves are shown only as isolated endpoint markers.
2. **Retained source-vertex spans:** local X/Y/Z = **64.400 × 38.000 × 62.750 mm**. These values measure the aggregate topological-vertex set under the retained rigid frame; they retain the boundary-curve scope stated above.
3. **Source shaft body 3142:** cylindrical support Ø6.000 mm; flat plane X = 2.400 mm, planar-face chord 3.600 mm, trimmed flat face Z = 1.100…13.100 mm. The original source tip bevel is retained.
4. **Source mounting body 3137:** broad front plane Z = −2.500 mm; boss front Z = 0.000 mm. Four outer mounting centres X = −5.700/44.300 mm and Y = ±13.250 mm give 50.000 × 26.500 mm pitches. Their circular mouths measure Ø5.200 mm at Z = −2.500 mm and Ø3.200 mm at Z = −8.500 mm. These are measured source sections. Boss-front outer/inner mouths are Ø12.000/6.100 mm.
5. **Shaft projection source comparison:** the retained supplier dimensioned image prints **13.10 mm from the broad case-front face to the shaft tip**. The manufacturer source CAD measures **15.600 mm from that broad face to the tip**, and **13.100 mm from the boss-front datum to the tip**. These source values use the stated distinct datums; the same-face CAD/raster difference is 2.500 mm. Retained image SHA-256: `27864539eaf03eed0e738773d2311c1265beb05b6878a7414a4ed89cb2d79a62`.
6. Drawing measurements use the retained numeric source frame and millimetres; three decimal places are displayed. Source DWG and geometry remain unchanged.

## References — library

1. [Isometric boundary view](<../../images/pico-gearmotor-manufacturer-source-local-isometric.png>).
2. [Top boundary view](<../../images/pico-gearmotor-manufacturer-source-local-XY.png>).

## Sources — online

1. Manufacturer-linked STEP file, unchanged original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, source Q&A links the model-drawing folder and component documentation.

The source-closed derivative preserves every selected geometry entity payload and original millimetre context; its solid list filters unrelated bodies. Derivative SHA-256: `d6ec54e1981e94ec181a8b52414fea05d54ce8a22f35484ee4758ca22be1ff10`. Source inventory, selected-body mapping, native records, source/native checks and persistence receipts are retained in the consuming project's ignored execution storage.
