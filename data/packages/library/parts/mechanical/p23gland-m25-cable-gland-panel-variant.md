THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# M25 gland insert carrier

1. **Library number:** 195.
2. **Type:** part.
3. **CAD file:** [p23gland-m25-cable-gland-panel-variant.dwg](<p23gland-m25-cable-gland-panel-variant.dwg>).
4. **DWG SHA-256:** `f32c0fc4cf3f320b0714b853f8efe5a0972f691bdb491abecb9625bafe12cad8`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** M25 gland insert carrier — P23Gland.

**Design status:** Discussion construction proposal.

## Technical specification

Date: 13 November 2026. Discussion inventory input. Route: main cable entry. Quantity: one per distinct geometry; repeated identical shapes use instances.

### Geometry and provenance

Panel entry uses the ESKV25 M25 thread interface. Panel thickness, gasket seat, gland wrench clearance and cable bend path follow actual selected enclosure wall and cable route.

### Units and local datum

Millimetres. Datum A: outside panel face. Datum B: device or gland opening axis. Record the panel edge datum and local-to-assembly transform for each opening centre.

### Mating interfaces and hardware

Parent family: P23. Connection: E01/E02. Measure the corresponding mating parts before fabrication.

### Installation and access

Keep gland-nut and locknut tools, wall-seal seating and cable strain relief accessible on both panel faces.

### CAD measurements

Record gland entry axis, thread/through-hole diameter, wall thickness, seal/locknut stack, installed projections and cable bend clearance.

### Construction and dimension-chain closure — 13 November 2026

**Wall-stack fields:** C099 source M25×1.5, external mounting thread length10 mm; proposed panel3 mm. Calculated remaining axial thread allocation is10−3=7 mm before wall seal and locknut engagement. Record seal thickness tG and locknut usable thread interval; usable allocation becomes7−tG mm before runout. Through-hole diameter follows exact accessory drawing/tolerance; a tapped-panel alternative uses the specified thread instead of a fabricated clearance size. Record AF29 tool sweep and actual cable bend envelope at the entry.

### Removable thin-insert construction proposal

1. **Parent geometry reuse:** P23 — functional panel family supplies the proposed 100 × 140 × 3 mm carrier outline and four M6 support axes. This carrier uses corner radius 3 mm and support holes Ø6.5 mm at (u,v) = (±40,±60) mm.
2. **Common datum:** finished gland-insert front n = 0; carrier metal occupies n = −4.5…−1.5 mm. Carrier outline u = ±50 mm, v = ±70 mm. The P23GThin — 1.5 mm insert lies n = −1.5…0 mm.
3. **Carrier openings:** one centred Ø40 mm through passage for the locknut, plus four Ø4.5 mm insert holes at (u,v) = (±24,±24) mm. The source EMUG 25 LG collar envelope is Ø36 mm, giving nominal radial clearance 2 mm to that collar through the proposed opening. The source SW32 mm regular-hexagon reference has corner diameter 36.9504 mm, giving 1.5248 mm radial passage clearance; actual nut corners control the supplied-part fit.
4. **Nominal ligaments:** insert-hole to central carrier opening = √(24² + 24²) − 2.25 − 20 = 11.6911 mm. Carrier M6 support-hole to straight edge = 10 − 6.5/2 = 6.75 mm.
5. **Stack correction:** the earlier direct 3 mm panel branch gives 3 + 2 + 6 = 11 mm against source 10 mm thread. The removable 1.5 mm insert branch gives 9.5 mm nominal stack. Its exact hardware, source torque conditions and actual-length criterion are in P23GThin. Both branches retain their stated construction inputs.
6. **Construction:** cut the rounded carrier outline, central Ø40 mm passage, four Ø4.5 mm insert holes and four Ø6.5 mm support holes. Bench-assemble the gland and mounting accessories on the thin insert, then bolt the insert onto the carrier.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed M25 gland insert carrier | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-50.0, 50.0], [-70.0, 70.0], [-4.5, -1.5]] | mm |
| Source-sheet hole group 1 | PASS | [[0.0, 0.0]] | mm |
| Source-sheet hole group 2 | PASS | [[-24.0, -24.0], [-24.0, 24.0], [24.0, -24.0], [24.0, 24.0]] | mm |
| Source-sheet hole group 3 | PASS | [[-40.0, -60.0], [-40.0, 60.0], [40.0, -60.0], [40.0, 60.0]] | mm |
| Outside corner radius | PASS | [3.0] | mm |

## Sources — online

1. Exact manufacturer data sheet.
2. manufacturer data sheet.
3. manufacturer data sheet.
4. WISKA mounting instruction.
5. Kelly KLS-N wiring diagram, §3.2.2, p.14.
6. Exact AHDBM04-24-91PN drawing.
7. c040 amphenol ahdbm04 24 91pn receptacle.
8. Schneider exact button.
9. Schneider exact reset button.

## References — local

196. [Removable M25 gland insert](<p23gthin-removable-m25-gland-insert.md>) — library entry 196.
