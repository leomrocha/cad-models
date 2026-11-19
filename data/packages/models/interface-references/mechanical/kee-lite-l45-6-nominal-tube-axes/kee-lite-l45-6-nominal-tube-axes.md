# Kee Lite L45-6 nominal tube axes

1. **Library number** 307.
2. **Plan component** Model 36, Kee Lite L45-6 crossover fitting.
3. **CAD** [Nominal tube axes](<kee-lite-l45-6-nominal-tube-axes.dwg>).
4. **DWG SHA-256:** `ee7ad56e97e31678fe555d692aeff60d1041e653b6fa3a084501b8121e2490df`. DWG 2018, 27,765 bytes.
5. **Representation** Two analytic tube-section circles and their common perpendicular. Use the circles' normals to register the nominal tube centre lines.
6. **Execution models** Construction and checking identities unavailable.

## Technical specification

1. **Front tube** Ø33.7 mm, centre (0, 0, 0) mm, axis direction +X.
2. **Rear tube** Ø33.7 mm, centre (0, 40, 0) mm, axis direction +Z.
3. **Axis relationship** The supplier calls the fitting a 90° crossover. Supplier dimension E gives 40 mm transverse spacing. The line connects the closest points of the two nominal axes in the local mounting frame.
4. **Front collar length** Supplier dimension D gives 44 mm across the front collar in the 2D drawing. Library 258 retains its drafting geometry. The two circles define nominal tube sections for joint registration.

## Verification

1. Current OCS entity records confirmed both centres, radii, plane normals and line endpoints. The file uses millimetres and each entity carries its source attribution.
2. Verified SAVE confirmed the target filename, byte size, SHA-256, two circles, one line and zero dropped entities. The [view from native records](<kee-lite-l45-6-nominal-tube-axes.png>) was inspected. Guarded closure passed for owned document 27.

## References

1. [Supplier dimensional reference, library 258](<../kee-lite-l45-6-supplier-dimension-reference/kee-lite-l45-6-supplier-dimension-reference.md>).
2. [Photo-estimated visible rear strip, library 264](<../../../mechanical-parts/components/kee-lite-l45-6-rear-visible-surface-estimate/kee-lite-l45-6-rear-visible-surface-estimate.md>).

## Sources — online

1. Scaffolding Direct L45-6 listing and projection, nominal tube outside diameter and D/E endpoints.
2. Kee Safety components catalogue, printed page 28, L45-6 fitting description and dimensions.
