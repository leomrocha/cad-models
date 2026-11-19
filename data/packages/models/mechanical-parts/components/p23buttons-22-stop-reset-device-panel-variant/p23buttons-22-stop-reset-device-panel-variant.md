THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Schneider stop/reset keyed-cutout insert

1. **Library number:** 194.
2. **Type:** part.
3. **CAD file:** [p23buttons-22-stop-reset-device-panel-variant.dwg](<p23buttons-22-stop-reset-device-panel-variant.dwg>).
4. **DWG SHA-256:** `659682d7023658b7455aaa4813aa0d75197f7c13932115949beb3f29bdda90ec`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Schneider stop/reset keyed-cutout insert — P23Buttons.

**Design status:** Discussion construction proposal.

## Technical specification

Date: 13 November 2026. Discussion inventory input. Route: stop/reset controls. Quantity: one per distinct geometry; repeated identical shapes use instances.

### Geometry and provenance

Schneider XB5AA31 recommended panel opening: Ø22.5 mm; drawing alternative Ø22.3 +0.4/−0 mm. Source: retained exact C050 feature bindings. Apply the exact XB5AS8445 opening, panel-thickness and rear contact-block drawing to the stop-device position separately.

### Units and local datum

Millimetres. Datum A: outside panel face. Datum B: device or gland opening axis. Record the panel edge datum and local-to-assembly transform for each opening centre.

### Mating interfaces and hardware

Parent family: P23. Connection: E19. Measure the corresponding mating parts before fabrication.

### Installation and access

Keep actuator operation, retaining-collar tools and rear contact-block removal accessible.

### CAD measurements

Record each button opening centre, anti-rotation feature, panel thickness, front actuator projection and rear contact-block envelope.

### Operator insert proposal

Use separate 3 mm operator insert with 100×140 mm candidate outline and four support axes(±40,±60) mm in faceX/Z. Candidate device centres(0,+25) for stop and(0,−25) for reset are custom placement proposals. Apply exact stop and reset apertures separately; verify actuator sweep and rear contact-block/retainer envelopes against 50 mm centre separation before drilling. Support wiring on removable rear clips so insert extraction preserves contact labels.

### Exact device cutouts — retained-drawing transfer

1. **Input and method:** Schneider XB5AS8445 data sheet dated 19 September 2016, page 4, and XB5AA31 data sheet dated 12 November 2026, page 7, show the same panel cutout detail. Root visually inspected both pages. Sources and unchanged-original hashes are registered as SCH049-PDF and SCH050-PDF. The stop drawing original and reset drawing original supply the dimension leaders.
2. **Plate constructor proposal:** retain the 100 × 140 × 3 mm metal insert. Local u spans −50…50 mm, v −70…70 mm, n −3…0 mm; outside operating face is n=0. Four proposed Ø6.6 mm support holes, normal n, are centred (u,v)=(±40,±60) mm. Source device positions retain stop (0,+25) mm and reset (0,−25) mm as project placements.
3. **Circular opening source:** each device uses recommended finished diameter 22.5 mm. Both drawings also give diameter 22.3 mm with +0.4/−0.0 mm tolerance, range 22.3–22.7 mm. Use the 22.5 mm recommendation for the proposed nominal constructor; retain that source diameter interval for the finished-opening record.
4. **Lug recess source:** notch width 3.2 mm with +0.2/−0.0 mm tolerance; overall vertical cutout extent 24.1 mm with +0.4/−0.0 mm tolerance; source notch-corner radius at most 0.8 mm. Orient each key recess toward +v. For nominal circle diameter 22.5 mm and overall 24.1 mm, the calculated notch-top coordinate is local v_device+24.1−11.25=v_device+12.85 mm. Its nominal side walls are u_device±1.6 mm. Join this recess to the circular opening and retain the source corner-radius limit. Stop notch top is v37.85 mm; reset notch top is v−12.15 mm. Source width/height intervals remain beside the nominal shape.
5. **Panel and spacing conditions:** both exact data sheets specify panel clamping thickness 1–6 mm. Proposed plate thickness 3 mm lies in that interval. Screw-clamp/plug-in array minimum vertical centre spacing is40 mm and horizontal spacing 30 mm. Proposed vertical spacing 50 mm exceeds the source vertical minimum by10 mm. The source mounting note recommends C170 — Schneider ZB5AZ902 anti-rotation plate for emergency-stop heads.
6. **Calculated nominal material:** support-hole edge ligament is10−3.3=6.7 mm. Each circular opening has 38.75 mm material to a side edge. Upper stop-notch top leaves 70−37.85=32.15 mm to the plate top. Reset circle bottom is−36.25 mm, leaving 33.75 mm to the plate bottom. The vertical opening-to-opening gap at u=0 is13.75−(−12.15)=25.9 mm. These calculations cover plate openings and the stated source array spacing.
7. **Fabrication and installation:** cut the plate outline and six through openings including the two lug recesses, finish the edges and inspect the source cutout dimensions. Orient stop/reset bodies to match their source terminal faces and the retained local u/v axes; use their supplied mounting hardware and the source anti-rotation accessory option. The F05 support route retains its separate shoe/spacer stack and device/harness access conditions.

### Anti-rotation accessory installation

Schneider ZB5AZ902 source interface, FAQ FA110722, gives the stop-head retaining order: inside panel face, metal anti-rotation plate, plastic ring nut. The proposed panel inside face is n=−3 mm; the source accessory and retaining nut follow that face. The head cutout dimensions above belong to the exact device panel drawing.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Schneider stop/reset keyed-cutout insert | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-50.0, 50.0], [-70.0, 70.0], [-3.0, 0.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-40.0, -60.0], [-40.0, 60.0], [40.0, -60.0], [40.0, 60.0]] | mm |
| Source-sheet hole group 2 | PASS | [[0.0, -25.0], [0.0, 25.0]] | mm |
| Specified notch boundary vertices | PASS | [1, 1, 1, 1, 1, 1, 1, 1] | count |

## Sources — online

1. c170 schneider zb5az902 anti rotation plate.
2. Schneider FAQ FA110722.
3. TraceParts Schneider ZB5AZ902 listing.
4. Weldable steel plate stock family — supplier reference.

## References — local

207. [Schneider XB5AA31 reset button](<../../profiles/schneider-xb5aa31-projected-profile-clearance-reference/schneider-xb5aa31-projected-profile-clearance-reference.md>) — library entry 207.
