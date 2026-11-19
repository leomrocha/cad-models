THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Recessed-captive deck ledge

1. **Library number:** 128.
2. **Type:** part.
3. **CAD file:** [p04ljrc-j3f-recessed-captive-deck-ledge.dwg](<p04ljrc-j3f-recessed-captive-deck-ledge.dwg>).
4. **DWG SHA-256:** `035088e106e4d55622f99cabce9fdd9cf61b7a342286853747d7dc3562989768`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Recessed-captive deck ledge — P04LJRC.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: two identical ledges mirrored aboutY0.
1. **Cut strip and caps:** steel 600×25×3 mm. LeftX−300…300,Y175…200,Z767…770; right mirrorsY. Existing caps atX±250,Y170…200,Z764…767 retain their 40×25 mm ledge contact patches, existing posts/feet and the deck height chain. This plate has its own cup-hole geometry; the direct tapped-hole ledge remains a separate input.
2. **Cup passages:** fourØ19 mm through holes normalZ atX−215,−125,125,215 andY187.5 on the left, mirrored on the right. Nominal hole-to-Y-edge ligament 12.5−9.5=3 mm. P04JRC — moving cup lower bodyØ18 passes through; flangeØ22 rests on the ledge top with 1.5 mm radial bearing width. Four P04JRFB — fixed receiver bodies attach under each ledge.
3. **Seam-beam seat:** retain source-associated DIN74 TypeF M8 countersink axisX0,Y187.5, mirroredright, machined through the 3 mm ledge and 3 mm removable beam-base stack. Source boreØ9.00…9.22 mm, mouthØ18.25…18.58 mm, nominal 90°; project seat angle 90°±1°. P04LJFL — retained seat source/dimension chain records its actual C160 profile and depth. The nearest cup axisX125 gives 125−11−9.29=104.71 mm between cup-flange envelope and maximum countersink mouth. The correspondingØ19 ledge hole gives 125−9.5−9.29=106.21 mm material separation to that mouth.
4. **Assembly:** weld the fixed receiver bodies under the ledge before fitting the caps/panels, preserving the central beam seat. Machine the paired beam/ledge counterseats using the existing matched-seat construction. Bench-form panel standoffs with manufacturer tools, then fit the recessed panel so its eight cups enter these holes and fixed cavities. Actual formed-nose gap, thread overlap and screw-release travel follow P04JPNR — assembly criteria.

1. **Cut strip and caps:** steel 600×25×3 mm. LeftX−300…300,Y175…200,Z767…770; right mirrorsY. Existing caps atX±250,Y170…200,Z764…767 retain their 40×25 mm ledge contact patches, existing posts/feet and the deck height chain. This plate has its own cup-hole geometry; the direct tapped-hole ledge remains a separate input.
2. **Cup passages:** fourØ19 mm through holes normalZ atX−215,−125,125,215 andY187.5 on the left, mirrored on the right. Nominal hole-to-Y-edge ligament 12.5−9.5=3 mm. P04JRC — moving cup lower bodyØ18 passes through; flangeØ22 rests on the ledge top with 1.5 mm radial bearing width. Four P04JRFB — fixed receiver bodies attach under each ledge.
3. **Seam-beam seat:** retain source-associated DIN74 TypeF M8 countersink axisX0,Y187.5, mirroredright, machined through the 3 mm ledge and 3 mm removable beam-base stack. Source boreØ9.00…9.22 mm, mouthØ18.25…18.58 mm, nominal 90°; project seat angle 90°±1°. P04LJFL — retained seat source/dimension chain records its actual C160 profile and depth. The nearest cup axisX125 gives 125−11−9.29=104.71 mm between cup-flange envelope and maximum countersink mouth. The correspondingØ19 ledge hole gives 125−9.5−9.29=106.21 mm material separation to that mouth.
4. **Assembly:** weld the fixed receiver bodies under the ledge before fitting the caps/panels, preserving the central beam seat. Machine the paired beam/ledge counterseats using the existing matched-seat construction. Bench-form panel standoffs with manufacturer tools, then fit the recessed panel so its eight cups enter these holes and fixed cavities. Actual formed-nose gap, thread overlap and screw-release travel follow P04JPNR — assembly criteria.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed deck interface part | PASS | [1, 1, 1, 1] | count |
| Source stock bounds | PASS | [[-300.0, 300.0], [175.0, 200.0], [767.0, 770.0]] | mm |
| Source clearance diameter 19 mm | PASS | [[-215.0, 187.5], [-125.0, 187.5], [125.0, 187.5], [215.0, 187.5]] | mm |
| Nominal45-degree cone half-angles | PASS | [45.0] | degrees |

## Sources — online

1. Weldable steel plate stock family — supplier reference.

## References — local

120. [Raised deck upright top cap](<p04jcp-j-deck-upright-top-cap.md>) — library entry 120.
127. [Fixed recessed-cup receiver](<p04jrfb-j3f-recessed-captive-fixed-receiver-body.md>) — library entry 127.
