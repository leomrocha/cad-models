# neugart ngv090 wheel 200

1. **Library number:** 108.
2. **Type:** part.
3. **CAD file:** [neugart-ngv090-wheel-200.dwg](<neugart-ngv090-wheel-200.dwg>).
4. **DWG SHA-256:** `d6e0b4ff132e18fbf855495eb087f9f0511af67af066aeec4bfc61b05a67e941`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

### Model

- NGV090 wheel 200 DWG, OpenCADStudio 2026.42, DWG AC1032, millimetres.
- Executing model: GPT-6.1 Sol.
- Eleven separate native solids: cast-iron body, Besthane tread, central closure cap and eight socketed mounting screws.
- Axle: Z. Origin: wheel recess bottom and gearbox output mounting plane. Positive Z points towards the outer wheel face.
- Wheel axial span: Z = −47.5 to +12.5 mm.

### Manufacturer evidence

- Retained catalogue, product page and geometry tables, catalogue printed page 147, **NGV wheel 200** column; cutaway printed page 142.
- Nominal outside diameter 200 mm; overall width 60 mm; rim recess Ø155 mm, depth 47.5 mm; centring outside diameter 31.5 mm.
- Eight Ø6.6 mm through-bores and eight Ø11 mm head recesses on a Ø50 mm pitch circle, at 45° intervals.
- Manufacturer tolerances: outside diameter ±1.2 mm; width ±0.5 mm; recess depth ±0.2 mm; centring diameter h7; screw-bores H13.
- Calculated outer web span: 60 − 47.5 = 12.5 mm.

### Drawing-based reconstruction parameters

- Body outside radius 85 mm; tread running radius 100 mm; tread shoulder radius 2.5 mm.
- Centring-spigot projection 4.5 mm with 0.5 mm entry chamfer; central passage Ø24 mm; recess-bottom fillet 2 mm.
- Central cap: Ø24 × 3 mm plug, Ø25.5 × 1 mm flange; outer face Z = +12.5 mm.
- Head recess depth 7 mm, Z = +5.5 to +12.5 mm.
- Nominal cylindrical screw shank Ø6 mm, Z = −10 to +5.5 mm; head Ø10 × 6 mm; socket 5 mm across flats, depth 3 mm.
- Source front, side and cutaway views supply the reconstructed contour and hardware representation. The parameters above describe authored geometry rather than manufacturer dimensional specifications.
- Source and reconstruction metadata are stored per solid under `NEUGART_NGV090_WHEEL` XData.

### Checks and display

- Native feature checks: fifteen checks pass before saving, using native SAT surfaces and edges.
- Checks cover tread diameter and width, shoulder radii, both hole counts and diameters, pitch-circle diameter, angular coordinates, recess and spigot diameters, recess depth datums, solid count and audit.
- Save and reopened audits: eleven native 3D solids; zero errors, zero warnings and zero dropped entities. All eleven reopened solids report positive mesh volumes.
- OCS native state identifies the open NGV090 wheel drawing, with a named `NGV090_Isometric` view.
- The OCS capture pipeline has returned another document's viewport for the NGV064 drawing; that capture supplies no visual evidence for this wheel.

## Sources — online

1. neugart ngv wheel geometry.
2. neugart ngv wheel geometry.
