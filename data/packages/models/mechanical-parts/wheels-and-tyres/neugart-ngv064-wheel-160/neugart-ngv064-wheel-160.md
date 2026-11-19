# neugart ngv064 wheel 160

1. **Library number:** 107.
2. **Type:** part.
3. **CAD file:** [neugart-ngv064-wheel-160.dwg](<neugart-ngv064-wheel-160.dwg>).
4. **DWG SHA-256:** `66e553c80c697ec1574918234bffaefc759ab54314b576fe90df42e8036f50b9`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

### Model and frame

- File: NGV064 wheel 160.
- Application: OpenCADStudio 2026.42. Executing model: GPT-6.1 Sol.
- Format: DWG AC1032, eleven native 3D solids, millimetres.
- Solids: cast-iron wheel body, Besthane tread, central closure cap and eight socketed mounting screws.
- Axis: Z. Origin: wheel-to-gearbox mounting plane at the bottom of the rim recess. Positive Z points towards the outer wheel face.
- Wheel axial span: Z = −36 to +14 mm. The centring spigot projects into the recess, from Z = −3 to 0 mm.
- Each solid contains published and reconstructed dimensions in `NEUGART_NGV064_WHEEL` XData.

### Sources

- Manufacturer originals, retrieval record and dimension tables.
- Catalogue wheel drawing, printed page 147.
- Catalogue assembly cutaway, printed page 142.

### Published nominal geometry represented

- Wheel outside diameter: 160 mm. Overall axial width: 50 mm.
- Rim recess: Ø114 mm, depth 36 mm.
- Centring spigot: Ø20 mm.
- Mounting pattern: eight Ø5.5 mm through-bores at 45° intervals on a Ø31.5 mm pitch circle.
- Screw-head recesses: eight Ø10 mm bores on the same pitch circle.
- The 14 mm outer-face distance from the recess bottom is calculated from 50 − 36 mm.

### Drawing-based reconstruction parameters

- Cast-body outside radius: 63 mm. Tread radius: 80 mm, with 2 mm quarter-circle shoulder fillets.
- The material boundary follows the source front view and cutaway. The running section is cylindrical; the shoulder fillets use native circular profile arcs.
- Centring-spigot projection: 3 mm; entry chamfer: 0.5 mm.
- Rim-recess bottom fillet: 1.5 mm.
- Central closure-cap passage: Ø16 mm; flange seat: Ø17.5 mm, depth 1 mm.
- Closure cap: Ø16 mm plug of length 3 mm, with Ø17.5 × 1 mm flange; outer face Z = +14 mm.
- Screw-head recess depth: 6 mm, from Z = +8 to +14 mm.
- Screw representation: Ø5 × 15 mm nominal cylindrical shank, Ø8.5 × 5 mm head, 4 mm across-flats hexagonal socket of depth 2.5 mm. Shank Z = −7 to +8 mm; head Z = +8 to +13 mm.
- These reconstructed dimensions describe the authored geometry. Manufacturer tolerance designations apply to the published features in the source table.

### Native geometry checks

- Machine-readable native checks, OCS document 51, revision 137, geometry revision 5508.
- Fourteen feature and audit checks pass before saving. The checks read native SAT surface records from OCS entities.
- Readback confirms the 80 mm running radius, axial planes −36 and +14 mm, both 2 mm shoulder fillets, eight through-bores and eight head recesses on a 31.5 mm pitch circle, 45° hole spacing, 57 mm recess radius and 10 mm centring radius.
- Save and reopened drawing audits: eleven 3D solids, zero errors, zero warnings and zero dropped entities.
- All eleven reopened solids report positive mesh volumes.
- The nine existing component DWGs retain their SHA-256 hashes.

### OCS measurement and display observations

- Before saving, the bounds API reports the tread's inner radius, 63 mm, as its outer bound. A bounds-equality check against the 80 mm outer radius fails. Native cylinder and torus records contain the 80 mm outer radius.
- Reopened DWG solids expose binary SAB data and zero reported bounds. The SAT-only feature reader returns no cylinders for that binary representation. The fourteen detailed feature checks refer to the pre-save native SAT records.
- Native OCS state identifies the open drawing as the NGV064 wheel DWG. Its named `NGV064_Isometric` view includes a display margin for the full 160 mm diameter.
- The captured viewport retains the SKF assembly while native state identifies the wheel document. The capture does not supply a wheel-view comparison.

## Sources — online

1. neugart ngv wheel geometry.
2. neugart ngv wheel geometry.
