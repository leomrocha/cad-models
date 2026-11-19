THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Battery tray gusset with R3 corner relief

1. **Library number:** 183.
2. **Type:** part.
3. **CAD file:** [p18jgr-tray-gusset-r3-corner-relief.dwg](<p18jgr-tray-gusset-r3-corner-relief.dwg>).
4. **DWG SHA-256:** `0b9710b3daeea93280ab99a596fe58294f6e67fb4578bd3ad1acda97709c5b0d`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Battery tray gusset with R3 corner relief — P18JGR.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: eight per matching elevated-tray support arrangement.

### Inputs and recorded fit conflict

1. **Original brace:** P18JG — triangular tray gusset gives 6 mm thickness and YZ triangle vertices (162,545), (137,572), (162,572) mm.
2. **Mating angle:** P18JA — elevated-tray support angle specifies 3 mm material and 3 mm inside bend radius. Its section has bend centre Y = 159 mm, Z = 569 mm. Saved angle geometry checks record native cylindrical radii of 3 mm and 6 mm.
3. **Recorded error:** the original support-group record records interior overlap of the straight-corner brace with the angle bend. The original CAD files retain that discussion geometry.

### Proposed relieved shape

1. **Local axes:** X is thickness; Y and Z retain the original brace coordinates. Bounds X = −3…3 mm, Y = 137…162 mm, Z = 545…572 mm.
2. **Section boundary:** start at (Y,Z) = (162,545) mm; straight to (137,572) mm; straight to (159,572) mm; clockwise quarter-circle to (162,569) mm about centre (159,569) mm with radius 3 mm; straight back to (162,545) mm. Extrude this section by 6 mm along X.
3. **Mating contact:** the straight upper edge contacts the angle underside at Z = 572 mm over Y = 137…159 mm. The straight right edge contacts the angle inner face at Y = 162 mm over Z = 545…569 mm. The 3 mm curved edge follows the angle inside bend between those tangent points.
4. **Instances:** retain two braces at each pad centre X ±9 mm, pad centres X = −120 mm and +270 mm. Mirror Y for the opposite support. This proposal uses two angles, four pads and eight relieved braces in its own group file.

### Geometry and persistence checks

1. Verify a single closed solid, thickness and coordinate bounds, both bend tangent points, and the native 3 mm cylindrical relief surface.
2. Compare the relief centre and tangent points with the saved angle geometry. Check the original overlap point against both solids and check the remaining contact faces in the separate group variant.
3. Save/reopen the component and group; retain source hashes, measured placements and images from those saved models.

Geometry dependencies: P18JA — tray support angle; P18JG — original triangular gusset; P18JR — tray riser pad. The relieved shape is derived proposal geometry.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Battery tray gusset with R3 corner relief | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-3.0000000000000266, 2.999999999999977], [137.0, 162.0], [545.0, 572.0]] | mm |
| Native concave relief cylinder radius 3 mm and centre (Y159,Z569) mm | PASS | [[159.0, 569.0]] | mm |
| Relief tangent vertices on both thickness faces | PASS | "" |  |

## Sources — online

1. EVShop product 216.
2. Exact-order manufacturer sheet.
3. manufacturer sheet.
4. manufacturer sheet.
5. Manufacturer instruction.
6. Kelly KLS-N wiring diagram, §3.2.2, p.14.

## References — local

181. [BMW elevated tray support angle, welded branch](<../p18ja-j-bmw-tray-support-angle/p18ja-j-bmw-tray-support-angle.md>) — library entry 181.
182. [Battery tray angle riser gusset](<../p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — library entry 182.
184. [BMW elevated tray welded riser pad](<../p18jr-j-tray-frame-riser/p18jr-j-tray-frame-riser.md>) — library entry 184.
