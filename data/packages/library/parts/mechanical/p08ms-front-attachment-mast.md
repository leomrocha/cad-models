THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# S attachment mast tube

1. **Library number:** 157.
2. **Type:** part.
3. **CAD file:** [p08ms-front-attachment-mast.dwg](<p08ms-front-attachment-mast.dwg>).
4. **DWG SHA-256:** `44165d0aad89e92329afe90cac4dc1fb3e897d22d3370a4f810e54cf627db68a`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** S attachment mast tube — P08MS.

**Design status:** Discussion nominal hollow-section reference.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 1 per corresponding interface. Assembly/reference family:P08. Repeated identical pieces use instances.

### Geometry, datum and interfaces

Proposed 40×40×3 steel mast tube 460 long Z 283…743, centre X+328 front/−328 rear,Y 0. Lower face seats P08BS/P09BS upper 283. Upper carrier blank 120 high spans Z 683…803, with its lower 60 contacting mast upper 60; front plate X 348…358/rear mirror, mast outer face X±348. Custom upper pivot axis at Z 743 in proposedØ19.5 alternative, or exact source indexed template on upper blank. The 460 tube length is a custom support input, distinct from source 460 shoulder/mast relationship. Rear mast and caster/hitch are alternate modules.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed hollow tube body | PASS | [1, 1, 1, 1] | count |
| Section and cut-length vertex bounds | PASS | [[-20.0, 20.0], [-20.0, 20.0], [0.0, 460.0]] | mm |
| Nominal inner and outer corner radii | PASS | [3.0, 6.0] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
