THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Front upper attachment carrier, proposed 19.5 mm chassis-pivot alternative

1. **Library number:** 158.
2. **Type:** part.
3. **CAD file:** [p08ub-front-upper-attachment-blank.dwg](<p08ub-front-upper-attachment-blank.dwg>).
4. **DWG SHA-256:** `7f5f03daf38e2cad3eb16d5aa31c53aa04b0f188d59654d9b4c5a4e32927921d`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Front upper attachment carrier, proposed 19.5 mm chassis-pivot alternative — P08UB.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 1 per corresponding interface. Assembly/reference family:P08. Repeated identical pieces use instances.

### Geometry, datum and interfaces

Steel 10 thick, local 100 u×120 v rectangle u±50,v 0…120. Local plane Y/Z, axis normal X. Source-specific upper interface cut is indexed parameter(uTOP,vTOP,dTOP). Proposed central custom carrier holeØ19.5 at(0,60) is a separately labelled chassis-pivot alternative, not a source standard hole. Weld the lower60 mm to the centred40 mm mast face. Do not drill the earlier±30 frame axes; they miss the mast. Source upper-interface parameters and the proposedØ19.5 pivot retain their own geometry.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

### Welded mast attachment proposal

Omit the two earlier frame holes at(u,v)=(±30,20): they lie outside the40 mm mast width. Keep source-specific upper-interface features and the separately proposedØ19.5 pivot unchanged. Weld the lower60 mm of the100 mm-wide blank to the actual40 mm mast face, centredu0, using its two vertical contact edges and accessible bottom edge. Actual shared face is40×60. Weld size follows attachment loads; this recipe adds no pin articulation mechanism.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Front upper attachment carrier, proposed 19.5 mm chassis-pivot alternative | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[347.99999999999994, 357.99999999999994], [-50.0, 50.0], [683.0, 803.0]] | mm |
| Source-sheet hole group 1 | PASS | [[6.123233995737045e-17, 743.0]] | mm |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
