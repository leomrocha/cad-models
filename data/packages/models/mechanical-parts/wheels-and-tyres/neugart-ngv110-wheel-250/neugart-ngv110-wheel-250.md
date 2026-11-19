# neugart ngv110 wheel 250

1. **Library number:** 109.
2. **Type:** part.
3. **CAD file:** [neugart-ngv110-wheel-250.dwg](<neugart-ngv110-wheel-250.dwg>).
4. **DWG SHA-256:** `6cdc301c65f4317826d80f7aef857a173eb46aa1a07de8150d73c18edbf9543b`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

### Model

- NGV110 wheel 250 DWG, OpenCADStudio 2026.42, DWG AC1032, millimetres.
- Executing model: GPT-6.1 Sol.
- Fifteen separate native solids: cast-iron body, Besthane tread, central closure cap and twelve socketed mounting screws.
- Axle: Z. Origin: wheel recess bottom and gearbox output mounting plane. Positive Z points towards the outer wheel face.
- Wheel axial span: Z = −66 to +14 mm.

### Manufacturer evidence

- Retained catalogue, product page and geometry tables, catalogue printed page 147, **NGV wheel 250** column and front view; cutaway printed page 142.
- Nominal outside diameter 250 mm; overall width 80 mm; rim recess Ø183 mm, depth 66 mm; centring outside diameter 40 mm.
- Twelve Ø6.6 mm through-bores and twelve Ø11 mm head recesses on a Ø63 mm pitch circle.
- Reconstructed full-view angular coordinates from the manufacturer's half-view and its reflection: 0°, 22.5°, 45°, 90°, 135°, 157.5°, 180°, 202.5°, 225°, 270°, 315°, 337.5°, measured from +X towards +Y.
- Manufacturer tolerances: outside diameter ±1.2 mm; width ±0.5 mm; recess depth ±0.2 mm; centring diameter h7; screw-bores H13.
- Calculated outer web span: 80 − 66 = 14 mm.

### Drawing-based reconstruction parameters

- Body outside radius 103.5 mm; tread running radius 125 mm; tread shoulder radius 3 mm.
- Centring-spigot projection 6 mm with 0.5 mm entry chamfer; central passage Ø30 mm; recess-bottom fillet 2.5 mm.
- Central cap: Ø30 × 3 mm plug, Ø31.5 × 1 mm flange; outer face Z = +14 mm.
- Head recess depth 7 mm, Z = +7 to +14 mm.
- Nominal cylindrical screw shank Ø6 mm, Z = −12 to +7 mm; head Ø10 × 6 mm; socket 5 mm across flats, depth 3 mm.
- Source front, side and cutaway views supply the reconstructed contour and hardware representation. The parameters above describe authored geometry rather than manufacturer dimensional specifications.
- Source and reconstruction metadata are stored per solid under `NEUGART_NGV110_WHEEL` XData.

### Checks and display

- Native feature checks: fifteen checks pass before saving, using native SAT surfaces and edges.
- Checks cover tread diameter and width, shoulder radii, both hole counts and diameters, pitch-circle diameter, individual angular coordinates, recess and spigot diameters, recess depth datums, solid count and audit.
- Save and reopened audits: fifteen native 3D solids; zero errors, zero warnings and zero dropped entities. All fifteen reopened solids report positive mesh volumes.
- OCS native state identifies the open NGV110 wheel drawing, with a named `NGV110_Isometric` view.
- The capture recorded for the NGV064 drawing contains the SKF viewport. It supplies no visual evidence for this wheel.

## Sources — online

1. neugart ngv wheel geometry.
2. neugart ngv wheel geometry.
