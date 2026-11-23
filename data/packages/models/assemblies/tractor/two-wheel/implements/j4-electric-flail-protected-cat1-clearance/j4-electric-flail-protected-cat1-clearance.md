# Guarded electric flail

Category 1 electric flail with a guarded rotor, belt, recessed motor and rear gauge roller.

1. **CAD file.** [DWG 2018](j4-electric-flail-protected-cat1-clearance.dwg). SHA-256 `484d71f4147f8e5f6f3290f2e06262b4b31783b96023429db7af3c6905392c15`.
2. **Geometry and design case.** Twenty-four knives occupy twelve opposing rotor stations. A removable cover encloses the motor. Lower shoulders span 683 mm and lower pins are Ø22 mm. The conservative working-position tip height is 35 mm.
3. **Lower joint clearance.** The 681 mm crossmember overlaps each lug by 9 mm and leaves a nominal 1 mm lateral gap at each seated ball face. Native readback preserves the motor, shafts, lower pins, keeper cross-drills and working roller geometry.
4. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

5. **Native display.** Revision 2 retains native geometry and exact placements for all 146 solid occurrences. OpenCADStudio verified and isolated the eleven functional groups and restored normal visibility. Five inherited part labels now identify both lower pins, their two retainer spacers and the height roller shaft.

   - `Display-Implement-Frame` — side cheeks, bearing plates and motor mounting plate, `#667584`.
   - `Display-Implement-Interface` — Category 1 crossmember, ears and mast, `#C6484D`.
   - `Display-Implement-Guards` — rigid hoods, flexible skirts, drive returns and motor shroud, `#D89A27`.
   - `Display-Implement-Guard-Lids` — removable lids and storage cable-entry blank, `#F2D389`.
   - `Display-Implement-Drive` — rotor, pulley registers and knife pivot lugs, `#B99A50`.
   - `Display-Implement-Belts` — belt envelope, `#654632`.
   - `Display-Implement-Motors` — source-linked motor reference, `#6147A7`.
   - `Display-Implement-Working-Surfaces` — 24 hinged knives, `#4F80A6`.
   - `Display-Implement-Pins-and-Locks` — hitch and knife pins, and lower-pin spacers, `#B99DDD`.
   - `Display-Implement-Supports` — rear roller bearing brackets and side frame splices, `#31BDB2`.
   - `Display-Implement-Roller` — height roller barrel, hubs and shaft, `#728EA3`.

## Technical sources

- [ISO 730:2009+A1:2014 Category 1 dimensions](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
- [Rapid flail mower working width reference](https://rapid.ch/fr_CH/debroussailleuses-a-fleaux)
