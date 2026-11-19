THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# 34 mm M6 equipment angle shoe

1. **Library number:** 191.
2. **Type:** part.
3. **CAD file:** [p22sh34-m6-equipment-angle-shoe-34mm.dwg](<p22sh34-m6-equipment-angle-shoe-34mm.dwg>).
4. **DWG SHA-256:** `c31d628c42430ea3c80b88ccd9445a0182e315389e92e1117eb888212410c597`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** 34 mm M6 equipment angle shoe — P22SH34.

**Design status:** Discussion construction proposal.

## Technical specification

Discussion construction proposal. Units: mm. Quantity: four per shoe-supported carrier, as an alternative to the earlier 20 mm shoe. Repeated identical shapes use instances.

### Finite formed-angle construction proposal

1. **Proposed stock and profile:** steel 3 mm thick, width 30 mm, finished outer legs 34 × 34 mm. All following coordinates are millimetres. Local cross-section coordinates are x and z; width coordinate w = −15…15 mm. Horizontal straight metal is x = 6…34, z = 0…3. Vertical straight metal is x = 0…3, z = 6…34. The quarter-annulus bend has centre (x,z) = (6,6), inside radius 3 mm, outside radius 6 mm, and occupies x ≤ 6, z ≤ 6. Extrude this connected cross-section through the 30 mm width. Finished hole axes are horizontal-foot (x,w) = (24,0), normal z, and upright-leg (z,w) = (24,0), normal x; each bore is Ø6.6 mm. This is a project construction proposal.
2. **Source washer and nut dimensions:** C146 — M6 washer gives source maximum OD 12 mm and thickness 1.8 mm. C152 — M6 nut gives maximum height 6 mm and AF 10 mm. The proposed flat washer disk spans leg coordinates 18…30 mm; clearance to bend tangency is 18 − 6 = 12 mm, to free end 34 − 30 = 4 mm and to each width edge 15 − 6 = 9 mm. Hole-to-free-end ligament is 34 − 24 − 3.3 = 6.7 mm.
3. **Perpendicular hardware and tool space:** orient the carrier-side and frame-side nuts toward the angle interior. Limit each installed inward nut/washer/thread projection to 13 mm measured from the corresponding inner flat face x = 3 or z = 3. Their endpoint bound is therefore coordinate 16 mm. Reserve a proposed Ø14 mm occupied-hardware cylinder about each hole axis and a proposed Ø14 mm socket cylinder for individual tightening. The opposite hole is at coordinate 24 mm, so each cylinder starts at 24 − 7 = 17 mm, leaving 17 − 16 = 1 mm between the reserved tool cylinder and the opposite installed axial end. Source washer plus nut is at most 1.8 + 6 = 7.8 mm, so the 13 mm projection limit allocates up to 5.2 mm for exposed thread beyond the source nut. These are construction-space conditions for the supplied fasteners and tool.
4. **Parent carrier transform:** preserve every existing carrier support-hole centre P and its mounting contact plane. Let n be the unit vector from the shoe foot contact into the angle interior; let e be the perpendicular carrier-plane unit vector from the bend toward the foot free end; let a = n × e be the width direction. The local foot inner contact datum is (x,w,z) = (24,0,3). Place each point by world position P + (x − 24)e + w a + (z − 3)n. Thus the carrier-side foot axis stays at P. The frame-side inner contact-axis point is P − 21e + 21n, with axis parallel to e. Choose the rotation about n from the actual supporting rail face. This transform defines the proposal's local orthogonal frame-contact plane. Compare that plane with the existing support face when positioning the shoe in the assembly.
5. **Spacer branch:** where the parent uses a 10 mm P22SP10 spacer, P is the foot contact at the spacer's frame-facing end, on the same unchanged parent hole axis. The spacer's two parallel contact planes and original carrier axis are preserved. Four shoes per shoe-supported carrier retain their existing count. The BMW supervision-board direct-parallel branch and the J post/sleeve branch retain their separate geometry.
6. **Fabrication:** form the stated bend profile, then drill the two axes from the finished outside faces and deburr both bores. The finished straight lengths are 28 mm per leg. A blank-development illustration uses bend allowance BA = (π/2)(3 + K × 3) mm and total blank length 56 + BA mm, where K is the fabricator's process neutral-axis factor. For illustrative K = 0.4, BA = 6.5973 mm and blank length = 62.5973 mm. The finished 34 mm legs and measured bend radii control the part.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed 34 mm M6 equipment angle shoe | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[0.0, 34.0], [-15.0, 15.000000000000002], [0.0, 34.0]] | mm |
| Source-sheet hole group 1 | PASS | [[24.0, 0.0]] | mm |
| Source-sheet hole group 2 | PASS | [[1.7763568394002505e-15, 24.0]] | mm |
| Native circular corner radius 3 mm | PASS | [[6.0, 6.0]] | mm |
| Native circular corner radius 6 mm | PASS | [[6.0, 6.0]] | mm |
| R3/R6 bend tangent vertices on both width faces | PASS | [1, 1, 1, 1, 1, 1, 1, 1] | count |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

77. [DIN985 M6 nominal nut reference](<../../fasteners/nuts/c152-din-985-m6-nylon-insert-nut-proposed-class-8/c152-din-985-m6-nylon-insert-nut-proposed-class-8.md>) — library entry 77.
90. [ISO 7089 M6 plain washer, proposed 200 HV](<../../fasteners/washers/iso7089-m6-washer-6p4x12x1p6-reference/iso7089-m6-washer-6p4x12x1p6-reference.md>) — library entry 90.
