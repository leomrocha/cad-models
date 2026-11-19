THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Fixed recessed-cup receiver

1. **Library number:** 127.
2. **Type:** part.
3. **CAD file:** [p04jrfb-j3f-recessed-captive-fixed-receiver-body.dwg](<p04jrfb-j3f-recessed-captive-fixed-receiver-body.dwg>).
4. **DWG SHA-256:** `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Fixed recessed-cup receiver — P04JRFB.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion machined-part proposal. Units: mm. Quantity: four per ledge, eight per deck.
1. **Stock and cavity:** steel 26 mm alongX×25 mm alongY×13.5 mm alongZ, centred on its associated source fastener axisX±215/±125,Y±187.5. Top faceZ767 contacts ledge underside 767; bottom 753.5. Bore aØ19 mm coaxial blind cavity from top 767 to floor 758.5, depth 8.5 mm. Remaining floor thickness is 5 mm. Minimum cavity wall thicknesses are(26−19)/2=3.5 mm inX and(25−19)/2=3 mm inY. The moving cupØ18 reaches its inner bottom face 759,0.5 mm above this fixed cavity floor.
2. **Receiver thread:** M3×0.5 through the 5 mm floor, coaxial with the cavity. Proposed entry/exit chamfers 0.25 mm axial each give full-form tapped intervalZ753.75…758.25. Source nominal drawn screw portionZ751.3…758.3 intersects that interval over 4.5 mm. Calculate actual fully formed mating overlap from the source screw interval and target at least 2.5 mm, as defined in P04JPNR — assembly. Nominal screw tip 751.3 projects 2.2 mm below the fixed-body bottom 753.5; actual installed thread/end profile controls that projection.
3. **Weld and cap clearance:** join the two X-end upper edges to ledge underside 767 with proposed 1 mm-leg fillets, extending the fixed body's plan envelope fromXcentre±13 to±14 mm. At outer axisX215 this reaches 229,1 mm before cap edge 230; mirror on rear. Y stays within 175…200 and its mirrored interval. The counterpart atX125 startsX112,99.5 mm beyond the retained centre-beam M8 block edgeX12.5; the 1 mm weld leaves 98.5 mm. Welds are finished inside these proposed envelopes.
4. **Cable/body conditions:** central planning cable edge|Y|167 is 8 mm from the receiver inner side 175. The bypassY210 inner cable edge 203 is 3 mm beyond its outer side 200. Source main/post/controller/cabinet bounds and the rotated seam-beam removal remain separate named construction checks. The actual completed standoff nose must remain at least proposed 0.2 mm above fixed floor 758.5 when the panel flange seats at 770.

1. **Stock and cavity:** steel 26 mm alongX×25 mm alongY×13.5 mm alongZ, centred on its associated source fastener axisX±215/±125,Y±187.5. Top faceZ767 contacts ledge underside 767; bottom 753.5. Bore aØ19 mm coaxial blind cavity from top 767 to floor 758.5, depth 8.5 mm. Remaining floor thickness is 5 mm. Minimum cavity wall thicknesses are(26−19)/2=3.5 mm inX and(25−19)/2=3 mm inY. The moving cupØ18 reaches its inner bottom face 759,0.5 mm above this fixed cavity floor.
2. **Receiver thread:** M3×0.5 through the 5 mm floor, coaxial with the cavity. Proposed entry/exit chamfers 0.25 mm axial each give full-form tapped intervalZ753.75…758.25. Source nominal drawn screw portionZ751.3…758.3 intersects that interval over 4.5 mm. Calculate actual fully formed mating overlap from the source screw interval and target at least 2.5 mm, as defined in P04JPNR — assembly. Nominal screw tip 751.3 projects 2.2 mm below the fixed-body bottom 753.5; actual installed thread/end profile controls that projection.
3. **Weld and cap clearance:** join the two X-end upper edges to ledge underside 767 with proposed 1 mm-leg fillets, extending the fixed body's plan envelope fromXcentre±13 to±14 mm. At outer axisX215 this reaches 229,1 mm before cap edge 230; mirror on rear. Y stays within 175…200 and its mirrored interval. The counterpart atX125 startsX112,99.5 mm beyond the retained centre-beam M8 block edgeX12.5; the 1 mm weld leaves 98.5 mm. Welds are finished inside these proposed envelopes.
4. **Cable/body conditions:** central planning cable edge|Y|167 is 8 mm from the receiver inner side 175. The bypassY210 inner cable edge 203 is 3 mm beyond its outer side 200. Source main/post/controller/cabinet bounds and the rotated seam-beam removal remain separate named construction checks. The actual completed standoff nose must remain at least proposed 0.2 mm above fixed floor 758.5 when the panel flange seats at 770.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed deck interface part | PASS | [1, 1, 1, 1] | count |
| Source stock bounds | PASS | [[-13.0, 13.0], [-12.5, 12.5], [753.5, 767.0]] | mm |
| Nominal thread-reference axes | PASS | [[0.0, 4.6153876242865875e-14]] | mm |
| Receiver cavity diameter19 mm | PASS | [[0.0, 0.0]] | mm |
| Nominal45-degree cone half-angles | PASS | [45.0, 45.0] | degrees |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
