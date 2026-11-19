THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# motenergy pair and adjustment frame j3f

1. **Library number:** 42.
2. **Type:** group.
3. **CAD file:** [motenergy-pair-and-adjustment-frame-j3f.dwg](<motenergy-pair-and-adjustment-frame-j3f.dwg>).
4. **DWG SHA-256:** `b2b052a2701eebbfaa654c066eef4bb877a2c5e533d6e5d9ca6f9282f31a229d`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Date: 12 November 2026. CAD input sheet; custom proposal. Group: drive. Route: ME0907. Quantity: 2.

### Geometry and provenance

Material proposal steel plate. Carry exact source motor face holes; include adjustment feature for the route chain centres.

### Units and local datum

Units: mm. Datum A: motor contact face; B: output shaft axis; C: chain-plane reference.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates C005 motor and P03 chassis support; use selected inch hole group with drawing-specified engagement and fastening stack.

### Space and access

Keep fan inlet, outlet, terminal access and tool movement through full adjustment.

### Custom construction

Cut, drill/machine adjustment, deburr, finish contact face and coat protected areas.

### Dimensioned structural proposal variant S — 13 November 2026

**PROPOSAL VARIANT; no design selection.** Units:mm. Geometry below is proposed unless expressly identified as a source dimension. Datum/placement uses existing X forward,Y left,Z up and layout-proposals.md. Proposed steel thicknesses/sections require the named joint/load checks.

Motor variant S: steel 240 u×240 v×10 plate, motor centreu=v=0, shaft along face normal. Reviewed local source 0 JWT.301.073 in ../cad/checks/component-results/component-led-2026-11-12/c 005-build-01/source/coordinator-review.md gives outer cardinal 3/8-16 group PCD 149.2: axes(±74.6,0),(0,±74.6), depth 18; inner 5/16-18 group PCD 106.4 at 45°: axes(±37.618,±37.618), depth 15. Use outer group as this variant's proposed fastening group: fourØ10.5 clearance bores, actual screw engagement determined from 10 mm plate/washer stack and 18 mm source depth. Source pilotØ114.3 +0/−0.05 projects 3.2; proposed plate clearance apertureØ115 is non-locating. Propose source pilot locating fit as separate precision alternative, with actual tolerance specified on drawing. Do not drill both groups if clearance aperture removes inner group: inner-axis radius 53.2 lies inside 57.5 aperture radius, so inner group cannot be used with this through-aperture proposal.

Adjustment proposal: fourØ11×41 overall vertical slots with end-centres 30 apart at plate-lo ca lu±100, v−50/+50; usable motor-centre translation 30 mm. Nominal motor-centre assembly Z 353 gives plate bounds 233…473 and sourceØ201 motor low 252.5; vertical slide±15 changes motor low 237.5…267.5, preserving motor≥233. Plate low at lower travel 218 violates structural boundary: trim lower 15 mm or move nominal motor centre to 368 and revise backbone axes. **Boundary-preserving variant:** nominal centre Z 368, travel±15, plate low 233…263 and top 473…503; motor low 252.5…282.5. P03 fixed joint axes then X±100,Z 318/418 for nominal plate; corresponding backbone must span at least Z 298…438 with 20 mm edge land. P03M backbone 240×180 mounted Z 283…463 meets these rows. Slots are custom adjustment geometry, not source motor holes. Chain path/length defines final nominal centre and adjustment sufficiency.

### J frame source-screw head envelope

1. **Proposed plate placement:** retain the local 240×240×10 mm plate. Assembly axes are X forward, Y left and Z up. For local in-plane coordinates (u,v), left placement is X = −30+u, Z = 430+s+v mm, with s = −15…+15 mm adjustment and plate Y = 115…125 mm. Right placement uses X = 180+u, the same Z equation and plate Y = −125…−115 mm. These are the existing J motor/frame poses from the combined electrical installation.
2. **Top mounting-axis sweep:** source outer screw axes are cardinal points of the 149.2 mm bolt circle. The top source axis has local (u,v) = (0,74.6) mm. Its assembly Z range is 430−15+74.6 = 489.6 mm through 430+15+74.6 = 519.6 mm. Left X is −30 mm; right X is 180 mm. Each top axis therefore enters the raised rail's Z = 500…540 mm band during adjustment.
3. **Available head space:** the left plate outer face is Y = 125 mm and rail inner face is Y = 130 mm. The intervening 5 mm backbone has the source-head clearance capsule. For the screw-head sweep overlapping the rail, the total washer-plus-head protrusion from the moving plate must be at most 130−125 = 5 mm. Right-side coordinates mirror Y. Check actual head, washer, installation tool and adjustment envelopes against this limit.
4. **Flush-seat proposal for source research:** a countersunk 3/8-16 UNC screw can place its outer head face on the plate face Y = 125 mm, using a source-matched cone fully contained in the 10 mm plate. Source head diameter, included angle, actual/theoretical cone dimensions and length datum define that seat. Let the Ø10.5 mm through bore meet a proposed countersink mouth diameter D at angle α. Nominal geometric cone depth is (D−10.5)/(2 tan(α/2)) mm; remaining plate section is 10 mm minus that depth. Use the actual source transition radii and head profile to complete the contact geometry.
5. **Nominal entry illustration:** for a proposed overall-head length of 1 inch = 25.4 mm and a head seated flush in the 10 mm plate, nominal entry beyond the motor contact face is 25.4−10 = 15.4 mm. Against the source 18 mm mounting-hole depth, nominal tip-to-depth margin is 18−15.4 = 2.6 mm. Actual length tolerance, source head-length datum, full threads and thread-end form accompany this calculation. The source screw family and property class are being researched.
6. **Source basis and status:** source outer 3/8-16 UNC pattern and 18 mm depth come from C005 — Motenergy ME0907, outline 0JWT.301.073. Plate, motor travel and rail poses are discussion proposals already recorded in the linked installation. The 5 mm head-space limit and 489.6…519.6 mm axis sweep are calculated from those inputs. The flush seat is a construction proposal.


### Corrected ASME reference and project machining seat

1. **Source screw:** C161 — ASME B18.3 Table 8 flat-head 3/8-16×1 in, alloy-steel ASTM F835 proposal. Maximum A = 19.8374 mm is the theoretical sharp 82° countersink flush reference (Note 11); separate A minimum is 18.288 mm. Actual head-top diameter is determined from the supplied profile. The earlier label “actual maximum head diameter” and source-radius clearance claim are corrected. Reference H = 5.9436 mm, bearing cone 82° ±2°, transition diameter F ≤10.287 mm and overall length 24.638…25.400 mm retain their source labels.
2. **Source gage:** use the flat lapped-sharp-edge, straight GP bore 16.5608…16.5862 mm and ≥60 HRC tool-steel gage. Head top must lie 1.2700…2.2352 mm above the flat gage top plane. This is the Mandatory Appendix II Figure II-1 datum; gaging uses the straight bore and its sharp edge.
3. **Project seat:** retain Ø10.5 mm clearance bore and mouth Ø20.20 ±0.10 mm in the 10 mm plate. Proposed machining angle is 82° ±1°; this is a project tolerance, separate from the source head's 80°…84° range. Nominal ideal depth is (20.20−10.50)/(2 tan 41°) = 5.579287 mm, leaving 4.420713 mm section. Project limit mouth 20.30/angle 81° gives depth (20.30−10.50)/(2 tan 40.5°) = 5.737163 mm, leaving 4.262837 mm. The earlier 80° depth 5.839593 mm is a wider-angle sensitivity from the screw range, not the proposed seat tolerance.
4. **Constructed profile versus receiving:** sharp reference r(z) = 9.9187 − z tan 41°. A matching ideal 82° cone at nominal mouth gives constructed recess (20.20−19.8374)/(2 tan 41°) = 0.208562 mm. This is an ideal-profile calculation. Actual head rounding/truncation, transition and conical contact determine finished recess. Require the actual gage-compliant screw and machined seat to satisfy inspected 0 ≤ρ≤1.0 mm recession toward the motor, with bearing contact established from their actual cone/radii. The source gage result alone does not imply that receiving interval.
5. **Conditional gage-to-seat equation:** if the same straight bearing cone of measured half-angle β contacts both the GP sharp edge and machining seat, its head recess is ρ = (D_mouth−GP)/(2 tanβ) −h_GP, where h_GP is actual protrusion above the flat GP gage. This equation applies at the actual contact sections; rounded-edge or transition contact requires the full supplied profile. Evaluate actual cone mismatch and bearing contact; the source/proposed angle intervals alone do not specify contact area.
6. **Plate ligaments and transition:** project mouth maximum 20.30 mm leaves 74.6−57.5−10.15 =6.95 mm to the Ø115 pilot aperture. Nearest slot-end separation is sqrt(25.4²+35²)−10.15−5.5 =27.59535 mm. Source maximum transition diameter 10.287 mm is 0.213 mm below the 10.5 bore, giving 0.1065 mm nominal radial clearance before bore/transition tolerances. The actual transition fillet and bore edge use their supplied profiles.
7. **Backbone/head/tool:** keep radius 10.5 mm clearance capsules over ±15 mm travel. Their 0.5813 mm radial difference from the ideal sharp reference radius 9.9187 mm is a constructed-reference comparison; actual head/capsule clearance requires the actual supplied head envelope and inspected recess. The project receiving condition is that all screw material is at or inside the plate outer face, retaining the 5 mm rail gap. Tighten motor-to-plate before installing the moving assembly. Proposed 10 mm OD straight tool at the lowered upper axis Z489.6 reaches Z494.6,5.4 mm below rail underside 500; actual handle/key insertion remains the tool input. Frozen motor 430±15/frame 500/tray 575/deck 770 and both Kelly X−30/Y-mirror poses remain unchanged.
8. **Entry and full threads:** inspectedρ0…1.0 mm and source overall length 24.638…25.400 mm give penetration L−10+ρ =14.638…16.400 mm, with minimum physical-depth margin 18−16.4 =1.600 mm. This is a conditional receiving calculation. Actual full-thread start, point incomplete thread, motor entry chamfer and bottom runout determine full engagement; source 18 mm drawing depth is the physical-depth datum. Source socket and hex alternatives remain in the retained source report; their head heights exceed the 5 mm gap.

Source: seat-gage and receiver source extraction.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| Raised frame, fixed backbones and moving motor plates | 1 | [motor adjustment plates and frame j3f](<motor-adjustment-plates-and-frame-j3f.md>) — 43 | `edcea5efb3558529584e018a61871639d25a403d4d254c3a7a3945bce58b971a` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| C005 — Left ME0907 source mechanical reference; keywayup | 1 | [Motenergy ME0907 motor](<../parts/electrical/motenergy-me0907-mechanical-reference.md>) — 106 | `6c9c1505c3beb528b10cb27c5a2af0406c16e00a2f766cfaa27bed8c132d1a33` | `{"position_mm":[30.0,430.0,115.00000000000003],"scale":[1.0,1.0,1.0],"rotation_radians":-1.2246467991473532e-16,"normal":[0.0,1.0,6.123233995736766e-17]}` |
| C005 — Right ME0907 source mechanical reference; keywayup | 1 | [Motenergy ME0907 motor](<../parts/electrical/motenergy-me0907-mechanical-reference.md>) — 106 | `6c9c1505c3beb528b10cb27c5a2af0406c16e00a2f766cfaa27bed8c132d1a33` | `{"position_mm":[180.0,430.0,115.00000000000003],"scale":[1.0,0.9999999999999999,1.0],"rotation_radians":0.0,"normal":[0.0,-1.0,6.123233995736766e-17]}` |

## Sources — online

1. ME0907 outline drawing0JWT.301.073.
2. Kelly KLS-N user manual v2.11.
3. Kelly KLS-N wiring diagram, §3.2.2, p.14.
4. ME0907 specification and drawing downloads.
5. Kobe EV ME0907 data.
6. Motenergy ME0907 family page.
7. EV Europe ME0907 specification.
8. Kelly ME0907 page.
9. QS Motor KLS7240N offer.
10. KellyController.eu ME0907 offer.
11. Square steel tube stock family — supplier reference.
12. Weldable steel plate stock family — supplier reference.

## References — local

43. [motor adjustment plates and frame j3f](<motor-adjustment-plates-and-frame-j3f.md>) — library entry 43.
106. [Motenergy ME0907 motor](<../parts/electrical/motenergy-me0907-mechanical-reference.md>) — library entry 106.

## Views

1. [motenergy pair and adjustment frame j3f isometric](<../images/motenergy-pair-and-adjustment-frame-j3f-isometric.png>).
