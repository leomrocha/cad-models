THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Motenergy left fixed motor backbone

1. **Library number:** 117.
2. **Type:** part.
3. **CAD file:** [p03jin-j-motor-inboard-backbone-upright.dwg](<p03jin-j-motor-inboard-backbone-upright.dwg>).
4. **DWG SHA-256:** `443e1946dd6c2d0cd2b13aaac2fd9557978827ad51e72ac45c7a242f98e800c2`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Motenergy left fixed motor backbone — P03JIN.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 1 per left J3f motor. Assembly/reference family:P03M. Repeated identical pieces use instances.

### Geometry, datum and interfaces

Proposed left fixed motor backbone 5 mm steel plate X−155…95,Z 285…565,Y 125…130. Source motor centre X−30/Z 430; fourØ11 slide-joint axes X−130/70,Z 380/480. Subtract source pilotØ115 clearance capsule over±15 Z travel and source outer mounting screw-head capsules radius10 over same travel at cardinal source axes±74.6. Rail contact outer face Y 130/Z 500…540; moving plate outer face Y 125 touches backbone inner face 125. Cabinet end−175 gives 20 mm longitudinal gap. J3f right backbone is separate P03JBR because its front-edge cut differs. Source motor fastener/tool sweeps replace proposed head radius before manufacturing.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

### Source-screw adjustment envelope

The source upper mounting screw moves through Z = 489.6…519.6 mm in the J motor pose. Plate outer face and rail inner face are 5 mm apart in Y. The P11 — motor plate head-space calculation gives the source axis, local-to-assembly transform and flush-seat construction proposal. Evaluate the actual screw/washer swept geometry throughout the 30 mm adjustment travel at this rail interface.


### Source-backed flush-head clearance revision

Retain the existing motor, rail and backbone transform. The four source-axis clearance capsules use proposed radius 10.5 mm through the 5 mm backbone over motor travel±15 mm. C161 — ASME B18.3 flat-head 3/8-16×1 in is seated in P11; the ideal theoretical sharp reference radius9.9187 mm is0.5813 mm inside the capsule; actual head/capsule clearance is determined from the supplied profile and seated position. Flush to 1.0 mm inspected recess heads preserve the 5 mm rail gap. Source pilot-clearance capsule andØ11 slide axes are unchanged. Motor-to-plate tightening precedes installation on this backbone; the P11 constructor gives the lower-position tool approach and full plate/seat/thread calculation.


Source correction: ASME Table 8 A maximum is a theoretical sharp 82° flush reference. Radius10.5 mm is the proposed capsule, with actual head/seat receiving condition in P11 — motor plate. The source protrusion inspection uses straight GP bore16.5608…16.5862 mm and head-top height1.2700…2.2352 mm above a flat lapped-sharp-edge gage; its datum is separate from the plate seat.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed motor backbone | PASS | [1, 1, 1, 1] | count |
| Source backbone bounds | PASS | [[-155.0, 95.0], [125.00000000000001, 130.00000000000003], [285.0, 565.0]] | mm |
| Four slide-joint axes | PASS | [[-129.9999999999999, 479.99999999999994], [-129.99999999999963, 379.9999999999999], [69.99999999999999, 480.0], [70.00000000000016, 379.99999999999994]] | mm |
| Visible pilot travel-end arcs | PASS | [[-29.99999999999997, 414.9999999999999], [-29.999999999999538, 444.99999999999983]] | mm |
| Six exposed screw-head sweep end arcs | PASS | [[-104.60000000000001, 415.0000000000001], [-104.59999999999998, 445.00000000000006], [-30.000000000000107, 519.6000000000003], [-30.0, 340.3999999999999], [44.59999999999999, 445.0], [44.6, 415.00000000000006]] | mm |

## Sources — online

1. Motenergy ME0907 family page.
2. EV Europe ME0907 specification.
3. Square steel tube stock family — supplier reference.
4. Weldable steel plate stock family — supplier reference.
