# Category 1 adjustable ridger

**Representation.** Passive ridger with a replaceable central share and two width-adjustable 25° moldboards.

1. **CAD.** [Editable DWG 2018](j4-category1-ridger.dwg). SHA-256 `9abea40d56e633ccb005d1c95e22432222aa1f9fbb78aaa3eaee4c441af3cd95`. Native geometry checks passed for 49 named parts.
2. **Construction.** A four-bolt replaceable tapered nose seats on its own support. Two independently removable inclined moldboards attach to three-position guide carriages. Each guide has paired M12 locking positions 145, 190 and 235 mm from centre. The default geometry is 190 mm per side.
3. **Geometry.** Nominal projected widths are 553, 643 and 733 mm. The moldboards are inclined 25°. The straight nominal rear pitch comparison reaches 80 mm leading-share penetration. Soil loads and stock material are separate, and the design uses explicit assumed static cases.
4. **Datums.** Millimetres. X outward from the implement connection, Y transverse, Z up. Origin at the lower pin-axis midpoint.
5. **Native inspection.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

6. **Native display.** Revision 2 preserves the 49 physical solid occurrences, the selected 190 mm side setting and the three hidden ISO reference solids. OpenCADStudio verified the seven physical groups:

   - `Display-Implement-Frame` — crossbeam, mast tie, shank, nose seat and wing stays, `#667584`.
   - `Display-Implement-Interface` — lower hitch lugs and mast cheeks, `#C6484D`.
   - `Display-Implement-Working-Surfaces` — replaceable central share, `#4F80A6`.
   - `Display-Implement-Moldboards` — both inclined soil-deflecting wings, `#548E91`.
   - `Display-Implement-Adjustment` — width guides, carriages and moldboard seats, `#B99A50`.
   - `Display-Implement-Pins-and-Locks` — hitch pins, keepers and M12 width locks, `#B99DDD`.
   - `Display-Implement-Fasteners` — nose and moldboard heads and nuts, `#A2A8AF`.

7. **Hidden interface reference.** The three ISO reference solids use `Display-Implement-Reference` in `#788FA0`. Their parent layer `Reference-Category1-ISO730` remains hidden.

## Technical sources

- [ISO 730:2009+A1:2014, Category 1 hitch dimensions](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
