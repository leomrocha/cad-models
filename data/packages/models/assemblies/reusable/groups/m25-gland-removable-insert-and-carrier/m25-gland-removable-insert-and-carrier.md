THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# m25 gland removable insert and carrier

1. **Library number:** 40.
2. **Type:** group.
3. **CAD file:** [m25-gland-removable-insert-and-carrier.dwg](<m25-gland-removable-insert-and-carrier.dwg>).
4. **DWG SHA-256:** `b547105412fc82478596f5b137a6a0c3b50f85040068fe13d9a4c9e2059df2c2`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Discussion construction proposal. Parent: P23Gland — cable-gland carrier. Quantity: one per standalone WISKA ESKV 25 LG 10066413 entry. All dimensions in mm.

### Source interfaces and proposed geometry

1. **Source gland:** WISKA ESKV 25 LG order 10066413, male M25 × 1.5 thread, screw-in length 10 mm and collar diameter 32 mm. Exact manufacturer data sheet.
2. **Source mounting accessories:** WISKA EADR 25 order 10062804, uncompressed thickness 2 mm, manufacturer data sheet; WISKA EMUG 25 LG order 10060773, total height 6 mm, M25 × 1.5 thread, AF32 mm and collar diameter 36 mm, manufacturer data sheet.
3. **Reason for the insert:** nominal 3 mm parent plate + 2 mm source gasket + 6 mm source nut = 11 mm; source gland thread is 10 mm. Proposed 1.5 mm insert + 2 mm uncompressed gasket + 6 mm nut = 9.5 mm, giving 0.5 mm nominal thread-length allowance. This calculation uses the uncompressed source gasket thickness.
4. **Proposed blank:** 60 × 60 × 1.5 mm steel, four corner radii 3 mm. Local u/v origin is the gland axis. Local n points outward; insert front face n = 0, metal n = −1.5…0 mm. Outline u/v = ±30 mm.
5. **Proposed gland opening:** one centred Ø26.0 mm through hole, normal n. This is a project clearance-hole proposal around the source nominal M25 thread. Nominal radial thread clearance = (26 − 25)/2 = 0.5 mm. Source Ø32 mm collar gives (32 − 26)/2 = 3 mm nominal radial coverage.
6. **Insert-fixing holes:** four Ø4.5 mm through holes at (u,v) = (±24,±24) mm. Their pattern mates the four carrier holes. Proposed insert edge ligament = 30 − 24 − 2.25 = 3.75 mm.

### Gland, gasket and locknut stack

1. **Nominal uncompressed pose:** panel front n = 0; gasket n = 0…2 mm; gland thread shoulder n = 2 mm; free thread end n = 2 − 10 = −8 mm. Locknut front contact is the insert back n = −1.5 mm; nut body extends to n = −7.5 mm. Nominal thread end projects 0.5 mm beyond that body envelope.
2. **Actual-length criterion:** supplied screw-in length L must cover actual insert thickness tP, compressed gasket thickness tG and source locknut axial envelope tN: L ≥ tP + tG + tN. Nominal source screen uses L = 10, tP = 1.5, uncompressed tG = 2 and tN = 6 mm. The nut's actual usable thread/chamfer geometry belongs to its source part.
3. **Carrier passage:** the parent carrier has a centred Ø40 mm opening around the source Ø36 mm nut envelope, giving 2 mm nominal radial clearance to that collar. A calculated regular hexagon with source 32 mm across flats has corner diameter 32/cos(30°) = 36.9504 mm; the Ø40 mm passage gives 1.5248 mm radial clearance to this hexagon reference. The supplied nut profile controls its passage fit. Assemble the gland, EADR gasket and EMUG nut on the insert at the bench, then fit the insert to the carrier. This sequence gives locknut wrench access before the carrier surrounds it.
4. **Manufacturer installation:** the WISKA ESKV mounting instruction gives fitting torque 4 N·m with EADR and cap-nut torque 4 N·m for ESKV 25. These are source guide values measured with test mandrels under EN 62444 conditions. WISKA mounting instruction.

### Insert-to-carrier fixing proposal

1. **Solid grip:** 1.5 mm insert + 3 mm carrier = 4.5 mm. Four joints use four C135 — M4 × 16 mm screws, eight C144 — M4 washers and four C150 — M4 nuts.
2. **Length criterion:** washer maximum thickness 0.9 mm each, nut maximum height 5 mm, source M4 pitch 0.7 mm and proposed exposed thread of two pitches. Required actual screw length is L ≥ G + 2 × 0.9 + 5 + 2 × 0.7 = G + 8.2 mm. Nominal G = 4.5 mm requires 12.7 mm. Proposed nominal length 16 mm gives 3.3 mm nominal arithmetic allowance.
3. **Access:** release these four screws and withdraw the gland/insert assembly outward while supporting the cable. The source locknut is accessible on the removed insert. Source gland body and cable bends use their actual installed geometry.

### Source and construction record

1. WISKA panel-mount research records the accessory identities and source dimensions.
2. P23Gland — carrier gives the mating plate, opening and hole pattern.
3. **CAD construction:** draw the rounded 60 mm square, extrude 1.5 mm, cut the central Ø26 mm bore and four Ø4.5 mm fixing holes, and preserve the named front-face datum. These are proposed manufactured dimensions.

### Finite fixing and service-space proposal

1. **M4 washer seats:** C144 — M4 washer has source maximum OD 9 mm. At fixing centres (±24,±24) mm, each washer has 30 − 24 − 4.5 = 1.5 mm clearance to each adjacent straight insert edge. The adjacent rounded-corner arc has centre (±27,±27) mm and lies in the outward quadrant. Its nearest points to the fixing centre are its endpoints, at distance √45 = 6.7082 mm; the washer-to-arc gap is therefore 6.7082 − 4.5 = 2.2082 mm. Carrier-side washers sit fully outside the central Ø40 mm opening: √1152 − 4.5 − 20 = 9.4411 mm radial material allowance.
2. **Screw pose:** insert front n = 0; front washer occupies n = 0…0.9 mm at its source thickness ceiling; the screw head bears on that washer and the screw points inward. Carrier rear n = −4.5 mm; rear washer ends at n = −5.4 mm and the source maximum-height 5 mm nut ends at n = −10.4 mm. A nominal 16 mm screw measured from bearing face n = 0.9 ends at n = −15.1 mm; nominal projection past this maximum stack is 4.7 mm. Actual screw length and washer thickness set the supplied-parts pose.
3. **Proposed tool space:** reserve a Ø16 mm cylinder at each M4 axis from n = −25…10 mm. Its radial separation from the gland axis is √1152 − 8 = 25.9411 mm; a separate proposed gland-body/tool reservation of radius 20 mm leaves 5.9411 mm plan separation. These are project tool-envelope inputs. The M4 tool radius exceeds the insert edge by 2 mm, so the surrounding carrier space remains open at each axis; fasteners are accessed individually.
4. **Assembly sequence:** clamp the removed insert, seat the EADR gasket, tighten the gland fitting using the source EADR torque condition, and fit the cap nut using its source condition. Pass the assembled nut through the carrier passage, fit the four front screws/washers and rear washers/nuts, then tighten each M4 joint with front and rear access. Removing those four joints withdraws the complete insert; cable support accompanies that movement.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P23Gland — M25 gland carrier | 1 | [M25 gland insert carrier](<../../../../mechanical-parts/components/p23gland-m25-cable-gland-panel-variant/p23gland-m25-cable-gland-panel-variant.md>) — 195 | `f32c0fc4cf3f320b0714b853f8efe5a0972f691bdb491abecb9625bafe12cad8` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P23GThin — Removable M25 thin insert | 1 | [Removable M25 gland insert](<../../../../mechanical-parts/components/p23gthin-removable-m25-gland-insert/p23gthin-removable-m25-gland-insert.md>) — 196 | `d51150c487c2fce1ae1fbc9b7cac0920e6a03da152bf4e9dbfb67d42b78d7fb3` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. Exact manufacturer data sheet.
2. manufacturer data sheet.
3. manufacturer data sheet.
4. WISKA mounting instruction.
5. Weldable steel plate stock family — supplier reference.

## References — local

195. [M25 gland insert carrier](<../../../../mechanical-parts/components/p23gland-m25-cable-gland-panel-variant/p23gland-m25-cable-gland-panel-variant.md>) — library entry 195.
196. [Removable M25 gland insert](<../../../../mechanical-parts/components/p23gthin-removable-m25-gland-insert/p23gthin-removable-m25-gland-insert.md>) — library entry 196.

## Views

1. [m25 gland removable insert and carrier isometric](<m25-gland-removable-insert-and-carrier-isometric.png>).
