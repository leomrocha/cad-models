THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Seam beam M8 threaded block

1. **Library number:** 124.
2. **Type:** part.
3. **CAD file:** [p04jmb-j3f-seam-beam-m8-thread-block.dwg](<p04jmb-j3f-seam-beam-m8-thread-block.dwg>).
4. **DWG SHA-256:** `c22cdc9dd8bcc28ca8db6aaff2484a357196f7c46cd37c702b22c6a75505fc2b`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Seam beam M8 threaded block — P04JMB.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: two identical blocks per P04JCB assembly.
1. **Proposed stock:** steel 25×25×8 mm, centredX0,Y±187.5, withZ756…764. M8×1.25 through-tapped axis is normalZ through its centre; source thread designation matches C160 — countersunk screw. Proposed entry/exit thread chamfers are 0.5 mm axial at 45°, giving 7 mm nominal full-form tapped length. Actual source screw/full-form overlap is checked against the beam's 5 mm project target.
2. **Attachment:** upper faceZ764 contacts the beam-base lower face. Weld along both X-end edges using a proposed 1 mm fillet towardX±13.5 mm; the 30 mm-wide base extends toX±15, giving 1.5 mm nominal weld-to-edge space. Keep Y within 175…200 and its mirrored interval, retaining the 400 mm deck footprint. The block remains integral with the removable beam.
3. **Service:** source screw heads are accessed from above after removing deck panels. Fixed threaded blocks retain the receiver threads while the beam is released; P04JCB — assembly input gives screw reach and the vertical extraction sequence.

1. **Proposed stock:** steel 25×25×8 mm, centredX0,Y±187.5, withZ756…764. M8×1.25 through-tapped axis is normalZ through its centre; source thread designation matches C160 — countersunk screw. Proposed entry/exit thread chamfers are 0.5 mm axial at 45°, giving 7 mm nominal full-form tapped length. Actual source screw/full-form overlap is checked against the beam's 5 mm project target.
2. **Attachment:** upper faceZ764 contacts the beam-base lower face. Weld along both X-end edges using a proposed 1 mm fillet towardX±13.5 mm; the 30 mm-wide base extends toX±15, giving 1.5 mm nominal weld-to-edge space. Keep Y within 175…200 and its mirrored interval, retaining the 400 mm deck footprint. The block remains integral with the removable beam.
3. **Service:** source screw heads are accessed from above after removing deck panels. Fixed threaded blocks retain the receiver threads while the beam is released; P04JCB — assembly input gives screw reach and the vertical extraction sequence.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed deck interface part | PASS | [1, 1, 1, 1] | count |
| Source stock bounds | PASS | [[-12.5, 12.5], [-12.5, 12.5], [756.0, 764.0]] | mm |
| Nominal thread-reference axes | PASS | [[0.0, 4.632226517774863e-14]] | mm |
| Nominal45-degree cone half-angles | PASS | [45.0, 45.0] | degrees |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
