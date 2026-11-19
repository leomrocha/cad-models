THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# bmw module and independent shield uprights j3f

1. **Library number:** 11.
2. **Type:** group.
3. **CAD file:** [bmw-module-and-independent-shield-uprights-j3f.dwg](<bmw-module-and-independent-shield-uprights-j3f.dwg>).
4. **DWG SHA-256:** `87dc5639a19d44af85ffb6bc04c4d829a774abb35ee97a3466e6030d006fa4d6`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

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

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| C022 — BMW i3 source/photo-derived module exterior | 1 | [BMW i3 94Ah battery module](<../../../../../electronics/components/bmw-i3-94ah-module/bmw-i3-94ah-module.md>) — 64 | `95404b6f6410cf73dffd875f34d33959afcc8d6c99a7cb8506f0e694b6589e2c` | `{"position_mm":[75.0,0.0,578.25],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P20BMWUP — Independent formed shield upright | 1 | [BMW shield independent formed upright](<../../../../../mechanical-parts/components/p20bmwup-bmw-shield-independent-z-upright/p20bmwup-bmw-shield-independent-z-upright.md>) — 185 | `6917d788dc1ec284733f91efad6467eb0de387285a9044969e1880f243886bc5` | `{"position_mm":[75.0,-140.0,578.25],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P20BMWUP — Independent formed shield upright | 1 | [BMW shield independent formed upright](<../../../../../mechanical-parts/components/p20bmwup-bmw-shield-independent-z-upright/p20bmwup-bmw-shield-independent-z-upright.md>) — 185 | `6917d788dc1ec284733f91efad6467eb0de387285a9044969e1880f243886bc5` | `{"position_mm":[75.0,140.0,578.25],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P20BMWUP — Independent formed shield upright | 1 | [BMW shield independent formed upright](<../../../../../mechanical-parts/components/p20bmwup-bmw-shield-independent-z-upright/p20bmwup-bmw-shield-independent-z-upright.md>) — 185 | `6917d788dc1ec284733f91efad6467eb0de387285a9044969e1880f243886bc5` | `{"position_mm":[75.0,-140.0,578.25],"scale":[1.0,1.0,1.0],"rotation_radians":3.141592653589793,"normal":[0.0,0.0,1.0]}` |
| P20BMWUP — Independent formed shield upright | 1 | [BMW shield independent formed upright](<../../../../../mechanical-parts/components/p20bmwup-bmw-shield-independent-z-upright/p20bmwup-bmw-shield-independent-z-upright.md>) — 185 | `6917d788dc1ec284733f91efad6467eb0de387285a9044969e1880f243886bc5` | `{"position_mm":[75.0,140.0,578.25],"scale":[1.0,1.0,1.0],"rotation_radians":3.141592653589793,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. EVShop product 216.
2. Weldable steel plate stock family — supplier reference.
3. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.

## References — local

64. [BMW i3 94Ah battery module](<../../../../../electronics/components/bmw-i3-94ah-module/bmw-i3-94ah-module.md>) — library entry 64.
185. [BMW shield independent formed upright](<../../../../../mechanical-parts/components/p20bmwup-bmw-shield-independent-z-upright/p20bmwup-bmw-shield-independent-z-upright.md>) — library entry 185.

## Views

1. [bmw module and independent shield uprights j3f isometric](<bmw-module-and-independent-shield-uprights-j3f-isometric.png>).
