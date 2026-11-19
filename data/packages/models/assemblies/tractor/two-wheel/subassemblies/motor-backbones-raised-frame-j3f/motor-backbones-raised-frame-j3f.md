THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# motor backbones raised frame j3f

1. **Library number:** 44.
2. **Type:** group.
3. **CAD file:** [motor-backbones-raised-frame-j3f.dwg](<motor-backbones-raised-frame-j3f.dwg>).
4. **DWG SHA-256:** `d62ffc1053756bceeb44a0174cdb4c0e54cd00d08172960fbdc990bde7adf007`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

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

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| Raised J3f frame core | 1 | [frame core raised j3f](<../frame-core-raised-j3f/frame-core-raised-j3f.md>) — 27 | `6e8fde3c690850d086a05f1ca5388ee926d8e0c0b6eb4289caece7c74a91a8ef` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P03JIN — Left fixed motor backbone | 1 | [Motenergy left fixed motor backbone](<../../../../../mechanical-parts/components/p03jin-j-motor-inboard-backbone-upright/p03jin-j-motor-inboard-backbone-upright.md>) — 117 | `443e1946dd6c2d0cd2b13aaac2fd9557978827ad51e72ac45c7a242f98e800c2` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P03JBR — Right fixed motor backbone | 1 | [Motenergy right fixed motor backbone](<../../../../../mechanical-parts/components/p03jbr-j-right-motor-fixed-backbone/p03jbr-j-right-motor-fixed-backbone.md>) — 116 | `675373e05f38ce8f8be5975ec8cdb113ad80d19074953c8898453bb3a24b2d52` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

27. [frame core raised j3f](<../frame-core-raised-j3f/frame-core-raised-j3f.md>) — library entry 27.
116. [Motenergy right fixed motor backbone](<../../../../../mechanical-parts/components/p03jbr-j-right-motor-fixed-backbone/p03jbr-j-right-motor-fixed-backbone.md>) — library entry 116.
117. [Motenergy left fixed motor backbone](<../../../../../mechanical-parts/components/p03jin-j-motor-inboard-backbone-upright/p03jin-j-motor-inboard-backbone-upright.md>) — library entry 117.

## Views

1. [motor backbones raised frame j3f isometric](<motor-backbones-raised-frame-j3f-isometric.png>).
