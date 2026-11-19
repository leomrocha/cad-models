THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Caster arm box member

1. **Library number:** 148.
2. **Type:** part.
3. **CAD file:** [p06t-caster-arm-box-member.dwg](<p06t-caster-arm-box-member.dwg>).
4. **DWG SHA-256:** `61deadc5238c1a9f11ce8edfc1a325d72002a132d31b6477afd824a3166773d3`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Caster arm box member — P06T.

**Design status:** Discussion nominal hollow-section proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 1 per caster arm; same translated geometry for 250/300. Assembly/reference family:P06. Repeated identical pieces use instances.

### Geometry, datum and interfaces

50 Y×40 Z×3 steel box cut 205 long X−300…−95. Authoritative zero-angle bounds Z 315…355 plusΔH, withΔH 0/50 for source 250/300 height. Cross-holesØ30 andØ22 through sidewalls at X−220/−120,Z 333+ΔH (18 above lower face). Through sleeves P05PSL/P05SSL occupy these bores. Head plate top 315+ΔH contacts arm underside at Z 315+ΔH over shared X/Y region; no 2 mm overlap. Arm is above caster support plate for both variants. Cheek/pin axes raise together withΔH; primary local coordinates remain unchanged.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed source hollow arm | PASS | [1, 1, 1, 1] | count |
| Local section and cut bounds | PASS | [[-25.000000000264986, 25.0], [-20.0, 20.0], [0.0, 205.0]] | mm |
| Nominal inner/outer section corner radii | PASS | [3.0, 6.0] | mm |
| Source 30 mm projected bore axis | PASS | [[-2.0, 80.0]] | mm |
| Source 22 mm projected bore axis | PASS | [[-2.0, 180.0]] | mm |
| 30 mm bore actual left sidewall cylindrical cut | PASS | "" |  |
| 30 mm bore actual right sidewall cylindrical cut | PASS | "" |  |
| 22 mm bore actual left sidewall cylindrical cut | PASS | "" |  |
| 22 mm bore actual right sidewall cylindrical cut | PASS | "" |  |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
