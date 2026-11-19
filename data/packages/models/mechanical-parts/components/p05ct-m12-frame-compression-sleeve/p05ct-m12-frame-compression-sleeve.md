THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# M12 frame compression sleeve

1. **Library number:** 132.
2. **Type:** part.
3. **CAD file:** [p05ct-m12-frame-compression-sleeve.dwg](<p05ct-m12-frame-compression-sleeve.dwg>).
4. **DWG SHA-256:** `317c26a373476d1b5eb4799545c8b698c3359aafd92bfd565499088ed23d4f64`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** M12 frame compression sleeve — P05CT.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 4 per caster doubler; reuse instances for matching frame joints. Assembly/reference family:P05D. Repeated identical pieces use instances.

### Geometry, datum and interfaces

Turned steel tube OD 20,bore 13,length 34, axis along actual through-tube fastener. Nominal 40×40×3 rail inside clear 34; end faces contact inner walls so bolt clamp crosses solid sleeve. Verify real tube internal radius/seam and measured wall spacing. Holes in tube wallsØ13; sleeve can be inserted through open tube end before crossmember closure, then retained to alignment fixture. Sleeve ends are internal; upper/lower 3 mm walls plus 34=40.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed sleeve | PASS | [1, 1, 1, 1] | count |
| Nominal outside diameter | PASS | [[0.0, 0.0]] | mm |
| Nominal bore diameter | PASS | [[0.0, 2.0818995585505003e-15]] | mm |
| Square cut end planes and cut length | PASS | [0.0, 34.0] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
