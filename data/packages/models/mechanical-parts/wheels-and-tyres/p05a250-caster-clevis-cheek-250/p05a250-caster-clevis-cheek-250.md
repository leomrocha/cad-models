THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Caster clevis cheek for 250 mm wheel

1. **Library number:** 130.
2. **Type:** part.
3. **CAD file:** [p05a250-caster-clevis-cheek-250.dwg](<p05a250-caster-clevis-cheek-250.dwg>).
4. **DWG SHA-256:** `6810fd89439e6aaec20cf7819336a9f4f3f91dd73dfea3e28afbb392b8f072c3`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Caster clevis cheek for 250 mm wheel — P05A250.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: two per matching caster support.

### Source and manufactured shape

1. **Source family:** P05A — caster clevis cheek, structural variant S and its zero-setting head-plate clearance cut.
2. **Material proposal:** 8 mm steel plate. Left inner face Y = 30 mm, outer face Y = 38 mm. Mirror Y for the opposite instance.
3. **Finished XZ boundary:** (-212.5, 273), (-85, 273), (-85, 393), (-265, 393), (-265, 316), (-212.5, 316) mm, closed by a straight segment to the first point. This transfers the source rectangle and its rear lower clearance cut.
4. **Primary bore:** diameter 20.2 mm, axis normal to Y through X = −220 mm, Z = 333 mm.
5. **Three setting bores:** diameter 12.2 mm, axes normal to Y. For α = −20°, 0°, +20°, their coordinates are X = −220 + 100 cos α mm and Z = 333 + 100 sin α mm. The 100 mm radius and angle values are source discussion inputs.
6. **Reference height:** this 250 mm wheel branch uses the source height translation ΔH = 0 mm. The rear lower relief boundary is X = -212.5 mm, Z = 316 mm.

### Assembly and interfaces

1. Primary and setting joints use C018 — primary removable pin and C019 — angle-setting pin, with their separate sleeves and side spacers.
2. The left cheek outer face Y = 38 mm contacts the matching P05W250 — caster support web inner face. Mirror the pair on the right.
3. The rearward caster arrangement applies the existing source X translation of −240 mm to the complete matching group.
4. The zero setting is the source ground-working proposal. The ±20° holes describe the source unloaded stow/service positions.

### CAD checks

1. Check closed-body topology, 8 mm thickness, the six boundary vertices and the transferred hole diameters and axes.
2. Compare trigonometric setting-hole coordinates with the native cylindrical axes using one-to-one tolerance matching.
3. Check parallel cheek faces, the 60 mm inner gap, matching support-web contact and the zero-setting head-plate clearance in the group.
4. Save/reopen this separate part and retain source hashes, measured geometry and its own source-labelled group placement.

Geometry dependencies: P05A — caster cheek source family; C018 — primary pin; C019 — setting pin. All custom geometry retains discussion-proposal status.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Caster clevis cheek for 250 mm wheel | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-265.0, -85.0], [30.000000000000018, 38.00000000000002], [273.0, 393.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-220.0, 333.0]] | mm |
| Source-sheet hole group 2 | PASS | [[-126.03073792140916, 298.7979856674331], [-126.03073792140916, 367.2020143325669], [-120.0, 333.0]] | mm |
| Source rear lower relief boundary vertices | PASS | [1, 1, 1, 1, 1, 1] | count |

## Sources — online

1. Weldable steel plate stock family — supplier reference.

## References — local

65. [Caster primary removable pin, structural-S proposal](<../c018-caster-primary-removable-pin/c018-caster-primary-removable-pin.md>) — library entry 65.
66. [Caster angle-setting pin, structural-S proposal](<../c019-caster-angle-setting-pin/c019-caster-angle-setting-pin.md>) — library entry 66.
