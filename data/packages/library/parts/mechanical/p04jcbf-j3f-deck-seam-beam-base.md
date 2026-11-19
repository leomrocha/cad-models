THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Seam beam base

1. **Library number:** 119.
2. **Type:** part.
3. **CAD file:** [p04jcbf-j3f-deck-seam-beam-base.dwg](<p04jcbf-j3f-deck-seam-beam-base.dwg>).
4. **DWG SHA-256:** `0f0caf750c51ad56bf69cb62b1a11be7a5cef58932c4f154396623d74ff644cd`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Seam beam base — P04JCBF.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: one per P04JCB assembly.
1. **Cut stock:** steel 30×400×3 mm, X±15,Y±200,Z764…767. This base has planar upper and lower faces. End patchesY175…200 and−200…−175 contact the ledge undersideZ767.
2. **Crown plug welds:** three proposedØ8 mm holes normalZ atX0,Y−120,0,120 mm; fill by plug welding to the crown lower face and finish withinZ764…767. P04JCBC — crown is seated atZ767. Nominal ligament from an 8 mm plug hole to an M3 thread axisX±8 at the sameY is 8−4−1.5=2.5 mm for the centre row. Other receiver axes have their own separation from those plug holes.
3. **Six threaded panel receivers:** after welding, tap M3×0.5 through the combined base/crown stack atX±8,Y−140,0,140 mm. Enter fromZ770. Proposed entry/exit chamfers 0.25 mm axial each give 5.5 mm nominal full-form tapped interval. The source C118 installed profile controls actual thread overlap; P04JPN — panel input records the 2.5 mm overlap proposal and hardware pocket.
4. **Beam-retaining seats:** atX0,Y±187.5 mm, the source-associated TypeF seat continues down from the matching ledge through this base. Drill/countersink the clamped two-piece stack using P04LJFL — ledge template. Welded M8 blocks receive those screws below the base.

1. **Cut stock:** steel 30×400×3 mm, X±15,Y±200,Z764…767. This base has planar upper and lower faces. End patchesY175…200 and−200…−175 contact the ledge undersideZ767.
2. **Crown plug welds:** three proposedØ8 mm holes normalZ atX0,Y−120,0,120 mm; fill by plug welding to the crown lower face and finish withinZ764…767. P04JCBC — crown is seated atZ767. Nominal ligament from an 8 mm plug hole to an M3 thread axisX±8 at the sameY is 8−4−1.5=2.5 mm for the centre row. Other receiver axes have their own separation from those plug holes.
3. **Six threaded panel receivers:** after welding, tap M3×0.5 through the combined base/crown stack atX±8,Y−140,0,140 mm. Enter fromZ770. Proposed entry/exit chamfers 0.25 mm axial each give 5.5 mm nominal full-form tapped interval. The source C118 installed profile controls actual thread overlap; P04JPN — panel input records the 2.5 mm overlap proposal and hardware pocket.
4. **Beam-retaining seats:** atX0,Y±187.5 mm, the source-associated TypeF seat continues down from the matching ledge through this base. Drill/countersink the clamped two-piece stack using P04LJFL — ledge template. Welded M8 blocks receive those screws below the base.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed deck interface part | PASS | [1, 1, 1, 1] | count |
| Source stock bounds | PASS | [[-15.0, 15.0], [-200.0, 200.0], [764.0, 767.0]] | mm |
| Source clearance diameter 8 mm | PASS | [[0.0, -120.0], [0.0, 0.0], [0.0, 120.0]] | mm |
| Nominal thread-reference axes | PASS | [[-8.0, -139.99999999999994], [-8.0, 4.6796815812418235e-14], [-8.0, 140.00000000000006], [8.0, -139.99999999999994], [8.0, 4.6796815812418235e-14], [8.0, 140.00000000000006]] | mm |
| Nominal45-degree cone half-angles | PASS | [45.0, 45.0, 45.0, 45.0, 45.0, 45.0, 45.0, 45.0] | degrees |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
