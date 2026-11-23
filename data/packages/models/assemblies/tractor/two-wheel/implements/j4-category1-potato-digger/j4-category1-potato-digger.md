# Category 1 potato digger

**Representation.** Passive potato digger with an inclined replaceable share, two height settings and seven individually retained sifting tines.

1. **CAD.** [Editable DWG 2018](j4-category1-potato-digger.dwg). SHA-256 `5cd6124f5c808a367df7f1aef88f54334c14d6c3f8ecf86f0477e2748c17f65a`.
2. **Construction.** A replaceable 18° share uses four M12 fastener envelopes. Two pinned side carriers provide 0 and −30 mm height settings. Seven sifting tines run through aligned Ø16.5 mm holes in two 18 mm guide plates. Separate keeper pins fit in the 12 mm service gap between the plates.
3. **Geometry.** The 384 mm wide share feeds seven Ø16 mm rods at 48 mm pitch, with 32 mm gap between adjacent rods. The nominal pitch screen targets 140 mm leading-share penetration. The tines, rail, welds and hardware use proposal dimensions.
4. **Datums.** Millimetres. X outward from the implement connection, Y transverse, Z up. Origin at the lower pin-axis midpoint.
5. **Native inspection.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

6. **Native display.** Revision 2 preserves the 68 physical solid occurrences, their positions and the three hidden ISO reference solids. OpenCADStudio verified the seven physical groups:

   - `Display-Implement-Frame` — crossbeam, mast tie, shanks, tine guide plates and spacers, `#667584`.
   - `Display-Implement-Interface` — lower hitch lugs and mast cheeks, `#C6484D`.
   - `Display-Implement-Working-Surfaces` — replaceable digging share, `#4F80A6`.
   - `Display-Implement-Sifting-Tines` — seven Ø16 mm sifting rods, `#548E91`.
   - `Display-Implement-Adjustment` — share seat and height carriages, `#B99A50`.
   - `Display-Implement-Pins-and-Locks` — hitch pins, height locks and tine-keeper hardware, `#B99DDD`.
   - `Display-Implement-Fasteners` — share bolt heads and nuts, `#A2A8AF`.

7. **Hidden interface reference.** Three ISO datum solids use `Display-Implement-Reference` in `#788FA0`. Their parent layer `Reference-Category1-ISO730` remains hidden.

## Technical sources

- [ISO 730:2009+A1:2014, Category 1 hitch dimensions](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
