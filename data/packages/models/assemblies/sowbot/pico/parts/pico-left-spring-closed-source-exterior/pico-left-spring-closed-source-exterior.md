# Hiwonder Pico left tension spring source exterior

1. **Library number** 308.
2. **Plan component** Model 19, Pico suspension tension spring.
3. **Native drawing** [Pico left tension spring exterior](<pico-left-spring-closed-source-exterior.dwg>).
4. **DWG SHA-256:** `76c05f0f4fdf82c23c6b508122e52bbd01c736b96ed5926d42c9faa1fa9fb084`. DWG 2018, 6,542,474 bytes.
5. **Execution models** Source tessellation, native construction and checking identities unavailable.

## Technical specification

1. **Geometry:** The twelve trimmed source faces of Hiwonder STEP body 3182 supply twelve native Mesh entities with subdivision level zero. The exterior contains **309,074 triangles**. Joining identical XYZ vertices across the source faces produces **154,539 vertices**, one connected shell, zero open or nonmanifold edges and consistent outward triangle winding. The join moved vertices **0 mm** at the 1 × 10⁻⁹ mm lookup scale.
2. **Local frame:** Millimetres. X = source Y − 67.45145966994615 mm, Y = −source X − 54.680151364355 mm and Z = source Z − 43.2323659374299 mm. This is the saved frame used by library 292.
3. **Orientation:** The original source face winding gives negative signed volume. The mesh reverses all retained triangles for outward normals and removes four zero-area seam triangles with coincident corners.
4. **Surface sampling:** OpenCASCADE linear deflection input **0.01 mm** and angular input **0.10 rad**. The direct UV-parameter correspondence check reports **0.038752 mm** at its worst sample, above the **0.03 mm** gate. All 34 exceeding samples occur on one face. A direct check against that finite face gives a maximum distance of **0.00008442 mm** over those 34 samples. These are measured sample results.

5. **Installed mesh spans:** X = **35.081 mm**, Y = **13.428 mm** and Z = **35.371 mm**, measured from the twelve saved mesh vertex arrays in the local frame. Amber markers show source contact points with the lower suspension arm (body 3186) and upper carrier (body 3234). [Dimensioned four-view drawing](<pico-left-spring-closed-source-dimensioned.png>).

## Verification

1. Source solid validity and all twelve face identities passed before meshing. Source and imported topological vertices matched.
2. DXF carrier readback and the current native records match each of the twelve face vertex arrays, triangle indices, winding and 0 subdivision. The source frame and 12-face representation are carried in the native metadata.
3. Verified save matched the final DWG path, byte size, SHA-256 and native audit. Zero entities dropped. The [current-record spring views](<pico-left-spring-closed-source-exterior.png>) show the coil and both end loops. Owned document 28 passed guarded closure.

## References

1. [Previous source-trimmed spring stage, library 292](<../pico-tension-spring-source-trimmed-exterior-stage/pico-tension-spring-source-trimmed-exterior-stage.md>).
2. [Eight source spring placements, library 303](<../../subassemblies/pico-eight-spring-source-visual-installation/pico-eight-spring-source-visual-installation.md>).

## Sources — online

1. Hiwonder manufacturer STEP, original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis, manufacturer spring and chassis imagery.
