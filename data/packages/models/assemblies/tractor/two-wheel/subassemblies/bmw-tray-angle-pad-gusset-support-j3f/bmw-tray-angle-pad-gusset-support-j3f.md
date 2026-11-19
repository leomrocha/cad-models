THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# bmw tray angle pad gusset support j3f

1. **Library number:** 12.
2. **Type:** group.
3. **CAD file:** [bmw-tray-angle-pad-gusset-support-j3f.dwg](<bmw-tray-angle-pad-gusset-support-j3f.dwg>).
4. **DWG SHA-256:** `f22368640f54a511e1cc5b7000f53bbba1dbba0b0cf3d2c4fbf2708a61fe80fc`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Date: 13 November 2026. Discussion inventory input. Route: BMW. Quantity: One per distinct physical geometry; repeated identical parts use instances.

### Geometry and provenance

Retain BMW 410×310×150 mm source envelope reference; define tray contact surface, edge restraint and supervision-board clearance from exact BMW module casing and harness drawing.

### Units and local datum

Millimetres unless explicitly stated otherwise. Establish the datum from the named mating faces and source axes. Assembly placement axes: X forward, Y left, Z up. Source dimensions and proposal geometry remain separately labelled.

### Mating interfaces and hardware

Mates the exact source component and corresponding support family; dimensions are route-specific and source-part datums control the pattern.

### Installation and access

Transfer mating dimensions before fabrication; keep removal, tool and service access in the geometry sheet.

### CAD measurements

Record mating dimensions, clearances, fastener tool access, harness/service envelope and removal direction against the cited source revision or custom-part drawing.

### Engineering transfer — 13 November 2026

1. **Input and status:** BMW exterior reconstruction, local case origin at body centre on base underside; X along length, Y across width, Z up; mm. Seller supplies 410×310×150 overall dimensions and M8 bolt size. The four Ø8.5 bores at (X,Y)=(±198.75,±139) are photo-derived reconstruction inputs.
2. **Dimensioned proposal:** locate four tray clearance-hole axes at those same local (X,Y) coordinates; preserve the four Ø8.5 reconstruction bores as the template feature. Calculated centre spans: 2×198.75=397.5 mm along X and 2×139=278 mm along Y. Method: direct transfer of the reconstructed mating pattern; tray support plane coincides with the battery underside after accounting for the actual insulation layer.
3. **Construction dependency:** verify the four bore centres and diameters against the physical module before drilling a fabrication tray. The module model's 7 mm base and tray proposal's 3 mm sheet are separate stack layers; fastener grip also includes insulation, washers and the actual tab contact stack. Keep the cable model's outboard path to Y=−230 clear of tray returns.
4. **Restraint proposal:** use these four tab interfaces as the tray restraint pattern, with accessible removable hardware and support under each tab. Restraint loads, plate bending and fastener strength require the mechanical load case; the transferred pattern supplies geometry only.

### Supported battery construction proposal — 13 November 2026

See battery load cases and construction for explicitly proposed masses,2g/3g/1g scenarios and1.5 strength multiplier.

Propose430×330 mm tray floor around the410×310 mm source envelope, giving10 mm plan allowance per side, with25 mm folded returns outside contact regions. Support all four tabs directly beneath the397.5×278 mm reconstructed fixing pattern; clamp the actual supported tab/insulation stack. Keep donor-hole confirmation before drilling. Add positive end stops beside crossmembers; keep terminal and CSC access beneath independently removable covers. Cable corridorY=−230 extends beyond the nominal floor and needs an open/protected return. Tray envelope and this corridor are separate layout reservations.


Proposed clear tray430×330 mm,3 mm steel,25 mm returns with interrupted harness exit; module410×310×150; four supported tab axes(±198.75,±139) mm. Existing module-local harness reachesY=−230 mm,65 mm beyond the tray clear edgeY=−165; provide an outboard protected corridor. Two30×30×3 angles and four M8 frame joints carry the proposed35 kg supported assembly. See section8 of physical support proposal for assumed forces and strength-evaluation fields.

### Combined layout proposal J

ME0907/BMW elevated-tray alternativeJ places the battery above full-travel motors, side-mounted controllers above tyre crowns and rear cabinet on650mm body; proposed deck undersideZ770. Tray underside575/support578/case top728.25, vertical controller thermal facesY±200/carrierZ480..668/body500..648, separate rear receiver. Revised chainplaneY150/120mm bearing spacing and explicit local enclosed chain-pocket clearance alternative accompany this branch. Preserve earlier600/537 packaging study separately. J exact source-terminal, shoe, thermal/strength, guard/cavity and support-interface parameters retain their named evaluation fields.

### Separate manufactured shapes and quantity basis — 13 November 2026

Existing parent plate/body retains its own manufacturing role; helpers are separate applicable pieces.
- P18JA — J BMW tray support angle: 2 per elevated J tray; Raised frame J3 discussion variant; electrical installation table motor 430/tray 575/deck 770.
- P18JR — J tray frame riser: 4 per J tray; Raised frame J3 discussion variant; electrical installation table motor 430/tray 575/deck 770.
- P18JC — J tray riser angle cap: 0 for J3; Earlier J support comparison.
- P18JG — J tray angle riser gusset: 8 per J tray; Raised frame J3 discussion variant; electrical installation table motor 430/tray 575/deck 770.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P18JA — Tray support angle | 1 | [BMW elevated tray support angle, welded branch](<../../../../../mechanical-parts/components/p18ja-j-bmw-tray-support-angle/p18ja-j-bmw-tray-support-angle.md>) — 181 | `33e532c71e221a1ab8753f241328138b4de82b1c004b2a9c94ad4276cd117bcc` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JR — Tray welded riser pad | 1 | [BMW elevated tray welded riser pad](<../../../../../mechanical-parts/components/p18jr-j-tray-frame-riser/p18jr-j-tray-frame-riser.md>) — 184 | `3b543700b97b785588fdb87f9a1bc0ab30703104293cfea656c8b7d30ae72432` | `{"position_mm":[-120.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JG — Retained triangular tray gusset | 1 | [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — 182 | `f94737ff7f59ff4c009d440a6e67c552e470db8b736563be1870313ae6bd12cd` | `{"position_mm":[-129.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JG — Retained triangular tray gusset | 1 | [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — 182 | `f94737ff7f59ff4c009d440a6e67c552e470db8b736563be1870313ae6bd12cd` | `{"position_mm":[-111.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JR — Tray welded riser pad | 1 | [BMW elevated tray welded riser pad](<../../../../../mechanical-parts/components/p18jr-j-tray-frame-riser/p18jr-j-tray-frame-riser.md>) — 184 | `3b543700b97b785588fdb87f9a1bc0ab30703104293cfea656c8b7d30ae72432` | `{"position_mm":[270.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JG — Retained triangular tray gusset | 1 | [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — 182 | `f94737ff7f59ff4c009d440a6e67c552e470db8b736563be1870313ae6bd12cd` | `{"position_mm":[261.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JG — Retained triangular tray gusset | 1 | [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — 182 | `f94737ff7f59ff4c009d440a6e67c552e470db8b736563be1870313ae6bd12cd` | `{"position_mm":[279.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JA — Tray support angle | 1 | [BMW elevated tray support angle, welded branch](<../../../../../mechanical-parts/components/p18ja-j-bmw-tray-support-angle/p18ja-j-bmw-tray-support-angle.md>) — 181 | `33e532c71e221a1ab8753f241328138b4de82b1c004b2a9c94ad4276cd117bcc` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JR — Tray welded riser pad | 1 | [BMW elevated tray welded riser pad](<../../../../../mechanical-parts/components/p18jr-j-tray-frame-riser/p18jr-j-tray-frame-riser.md>) — 184 | `3b543700b97b785588fdb87f9a1bc0ab30703104293cfea656c8b7d30ae72432` | `{"position_mm":[-120.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JG — Retained triangular tray gusset | 1 | [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — 182 | `f94737ff7f59ff4c009d440a6e67c552e470db8b736563be1870313ae6bd12cd` | `{"position_mm":[-129.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JG — Retained triangular tray gusset | 1 | [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — 182 | `f94737ff7f59ff4c009d440a6e67c552e470db8b736563be1870313ae6bd12cd` | `{"position_mm":[-111.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JR — Tray welded riser pad | 1 | [BMW elevated tray welded riser pad](<../../../../../mechanical-parts/components/p18jr-j-tray-frame-riser/p18jr-j-tray-frame-riser.md>) — 184 | `3b543700b97b785588fdb87f9a1bc0ab30703104293cfea656c8b7d30ae72432` | `{"position_mm":[270.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JG — Retained triangular tray gusset | 1 | [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — 182 | `f94737ff7f59ff4c009d440a6e67c552e470db8b736563be1870313ae6bd12cd` | `{"position_mm":[261.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P18JG — Retained triangular tray gusset | 1 | [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — 182 | `f94737ff7f59ff4c009d440a6e67c552e470db8b736563be1870313ae6bd12cd` | `{"position_mm":[279.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. EVShop product 216.
2. Weldable steel plate stock family — supplier reference.

## References — local

181. [BMW elevated tray support angle, welded branch](<../../../../../mechanical-parts/components/p18ja-j-bmw-tray-support-angle/p18ja-j-bmw-tray-support-angle.md>) — library entry 181.
182. [Battery tray angle riser gusset](<../../../../../mechanical-parts/components/p18jg-j-tray-angle-riser-gusset/p18jg-j-tray-angle-riser-gusset.md>) — library entry 182.
184. [BMW elevated tray welded riser pad](<../../../../../mechanical-parts/components/p18jr-j-tray-frame-riser/p18jr-j-tray-frame-riser.md>) — library entry 184.

## Views

1. [bmw tray angle pad gusset support j3f isometric](<bmw-tray-angle-pad-gusset-support-j3f-isometric.png>).
