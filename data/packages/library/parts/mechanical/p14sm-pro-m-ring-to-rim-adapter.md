THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Sumitomo PRO-M ring-to-rim adapter

1. **Library number:** 174.
2. **Type:** part.
3. **CAD file:** [p14sm-pro-m-ring-to-rim-adapter.dwg](<p14sm-pro-m-ring-to-rim-adapter.dwg>).
4. **DWG SHA-256:** `78b8bb89ea71ef07b7733c4d65d0d4d39736a869075aad6509c823085dd7efd9`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Sumitomo PRO-M ring-to-rim adapter — P14SM.

**Design status:** Discussion construction proposal.

## Technical specification

Date: 12 November 2026. CAD input sheet; custom proposal. Group: drive. Route: Sumitomo PRO-M. Quantity: 2.

### Geometry and provenance

Source ring sideØ145 h7 pilot/12×M5 pattern with G-140 contact; rim side4×100/centre60. Complementary adapter fit follows exact gearmotor drawing.

### Units and local datum

Units: mm. Datum A: ring axis; B: ring mating face; C: rim seating face.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates C010 and C003/C004. Record ring versus rim hardware separately; preserve O-ring interface.

### Space and access

Reserve bolt insertion and axle/tyre offset clearance; check body placement against axle-height condition.

### Custom construction

Turn concentric interfaces; machine source seal/contact features; drill variant patterns.

### Source-template transfer — 13 November 2026

**Rim-side dimensioned proposal:** localu/v in rim-contact plane centred on wheel axis, mm. Source4×100 pattern supplies radius50 mm. With proposed phase angleθ, hole axes are(50cos(θ+90k),50sin(θ+90k)),k=0…3; θ is a layout proposal tied to actual output-pattern/socket clearance. Atθ=0 the template axes are(±50,0),(0,±50). Source centre holeØ60 is the mating rim dimension; complementary hub-register fit/tolerance and pilot length require the exact mating requirement. Knott spherical seat and Keiyama contact-profile record retain separate hardware.

**Axial chain fields:** ring/donor/shaft mating faceB; rim-contact faceC; signedB→C offset t; wheel-register length/fit; bolt under-seat datum and usable full-thread limits; exact source output-pattern diameter/phase/thread depth; full seal-groove/contact shape when applicable. Calculate installed wheel plane only after t and the local-to-assembly transform are recorded. Rim ET0 supplies the nominal rim centre relation, not a custom adapter thickness. Use M03 seated-bolt interval method and keep housing, ring and wheel fasteners separate.

### Modelable relieved cup adapter proposal

Datum B is the source ring-bolt mouth/seating plane, n = 0; positive n points toward the wheel. The retained manufacturer outline side-view witnesses place the Ø123 central-member frontmost face at n = +28 mm, so hBoss = 28 mm. Detail A places the groove near edge 19.4 mm behind B and gives groove width 4.1 mm. The reviewed source datum mapping identifies the view, model and witness endpoints. hBoss is a printed source span; gNear is calculated from the printed far-edge span minus groove width.

**Proposed constructor:** one steel cylinderOD160. Complementary rear socketØ145 H7 extendsn−lS…0, where lS=gNear+wGroove+3 and3 mm is a proposed sealing-land margin. The source h7 male ring carries its own circumferential groove/O-ring; custom adapter supplies a smooth cylindrical contact land. No duplicate groove is machined. This variant uses source groove width 4.1 mm and the signed groove coordinates recorded above.

FromB forward, relieve the central member with boreØ124 to depthq=hBoss+2; the1 mm diametral and2 mm axial gaps are proposed assembly clearances. Keep a20 mm front web fromnq…q+20; rim faceC=q+20 and signedB→C offset is+hBoss+22. This replaces the earlier20 mm offset that could intersect the central projection. Using source hBoss = 28 mm gives proposed relief depth q = 30 mm and rim face C = +50 mm. Source groove geometry gives rear socket length lS = 19.4 + 4.1 + 3 = 26.5 mm. The adapter rear end is n = −26.5 mm, inside the source pilot span 27.5 mm, leaving a calculated 1.0 mm axial margin at that span endpoint. Overall proposed blank axial extent is 76.5 mm, from n = −26.5 to +50 mm. The 2/3/20 mm clearances, margin and front web are proposed constructor inputs.

Source twelveM5 holes lie onØ134 PCD, phase0; axes(67.0cos30k,67.0sin30k), k0…11. Through boresØ5.5 pass fromC toB. Recess source ring-bolt heads fromC with proposed counterboreØ9 depth6; this recess lies entirely in the20 mm front web. Required under-head length is(C−6)+eRing plusactualwasher correction, where source joint engagement eRing and12 mm tapped-depth bottomclearance are checked separately. With current C = 50 mm and counterbore depth 6 mm, the proposed head seating plane is n = +44 mm. A 55 mm under-head length gives 11 mm nominal thread entry and 1 mm to the source 12 mm tapped-depth limit before washer, tip and runout corrections. This is a dimensional bolt-length illustration; actual source-compatible hardware and full-thread engagement define the final stack.

Rim holes are fourM12×1.5 onPCD100, proposed phase15° to the source twelve-hole rays. Threaded depth12 fromC is a proposed engagement evaluation input with8 mm web beneath it; exact required engagement uses M03. Rim registerØ60 complementary fit has proposed4 mm projection fromC. Knott/Keiyama retain separate actual seats. ProposedOD160 is below the housing bolt PCD, but actual stationary-head/socket and rim-barrel envelopes must be checked at the exact signed source housing-face offset. The direct coaxial motor route retains its below-axis conflict.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed adapter body | PASS | [1, 1, 1, 1] | count |
| Coaxial nominal diameter 160 mm | PASS | [[0.0, -1.622657008870243e-15]] | mm |
| Coaxial nominal diameter 145 mm | PASS | [[0.0, 0.0]] | mm |
| Coaxial nominal diameter 124 mm | PASS | [[0.0, 1.83697019872103e-15]] | mm |
| Coaxial nominal diameter 60 mm | PASS | [[0.0, 3.061616997868383e-15]] | mm |
| Twelve source ring bore axes | PASS | [[-67.0, 8.143901214329898e-15], [-58.02370205355739, 33.49999999999999], [-58.023702053557386, -33.50000000000001], [-33.50000000000003, -58.02370205355737], [-33.499999999999986, 58.02370205355739], [-1.2307700331430898e-14, -67.0], [4.102566777143633e-15, 67.0], [33.50000000000001, -58.023702053557386], [33.50000000000001, 58.023702053557386], [58.02370205355737, -33.50000000000003], [58.02370205355739, 33.49999999999999], [67.0, -6.123233995736744e-17]] | mm |
| Twelve proposed counterbore axes | PASS | [[-67.0, 1.0899356512411444e-14], [-58.02370205355739, 33.49999999999999], [-58.023702053557386, -33.50000000000001], [-33.50000000000003, -58.02370205355737], [-33.499999999999986, 58.02370205355739], [-1.2307700331430898e-14, -67.0], [4.102566777143633e-15, 67.0], [33.50000000000001, -58.023702053557386], [33.50000000000001, 58.023702053557386], [58.02370205355737, -33.50000000000003], [58.02370205355739, 33.49999999999999], [67.0, 2.6942229581241772e-15]] | mm |
| Four M12 nominal reference axes; phase15 degrees | PASS | [[-48.29629131445341, -12.94095225512604], [-12.940952255126042, 48.29629131445341], [12.940952255126014, -48.29629131445342], [48.29629131445341, 12.940952255126037]] | mm |
| Socket, relief, bore-bottom, head-seat, rim-face and register planes | PASS | [-26.5, 0.0, 30.0, 38.0, 44.0, 50.0, 54.0] | mm |

## Sources — online

1. Knott rim listing.
2. Gearmotor installation manualDM1801E.
3. sumitomo exact interfaces.
4. Sumitomo smartris product specifications.
5. 2024 Sumitomo catalog.
6. servo-drive manual DM1802E, brake and STO sections.
7. Weldable steel plate stock family — supplier reference.

## References — local

215. [Sumitomo PRO-M CH54065G10 gearmotor](<../electrical/sumitomo-pro-m-ch54065.md>) — library entry 215.
