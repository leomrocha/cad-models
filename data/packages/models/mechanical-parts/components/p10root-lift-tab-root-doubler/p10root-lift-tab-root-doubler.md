THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Side lifting-tab root doubler

1. **Library number:** 162.
2. **Type:** part.
3. **CAD file:** [p10root-lift-tab-root-doubler.dwg](<p10root-lift-tab-root-doubler.dwg>).
4. **DWG SHA-256:** `2f39ac7c65689cdcffb11a1f9c4679b7975ff60b7177afcf0b0d5ad051ff62d3`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Side lifting-tab root doubler — P10ROOT.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 4 per lift support S. Assembly/reference family:P10. Repeated identical pieces use instances.

### Geometry, datum and interfaces

8 mm steel 60 X×60 Z rectangle, plane XZ at outer arm end. Inner face Y 210,outer 218 on left; mirror right. Bounds X tab centre±30,Z 430…490. Arm end 40×40 contacts doubler inner face at Z 440…480. Lift tab same plate can be integral with root: parent tab must instead attach outer face Y 218 and start Z 440,thickness 8 to 226. For separate geometry inventory, use this root plus existing P10tab flat blank 60×120×8 at Y 218…226, Z 440…560 with eye 20 at 540. Shared face contact Z 440…490 has 50 mm overlap; weld perimeter as calculated.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Side lifting-tab root doubler | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-30.0, 30.0], [210.0, 218.0], [430.0, 490.0]] | mm |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
