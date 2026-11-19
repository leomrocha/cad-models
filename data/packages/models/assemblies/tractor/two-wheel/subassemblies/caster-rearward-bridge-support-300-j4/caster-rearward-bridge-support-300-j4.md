THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# caster rearward bridge support 300 j4

1. **Library number:** 19.
2. **Type:** group.
3. **CAD file:** [caster-rearward-bridge-support-300-j4.dwg](<caster-rearward-bridge-support-300-j4.dwg>).
4. **DWG SHA-256:** `b803500f89251485a14a134882e4a23eb857553d41192622509d399e4a2e53dc`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Represented geometry

Nine-piece rearward bridge support: two bridge tubes, four welded root plates, two drop tubes and one upper tie

## Technical specification

Status: Discussion proposal. Units: mm. Route:Rearward caster J4 placement alternative. Quantity: 2 per rearward caster alternative.

### Geometry, datum and interfaces

40×40×3 box tube 135 long X−460…−325; centre Y±150,Z 520; bottom 500/top 540. Front end X−325 contacts rear end of 650 rail; load joint uses explicit external root plates P05JROOT. All arm/cheek/head/pin source-S geometry translates X−240: caster axis−540, primary−460, arm end−335. Arm front end−335 clears cabinet rear−325 by 10. This changes rear support-wheel location and total length; it is a separate placement alternative, not same J3f caste axis−300.

### Source and construction

Parent P05D — Caster frame doubler; current J3f/J4 arrangement. All custom dimensions here are proposed inputs. Cut/turn/form, deburr and inspect stated contact faces, axes and length before assembly.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P05JBR — Left rearward bridge tube | 1 | [Rearward caster raised frame bridge](<../../../../../mechanical-parts/wheels-and-tyres/p05jbr-rearward-caster-raised-frame-bridge/p05jbr-rearward-caster-raised-frame-bridge.md>) — 134 | `8fa9ed8cb308c1249b367009b6cc3f7dfa88ad1f18b748d847cbafe202b7de13` | `{"position_mm":[150.0,520.0,-459.99999999999994],"scale":[1.0,0.9999999999999999,0.9999999999999999],"rotation_radians":-1.5707963267948966,"normal":[1.0,0.0,6.123233995736766e-17]}` |
| P05JBR — Right rearward bridge tube | 1 | [Rearward caster raised frame bridge](<../../../../../mechanical-parts/wheels-and-tyres/p05jbr-rearward-caster-raised-frame-bridge/p05jbr-rearward-caster-raised-frame-bridge.md>) — 134 | `8fa9ed8cb308c1249b367009b6cc3f7dfa88ad1f18b748d847cbafe202b7de13` | `{"position_mm":[-150.0,520.0,-459.99999999999994],"scale":[1.0,0.9999999999999999,0.9999999999999999],"rotation_radians":-1.5707963267948966,"normal":[1.0,0.0,6.123233995736766e-17]}` |
| P05JROOT — Left outer welded root plate | 1 | [Rearward caster bridge root plate, welded branch](<../../../../../mechanical-parts/wheels-and-tyres/p05jroot-rearward-caster-bridge-root-plate/p05jroot-rearward-caster-bridge-root-plate.md>) — 139 | `2a1adf6bd4879c0e3d7031d8c1c25a1b875ba3dd6c5ee4e43fab4d8c4fd594f7` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P05JROOT — Left inner welded root plate | 1 | [Rearward caster bridge root plate, welded branch](<../../../../../mechanical-parts/wheels-and-tyres/p05jroot-rearward-caster-bridge-root-plate/p05jroot-rearward-caster-bridge-root-plate.md>) — 139 | `2a1adf6bd4879c0e3d7031d8c1c25a1b875ba3dd6c5ee4e43fab4d8c4fd594f7` | `{"position_mm":[0.0,-46.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P05JROOT — Right inner welded root plate | 1 | [Rearward caster bridge root plate, welded branch](<../../../../../mechanical-parts/wheels-and-tyres/p05jroot-rearward-caster-bridge-root-plate/p05jroot-rearward-caster-bridge-root-plate.md>) — 139 | `2a1adf6bd4879c0e3d7031d8c1c25a1b875ba3dd6c5ee4e43fab4d8c4fd594f7` | `{"position_mm":[0.0,-300.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P05JROOT — Right outer welded root plate | 1 | [Rearward caster bridge root plate, welded branch](<../../../../../mechanical-parts/wheels-and-tyres/p05jroot-rearward-caster-bridge-root-plate/p05jroot-rearward-caster-bridge-root-plate.md>) — 139 | `2a1adf6bd4879c0e3d7031d8c1c25a1b875ba3dd6c5ee4e43fab4d8c4fd594f7` | `{"position_mm":[0.0,-346.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P05JDP300 — Left bridge drop tube | 1 | [Caster bridge drop 47 mm](<../../../../../mechanical-parts/wheels-and-tyres/p05jdp300-rearward-caster-bridge-drop-300/p05jdp300-rearward-caster-bridge-drop-300.md>) — 138 | `f02cad5c6aa2d50abc4010cf8d1dea8f333ea10b207933206cf6e892316f8a0c` | `{"position_mm":[-380.0,150.0,453.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P05JDP300 — Right bridge drop tube | 1 | [Caster bridge drop 47 mm](<../../../../../mechanical-parts/wheels-and-tyres/p05jdp300-rearward-caster-bridge-drop-300/p05jdp300-rearward-caster-bridge-drop-300.md>) — 138 | `f02cad5c6aa2d50abc4010cf8d1dea8f333ea10b207933206cf6e892316f8a0c` | `{"position_mm":[-380.0,-150.0,453.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P05JCT — Rearward caster upper tie | 1 | [Rearward caster upper tie, 250 mm caster base pose](<../../../../../mechanical-parts/wheels-and-tyres/p05jct-rearward-caster-cheek-upper-tie/p05jct-rearward-caster-cheek-upper-tie.md>) — 135 | `556d7bf97bcb068d635bc72aaa157f4a6bf758ec925d3be5e3bdaa14026afde8` | `{"position_mm":[0.0,0.0,50.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

134. [Rearward caster raised frame bridge](<../../../../../mechanical-parts/wheels-and-tyres/p05jbr-rearward-caster-raised-frame-bridge/p05jbr-rearward-caster-raised-frame-bridge.md>) — library entry 134.
135. [Rearward caster upper tie, 250 mm caster base pose](<../../../../../mechanical-parts/wheels-and-tyres/p05jct-rearward-caster-cheek-upper-tie/p05jct-rearward-caster-cheek-upper-tie.md>) — library entry 135.
138. [Caster bridge drop 47 mm](<../../../../../mechanical-parts/wheels-and-tyres/p05jdp300-rearward-caster-bridge-drop-300/p05jdp300-rearward-caster-bridge-drop-300.md>) — library entry 138.
139. [Rearward caster bridge root plate, welded branch](<../../../../../mechanical-parts/wheels-and-tyres/p05jroot-rearward-caster-bridge-root-plate/p05jroot-rearward-caster-bridge-root-plate.md>) — library entry 139.

## Views

1. [caster rearward bridge support 300 j4 isometric](<caster-rearward-bridge-support-300-j4-isometric.png>).

1. [caster rearward bridge support 300 j4 orthographic](<caster-rearward-bridge-support-300-j4-orthographic.png>).

1. [caster rearward bridge support 300 j4 orthographic](<caster-rearward-bridge-support-300-j4-orthographic.svg>).
