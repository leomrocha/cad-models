THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Seam beam crown

1. **Library number:** 118.
2. **Type:** part.
3. **CAD file:** [p04jcbc-j3f-deck-seam-beam-crown.dwg](<p04jcbc-j3f-deck-seam-beam-crown.dwg>).
4. **DWG SHA-256:** `15d35d0f4b29da4c468b6ffb56f3fbb5079b7316f6caeae007a95b9bdede70bb`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Seam beam crown — P04JCBC.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: one per P04JCB assembly.
1. **Cut stock:** steel 30×350×3 mm, X±15,Y±175,Z767…770. Lower face contacts the beam base top 767; upper face 770 contacts both panel seam strips. Crown ends coincide with the ledge inner edgesY±175.
2. **Weld and thread interfaces:** locate the crown on P04JCBF — base, plug weld through its threeØ8 holes from below, then drill/tap the six M3×0.5 source-aligned receiver axesX±8,Y−140,0,140 mm through the 6 mm combined stack. Keep the top bearing plane 770 planar. Six receiver axes correspond to the seam fixings of the two P04JPN — removable panels.

1. **Cut stock:** steel 30×350×3 mm, X±15,Y±175,Z767…770. Lower face contacts the beam base top 767; upper face 770 contacts both panel seam strips. Crown ends coincide with the ledge inner edgesY±175.
2. **Weld and thread interfaces:** locate the crown on P04JCBF — base, plug weld through its threeØ8 holes from below, then drill/tap the six M3×0.5 source-aligned receiver axesX±8,Y−140,0,140 mm through the 6 mm combined stack. Keep the top bearing plane 770 planar. Six receiver axes correspond to the seam fixings of the two P04JPN — removable panels.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed deck interface part | PASS | [1, 1, 1, 1] | count |
| Source stock bounds | PASS | [[-15.0, 15.0], [-175.0, 175.0], [767.0, 770.0]] | mm |
| Nominal thread-reference axes | PASS | [[-8.0, -139.99999999999994], [-8.0, 4.6903972407343625e-14], [-8.0, 140.00000000000006], [8.0, -139.99999999999994], [8.0, 4.6903972407343625e-14], [8.0, 140.00000000000006]] | mm |
| Nominal45-degree cone half-angles | PASS | [45.0, 45.0, 45.0, 45.0, 45.0, 45.0] | degrees |

## Sources — online

1. Weldable steel plate stock family — supplier reference.

## References — local

119. [Seam beam base](<p04jcbf-j3f-deck-seam-beam-base.md>) — library entry 119.
