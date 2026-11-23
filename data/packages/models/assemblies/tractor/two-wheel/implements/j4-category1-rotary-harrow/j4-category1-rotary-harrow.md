# Category 1 750 mm rotary harrow

**Representation.** Five timed vertical shafts, removable paired tines, a guarded gear-train layout and a trailing depth roller in its lower index with four positive locks.

1. **Native CAD.** [DWG 2018](j4-category1-rotary-harrow.dwg). SHA-256: ce7f89dbf4b27385e46886646bf510cf5d2ad74b1a521f0b8bb9c269b1e69e10.
2. **Native revision checks.** The lower index and lock geometry passed. Readback matched 137 fixed solid fingerprints to the preceding protected revision. The roller tube, axle, hubs, carriers and lock hardware move together 25 mm down to roller axis X = 535 mm, Z = −145 mm in implement coordinates.
3. **Positive depth-index locks.** Four positions use Ø10 mm shanks through Ø11 mm bores, Ø14 mm heads, washers and locknuts. Readback verified 20 mm bracket/carrier grip, 2 mm head-to-hub clearance and 9 mm minimum radial land. The guarded revision keeps the 2 mm bracket-to-axle side gap.
4. **Working arrangement.** Nominal 750 mm span. Shafts are on 150 mm centres. Verified phases at Y = −300, −150, 0, +150, +300 mm are 0°, 90°, 0°, 90°, 0°. The five gear bodies represent pitch layout stock. The preceding analytical model used an 18 mm nominal guard gap.
5. **Hitch.** Nominal ISO 730 Category 1 with 683 mm shoulder span, 460 mm mast height and Ø22/Ø19 mm nominal pins.
6. **Proposed operating cases.** The preceding comparison assumed 55 mm depth, 3 kW at 260 rpm and 90 kg gross implement mass. The separate lower-index working pose yields a nominal 9.567 mm cut depth and 47.752 mm minimum guard clearance to its reference grade. These are geometric results for the screened pose.
7. **Gearcase and protection.** The widened case end and side walls retain 4.5 mm and 5.5 mm nominal clearance respectively to the proposed Ø155 mm gear rim. The gearcase, side skirts, transverse flexible curtains and 32-solid motor shroud retain their native geometry. The case-lid shroud retains its 2 mm nominal radial clearance, 18 mm top air gap, limits Y ±102 mm, removable service cap and recessed cable feed. Seeder mounting rails remain in their prior geometry.
8. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

9. **Native display.** Revision 3 preserves the geometry and placements of 152 physical solid occurrences and the three hidden ISO reference solids. The 13 physical layers are:

   - `Display-Implement-Frame` — crossbeam, side members and mounts, `#667584`.
   - `Display-Implement-Interface` — hitch lugs and mast, `#C6484D`.
   - `Display-Implement-Working-Surfaces` — ten bent tine wear ends, `#4F80A6`.
   - `Display-Implement-Shanks` — ten removable tine shanks, `#426A83`.
   - `Display-Implement-Guards` — case walls, skirts, curtains and shroud, `#D89A27`.
   - `Display-Implement-Guard-Lids` — removable protection covers, `#F2D389`.
   - `Display-Implement-Drive` — five shaft stations and their gear and bearing geometry, `#B99A50`.
   - `Display-Implement-Motors` — motor installation envelope, `#6147A7`.
   - `Display-Implement-Roller` — depth roller, axle and hubs, `#728EA3`.
   - `Display-Implement-Supports` — roller carriers and lower-index brackets, `#31BDB2`.
   - `Display-Implement-Pins-and-Locks` — hitch pins and depth-index locks, `#B99DDD`.
   - `Display-Implement-Fasteners` — tine and protection fasteners, `#A2A8AF`.
   - `Display-Implement-Power-Access` — feed and terminal bulkhead geometry, `#9EAFF0`.

10. **Hidden hitch reference.** Three ISO datum solids use `Display-Implement-Reference` in `#788FA0`. The parent layer `J4-Rotary-Tool-Iso-Reference` stays hidden.

## Technical references

- [ISO 730:2009+A1:2014, Category 1 hitch interface](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
- [Rapid rotary harrow, 750 mm working width reference](https://rapid.ch/fr_CH/herses-rotatives)

## Evidence status

Discussion construction proposal with verified native lower-index, lock and fixed protection geometry. Supplier drive selection and the physical operating rating require verification.
