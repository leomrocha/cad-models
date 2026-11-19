THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Deck side upright nominal section

1. **Library number:** 129.
2. **Type:** part.
3. **CAD file:** [p04upj20-j-deck-side-upright-20-tube.dwg](<p04upj20-j-deck-side-upright-20-tube.dwg>).
4. **DWG SHA-256:** `9c3de00c986b27d0b1eefed4d83a1423ae2118b23b30bef5957010ab979ead46`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Deck side upright nominal section — P04UPJ20.

**Design status:** Discussion nominal hollow-section reference.

## Technical specification

Status: Discussion input. Units: mm. Quantity: 4 per raised J3fdeck. Route:J3f raised deck side support.

### Geometry, datum and interfaces

Proposed 20×20×2 steel tube 216 long, centres X±250,Y±185. Bottom 548 onP04JFT top 548; upper 764. Post Y 175…195 clears Bmw tray outer 168 by 7 and receiver carrier inner 202 by 7. Rear cabinet outer 150 gives 25 gap. Source Jdeck 770 closes withP04JCP3 and ledge 3. Tube is above crown 471 throughout range; body X/Y extensions under 400 wide deck are explicit.

### Source and construction

Parent P04L — Deck support ledge; SKF dimension/source note; current combined proposal. Custom dimensions are proposed. Inspect contact faces, axes, purchased-source revision and exact hardware after cutting/turning/forming.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed hollow tube body | PASS | [1, 1, 1, 1] | count |
| Section and cut-length vertex bounds | PASS | [[-10.0, 10.0], [-10.0, 10.0], [0.0, 216.0]] | mm |
| Nominal inner and outer corner radii | PASS | [2.0, 4.0] | mm |

## Sources — online

1. skf sy25tf sy30tf dimensions.
2. skf sy25tf sy30tf dimensions.
3. skf sy25tf sy30tf dimensions.
4. official manufacturer PDF.
5. Square steel tube stock family — supplier reference.
6. Weldable steel plate stock family — supplier reference.
