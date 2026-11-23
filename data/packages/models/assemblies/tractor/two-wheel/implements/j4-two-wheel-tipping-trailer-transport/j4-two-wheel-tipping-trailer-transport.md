# Two-wheel tipping trailer, transport configuration

**Representation.** Single-axle tipping trailer with hinged bin, transport retention, stowed rear supports and a source-pattern square drawbar.

1. **CAD, revision 2.** [DWG 2018](j4-two-wheel-tipping-trailer-transport.dwg). SHA-256 a8be9da41de4e515041731a1a1d30991bf35e367df31701f3ec2d30f22e5aba6.
2. **Construction.** The closed bin sits on a single-axle chassis with a pinned rear hinge, two transport lock pins, retained tailgate and stowed rear supports. Two Trelleborg T539 tyre derivatives reproduce the retained tread at the checked wheel centres. Proposed hubs use the retained nominal 4 × 100 mm wheel fixing pattern.
3. **Geometry.** A 50 × 50 × 4 mm proposed drawbar uses two vertical Ø12.5 mm axes 90 mm apart. Steelpress specifies a Class A Ø50 mm coupling ball and 430 ±35 mm coupling height for the illustrated level loading condition. The 440.676 mm ball-height datum and its position relative to the bore pair are engineering placement estimates. The production coupling, matched wheel, locking stack and validated structure require measured and rated components.
4. **Coupling assembly.** The nominal square drawbar seats in the traced Steelpress envelope with 0.25 mm per-face and 0.5 mm end clearances. The two M12 bolt stacks include internal support sleeves. The traced handle clears the modeled bolt heads by 34.78 mm.
5. **Datums.** Millimetres. X forward, Y left, Z up. Origin on the nominal ground plane below the trailer ball reference.
6. **Native inspection.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

7. **Display.** Twelve functional layers separate the trailer systems. Revision 2 restores 67 names from the construction receipt. The 516 solid occurrences, poses and definition memberships match revision 1.

## Native display layers

1. **Tipping actuator envelopes and their supports.** `Display-Implement-Actuators` · `#6147A7`.
2. **Axle tube, spindles and spindle sleeves.** `Display-Implement-Axles` · `#4F80A6`.
3. **Hub bearing envelopes.** `Display-Implement-Bearings` · `#13877D`.
4. **Tipping bin and tailgate.** `Display-Implement-Bodies` · `#929FB6`.
5. **Steelpress shell and handle fit envelopes.** `Display-Implement-Coupler-Envelope` · `#C6484D`.
6. **Drawbar fitting bolts, nuts, washers and support sleeves.** `Display-Implement-Fasteners` · `#A2A8AF`.
7. **Chassis, drawbar and axle saddles.** `Display-Implement-Frame` · `#667584`.
8. **Fixed hinge brackets and moving hinge bushes.** `Display-Implement-Hinges` · `#4C8070`.
9. **Four-stud hub flanges.** `Display-Implement-Hubs` · `#2859BC`.
10. **Hinge pins, keepers, gate catches and transport locks.** `Display-Implement-Pins-and-Locks` · `#B99DDD`.
11. **Rear stabilizer sockets, braces and stowed leg envelopes.** `Display-Implement-Supports` · `#31BDB2`.
12. **T539 casing and tread solids.** `Display-Implement-Tyres` · `#30343B`.

## Technical sources

- [Trelleborg tyre technical manual, printed page 221](https://www.trelleborg-tires.com/-/media/tires-aft/datatsheet/technical-manual/trelleborg-technical-manual-en.pdf?hash=AB0C897622FFD6443624A33BDFA5552E&rev=258948143820400e9a05c5a63b8c7ae0&sc_lang=en#page=111)
- [Knott steel rim dimensional catalogue](https://www.knott-trailer.co.uk/catalogs/Katalog2018Downloadversion-Regenstauf.pdf#page=7)
- [Steelpress coupling catalogue, page 22](https://www.spp.net.pl/wp-content/uploads/2015/12/katalog-glowic-2016.pdf#page=22)
- [Steelpress coupling installation manual, Figure A and Figure B](https://www.spp.net.pl/wp-content/uploads/2025/04/Manual_ZSK_BC_EN_DE_FR_PL_scalona.pdf#page=1)
