# Pico tracked chassis

1. **Plan item** Assembly 2, mechanical chassis, manufacturer source positions.
2. **Native drawing** [Pico tracked chassis](<pico-chassis.dwg>).
3. **DWG SHA-256:** `fe91fbb4ed6d5771b8ef44761d89ede4893c64a3917d762fa7a139d02e2ce411`. DWG 2018, 14,920,799 bytes.
4. **State** SAVED_SOURCE_GEOMETRY_AND_PLACEMENTS_CHECKED.
5. **Execution models** gpt-6.2-sol for the original chassis readback, BOM and views. The native construction, assembly-frame correction and left-spring revision model identities are unavailable.

## Technical specification

The chassis combines the fixed frame, both gearmotors and drive sprockets, two guide end wheels, two upper return rollers, eight lower arm–roller pairs, two track loops, and eight tension spring exteriors. The assembly frame is in millimetres. X points forward, Y points left and Z points up. The lowest source track vertices set the ground datum at Z = 0.

1. **Assembly envelope from manufacturer STEP vertices** 279.94 × 193.43 × 119.39 mm, length × width × height.
2. **Track tip span from manufacturer STEP vertices** 269.62 mm along X.
3. **Model structure** 26 Model Space roots, 113 stored solids, 184 installed solid occurrences and 14,537 solid faces. Two mesh definitions store 24 meshes and produce 96 placed meshes and 1,479,296 triangles across eight spring positions. The four left springs share library 308's closed exterior.
4. **Installed BOM** 13 component rows and 42 physical units. Each physical unit records its STEP body IDs and current DWG root handles. Each spring exterior represents one physical spring.

## Verification

1. OpenCADStudio wrote the eight spring references into a new DWG using library 305 as a template. The finished file path, bytes and SHA-256 passed. Library 305 retained its source hash.
2. OpenCADStudio diagnostic readback verified both signed track placements, all 184 installed solid vertex sets, closed topology, and all eight spring transforms. Maximum solid vertex set error was 6.54e-13 mm. Maximum spring transform coefficient difference was 6.12e-17. All stored spring mesh vertices and triangle index winding survived unchanged.
3. The assembly frame applies the recorded source placement transform to all 26 top-level inserts. From manufacturer coordinates in millimetres, X = source Y − 14.125075966614006, Y = −source X + 9.027625898348703 and Z = source Z − 5.839632891977708. Saved assembly-frame readback confirmed the same block definitions, signed scales, 113 exact ACIS payloads and spring geometry. The maximum placement-matrix coefficient difference is 9.96 × 10⁻¹⁷. The saved assembly retains all BOM root handles.
4. The left-spring revision replaced 12 mesh records and rebound four existing references to the library 308 geometry from spring group 309. OpenCADStudio's headless codec saved the new DWG. Diagnostic readback checked all 26 matrices with zero coefficient change and matched all 113 ACIS payloads, 12 right spring mesh records and all other model/object records outside the replacement. The BOM retains 42 units and the same root handles, with the revised DWG hash. Revision verification.
5. Four revised saved-file views were inspected. The solid boundaries use lines and sampled trim endpoints. Spring points come from the revised mesh arrays.
6. Original STEP positions contain six overlaps between track links and guide end wheels or rear lower rollers. The largest is 16.77 mm³ on each side. The source study binds the checked bodies to the saved chassis BOM. [Wheel and track interface checks](<../../../../docs/sowbot/pico-track-wheel-alignment.md>).

## References

1. [Tracked running gear, library 305](<../../../../library/subassemblies/pico-tracked-running-gear-source-group.md>).
2. [Eight source spring exteriors, library 309](<../../../../library/subassemblies/pico-eight-spring-closed-source-placement.md>).
3. Installed BOM and CAD root handles.
4. [XY view](<../../../../images/sowbot/pico-chassis-XY.png>).
5. [XZ view](<../../../../images/sowbot/pico-chassis-XZ.png>).
6. [YZ view](<../../../../images/sowbot/pico-chassis-YZ.png>).
7. [Isometric view](<../../../../images/sowbot/pico-chassis-isometric.png>).

## Sources — online

1. Manufacturer-linked chassis STEP. Source SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
