# Category 1 700 mm reverse-rotor soil burier

1. **Native CAD.** [DWG 2018](j4-category1-rotary-burier.dwg). SHA-256 `1bd04118859214f89b04e0f5da521767b4eb9bed389964837560e90f34c51397`. The saved standalone assembly contains 176 solid occurrences, including 28 motor protection solids and three hidden ISO hitch datum solids.
2. **Working elements.** The 700 mm cutting span uses a 190.02 mm nominal tip radius. The reverse rotor carries replaceable tines. The separator and indexed depth roller are separate groups.
3. **Drive layout.** The 2:1 sealed side gearcase uses nominal Ø50 and Ø100 mm pitch diameters with 55 mm face width. The saved gear solids define root stock and axle position. The assumed 4 kW at 195 rpm case gives 7.84 kN factored tooth force.
4. **Design clearance.** The level 100 mm depth case leaves 28.02 mm below the gearcase. The calculated 20 mm margin reaches its limit at about 0.97° of roll. Use the documented case when choosing terrain and depth settings.
5. **Motor protection.** The removable motor shroud includes fixed seat extensions, closure screws and a recessed cable feed with a sealing blank. It clears level ground by 62.02 mm in the 100 mm depth case. The lower gearcase retains the 28.02 mm nominal clearance.
6. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

7. **Native display.** Revision 2 preserves the geometry and placements of 173 physical solid occurrences and three hidden ISO reference solids. The 14 physical layers are:

   - `Display-Implement-Frame` — main crossbeam, long members and motor seat, `#667584`.
   - `Display-Implement-Interface` — hitch lugs and mast, `#C6484D`.
   - `Display-Implement-Working-Surfaces` — fourteen bent tine wear ends, `#4F80A6`.
   - `Display-Implement-Shanks` — fourteen replaceable tine shanks, `#426A83`.
   - `Display-Implement-Separator` — 23 fixed separator rails and two crossrails, `#5D86A0`.
   - `Display-Implement-Guards` — rotor hood, curtains, sealed side gearcase and motor shroud, `#D89A27`.
   - `Display-Implement-Guard-Lids` — removable oil-case lid and motor-shroud ends, `#F2D389`.
   - `Display-Implement-Drive` — gear stock, shaft, rotor and root lugs, `#B99A50`.
   - `Display-Implement-Motors` — gearmotor installation envelope, `#6147A7`.
   - `Display-Implement-Roller` — roller tube, axle and hubs, `#728EA3`.
   - `Display-Implement-Supports` — roller brackets and carriers, `#31BDB2`.
   - `Display-Implement-Pins-and-Locks` — hitch pins and depth-index locks, `#B99DDD`.
   - `Display-Implement-Fasteners` — tine retainers and shroud screws, `#A2A8AF`.
   - `Display-Implement-Power-Access` — recessed gland bulkhead, cable gland and sealing blank, `#9EAFF0`.

8. **Hidden hitch reference.** Three ISO datum solids use `Display-Implement-Reference` in `#788FA0`. Their parent layer `J4-Rotary-Tool-Iso-Reference` remains hidden.

## Technical sources

- [ISO 730:2009+A1:2014, Category 1 hitch interface](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
- [Rapid soil burier working width and depth comparison](https://rapid.ch/fr_CH/enfouisseuse)
