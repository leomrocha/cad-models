THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Caster primary removable pin, structural-S proposal

1. **Library number:** 65.
2. **Type:** part.
3. **CAD file:** [c018-caster-primary-removable-pin.dwg](<c018-caster-primary-removable-pin.dwg>).
4. **DWG SHA-256:** `d446683f7bc1e8d8edb5cddf7e842cb9f291b0488777e9c0b1812307c546f783`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Caster primary removable pin, structural-S proposal — C018.

**Design status:** Discussion structural-S construction proposal.

## Technical specification

Date: 12 November 2026. CAD input sheet; pin component geometry input. Group: caster. Route: Retained fixed-setting arm proposal. Quantity: 1.

### Geometry and provenance

Pin geometry follows actual clevis/arm joint. ExistingØ40 source-report value is a layout placeholder.

### Units and local datum

Units: mm. Origin: pin axis at head shoulder.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates P05A/P05S/P06; include head, working shank and positive keeper interface.

### Space and access

Reserve full withdrawal path with arm supported.

### Dimensioned structural proposal variant S — 13 November 2026

**PROPOSAL VARIANT; no design selection.** Units:mm. Geometry below is proposed unless expressly identified as a source dimension. Datum/placement uses existing X forward,Y left,Z up and layout-proposals.md. Proposed steel thicknesses/sections require the named joint/load checks.

Custom pin variant S replaces the earlierØ40 placeholder for this variant only: proposed turned C45 steel pinØ20; working shank from head shoulder s 0 to tip s 88, headØ32×10 at s−10…0. Structural grip 76=8+60+8; positive keeper cross-holeØ4 at s 82, leaving 6 mm centre-to-tip. Keeper lies outside loaded cheek. Overall 98 mm. Chamfer 1×45° tip; final diameter/clearance/material heat treatment and fatigue follow joint loads. A headed pin with a separate positive keeper is the construction proposal; choose exact keeper wire/clip geometry to theØ4 cross-hole and retained clearance. Reserve 98 mm withdrawal plus hand/tool space, with arm supported.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed headed pin | PASS | [1, 1, 1, 1] | count |
| Proposed head diameter | PASS | [[0.0, -6.123233995736766e-16]] | mm |
| Proposed shank diameter | PASS | [[0.0, 0.0]] | mm |
| Keeper cross-bore diameter and axis | PASS | [[0.0, 82.0]] | mm |
| Head end, shoulder and pin tip planes | PASS | [-10.0, 0.0, 88.0] | mm |
| One 45 degree source tip chamfer slope | PASS | [0.9999999999999999] | mm |
| Chamfer boundary radii at Z=87 mm | PASS | [10.0] | mm |
| Chamfer boundary radii at Z=88 mm | PASS | [9.0] | mm |

## Sources — online

1. Exact manufacturer data sheet.
2. manufacturer data sheet.
3. manufacturer data sheet.
4. WISKA mounting instruction.
5. 08 parts and materials.
6. 08 parts and materials.
7. 08 parts and materials.
8. 08 parts and materials.
9. 08 parts and materials.
10. 08 parts and materials.
11. 08 parts and materials.
12. 08 parts and materials.
13. 08 parts and materials.
14. 08 parts and materials.
15. 08 parts and materials.
16. 08 parts and materials.
17. 08 parts and materials.
18. 08 parts and materials.
19. 08 parts and materials.
20. 08 parts and materials.
21. 08 parts and materials.
22. 08 parts and materials.
23. 08 parts and materials.
24. 08 parts and materials.
25. 08 parts and materials.
26. 08 parts and materials.
27. 08 parts and materials.
28. 08 parts and materials.
29. 08 parts and materials.
30. 08 parts and materials.
31. 08 parts and materials.
32. 08 parts and materials.
33. 08 parts and materials.
34. 08 parts and materials.
35. 08 parts and materials.
36. 08 parts and materials.
37. 08 parts and materials.
38. 08 parts and materials.
39. 08 parts and materials.
40. 08 parts and materials.
41. 08 parts and materials.
42. 08 parts and materials.
43. 08 parts and materials.
44. official manufacturer PDF.
45. sumitomo exact interfaces.
46. Kelly KLS-N wiring diagram, §3.2.2, p.14.
