THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Caster angle-setting pin, structural-S proposal

1. **Library number:** 66.
2. **Type:** part.
3. **CAD file:** [c019-caster-angle-setting-pin.dwg](<c019-caster-angle-setting-pin.dwg>).
4. **DWG SHA-256:** `9595fd9089bd1037263358af8cc86585cb1ee516d9487281681f51c5111f10a6`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Caster angle-setting pin, structural-S proposal — C019.

**Design status:** Discussion structural-S construction proposal.

## Technical specification

Date: 12 November 2026. CAD input sheet; pin component geometry input. Group: caster. Route: Retained fixed-setting arm proposal. Quantity: 1.

### Geometry and provenance

Separate setting pin fixes arm angle using chosen cheek/arm hole position.

### Units and local datum

Units: mm. Origin: pin axis at retaining head/shoulder.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates P05A/P06/P05S and its positive keeper; record useful engagement through both cheeks.

### Space and access

Allow setting change and pin withdrawal with support load removed.

### Dimensioned structural proposal variant S — 13 November 2026

**PROPOSAL VARIANT; no design selection.** Units:mm. Geometry below is proposed unless expressly identified as a source dimension. Datum/placement uses existing X forward,Y left,Z up and layout-proposals.md. Proposed steel thicknesses/sections require the named joint/load checks.

Custom pin variant S: proposed C45 steelØ12 pin, headØ24×8; shank 88 from shoulder, total 96;76 mm grip=8+60+8; keeper cross-holeØ3 at s 82 from shoulder,1×45° tip chamfer. Source status: all pin dimensions/material here are proposed custom inputs. Match sleeve/cheek 12.2 bores; load check includes double shear, cheek/sleeve bearing and setting force T/0.100 m for arm torque T. Unload/support arm before extraction; reserve 96 mm axial withdrawal and keeper access.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed headed pin | PASS | [1, 1, 1, 1] | count |
| Proposed head diameter | PASS | [[0.0, -4.898587196589413e-16]] | mm |
| Proposed shank diameter | PASS | [[0.0, 0.0]] | mm |
| Keeper cross-bore diameter and axis | PASS | [[0.0, 82.0]] | mm |
| Head end, shoulder and pin tip planes | PASS | [-8.0, 0.0, 88.0] | mm |
| One 45 degree source tip chamfer slope | PASS | [0.9999999999999999] | mm |
| Chamfer boundary radii at Z=87 mm | PASS | [6.0] | mm |
| Chamfer boundary radii at Z=88 mm | PASS | [5.0] | mm |

## Sources — online

1. Exact-order manufacturer sheet.
2. manufacturer sheet.
3. manufacturer sheet.
4. Manufacturer instruction.
