THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Sumitomo PRO-L ring-to-rim adapter

1. **Library number:** 173.
2. **Type:** part.
3. **CAD file:** [p14sl-pro-l-ring-to-rim-adapter.dwg](<p14sl-pro-l-ring-to-rim-adapter.dwg>).
4. **DWG SHA-256:** `69f61f21dbcade1d082efefdca8807428740779a2dfb550508484db3e7d53521`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Sumitomo PRO-L ring-to-rim adapter — P14SL.

**Design status:** Discussion construction proposal.

## Technical specification

Date: 12 November 2026. CAD input sheet; custom proposal. Group: drive. Route: Sumitomo PRO-L. Quantity: 2.

### Geometry and provenance

Source ring sideØ182 h7/12×M6 andAS568-261 contact; rim side4×100/centre60. Material/thickness are proposal drawing inputs.

### Units and local datum

Units: mm. Datum A: ring axis; B: ring contact face; C: rim face.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates C011 and C003/C004 with variant-specific hardware and complementary pilot fit.

### Space and access

Check ring fasteners, seal assembly, wheel offset and inward gearmotor placement.

### Custom construction

Turn interfaces; machine seal contact; drill source ring and rim patterns.

### Source-template transfer — 13 November 2026

**Rim-side dimensioned proposal:** localu/v in rim-contact plane centred on wheel axis, mm. Source4×100 pattern supplies radius50 mm. With proposed phase angleθ, hole axes are(50cos(θ+90k),50sin(θ+90k)),k=0…3; θ is a layout proposal tied to actual output-pattern/socket clearance. Atθ=0 the template axes are(±50,0),(0,±50). Source centre holeØ60 is the mating rim dimension; complementary hub-register fit/tolerance and pilot length require the exact mating requirement. Knott spherical seat and Keiyama contact-profile record retain separate hardware.

**Axial chain fields:** ring/donor/shaft mating faceB; rim-contact faceC; signedB→C offset t; wheel-register length/fit; bolt under-seat datum and usable full-thread limits; exact source output-pattern diameter/phase/thread depth; full seal-groove/contact shape when applicable. Calculate installed wheel plane only after t and the local-to-assembly transform are recorded. Rim ET0 supplies the nominal rim centre relation, not a custom adapter thickness. Use M03 seated-bolt interval method and keep housing, ring and wheel fasteners separate.

### Modelable relieved cup adapter proposal

Datum B is the source ring-bolt mouth/seating plane, n = 0; positive n points toward the wheel. The retained manufacturer outline side-view witnesses place the Ø155 central-member frontmost face at n = +30 mm, so hBoss = 30 mm. Detail A places the groove near edge 28.0 mm behind B and gives groove width 4.8 mm. The reviewed source datum mapping identifies the view, model and witness endpoints. hBoss is a printed source span; gNear is calculated from the printed far-edge span minus groove width.

**Proposed constructor:** one steel cylinderOD200. Complementary rear socketØ182 H7 extendsn−lS…0, where lS=gNear+wGroove+3 and3 mm is a proposed sealing-land margin. The source h7 male ring carries its own circumferential groove/O-ring; custom adapter supplies a smooth cylindrical contact land. No duplicate groove is machined. This variant uses source groove width 4.8 mm and the signed groove coordinates recorded above.

FromB forward, relieve the central member with boreØ156 to depthq=hBoss+2; the1 mm diametral and2 mm axial gaps are proposed assembly clearances. Keep a20 mm front web fromnq…q+20; rim faceC=q+20 and signedB→C offset is+hBoss+22. This replaces the earlier20 mm offset that could intersect the central projection. Using source hBoss = 30 mm gives proposed relief depth q = 32 mm and rim face C = +52 mm. Source groove geometry gives rear socket length lS = 28.0 + 4.8 + 3 = 35.8 mm. The adapter rear end is n = −35.8 mm, inside the source pilot span 38 mm, leaving a calculated 2.2 mm axial margin at that span endpoint. Overall proposed blank axial extent is 87.8 mm, from n = −35.8 to +52 mm. The 2/3/20 mm clearances, margin and front web are proposed constructor inputs.

Source twelveM6 holes lie onØ170 PCD, phase0; axes(85.0cos30k,85.0sin30k), k0…11. Through boresØ6.6 pass fromC toB. Recess source ring-bolt heads fromC with proposed counterboreØ11 depth7; this recess lies entirely in the20 mm front web. Required under-head length is(C−7)+eRing plusactualwasher correction, where source joint engagement eRing and12 mm tapped-depth bottomclearance are checked separately. With current C = 52 mm and counterbore depth 7 mm, the proposed head seating plane is n = +45 mm. A 55 mm under-head length gives 10 mm nominal thread entry and 2 mm to the source 12 mm tapped-depth limit before washer, tip and runout corrections. This is a dimensional bolt-length illustration; actual source-compatible hardware and full-thread engagement define the final stack.

Rim holes are fourM12×1.5 onPCD100, proposed phase15° to the source twelve-hole rays. Threaded depth12 fromC is a proposed engagement evaluation input with8 mm web beneath it; exact required engagement uses M03. Rim registerØ60 complementary fit has proposed4 mm projection fromC. Knott/Keiyama retain separate actual seats. ProposedOD200 is below the housing bolt PCD, but actual stationary-head/socket and rim-barrel envelopes must be checked at the exact signed source housing-face offset. The direct coaxial motor route retains its below-axis conflict.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed adapter body | PASS | [1, 1, 1, 1] | count |
| Coaxial nominal diameter 200 mm | PASS | [[0.0, -2.192117770473762e-15]] | mm |
| Coaxial nominal diameter 182 mm | PASS | [[0.0, 0.0]] | mm |
| Coaxial nominal diameter 156 mm | PASS | [[0.0, 1.959434878635765e-15]] | mm |
| Coaxial nominal diameter 60 mm | PASS | [[0.0, 3.184081677783118e-15]] | mm |
| Twelve source ring bore axes | PASS | [[-85.0, 1.0348265452795134e-14], [-73.6121593216773, 42.49999999999999], [-73.61215932167728, -42.50000000000001], [-42.500000000000036, -73.61215932167727], [-42.49999999999998, 73.6121593216773], [-1.5614246689128753e-14, -85.0], [5.204748896376251e-15, 85.0], [42.50000000000001, -73.61215932167728], [42.50000000000001, 73.61215932167728], [73.61215932167727, -42.500000000000036], [73.6121593216773, 42.49999999999999], [85.0, -6.123233995736766e-17]] | mm |
| Twelve proposed counterbore axes | PASS | [[-85.0, 1.3164953090834047e-14], [-73.6121593216773, 42.49999999999999], [-73.61215932167728, -42.50000000000001], [-42.500000000000036, -73.61215932167727], [-42.49999999999998, 73.6121593216773], [-1.5614246689128753e-14, -85.0], [5.204748896376251e-15, 85.0], [42.50000000000001, -73.61215932167728], [42.50000000000001, 73.61215932167728], [73.61215932167727, -42.500000000000036], [73.6121593216773, 42.49999999999999], [85.0, 2.7554552980815448e-15]] | mm |
| Four M12 nominal reference axes; phase15 degrees | PASS | [[-48.29629131445341, -12.94095225512604], [-12.940952255126042, 48.29629131445341], [12.940952255126014, -48.29629131445342], [48.29629131445341, 12.940952255126037]] | mm |
| Socket, relief, bore-bottom, head-seat, rim-face and register planes | PASS | [-35.8, 0.0, 32.0, 40.0, 45.0, 52.0, 56.0] | mm |

## Sources — online

1. Knott rim listing.
2. Gearmotor installation manualDM1801E.
3. sumitomo exact interfaces.
4. Sumitomo smartris product specifications.
5. 2024 Sumitomo catalog.
6. servo-drive manual DM1802E, brake and STO sections.
7. Weldable steel plate stock family — supplier reference.

## References — local

214. [Sumitomo PRO-L CH54527G10 gearmotor](<../electrical/sumitomo-pro-l-ch54527.md>) — library entry 214.
