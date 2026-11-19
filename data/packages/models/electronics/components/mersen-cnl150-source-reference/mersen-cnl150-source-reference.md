THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Battery fuse CNL150

1. **Library number:** 105.
2. **Type:** part.
3. **CAD file:** [mersen-cnl150-source-reference.dwg](<mersen-cnl150-source-reference.dwg>).
4. **DWG SHA-256:** `68518206529a3df6ad21d83a777cb8a71f28299df938542f5451a4c6c2b8cf7e`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Battery fuse CNL150 — C065.

## Technical specification

CAD input sheet; manufacturer component reference. Group: electrical. Route: Mersen fuse alternative. Quantity: Per protection proposal.

### Geometry and provenance

Mersen drawing 700866, revision G, page 1/1, lists CNL150 in its catalog table. Its printed metric outline length is 80.70 mm. The 2025 family datasheet gives 80.9 mm; preserve each value with its source revision.

### Units and local datum

Units: mm. Origin: terminal contact plane and long axis.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates source-compatible C031 holder and actual terminal stack.

### Space and access

Reserve cover and fuse replacement tools.

### Retained manufacturer outline and model — revision G

1. **Original drawing:** Mersen 700866 PDF, revision G, page 1/1. Revision table date 30 October 2024; title-block drawing/check dates 5 November 2024. CNL150 appears explicitly in the catalog-number table. The sheet is labelled outline dimensions, with a production-use restriction. Use it as the source component outline.
2. **Drawing metric dimensions:** overall longitudinal length 80.70 mm; distance between terminal-slot semicircle centres 61.70 mm; body longitudinal extent 37.34 mm; terminal tongue width 19.05 mm; body width 22.60 mm; two open-slot end diameters 8.74 mm; terminal thickness 1.27 mm; side-view overall body thickness 11.43 mm. These are printed manufacturer values on revision G. The slot openings have different directions in the shown views; retain the original source geometry when importing.
3. **Local datum proposal:** fuse long axis is v; terminal transverse direction is u; n is normal to the terminal contact plane. Put the midpoint of the two source terminal-slot centres at u=v=0. Their nominal coordinates are (u,v)=(0,−30.85) and (0,30.85) mm, calculated from the printed 61.70 mm spacing. Identify the actual planar contact surface on the source model before assigning n=0. Record the source-to-part rigid transform.
4. **Existing manufacturer model:** 700866 STEP is already retained in the C031 acquisition folder. The retained source identity record identifies it as the CNL/CNN fuse model and records its original manufacturer URL. Reuse the original model for the C065 fuse component. The CAD inventory already links mersen-cnl150-source-reference.dwg. Its CAD source review records the 19-solid import and save/reopen result. Source STEP uses inch conversion-based units; the native drawing uses millimetre document units. Reuse that existing source-reference drawing and preserve its import transform. Named feature measurements have their recorded CAD-check state.
5. **Original integrity:** PDF SHA-256 64fb3ca61ce04d88b039a2c58ea5f12a3fd876837efc567253470173e158eb45; STEP SHA-256 990e77d5bd9cb8867b003757f9bb59bdcd940cc1b7c6771e1b3028beae03c658. Both hashes were compared against the retained files on 13 November 2026. The PDF was rendered and visually inspected locally. Originals stay in their existing paths.
6. **CAD checks:** measure source envelope, two slot centres, terminal/contact thickness and contact-face normals after import. Compare these features with revision G, retain the manufacturer component boundary and record any conflict with the 2025 family-datasheet rounding. Installed holder and terminal hardware use their own mating geometry.

## Sources — online

1. Mersen CNL150 drawing.
