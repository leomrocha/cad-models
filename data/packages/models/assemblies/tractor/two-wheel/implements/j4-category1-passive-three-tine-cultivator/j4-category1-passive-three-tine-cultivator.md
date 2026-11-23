# Category 1 three-tine cultivator

**Representation.** Native assembly of a passive rear cultivator with three replaceable shares.

1. **CAD.** [DWG 2018](j4-category1-passive-three-tine-cultivator.dwg). SHA-256 `736c1ca7d65294704b83e2bd35c7af41c9584ec84cb384672cca52d079f10e02`.
2. **Working components.** Three 24 mm wide welded shanks on 225 mm centres. Each shank carries an 88 mm wide share and two M10 fasteners. The assembly has 30 designed solid occurrences, with the source reference on a separate hidden layer.
3. **Hitch.** Category 1, 683 mm lower shoulder span, 460 mm mast height, nominal Ø22 mm lower pins and Ø19 mm upper pin. The upper yoke has a 52 mm opening. The lower keeper axes are 49 mm from the respective shoulders.
4. **Design screen.** With an assumed 3 kN straight obstruction load per tine, the shank weld calculation gives 166.9 MPa against a provisional 193.6 MPa limit. The static screen uses assumed steel with a minimum yield stress of 355 MPa and a 4.2 mm effective weld throat. The calculated assembly mass is 29.5 kg at 7,850 kg/m³ for the modeled steel sections.
5. **Datums.** Millimetres, X outward from the rear hitch, Y transverse, Z up. The origin is the midpoint of the lower pin axes. The rear linkage fit calculation covers 361 straight pitch configurations.
6. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

7. **Native display.** Revision 2 preserves the 30 physical solid occurrences and the three hidden ISO reference solids at their original placements. OpenCADStudio verified the six physical layer groups:

   - `Display-Implement-Frame` — crossbeam and mast tie, `#667584`.
   - `Display-Implement-Interface` — lower lugs and mast cheeks, `#C6484D`.
   - `Display-Implement-Shanks` — three welded shanks, `#426A83`.
   - `Display-Implement-Working-Surfaces` — three replaceable shares, `#4F80A6`.
   - `Display-Implement-Pins-and-Locks` — hitch pins and retainer shafts, `#B99DDD`.
   - `Display-Implement-Fasteners` — six M10 bolts and six nuts, `#A2A8AF`.

8. **Hidden interface reference.** Three solids use `Display-Implement-Reference` in `#788FA0`. Their parent layer `J4-Cultivator-ISO730-Reference` remains hidden.

## Technical source

- [ISO 730:2009+A1:2014, Category 1 reference dimensions](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
