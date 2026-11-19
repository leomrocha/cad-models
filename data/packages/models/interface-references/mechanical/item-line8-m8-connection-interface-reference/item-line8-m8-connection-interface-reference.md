# item line8 m8 connection interface reference

1. **Library number:** 6.
2. **Type:** standard.
3. **CAD file:** [item-line8-m8-connection-interface-reference.dwg](<item-line8-m8-connection-interface-reference.dwg>).
4. **DWG SHA-256:** `ba71e9c1636305deed1cd601878cb60112fa31e99362b3c635e8f1fd17cff92f`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

### Model and source

- Native bracket-set DWG, OpenCADStudio 2026.42, DWG AC1032, millimetres.
- Executing model: GPT-6.1 Sol.
- Manufacturer originals, photographs and dimension drawings, parts 0.0.411.15 and 0.0.026.18, page 1 of each sheet.
- Ten separate native solids: zinc casting, PA-GF cap, two washers, two button-head screws, two nut bodies and two thrust balls.
- Casting axes: X and Z along the perpendicular legs; Y across the bracket. Outer bearing planes are X = 0 and Z = 0.
- Source 40 mm references define the leg endpoints and width. Source 20 mm references locate the mounting axes halfway along each leg.
- Published kit contents represented: two ISO 7380-M8×18 screws, two 13.9 × 13.9 × 2 mm washers and two 0.0.026.18 nuts.

### Casting reconstruction

- Two open cavities reproduce the hollow casting visible in the manufacturer photograph.
- Reference triangular section: (X,Z) = (0,0), (40,0), (0,40) mm; width Y = −20 to +20 mm.
- Reconstructed legs 4 mm thick, end walls 3 mm thick, central rib 5 mm thick and internal pocket fillets 2 mm.
- Reconstructed mounting slots: 12.5 × 8.5 mm; axes at X = 20 mm on the horizontal leg and Z = 20 mm on the vertical leg, both at Y = 0.
- Reconstructed washer-access pockets: 15 × 15 mm, with floors Z = 4 mm and X = 4 mm.
- Four integral locating tabs: 6 mm longitudinal length, 7.5 mm root width and 3 mm projection from the bearing planes. Centres lie 8 and 32 mm along each leg.
- Tabs extend to X = −3 mm or Z = −3 mm. Casting reference endpoints remain X = 40 mm and Z = 40 mm.

### Cap and hardware reconstruction

- Cap face: 39 mm wide × 36√2 mm long, approximately 50.912 mm; thickness 1.8 mm. Outer face plane: X + Z = 40 mm.
- Two integral retention tongues: 5 mm wide, projecting 5.5 mm from the outer face, with reconstructed hook geometry.
- Washers use the published outside dimensions and reconstructed Ø8.5 mm clearance bores.
- Screw representation: nominal Ø8 × 18 mm cylindrical shank; Ø13.8 mm button head, 4.4 mm high; 5 mm across-flats socket, depth 2.6 mm. Dome shape follows a reconstructed circular profile.
- Horizontal screw under-head plane: Z = 6 mm, shank end Z = −12 mm, axis X = 20 mm, Y = 0.
- Vertical screw under-head plane: X = 6 mm, shank end X = −12 mm, axis Y = 0, Z = 20 mm.
- Nut geometry reuses the standalone nut reconstruction. Nut placement transforms are stored per solid under `ITEM_SET_PLACEMENT` XData.
- The kit placement represents the parts around two perpendicular mounting planes. Profile and chassis geometry are separate components.
- Wall thicknesses, slot shapes, cap details and hardware clearances above are authored reconstructions from the source views; published dimensions remain separately labelled in each solid's XData.

### Native checks

- Native geometry readback: twenty-one checks pass before saving.
- Checks cover casting width, leg endpoints and bearing datums; washer sizes and bores; perpendicular M8 nut axes at 20 mm references; screw shaft radii and 18 mm shank extents; cap width and plane; solid count; positive volumes and audit.
- The reader applies each native SAT rigid-body transform before checking assembly coordinates.
- Save and reopened audits: ten native 3D solids, zero errors, zero warnings and zero dropped entities.
- Overlapping-cutter subtraction reports `SUBTRACT: the selected topology could not be cut safely.` Slot cuts use one combined cutter for each mounting axis.
- OCS native state identifies the bracket-set DWG and its named `ITEM_41115_Isometric` view. The known stale-capture behaviour supplies no independent visual comparison of this model.

## Sources — online

1. item line8 geometry.
2. item line8 geometry.

## Views

1. [item line8 m8 connection interface reference](<item-line8-m8-connection-interface-reference.png>).
