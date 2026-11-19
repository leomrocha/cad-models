THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Kelly raised rail gap spacer

1. **Library number:** 192.
2. **Type:** part.
3. **CAD file:** [p22sp7-kelly-raised-rail-gap-spacer.dwg](<p22sp7-kelly-raised-rail-gap-spacer.dwg>).
4. **DWG SHA-256:** `a162c9155b14cefdb16e9157360203411a592d6f6dfd059bf047a020200c4910`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Kelly raised rail gap spacer — P22SP7.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:J3f raised-frame discussion proposal. Quantity: 4 per J controller pair.

### Geometry, datum and interfaces

Turned steel OD 16,bore 6.6,length 7 along Y. Left occupies Y 170…177, right mirrored. Rail outer face 170 and post inner 177 are exact proposed contact planes. One per post rail-attachment axis X−137/77,Z 520. Joint clamp also uses rail/internal and post compression sleeves.

### Source and construction

Parent P22Kelly — Kelly KLS 7240 N support bracket; current J3f/J4 arrangement. All custom dimensions here are proposed inputs. Cut/turn/form, deburr and inspect stated contact faces, axes and length before assembly.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed sleeve | PASS | [1, 1, 1, 1] | count |
| Nominal outside diameter | PASS | [[0.0, 0.0]] | mm |
| Nominal bore diameter | PASS | [[0.0, 4.286263797015736e-16]] | mm |
| Square cut end planes and cut length | PASS | [0.0, 7.0] | mm |

## Sources — online

1. Kelly KLS-N wiring diagram, §3.2.2, p.14.
2. source review r02.
3. source review r02.
4. Square steel tube stock family — supplier reference.
5. Weldable steel plate stock family — supplier reference.
