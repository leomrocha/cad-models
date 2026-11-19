THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# chassis deck recessed foot hardware j3f

1. **Library number:** 20.
2. **Type:** group.
3. **CAD file:** [chassis-deck-recessed-foot-hardware-j3f.dwg](<chassis-deck-recessed-foot-hardware-j3f.dwg>).
4. **DWG SHA-256:** `50e2fa29034972022b85dbb60f6f4353f0ce538f7ff0bc80becabfb602b19a69`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: two identical panel assemblies per deck.

### Parts, axes and source fit

1. **Panel:** one P04JPNRP —299×400×3 mm panel plate, rear X−300…−1,Y±200,Z770…773 mm; front is a proper 180° rotation aboutZ of the rear. Each has four source fixing axes at local(u,v)=(85,±187.5),(175,±187.5) mm, with rear X=−300+u and front X=300−u,Y=−v. World axes are therefore X−215/−125 for rear and X125/215 for front, each atY±187.5. The centre seam stays 2 mm.
2. **Recesses:** four P04JRC — turned mounting cups per panel. Their flange tops share the deck load planeZ773; each source 3 mm mounting floor has outer faceZ762 and inner faceZ759. Install one C118 — Southco 51-72-610-24 captive screw/standoff assembly per cup. Its C119 standoff is included. Quantity is eight C118 packages per deck in this branch.
3. **Fixed support:** P04LJRC — matching ledges have fourØ19 mm passages per side. Each passage aligns with one P04JRFB — fixed receiver body. Receiver top isZ767; its cavity floor isZ758.5,0.5 mm below the moving cup inner face 759. Centre panel edges remain supported by the removable seam beam crownZ770. The seam beam retains its two independent M8 connections and the corrected removal sequence in its own input.
4. **Closed source-reference pose:** Southco page 250 gives shoulder-to-head-seat 6.3 mm, head height 4 mm, screw length 17 mm and drawn threaded portion 7 mm. With mounting outer faceZ762, nominal seatZ768.3, head topZ772.3, tipZ751.3 and drawn thread portionZ751.3…758.3. The head is nominally 0.7 mm below deck plane 773. Required actual closed head projection H from mounting outer face satisfies H≤11 mm. Source-reference 10.3 mm gives the nominal screen. Actual knurled head and standoff bodies must fit the cup boreØ14 mm.
5. **Engagement:** receiver floor isZ753.5…758.5 with proposed 0.25 mm entry/exit chamfers, giving full-form tapped intervalZ753.75…758.25. The nominal source drawn threaded portion intersects that interval over 4.5 mm. For actual source full-form screw interval[Slo,Shi], calculate E=max(0,min(Shi,758.25)−max(Slo,753.75)); project target E≥2.5 mm. Source 7 mm includes its tip/end form. Inspect the actual full-form thread and formed standoff profile when checking E.
6. **Body clearance:** nominal moving floor inner face 759 to fixed cavity floor 758.5 gives 0.5 mm. Proposed minimum separation between the actual formed standoff nose and the fixed floor is 0.2 mm. The completed source flare defines the actual nose endpoint. Source P3.2 is the pre-flare panel-grip reference. Moving cup bodyØ18 inside fixed passage/cavityØ19 gives 0.5 mm nominal radial clearance. Source mounting thickness remains 3 mm within the 2.9…3.3 mm product range.

### Named-shape spacing and service

1. **Existing caps:** deck caps atX±250 spanX230…270 and−270…−230, Y170…200,Z764…767. The nearest receiver atX215 spansX202…228; the mirrored receiver is−228…−202. Metal-to-cap X gap is 2 mm; proposed 1 mm X-edge fillets reduce it to 1 mm. Cup outer bodyØ18 reachesX224 at the positive outer axis,6 mm before cap edge 230. Source upper cabinet/receiver and side-controller poses retain their own geometry.
2. **Cable corridors:** fixed bodies occupy|Y|175…200, giving 8 mm to the central planning cable edge|Y|167. The source/proposal bypass atY210 has inner expanded edge 203, giving 3 mm to those bodies. Its transverse segment atX−280,Z754 has expanded X−287…−273; nearest fixed body startsX−228, giving 45 mm separation. These are retained OD14 planning-envelope comparisons from the physical installation record.
3. **Lifting parts:** lifting-post X extent reaches 190 mm at the positive 180 mm centre; receiver minimumX202 leaves 12 mm. Post/arm topsZ747 are 6.5 mm below receiver minimumZ753.5. Root/tab inner Y210/218 gives 10/18 mm lateral gaps from receiver outerY200. The eight recessed fixings stay within the deck footprintY±200.
4. **Panel service:** remove cargo, release the four C118 screws and verify each actual tip has cleared the fixed receiver. Proposed released-tip plane isZ759 or above,0.5 mm above receiver entry 758.5. From source nominal tip 751.3 this requires at least 7.7 mm upward screw travel. This is a project release criterion checked with the actual captive assembly. The source installation sequence withdraws the screw to check captivity. Then lift the panel vertically 60 mm at fixedX/Y, retaining the original panel service corridor. Released heads may rise above the load plane during this cargo-free service operation.
5. **Seam-beam sweep:** the closest fixed receiver/weld box to the beam origin has nearest plan point(|X|,|Y|)=(125−14,187.5−12.5)=(111,175) mm. Its radial distance is√(111²+175²)=207.234167 mm. The retained complete beam yaw-cylinder radius is√(200²+15²)=200.561711 mm, giving 6.672456 mm nominal plan separation throughout the original 0…40° yaw. The outer receivers are farther from that cylinder. This checks the fixed receiver/weld boxes against that retained swept planning bound.
6. **Battery service:** remove both panels, then follow the seam-beam input: disconnect and move crossing harnesses, remove the two M8 screws, support and lower the beam 3.5 mm, yaw 40°, then lift through the ledge gap. The independent battery shield, electrical connections and restraints retain their own service sequence. This eight-perimeter-fixing branch preserves the raised-head fourteen-fixing branch as its separate geometry.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| Raised frame core with foot passages | 1 | [frame core raised foot passages j3f](<frame-core-raised-foot-passages-j3f.md>) — 26 | `5ab966631d0bc4bb9df46d19f1e42100e8b2c55c59a63114b3dd25a7c023ac9f` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Four deck side supports | 1 | [deck side supports j3f](<deck-side-supports-j3f.md>) — 24 | `651b2df994ea7242d4bd2cdfe0375a3607c1725e2bb2f102d8c850a6052f3d88` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Four side lifting supports | 1 | [side lifting supports j3f](<side-lifting-supports-j3f.md>) — 49 | `2d06cf9551fe6440a6abd23f01c0da07c75f11a876be5df78c45858f26ee67bc` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Removable seam beam | 1 | [deck seam beam j3f](<deck-seam-beam-j3f.md>) — 23 | `f9fbbfee5c880f5bcfa2586381f0f453ef7754cb0e7c566cc3bc6d05b217005c` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Two-hole eight-foot nominal hardware proposal | 1 | [eight foot two hole nominal hardware j3f](<eight-foot-two-hole-nominal-hardware-j3f.md>) — 25 | `a4eb04059c8fe5875b98e9a4c8512711abff39b10d87c0a09d0be9cf0e0a5e13` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04LJRC — Recessed deck ledge | 1 | [Recessed-captive deck ledge](<../parts/mechanical/p04ljrc-j3f-recessed-captive-deck-ledge.md>) — 128 | `035088e106e4d55622f99cabce9fdd9cf61b7a342286853747d7dc3562989768` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JRFB — Fixed cup receiver | 1 | [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — 127 | `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964` | `{"position_mm":[-215.0,187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JRFB — Fixed cup receiver | 1 | [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — 127 | `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964` | `{"position_mm":[-125.0,187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JRFB — Fixed cup receiver | 1 | [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — 127 | `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964` | `{"position_mm":[125.0,187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JRFB — Fixed cup receiver | 1 | [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — 127 | `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964` | `{"position_mm":[215.0,187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04LJRC — Recessed deck ledge | 1 | [Recessed-captive deck ledge](<../parts/mechanical/p04ljrc-j3f-recessed-captive-deck-ledge.md>) — 128 | `035088e106e4d55622f99cabce9fdd9cf61b7a342286853747d7dc3562989768` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JRFB — Fixed cup receiver | 1 | [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — 127 | `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964` | `{"position_mm":[-215.0,-187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JRFB — Fixed cup receiver | 1 | [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — 127 | `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964` | `{"position_mm":[-125.0,-187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JRFB — Fixed cup receiver | 1 | [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — 127 | `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964` | `{"position_mm":[125.0,-187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JRFB — Fixed cup receiver | 1 | [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — 127 | `9af41ce4c299ef84659733b888e671775343a7b70aaf4a8d81fe07050bcde964` | `{"position_mm":[215.0,-187.5,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Rear deck panel with four cups | 1 | [deck half panel and cups j3f](<deck-half-panel-and-cups-j3f.md>) — 22 | `77226cde0f296ee7bf0f98ff00bd04d1fe2cb65c5aba56551396234b68afa4dd` | `{"position_mm":[-300.0,0.0,770.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Front deck panel with four cups | 1 | [deck half panel and cups j3f](<deck-half-panel-and-cups-j3f.md>) — 22 | `77226cde0f296ee7bf0f98ff00bd04d1fe2cb65c5aba56551396234b68afa4dd` | `{"position_mm":[300.0,0.0,770.0],"scale":[1.0,1.0,1.0],"rotation_radians":3.141592653589793,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. Southco Polished Series catalogue, printed pages 249–250.
2. Weldable steel plate stock family — supplier reference.

## References — local

22. [deck half panel and cups j3f](<deck-half-panel-and-cups-j3f.md>) — library entry 22.
23. [deck seam beam j3f](<deck-seam-beam-j3f.md>) — library entry 23.
24. [deck side supports j3f](<deck-side-supports-j3f.md>) — library entry 24.
25. [eight foot two hole nominal hardware j3f](<eight-foot-two-hole-nominal-hardware-j3f.md>) — library entry 25.
26. [frame core raised foot passages j3f](<frame-core-raised-foot-passages-j3f.md>) — library entry 26.
49. [side lifting supports j3f](<side-lifting-supports-j3f.md>) — library entry 49.
127. [Fixed recessed-cup receiver](<../parts/mechanical/p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — library entry 127.
128. [Recessed-captive deck ledge](<../parts/mechanical/p04ljrc-j3f-recessed-captive-deck-ledge.md>) — library entry 128.

## Views

1. [chassis deck recessed foot hardware j3f isometric](<../images/chassis-deck-recessed-foot-hardware-j3f-isometric.png>).

1. [chassis deck recessed foot hardware j3f orthographic](<../images/chassis-deck-recessed-foot-hardware-j3f-orthographic.png>).

1. [chassis deck recessed foot hardware j3f orthographic](<../images/chassis-deck-recessed-foot-hardware-j3f-orthographic.svg>).
