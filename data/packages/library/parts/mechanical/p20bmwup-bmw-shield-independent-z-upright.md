THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# BMW shield independent formed upright

1. **Library number:** 185.
2. **Type:** part.
3. **CAD file:** [p20bmwup-bmw-shield-independent-z-upright.dwg](<p20bmwup-bmw-shield-independent-z-upright.dwg>).
4. **DWG SHA-256:** `6917d788dc1ec284733f91efad6467eb0de387285a9044969e1880f243886bc5`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** BMW shield independent formed upright — P20BMWUP.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Quantity: 4 per BMW shield. Route: BMW shield support alternative.

### Geometry, datum and interfaces

Proposed 3 mm formed metal Z upright,20 mm width along local v. Local u points outward from the module centre; n is module height. Source shield ear axis is u 208.5,v±140, underside n 160. Straight upper cap occupies u =198.5…221 mm, n =157…160 mm; one Ø4.5 mm axis at u =208.5 mm. Straight web occupies u =224…227 mm, n =5.75…154 mm. Straight lower foot occupies u =207…221 mm, n =−0.25…2.75 mm; one Ø4.5 mm axis at u =212 mm. Two bends with inside radius 3 mm and outside radius 6 mm join these straight portions; exact centres and quadrants are below. The foot lower face is the tray support plane 0.25 below the module base in the J reference. Plate/upright material stays beyond module outer mounting-tab envelope u 205 by 2 mm at the foot and 19 mm at the web; compare exact donor tabs. Footu 207…218 overlaps existing tray floor to outer edge 218 by 11 mm; its remaining 9 mm is cantilever. Actual tray-floor edge and live/socket envelope may require a wider local support tab. Proposed bend inside R 3: maintain the stated functional contact planes when calculating tangent lengths. This one-piece Z profile supplies a continuous foot→web→cap path. Mirror/rotate identical parts at both ends; global ear axes in J are X−133.5/283.5,Y±140. Module base 578.25 gives cap top 738.25; the shield ears/roof remain the original single shield geometry.

### Construction

Parent P20CBMW — BMW terminal cover variant. All custom dimensions above are proposed inputs. Inspect cut/turned faces, hole axes, exact source mating parameters and assembly clearance.

### Finished curved-section constructor

1. **Inputs and status:** existing proposed3 mm metal sheet, inside radius3 mm, upper cap contact n =160 mm, lower support face n =−0.25 mm and web u =224…227 mm. Coordinates are local millimetres. This constructor retains both returns toward decreasing u from the web and the original upper/lower fixing axes.
2. **Lower bend:** centre(u,n)=(221,5.75) mm. Material occupies the quarter-annulus of radii3…6 mm in u ≥221 mm and n ≤5.75 mm. It joins the foot at u =221 mm, n =−0.25…2.75 mm to the web at u =224…227 mm, n =5.75 mm.
3. **Upper bend:** centre(u,n)=(221,154) mm. Material occupies the quarter-annulus of radii3…6 mm in u ≥221 mm and n ≥154 mm. It joins the web at u =224…227 mm, n =154 mm to the cap at u =221 mm, n =157…160 mm. Extrude this finished section across20 mm strip width in v. Mirror/place the identical part at the existing four shield-ear instances.
4. **Washer footprints:** C144 — ISO7089 M4 washer gives maximum outside diameter9 mm. Lower axis u =212 mm produces footprint207.5…216.5 mm on the flat foot:0.5 mm to free edge207 and4.5 mm to bend tangent221. Upper axis208.5 mm produces footprint204…213 mm on the cap:5.5 mm to free edge198.5 and8 mm to tangent221. Both axes are centred across the20 mm strip, giving5.5 mm to either v edge for that washer. These are calculated nominal flat-seat margins.
5. **Hole ligaments:** Ø4.5 mm holes leave lower free-edge ligament212−2.25−207 =2.75 mm and upper free-edge ligament208.5−2.25−198.5 =7.75 mm. Side ligaments are10−2.25 =7.75 mm. Lower/upper distances from hole edge to bend tangent are6.75/10.25 mm. The curved regions carry the3 mm section continuously between flat portions.
6. **Development formula:** straight lengths are14 +148.25 +22.5 =184.75 mm. With bend factor K, neutral-axis distance from inside surface divided by3 mm sheet thickness, two90° bends give L =184.75 +π(3+3K) mm. Illustrative K =0.40 gives197.945 mm; blank width20 mm. Material/tooling bend allowance controls the production blank; finished contact planes and fixing coordinates control the part.
7. **Preserved placement:** module base578.25 mm plus upper contact160 mm gives assembly cap top738.25 mm. Lower foot support face is578.25−0.25 =578.00 mm in that same J reference. Source shield-ear mating geometry and the original four transforms retain their own source attribution. C01 — shield ears to uprights and C02 — upright feet to tray keep their existing fastener quantities and grip definitions.

Source/proposal basis: this sheet's retained section, contact and fixing coordinates; P20CBMW — BMW shield input; and the cited M4 washer source limits. Bend centres, straight lengths, blank formula and margins are calculated construction proposals.

### C01/C02 sourced-length screen

Both existing joints have proposed nominal solid grip6 mm. With two C144 — M4 washers at source maximum0.9 mm each, C150 — M4 nut at source maximum5 mm and the proposed two-pitch protrusion criterion at M4 pitch0.7 mm, required actual under-head screw length is at least6+2×0.9+5+2×0.7 =14.2 mm. C135 — M4×16 nominal screw gives1.8 mm margin over that nominal-grip criterion. Actual manufactured grip and supplied screw length determine acceptance for each joint. Each group has four joints; combined C01/C02 quantities are8 screws,16 washers and8 nuts.

Sources: C135 — M4×16 screw; C150 — M4 nut; and C144 linked above. The two-pitch criterion is a construction proposal.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed BMW shield independent formed upright | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[198.5, 227.0], [-10.0, 10.00000000000001], [-0.25, 160.0]] | mm |
| Source-sheet hole group 1 | PASS | [[208.5, 0.0], [212.0, 0.0]] | mm |
| Native circular corner radius 3 mm | PASS | [[221.0, 5.75], [221.0, 154.0]] | mm |
| Native circular corner radius 6 mm | PASS | [[221.0, 5.75], [221.0, 154.0]] | mm |
| Both formed-bend tangent vertices on both width faces | PASS | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] | count |

## Sources — online

1. EVShop product 216.
2. Weldable steel plate stock family — supplier reference.
3. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.
