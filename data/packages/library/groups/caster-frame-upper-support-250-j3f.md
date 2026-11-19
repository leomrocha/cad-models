THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# caster frame upper support 250 j3f

1. **Library number:** 16.
2. **Type:** group.
3. **CAD file:** [caster-frame-upper-support-250-j3f.dwg](<caster-frame-upper-support-250-j3f.dwg>).
4. **DWG SHA-256:** `77478f22851697ce21d8758a0eb00ee35e29ed703a7f3a65358303c52340a6a4`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Quantity: 1 per retained-axis J3f caster.

### Geometry, datum and interfaces

Steel 120 X×340 Y×10 plate,X−300…−180,Y±170. ForC017 source height branch underside 393/top 403; forC016 underside 443/top 453. Same manufactured geometry translates 50 Z. Cheek top edge 393/443 and X−265…−85 overlaps underside by 85 mm X length; exact contact on paired cheek 8 mm thickness supplies weld lands. Four 30 square drop posts centred X−280/−200,Y±150 contact upper face. Reuse P05JDP25097 cut for source 250 orP05JDP30047 cut for source 300, four instances. Post stop 500 contacts raised rail underside 500. Cabinet bottom 550 clears upper post/frame; tie front edge−180 is 49.5 behind left motor box start−130.5. Source caster head axis−300 and primary−220 are retained. This high tie replaces lowP05D273…283 plate only in this J3f mount. Stationary cheek/web head plate-relief cut remains part of zero-setting assembly.

### Construction

Parent P05D — Caster frame doubler; J3f placement. Custom dimensions are proposed. Cut/turn, deburr and inspect lengths, contact faces and hole axes.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P05JCT0 — Caster upper tie | 1 | [Same-axis caster raised-frame upper tie](<../parts/mechanical/p05jct0-same-axis-caster-raised-frame-upper-tie.md>) — 136 | `5a5468271ed29d60ea5c9bc08861ee4e9cda53e5c48405b6b508428ccbf11f97` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Caster drop at [-280, -150] | 1 | [Caster bridge drop 97 mm](<../parts/mechanical/p05jdp250-rearward-caster-bridge-drop-250.md>) — 137 | `6acf9542fd96267b82a6f455b697375189f1c2d936c727db2ac409c6b10b3f28` | `{"position_mm":[-280.0,-150.0,403.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Caster drop at [-280, 150] | 1 | [Caster bridge drop 97 mm](<../parts/mechanical/p05jdp250-rearward-caster-bridge-drop-250.md>) — 137 | `6acf9542fd96267b82a6f455b697375189f1c2d936c727db2ac409c6b10b3f28` | `{"position_mm":[-280.0,150.0,403.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Caster drop at [-200, -150] | 1 | [Caster bridge drop 97 mm](<../parts/mechanical/p05jdp250-rearward-caster-bridge-drop-250.md>) — 137 | `6acf9542fd96267b82a6f455b697375189f1c2d936c727db2ac409c6b10b3f28` | `{"position_mm":[-200.0,-150.0,403.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| Caster drop at [-200, 150] | 1 | [Caster bridge drop 97 mm](<../parts/mechanical/p05jdp250-rearward-caster-bridge-drop-250.md>) — 137 | `6acf9542fd96267b82a6f455b697375189f1c2d936c727db2ac409c6b10b3f28` | `{"position_mm":[-200.0,150.0,403.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

136. [Same-axis caster raised-frame upper tie](<../parts/mechanical/p05jct0-same-axis-caster-raised-frame-upper-tie.md>) — library entry 136.
137. [Caster bridge drop 97 mm](<../parts/mechanical/p05jdp250-rearward-caster-bridge-drop-250.md>) — library entry 137.

## Views

1. [caster frame upper support 250 j3f isometric](<../images/caster-frame-upper-support-250-j3f-isometric.png>).
