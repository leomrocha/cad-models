THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# frame core raised j3f

1. **Library number:** 27.
2. **Type:** group.
3. **CAD file:** [frame-core-raised-j3f.dwg](<frame-core-raised-j3f.dwg>).
4. **DWG SHA-256:** `6e8fde3c690850d086a05f1ca5388ee926d8e0c0b6eb4289caece7c74a91a8ef`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:J3f raised-frame discussion proposal. Quantity: 1 per J3f.

### Geometry, datum and interfaces

Proposed steel rectangular tube 20 X×40 Z×3 wall, cut 260 long Y±130. Centre X 315/Z 520; bounds X 305…325,Z 500…540. Ends contact rail inner faces Y±130. Proposed calculation grade S355, E 210 GPa; actual certified stock/radii remain distinct source properties. Right moving motor plate ends X 300, giving 5 mm static plan gap. Right fixed backbone ends X 300 in this branch. Rear/middle crossmembers retain 40×40×3 cut 260 at X−305/−200. This narrow front section is a model able proposal subject to beam/joint load screen.

### Source and construction

Parent P02 — Main frame crossmember; current J3f/J4 arrangement. All custom dimensions here are proposed inputs. Cut/turn/form, deburr and inspect stated contact faces, axes and length before assembly.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P01J650 — Left raised longitudinal rail | 1 | [Raised J frame longitudinal rail](<../../../../../mechanical-parts/components/p01j650-raised-j-frame-longitudinal-rail/p01j650-raised-j-frame-longitudinal-rail.md>) — 112 | `f27495f31ba3f9cce1f41654f612c2934f13e11a46a779067e3840149de0fdad` | `{"position_mm":[150.0,520.0,-324.99999999999994],"scale":[1.0,0.9999999999999999,0.9999999999999999],"rotation_radians":-1.5707963267948966,"normal":[1.0,0.0,6.123233995736766e-17]}` |
| P01J650 — Right raised longitudinal rail | 1 | [Raised J frame longitudinal rail](<../../../../../mechanical-parts/components/p01j650-raised-j-frame-longitudinal-rail/p01j650-raised-j-frame-longitudinal-rail.md>) — 112 | `f27495f31ba3f9cce1f41654f612c2934f13e11a46a779067e3840149de0fdad` | `{"position_mm":[-150.0,520.0,-324.99999999999994],"scale":[1.0,0.9999999999999999,0.9999999999999999],"rotation_radians":-1.5707963267948966,"normal":[1.0,0.0,6.123233995736766e-17]}` |
| P02 — Rear crossmember | 1 | [Main frame crossmember](<../../../../../mechanical-parts/components/p02-main-frame-crossmember-reference/p02-main-frame-crossmember-reference.md>) — 114 | `f2cd4fdf0b6f1c7b2ddc58fbbe1f9680c92ecac4fee7365acececf92c55104c2` | `{"position_mm":[305.0,520.0,-129.99999999999997],"scale":[0.9999999999999999,1.0,0.9999999999999999],"rotation_radians":3.141592653589793,"normal":[0.0,1.0,6.123233995736766e-17]}` |
| P02 — Middle crossmember | 1 | [Main frame crossmember](<../../../../../mechanical-parts/components/p02-main-frame-crossmember-reference/p02-main-frame-crossmember-reference.md>) — 114 | `f2cd4fdf0b6f1c7b2ddc58fbbe1f9680c92ecac4fee7365acececf92c55104c2` | `{"position_mm":[200.0,520.0,-129.99999999999997],"scale":[0.9999999999999999,1.0,0.9999999999999999],"rotation_radians":3.141592653589793,"normal":[0.0,1.0,6.123233995736766e-17]}` |
| P02JF — Narrow front crossmember | 1 | [J front narrow crossmember](<../../../../../mechanical-parts/components/p02jf-j-front-narrow-crossmember/p02jf-j-front-narrow-crossmember.md>) — 115 | `cb2075536d1391cbae7ffd5a4b1cd9ac47f711adad08933f1a2d14a025140e0e` | `{"position_mm":[-315.0,520.0,-129.99999999999997],"scale":[0.9999999999999999,1.0,0.9999999999999999],"rotation_radians":3.141592653589793,"normal":[0.0,1.0,6.123233995736766e-17]}` |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

112. [Raised J frame longitudinal rail](<../../../../../mechanical-parts/components/p01j650-raised-j-frame-longitudinal-rail/p01j650-raised-j-frame-longitudinal-rail.md>) — library entry 112.
114. [Main frame crossmember](<../../../../../mechanical-parts/components/p02-main-frame-crossmember-reference/p02-main-frame-crossmember-reference.md>) — library entry 114.
115. [J front narrow crossmember](<../../../../../mechanical-parts/components/p02jf-j-front-narrow-crossmember/p02jf-j-front-narrow-crossmember.md>) — library entry 115.

## Views

1. [frame core raised j3f isometric](<frame-core-raised-j3f-isometric.png>).
