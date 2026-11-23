# Category 1 pivoting light bucket

Front light bucket with a replaceable wear lip, pinned hinge, actuator envelope and transport lock.

1. **CAD file.** [DWG 2018](j4-front-category1-pivoting-light-bucket.dwg). SHA-256 `1a347a3da3b272319e36720f8417b7d8dd06dcdb53aac464919c626a81b4536b`.
2. **Geometry and design case.** The modeled wear lip is 608 mm wide. The linkage screen uses a 15 kg assumed payload, 119.25 mm actuator stroke and 3.44 kN peak axial force. The screened vehicle configuration uses front rolling supports.
3. **View.** [OpenCADStudio isometric](open-cad-studio-isometric.png).

4. **Native display.** Revision 2 preserves the original geometry, placements and visibility. OpenCADStudio verified effective layers and RGB values for 37 physical occurrences, isolated the six physical groups and restored normal visibility.

   - `Display-Implement-Frame` — crossbeam wings, mast tie and stop supports, `#667584`.
   - `Display-Implement-Interface` — lower lugs, mast cheeks and pivot bearings, `#C6484D`.
   - `Display-Implement-Bodies` — folded bucket shell and two cheeks, `#929FB6`.
   - `Display-Implement-Working-Surfaces` — replaceable cutting lip, `#4F80A6`.
   - `Display-Implement-Drive` — actuator rod, cylinder and clevis geometry, `#B99A50`.
   - `Display-Implement-Pins-and-Locks` — hinge pins, stop blocks, lock ears and retention hardware, `#B99DDD`.

5. **Interface reference.** Three ISO Category 1 reference solids use `Display-Implement-Reference` in `#788FA0`. Their parent insert layer `J4-Bucket-Iso-Reference` retains its hidden state.

## Technical sources

- [ISO 730:2009+A1:2014 Category 1 dimensions](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso%3A730%3Aed-1%3Av1%3Aen)
