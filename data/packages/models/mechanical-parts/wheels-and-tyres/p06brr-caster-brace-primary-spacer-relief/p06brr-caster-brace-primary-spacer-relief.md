THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Caster arm brace with primary-spacer relief

1. **Library number:** 147.
2. **Type:** part.
3. **CAD file:** [p06brr-caster-brace-primary-spacer-relief.dwg](<p06brr-caster-brace-primary-spacer-relief.dwg>).
4. **DWG SHA-256:** `5b22a33c30d42a623c8806da7a976b4edcb7c2c72514d92b9096dc276404ec8d`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Caster arm brace with primary-spacer relief — P06BRR.

**Design status:** Discussion construction proposal.

## Technical specification

1. **Status:** Discussion construction proposal derived from P06BR — caster arm triangular brace. Units: mm. Quantity: two instances per arm. The 300 mm wheel branch translates this part upward by 50 mm.
2. **Source blank:** Retain the proposed XZ triangle (−300,315), (−220,315), (−220,355) mm and representative left thickness Y = 25…31 mm from P06BR — triangular brace. Right instance translates Y by −56 mm, giving −31…−25 mm.
3. **Proposed machining:** Cut a cylindrical opening along Y at X = −220 mm, Z = 333 mm, radius 16 mm, through the 6 mm plate. The opening meets the triangle's vertical edge, producing a semicircular relief. Retain the original triangle bottom and sloping edges.
4. **Construction-clearance proposal:** Relief radius 16 mm = P05PSP — primary spacer outside radius 15 mm + proposed radial clearance 1 mm. The primary sleeve outside radius is also 15 mm; its end face is Y = 25 mm. These are nominal discussion geometry values.

### Calculated geometry and contacts

1. **Original conflict:** Source contact analysis identifies the shared interior point (−232,27.5,333) mm. Its radius from the relief axis is 12 mm; the proposed cut removes this point.
2. **Triangle area:** 80 mm × 40 mm / 2 = 1600.000000 mm². The removed left semicircle area is π × (16 mm)² / 2 = 402.123860 mm². Retained nominal planar area is 1197.876140 mm².
3. **Semicircle containment:** Its bottom Z = 317 mm is 2 mm above the retained Z = 315 mm bottom contact. Against the sloping edge, max(sqrt(16²−t²)+t/2) = 16 sqrt(1.25) = 17.888544 mm for 0≤t≤16 mm; available vertical offset is 22 mm. The complete removed left semicircle lies inside the triangle.
4. **Arm contact:** Representative left mating face is Y = 25 mm. The retained arm has nominal outside corner radius 6 mm, recorded in its native component checks, so its flat side spans Z = 321…349 mm. The original triangle area within this flat strip is 1120 mm². Relief area in this strip is π × 16² / 2 minus the left-half circular segment below Z = 321 mm; that segment area is (16² acos(12/16) − 12 sqrt(16²−12²))/2 = 29.011952 mm². Calculated flat contact area is 746.888093 mm². The source arm primary bore radius 15 mm lies within the removed radius-16 mm area. The brace bottom edge retains its 80 mm contact with support-plate top Z = 315 mm. Right contact is mirrored. Planar brace area and actual flat mating area have separate values.
5. **Primary spacers and sleeve:** Radius-15 mm cylindrical outer envelopes have calculated radial clearance 1 mm to the relief surface across their overlapping Y intervals. The setting sleeve/spacers at X = −120 mm lie beyond the brace maximum X = −220 mm.
6. **Pin service:** The primary nominal shank radius 10 mm has radial clearance 0.1 mm inside the sleeve and 0.25 mm inside the spacer. A proposed axial shank-extraction corridor follows the primary Y axis. The pin head stays outside the cheek stack during outward extraction; the surrounding frame/cheek assembly is checked in its separate installed group.

### Construction and native checks

1. Cut the source triangle and open radius-16 mm semicircle, deburr, then inspect thickness, axis and relief radius. This part preserves the original P06BR as a separate alternative.
2. Save the part in its own DWG. Check closed native topology, representative bounds X = −300…−220 mm, Y = 25…31 mm, Z = 315…355 mm, actual relief-cylinder radius 16 mm and axis (−220, Y, 333) mm; verify the source bottom-edge vertices and stored metadata.
3. Assemble two copies with the original arm, two sleeves, four side spacers and wheel-branch support plate as a separate ten-occurrence discussion subassembly. Check native member transforms and the stated analytic contact/clearance conditions. Weld capacity follows its named load case.

### Contact-calculation revision

1. The saved native part retains the same triangle, thickness, radius-16 mm relief and datums. The construction source revision is preserved at P06BRR construction source R01. The contact-area calculation above includes the retained arm's radius-6 mm outside corners.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Caster arm brace with primary-spacer relief | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-300.0, -220.0], [25.00000000000002, 31.00000000000002], [315.0, 355.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-220.0, 333.0]] | mm |
| Retained source bottom-edge endpoints | PASS | [1, 1, 1, 1] | count |

## Sources — online

1. Weldable steel plate stock family — supplier reference.

## References — local

140. [Caster primary sleeve](<../p05psl-caster-primary-sleeve/p05psl-caster-primary-sleeve.md>) — library entry 140.
141. [Caster primary side spacer](<../p05psp-caster-primary-side-spacer/p05psp-caster-primary-side-spacer.md>) — library entry 141.
146. [Caster arm triangular brace](<../p06br-caster-head-arm-triangular-brace/p06br-caster-head-arm-triangular-brace.md>) — library entry 146.
