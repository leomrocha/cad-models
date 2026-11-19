THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# leaf layered modules endplates and floor reference

1. **Library number:** 39.
2. **Type:** group.
3. **CAD file:** [leaf-layered-modules-endplates-and-floor-reference.dwg](<leaf-layered-modules-endplates-and-floor-reference.dwg>).
4. **DWG SHA-256:** `b7bae5ceaea9837de4022583aefcd2d37ffed47c326d612543921532f7080788`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Quantity: 1 per two-cassette44 mm corridor alternative.

### Geometry and contacts

Proposed3 mm steel common floor488 alongbankU×300 alongN, U±244,N±150,V−3…0. Two source 222 mm-wide cans have centreU±133, giving44 mm clear inter-cassette corridor and total bare488. Source module300 axis mapsN; source stack height204 mapsV. This is a separate support-packing alternative to earlier454/10 mm corridor. Two20 mm-wide inner cover uprights leave4 mm between them in the 44 corridor. Outboard cover support edges reachU±264, total528, within a600 mm body-length reference. Hood front reachesN175, so combined case/hood width is325 fromN−150. Weld floor underside to the named cassette rail supports, retaining actual module permitted contact/insulation; no raised bolt heads occur beneath the module. Source clamp/end-restraint joints remain their own parts.

### Construction

Parent P17R — Leaf cassette support rail. Form/cut the proposed shape and inspect joints and holes.

### Module-to-bank transform — bare and layered stack proposals

1. **Local module reference:** retained Leaf reconstruction evidence defines source-model coordinates (x,y,z), can x =−150…150 mm, y =−111…111 mm, z =0…34 mm, and terminal contact plane x =162 mm. These coordinates describe the retained reconstruction. Bank coordinates (U,N,V) use this floor's datum: V =0 at the proposed floor top, U along the two cassette centres, N toward the terminal faces.
2. **Rigid placement proposal:** for cassette A set Uc =−133 mm; for cassette B set Uc =+133 mm. For module k =0…5, use (U,N,V) = (Uc−y, x, zk+z). The rotation matrix, with rows ordered U,N,V and columns x,y,z, is [[0,−1,0],[1,0,0],[0,0,1]]. Its determinant is +1. Translation is (Uc,0,zk) mm. Hood local axes u =y, v =z+zk, n =x therefore map to U =Uc−u, N =n, V =v. This explicit sign preserves a rigid rotation of the source model.
3. **Bare-stack comparison:** zk =34k mm gives module lower faces V =0,34,68,102,136,170 mm and can top V =204 mm. Cassette A can spans U =−244…−22 mm; cassette B U =22…244 mm. Their inner faces give the proposed 44 mm corridor. Both cans occupy N =−150…150 mm. The bare-stack placement is the reference used by the existing hood recipe.
4. **Layered-stack proposal:** use the existing proposed 3 mm lower end plate, one 0.25 mm lower barrier, five 0.25 mm intermediate barriers, one 0.25 mm upper barrier and 3 mm upper end plate. At nominal uncompressed thickness, module lower faces are zk =3.25+34.25k mm, giving 3.25,37.50,71.75,106.00,140.25,174.50 mm. The last module ends at 208.50 mm; upper barrier occupies208.50…208.75 mm and upper plate208.75…211.75 mm. Lower plate occupies0…3 mm and lower barrier3…3.25 mm. These offsets apply the previously recorded211.75 mm stack alternative to the floor datum. Material and clamp compression alter the installed offsets through their actual thicknesses.
5. **Transferred axes and terminals:** reconstructed four-bore axes (x,y)=(±138,±99) mm become (U,N)=(Uc∓99,±138) mm for each module. Source-model power terminal centres (x,y,z)=(162,±38,17) mm become (U,N,V)=(Uc∓38,162,zk+17) mm; centre-tap centre becomes(Uc,162,zk+17) mm. Bare-stack terminal centre heights are17,51,85,119,153,187 mm. Layered nominal heights are20.25,54.50,88.75,123.00,157.25,191.50 mm. Mating contact planes lie at N =162 mm in this retained reconstruction.
6. **Layout input use:** assign the above transform to each C021 — Leaf module instance and its associated terminal features before transferring P17E — end-restraint plate holes or C092 — busbar endpoints. The current P20CLeaf — terminal hood geometry uses the bare-stack reference; a layered-stack hood revision must evaluate its top/bottom margins, ear/support positions and installed conductor envelope with the layered offsets. Source-compatible module contact and clamping remain the basis for the actual restrained stack.

Sources and proposal inputs: P17E — end-restraint plate; C091 — insulation layers; P20CLeaf — terminal hood. Global chassis placement is a separate rigid transform of this complete bank frame.

### Assembled-stud floor openings — layered cassette proposal

1. **Inputs and geometry issue:** the layered stack in this sheet puts the lower end plate at V =0…3 mm, with its outer face at the floor top V =0. B04 uses an M8 washer and nut on that face. Their occupied volume extends below V =0 into the 3 mm floor. This proposal adds pass-through openings at those eight stud axes so the preassembled cassette can seat on the floor.
2. **Floor openings:** propose eight Ø18 mm through holes, axes parallel V, at every pair(U,N) with U =−232,−34,+34,+232 mm and N =−138,+138 mm. These are the four reconstructed clamp axes per cassette, transferred through the recorded proper rotation. Floor size remains488×300×3 mm. Each opening has a calculated3 mm nominal ligament to its nearest straight outer floor edge:244−232−9 =3 mm along U and 150−138−9 =3 mm along N. Internal opening-edge separation between U =−34/+34 is68−18 =50 mm.
3. **Hardware receiving envelope:** C147 gives nominal M8 washer outside diameter 16 mm; C153 gives nut AF maximum 13 mm and a calculated ideal-hex corner reference15.011 mm. Require the actual received nut/washer outer envelope to fit within proposed Ø17 mm for this opening variant. Ø18 opening then provides at least0.5 mm radial passage clearance to that receiving envelope. This Ø17 limit is a project inspection proposal. Verify the actual washer, nut corners, end plate and stud alignment before seating the cassette.
4. **Nominal stud position:** centre the proposed 240 mm C143 rod on the nominal 211.75 mm layered stack. Rod end planes are V =(211.75−240)/2 =−14.125 mm andV =225.875 mm. With source nominal 1.6 mm washers and source maximum 8 mm nuts, lower washer occupies V =−1.6…0 mm, lower nut−9.6…−1.6 mm, upper washer211.75…213.35 mm and upper nut213.35…221.35 mm. Nominal protrusion beyond each nut is4.525 mm. Proposed two-pitch criterion is2×1.25 =2.5 mm, leaving 2.025 mm nominal protrusion margin per end for these inputs. This calculation uses the uncompressed nominal stack and cut rod; actual layer thickness, rod cut and clamp compression set the installed positions.
5. **Underside reserve and assembly:** propose one Ø18 mm clear cylinder from V =−16 mm to0 at each stud axis. Nominal lower rod tip−14.125 leaves 1.875 mm to that proposed reserve depth. Assemble and tighten the module restraint using its source clamping procedure outside the floor assembly; lower the complete cassette so its nuts/rods pass through the openings. The 18 mm holes are passage openings. Nut-tool access is provided with the cassette removed from the floor.
6. **Support rails:** P17R supplies four identical300 mm long20×20×2 mm tube proposals under the floor, with top face V =−3 mm and bottom−23 mm. Their U centres are−193,−73,+73,+193 mm, their N extent−150…150 mm. Nearest stud/opening cylinders have20 mm transverse clearance to these proposed rails. Source-compatible cassette hold-downs retain their distinct load path into the structural supports.
7. **Clearance placement condition:** if the floor top is at chassis height Zf, rail underside is Zf−23 mm. The wheel-axis-height requirement at Z =233 mm therefore requires Zf≥256 mm for this particular floor/rail proposal. This is a calculated placement condition from the proposed geometry and the existing466 mm wheel/233 mm axle reference.

Sources: C143 — M8 cut threaded rod; C147 — M8 washer; C153 — M8 nut; P17R — support rails. The openings, receiving limit and underside reserve are construction proposals. Hole ligaments and protrusions describe the stated geometry; plate/floor stresses use the actual clamp and restraint loads.

### Nissan factory collar/alignment procedure reference

1. Nissan 2013 factory module-stack procedure, EVB-248–250 and 265–267, aligns inter-module collars, uses opposite-corner bolts and temporary Ø7 mm centring bars, then installs the remaining bolts. The rear-stack operation uses a lashing belt to square the stack and holds each bolt stationary while tightening its nut.
2. **Source contact condition:** Nissan identifies aligned collars as supports for the stack bolts. Preserve that supported contact path when comparing the proposed six-module end plates, threaded rods and insulation layers with the actual module collar faces. C021 retains the VT-Tech source bore claim Ø9.1 mm, reconstructed centre pattern276 ×198 mm and reconstructed boss diameter 22.4 mm; the factory7 mm bars describe temporary alignment tooling.
3. **Layered proposal:** six 34 mm seller-envelope modules, seven proposed 0.25 mm layers and two proposed 3 mm plates give211.75 mm nominal stack envelope. Check the layer outlines and actual collar bearing contacts in that specific layered arrangement. The cassette's separate inertia stops/bridges carry their recorded whole-bank loads.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| Leaf common floor and four support rails | 1 | [leaf common floor and four rails](<../leaf-common-floor-and-four-rails/leaf-common-floor-and-four-rails.md>) — 37 | `fb3411718c2e33f494a75d803406049fdb5172e99afb36b52fa09b6cd119b3fb` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module1 cassette-133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[-133.0,0.0,3.25],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module2 cassette-133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[-133.0,0.0,37.5],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module3 cassette-133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[-133.0,0.0,71.75],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module4 cassette-133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[-133.0,0.0,106.0],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module5 cassette-133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[-133.0,0.0,140.25],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module6 cassette-133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[-133.0,0.0,174.5],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| P17E — Source-proposal end-restraint plate | 1 | [Nissan Leaf six-module stack end-restraint plate](<../../../../mechanical-parts/components/p17e-leaf-stack-end-restraint-plate/p17e-leaf-stack-end-restraint-plate.md>) — 178 | `7673c28ef5e8a62864030d96a13caedf00ae309a08c5c8f99b69cc38e3197e4b` | `{"position_mm":[-133.0,0.0,0.0],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| P17E — Source-proposal end-restraint plate | 1 | [Nissan Leaf six-module stack end-restraint plate](<../../../../mechanical-parts/components/p17e-leaf-stack-end-restraint-plate/p17e-leaf-stack-end-restraint-plate.md>) — 178 | `7673c28ef5e8a62864030d96a13caedf00ae309a08c5c8f99b69cc38e3197e4b` | `{"position_mm":[-133.0,0.0,208.75],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module1 cassette133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[133.0,0.0,3.25],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module2 cassette133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[133.0,0.0,37.5],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module3 cassette133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[133.0,0.0,71.75],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module4 cassette133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[133.0,0.0,106.0],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module5 cassette133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[133.0,0.0,140.25],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| C021 — Leaf source reconstruction module6 cassette133 | 1 | [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — 110 | `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c` | `{"position_mm":[133.0,0.0,174.5],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| P17E — Source-proposal end-restraint plate | 1 | [Nissan Leaf six-module stack end-restraint plate](<../../../../mechanical-parts/components/p17e-leaf-stack-end-restraint-plate/p17e-leaf-stack-end-restraint-plate.md>) — 178 | `7673c28ef5e8a62864030d96a13caedf00ae309a08c5c8f99b69cc38e3197e4b` | `{"position_mm":[133.0,0.0,0.0],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |
| P17E — Source-proposal end-restraint plate | 1 | [Nissan Leaf six-module stack end-restraint plate](<../../../../mechanical-parts/components/p17e-leaf-stack-end-restraint-plate/p17e-leaf-stack-end-restraint-plate.md>) — 178 | `7673c28ef5e8a62864030d96a13caedf00ae309a08c5c8f99b69cc38e3197e4b` | `{"position_mm":[133.0,0.0,208.75],"scale":[0.9999999999999999,1.0,1.0],"rotation_radians":1.5707963267948966,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. EVShop module listing.
2. VT-Tech module article.
3. Jay Summet, Battery Bay Plan: Nissan Leaf Cells six group.
4. EcoTrust module without additional mounting points.
5. EcoTrust module with additional mounting points.
6. c091 nissan leaf module contact insulation pads.
7. Square steel tube stock family — supplier reference.
8. Weldable steel plate stock family — supplier reference.
9. Westfield Fasteners ISO 7089 washer dimensions and tolerances.

## References — local

37. [leaf common floor and four rails](<../leaf-common-floor-and-four-rails/leaf-common-floor-and-four-rails.md>) — library entry 37.
110. [Nissan Leaf Gen2 battery module](<../../../../electronics/components/nissan-leaf-gen2-module-300x222x34/nissan-leaf-gen2-module-300x222x34.md>) — library entry 110.
178. [Nissan Leaf six-module stack end-restraint plate](<../../../../mechanical-parts/components/p17e-leaf-stack-end-restraint-plate/p17e-leaf-stack-end-restraint-plate.md>) — library entry 178.
