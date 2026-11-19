THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# side lifting supports j3f

1. **Library number:** 49.
2. **Type:** group.
3. **CAD file:** [side-lifting-supports-j3f.dwg](<side-lifting-supports-j3f.dwg>).
4. **DWG SHA-256:** `2d06cf9551fe6440a6abd23f01c0da07c75f11a876be5df78c45858f26ee67bc`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Quantity: 4 per J lifting support.

### Geometry and contacts

Proposed20×20×3 steel tube199 longZ548…747, centresX±180,Y±185. Same8 mm P04JFT horizontal foot and P04JFTV vertical leg as deck supports, placedX±180; this is separate from deck centres±250. PostY175…195 clears trayouter168 by7 mm and rear cabinetcarrierY153.5 by21.5. Reused P10ROOT and tab sit atZ697…757 and707…827 respectively after source-S height translation267; tab eyeZ807 is37 above deck770, outside its usableY±200 edge. Source S lifting-load formula is retained; actual post/foot weld and load-sharing calculation use this revised section.

### Construction

Parent P10 — Side lifting tab; combined installation. Cut/form the proposed geometry, inspect joint contact and hole axes, then check the stated load path.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P04JFT — Lifting support horizontal foot | 1 | [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — 122 | `723d7e5f7b57c83177b432391eea337856569ec577c3cf41f9993382848559f2` | `{"position_mm":[-180.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFTV — Lifting support vertical leg | 1 | [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — 123 | `94ee558b3e0da6c07a1628b77335daa8b9dde6a90dec62c82ec31c6077ef9298` | `{"position_mm":[-180.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JST — Lifting stanchion nominal 20 x 20 x 3 tube | 1 | [J lifting stanchion nominal section](<../../../../../mechanical-parts/components/p10jst-j-outboard-lifting-stanchion/p10jst-j-outboard-lifting-stanchion.md>) — 160 | `d0a04176611a3b72555072443027181f500a9e5b9fbf22d188eb63d7f6b31412` | `{"position_mm":[-180.0,185.0,548.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10ROOT — Lifting tab root doubler | 1 | [Side lifting-tab root doubler](<../../../../../mechanical-parts/components/p10root-lift-tab-root-doubler/p10root-lift-tab-root-doubler.md>) — 162 | `2f39ac7c65689cdcffb11a1f9c4679b7975ff60b7177afcf0b0d5ad051ff62d3` | `{"position_mm":[-180.0,0.0,267.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JT — J lifting tab with diameter 20 mm eye | 1 | [J lifting tab](<../../../../../mechanical-parts/components/p10jt-j-lifting-tab/p10jt-j-lifting-tab.md>) — 161 | `32707443c7df3a1b1dcd3bb520e5fadd9ad2e9e5ec814509f9d8718f1fde4fe0` | `{"position_mm":[-180.0,218.0,707.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JAR — Lifting short arm nominal 40 x 40 x 3 tube | 1 | [J lifting short arm nominal section](<../../../../../mechanical-parts/components/p10jar-j-lifting-tab-short-arm/p10jar-j-lifting-tab-short-arm.md>) — 159 | `eff79ccdee729311f7e011e6909594575ec648f981493be22a14c0d728d44f6f` | `{"position_mm":[180.0,727.0,195.00000000000006],"scale":[0.9999999999999999,1.0,0.9999999999999999],"rotation_radians":3.141592653589793,"normal":[0.0,1.0,6.123233995736766e-17]}` |
| P04JFT — Lifting support horizontal foot | 1 | [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — 122 | `723d7e5f7b57c83177b432391eea337856569ec577c3cf41f9993382848559f2` | `{"position_mm":[180.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFTV — Lifting support vertical leg | 1 | [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — 123 | `94ee558b3e0da6c07a1628b77335daa8b9dde6a90dec62c82ec31c6077ef9298` | `{"position_mm":[180.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JST — Lifting stanchion nominal 20 x 20 x 3 tube | 1 | [J lifting stanchion nominal section](<../../../../../mechanical-parts/components/p10jst-j-outboard-lifting-stanchion/p10jst-j-outboard-lifting-stanchion.md>) — 160 | `d0a04176611a3b72555072443027181f500a9e5b9fbf22d188eb63d7f6b31412` | `{"position_mm":[180.0,185.0,548.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10ROOT — Lifting tab root doubler | 1 | [Side lifting-tab root doubler](<../../../../../mechanical-parts/components/p10root-lift-tab-root-doubler/p10root-lift-tab-root-doubler.md>) — 162 | `2f39ac7c65689cdcffb11a1f9c4679b7975ff60b7177afcf0b0d5ad051ff62d3` | `{"position_mm":[180.0,0.0,267.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JT — J lifting tab with diameter 20 mm eye | 1 | [J lifting tab](<../../../../../mechanical-parts/components/p10jt-j-lifting-tab/p10jt-j-lifting-tab.md>) — 161 | `32707443c7df3a1b1dcd3bb520e5fadd9ad2e9e5ec814509f9d8718f1fde4fe0` | `{"position_mm":[180.0,218.0,707.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JAR — Lifting short arm nominal 40 x 40 x 3 tube | 1 | [J lifting short arm nominal section](<../../../../../mechanical-parts/components/p10jar-j-lifting-tab-short-arm/p10jar-j-lifting-tab-short-arm.md>) — 159 | `eff79ccdee729311f7e011e6909594575ec648f981493be22a14c0d728d44f6f` | `{"position_mm":[-180.0,727.0,195.00000000000006],"scale":[0.9999999999999999,1.0,0.9999999999999999],"rotation_radians":3.141592653589793,"normal":[0.0,1.0,6.123233995736766e-17]}` |
| P04JFT — Lifting support horizontal foot | 1 | [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — 122 | `723d7e5f7b57c83177b432391eea337856569ec577c3cf41f9993382848559f2` | `{"position_mm":[-180.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFTV — Lifting support vertical leg | 1 | [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — 123 | `94ee558b3e0da6c07a1628b77335daa8b9dde6a90dec62c82ec31c6077ef9298` | `{"position_mm":[-180.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JST — Lifting stanchion nominal 20 x 20 x 3 tube | 1 | [J lifting stanchion nominal section](<../../../../../mechanical-parts/components/p10jst-j-outboard-lifting-stanchion/p10jst-j-outboard-lifting-stanchion.md>) — 160 | `d0a04176611a3b72555072443027181f500a9e5b9fbf22d188eb63d7f6b31412` | `{"position_mm":[-180.0,-185.0,548.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10ROOT — Lifting tab root doubler | 1 | [Side lifting-tab root doubler](<../../../../../mechanical-parts/components/p10root-lift-tab-root-doubler/p10root-lift-tab-root-doubler.md>) — 162 | `2f39ac7c65689cdcffb11a1f9c4679b7975ff60b7177afcf0b0d5ad051ff62d3` | `{"position_mm":[-180.0,0.0,267.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JT — J lifting tab with diameter 20 mm eye | 1 | [J lifting tab](<../../../../../mechanical-parts/components/p10jt-j-lifting-tab/p10jt-j-lifting-tab.md>) — 161 | `32707443c7df3a1b1dcd3bb520e5fadd9ad2e9e5ec814509f9d8718f1fde4fe0` | `{"position_mm":[-180.0,-218.0,707.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JAR — Lifting short arm nominal 40 x 40 x 3 tube | 1 | [J lifting short arm nominal section](<../../../../../mechanical-parts/components/p10jar-j-lifting-tab-short-arm/p10jar-j-lifting-tab-short-arm.md>) — 159 | `eff79ccdee729311f7e011e6909594575ec648f981493be22a14c0d728d44f6f` | `{"position_mm":[-180.0,727.0,195.00000000000006],"scale":[1.0,0.9999999999999999,1.0],"rotation_radians":0.0,"normal":[0.0,-1.0,6.123233995736766e-17]}` |
| P04JFT — Lifting support horizontal foot | 1 | [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — 122 | `723d7e5f7b57c83177b432391eea337856569ec577c3cf41f9993382848559f2` | `{"position_mm":[180.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFTV — Lifting support vertical leg | 1 | [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — 123 | `94ee558b3e0da6c07a1628b77335daa8b9dde6a90dec62c82ec31c6077ef9298` | `{"position_mm":[180.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JST — Lifting stanchion nominal 20 x 20 x 3 tube | 1 | [J lifting stanchion nominal section](<../../../../../mechanical-parts/components/p10jst-j-outboard-lifting-stanchion/p10jst-j-outboard-lifting-stanchion.md>) — 160 | `d0a04176611a3b72555072443027181f500a9e5b9fbf22d188eb63d7f6b31412` | `{"position_mm":[180.0,-185.0,548.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10ROOT — Lifting tab root doubler | 1 | [Side lifting-tab root doubler](<../../../../../mechanical-parts/components/p10root-lift-tab-root-doubler/p10root-lift-tab-root-doubler.md>) — 162 | `2f39ac7c65689cdcffb11a1f9c4679b7975ff60b7177afcf0b0d5ad051ff62d3` | `{"position_mm":[180.0,0.0,267.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JT — J lifting tab with diameter 20 mm eye | 1 | [J lifting tab](<../../../../../mechanical-parts/components/p10jt-j-lifting-tab/p10jt-j-lifting-tab.md>) — 161 | `32707443c7df3a1b1dcd3bb520e5fadd9ad2e9e5ec814509f9d8718f1fde4fe0` | `{"position_mm":[180.0,-218.0,707.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P10JAR — Lifting short arm nominal 40 x 40 x 3 tube | 1 | [J lifting short arm nominal section](<../../../../../mechanical-parts/components/p10jar-j-lifting-tab-short-arm/p10jar-j-lifting-tab-short-arm.md>) — 159 | `eff79ccdee729311f7e011e6909594575ec648f981493be22a14c0d728d44f6f` | `{"position_mm":[180.0,727.0,195.00000000000006],"scale":[1.0,0.9999999999999999,1.0],"rotation_radians":0.0,"normal":[0.0,-1.0,6.123233995736766e-17]}` |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

122. [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — library entry 122.
123. [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — library entry 123.
159. [J lifting short arm nominal section](<../../../../../mechanical-parts/components/p10jar-j-lifting-tab-short-arm/p10jar-j-lifting-tab-short-arm.md>) — library entry 159.
160. [J lifting stanchion nominal section](<../../../../../mechanical-parts/components/p10jst-j-outboard-lifting-stanchion/p10jst-j-outboard-lifting-stanchion.md>) — library entry 160.
161. [J lifting tab](<../../../../../mechanical-parts/components/p10jt-j-lifting-tab/p10jt-j-lifting-tab.md>) — library entry 161.
162. [Side lifting-tab root doubler](<../../../../../mechanical-parts/components/p10root-lift-tab-root-doubler/p10root-lift-tab-root-doubler.md>) — library entry 162.

## Views

1. [side lifting supports j3f isometric](<side-lifting-supports-j3f-isometric.png>).
