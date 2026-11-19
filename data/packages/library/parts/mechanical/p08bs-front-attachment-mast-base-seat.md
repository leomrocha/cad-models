THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Front/rear S attachment mast base seat

1. **Library number:** 153.
2. **Type:** part.
3. **CAD file:** [p08bs-front-attachment-mast-base-seat.dwg](<p08bs-front-attachment-mast-base-seat.dwg>).
4. **DWG SHA-256:** `b983773fa06b46a3d8974cca8598791ac256564160c5ae017d07395904d77545`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Front/rear S attachment mast base seat — P08BS.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 1 per corresponding interface. Assembly/reference family:P08. Repeated identical pieces use instances.

### Geometry, datum and interfaces

Proposed steel 80 X×80 Y×10 mast seat, centre X+328 front/−328 rear,Y 0; bottom 273/top 283. Front bounds X 288…368, rear mirrored. Mast 40×40 base rests on seat top 283; tube 460 reaches 743. Front seat overlaps front crossmember top over X 288…300, width 12, and Y±40. Add two parent support triangles on each side to transfer cantilever load into doubler/frame. Source rear/front standard reference remains distinct. Seat contact and brace welds require attachment load calculation.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Front/rear S attachment mast base seat | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[288.0, 368.0], [-40.0, 40.0], [273.0, 283.0]] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
