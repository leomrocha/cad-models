THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Caster arm triangular brace

1. **Library number:** 146.
2. **Type:** part.
3. **CAD file:** [p06br-caster-head-arm-triangular-brace.dwg](<p06br-caster-head-arm-triangular-brace.dwg>).
4. **DWG SHA-256:** `08636404238c4f444caa6d248ff667ff29e676d9d62859cc1bd584f6f43450e5`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Caster arm triangular brace — P06BR.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 2 per caster arm; same shape 250/300. Assembly/reference family:P06. Repeated identical pieces use instances.

### Geometry, datum and interfaces

6 mm steel triangular plate in XZ with vertices(−300,315),(−220,315),(−220,355), translatedΔH 0/50. Left thickness Y 25…31, right−31…−25. Bottom edge sits on head plate top 315+ΔH; sloping/vertical edges flank box side face Y±25. Positive face-lap contact with box over triangle area, edge contact to plate; calculate welds. Identical translated brace geometry uses instances, not two separately manufactured height shapes.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Caster arm triangular brace | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-300.0, -220.0], [25.00000000000002, 31.00000000000002], [315.0, 355.0]] | mm |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
