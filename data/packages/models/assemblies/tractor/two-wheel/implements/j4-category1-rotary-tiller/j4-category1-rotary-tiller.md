# Category 1 700 mm rotary tiller

**Representation.** Guarded horizontal rotor with seven staggered twin-tine stations, a depth roller in its lower index, four positive index locks and separate pulley-register parts.

1. **Native CAD.** [DWG 2018](j4-category1-rotary-tiller.dwg). SHA-256: 3acb07235ea1327655d1a06a0d9952cee11dee049705f32c6e9dc7874bc4f586.
2. **Native revision checks.** The index and lock geometry passed. Readback matched 139 fixed solid fingerprints to the preceding guarded revision. The roller tube, axle, hubs, carriers and lock hardware move together into the existing lower index. The roller axis moves 25 mm down to X = 515 mm, Z = −145 mm in implement coordinates.
3. **Positive depth-index locks.** The four lock positions use Ø10 mm shanks through Ø11 mm bores, Ø14 mm heads, washers and locknuts. The checked grip is 20 mm, head-to-hub clearance is 2 mm and remaining screw end after the washer and locknut is 5.4 mm. The nominal check also records 9 mm minimum hub annulus radial land.
4. **Hitch.** Nominal ISO 730 Category 1 with 683 mm shoulder span, 460 mm mast height and Ø22/Ø19 mm nominal pins.
5. **Working arrangement.** Nominal 700 mm span. The preceding guarded comparison used 80 mm depth, 3 kW at 225 rpm and 65 kg assumed gross implement mass. These assumptions describe the earlier comparison. The lower-index drawing records the implement configuration.
6. **Guarded components.** Shaft, bearings, hood, drive guard, depth roller and motor protection are separate parts. The retained motor shroud has a removable end cap and recessed cable feed, with the preceding 10 mm radial and 23 mm end-cap clearances. The 20.1 mm nominal rotor-to-upper-hood clearance uses retained rotor and hood geometry.
7. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

8. **Native display.** Revision 4 preserves the 154 physical solid occurrences, their original geometry and placements, and the three hidden ISO reference solids. OpenCADStudio verified the fourteen physical groups:

   - `Display-Implement-Frame` — tool crossbeam, longitudinal members and transfer tabs, `#667584`.
   - `Display-Implement-Interface` — hitch heading lugs and mast sides, `#C6484D`.
   - `Display-Implement-Working-Surfaces` — fourteen bent wear feet, `#4F80A6`.
   - `Display-Implement-Shanks` — fourteen replaceable tine shanks, `#426A83`.
   - `Display-Implement-Guards` — fixed hood, bearing cheeks, curtains and shroud, `#D89A27`.
   - `Display-Implement-Guard-Lids` — removable drive guard and axial service cap parts, `#F2D389`.
   - `Display-Implement-Drive` — rotor, shafts, root lugs, pulley registers and gearhead envelope, `#B99A50`.
   - `Display-Implement-Belts` — the two modeled belt runs, `#654632`.
   - `Display-Implement-Motors` — motor installation envelope, `#6147A7`.
   - `Display-Implement-Roller` — depth roller tube, axle and hubs, `#728EA3`.
   - `Display-Implement-Supports` — lower-index roller brackets and carriers, `#31BDB2`.
   - `Display-Implement-Pins-and-Locks` — hitch pins and depth-index lock hardware, `#B99DDD`.
   - `Display-Implement-Fasteners` — tine bolts and shroud-cap hardware, `#A2A8AF`.
   - `Display-Implement-Power-Access` — gland body, terminal bulkhead and feed blank, `#9EAFF0`.

9. **Hidden interface reference.** Three ISO datum solids use `Display-Implement-Reference` in `#788FA0`. Their parent layer `J4-Rotary-Tool-Iso-Reference` remains hidden.

## Technical reference

- [ISO 730:2009+A1:2014, Category 1 hitch interface](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)

## Evidence status

Discussion construction proposal with verified native lower-index and lock geometry. Supplier drive selection, actual operating depth and the physical operating rating require verification.
