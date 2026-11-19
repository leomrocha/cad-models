THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# deck side supports j3f

1. **Library number:** 24.
2. **Type:** group.
3. **CAD file:** [deck-side-supports-j3f.dwg](<deck-side-supports-j3f.dwg>).
4. **DWG SHA-256:** `651b2df994ea7242d4bd2cdfe0375a3607c1725e2bb2f102d8c850a6052f3d88`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion input. Units: mm. Quantity: 4 per raised J3fdeck. Route:J3f raised deck side support.

### Geometry, datum and interfaces

Proposed 20×20×2 steel tube 216 long, centres X±250,Y±185. Bottom 548 onP04JFT top 548; upper 764. Post Y 175…195 clears Bmw tray outer 168 by 7 and receiver carrier inner 202 by 7. Rear cabinet outer 150 gives 25 gap. Source Jdeck 770 closes withP04JCP3 and ledge 3. Tube is above crown 471 throughout range; body X/Y extensions under 400 wide deck are explicit.

### Source and construction

Parent P04L — Deck support ledge; SKF dimension/source note; current combined proposal. Custom dimensions are proposed. Inspect contact faces, axes, purchased-source revision and exact hardware after cutting/turning/forming.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P04JFT — Deck support horizontal foot | 1 | [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — 122 | `723d7e5f7b57c83177b432391eea337856569ec577c3cf41f9993382848559f2` | `{"position_mm":[-250.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFTV — Deck support vertical leg | 1 | [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — 123 | `94ee558b3e0da6c07a1628b77335daa8b9dde6a90dec62c82ec31c6077ef9298` | `{"position_mm":[-250.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04UPJ20 — Deck upright nominal 20 x 20 x 2 tube | 1 | [Deck side upright nominal section](<../../parts/p04upj20-j-deck-side-upright-20-tube/p04upj20-j-deck-side-upright-20-tube.md>) — 129 | `9c3de00c986b27d0b1eefed4d83a1423ae2118b23b30bef5957010ab979ead46` | `{"position_mm":[-250.0,185.0,548.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JCP — Deck upright top cap | 1 | [Raised deck upright top cap](<../../parts/p04jcp-j-deck-upright-top-cap/p04jcp-j-deck-upright-top-cap.md>) — 120 | `cab45bfd8383f6ee81aa9a89fbccb69cd5a80937f82433e08968f160207063a0` | `{"position_mm":[-250.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFT — Deck support horizontal foot | 1 | [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — 122 | `723d7e5f7b57c83177b432391eea337856569ec577c3cf41f9993382848559f2` | `{"position_mm":[250.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFTV — Deck support vertical leg | 1 | [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — 123 | `94ee558b3e0da6c07a1628b77335daa8b9dde6a90dec62c82ec31c6077ef9298` | `{"position_mm":[250.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04UPJ20 — Deck upright nominal 20 x 20 x 2 tube | 1 | [Deck side upright nominal section](<../../parts/p04upj20-j-deck-side-upright-20-tube/p04upj20-j-deck-side-upright-20-tube.md>) — 129 | `9c3de00c986b27d0b1eefed4d83a1423ae2118b23b30bef5957010ab979ead46` | `{"position_mm":[250.0,185.0,548.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JCP — Deck upright top cap | 1 | [Raised deck upright top cap](<../../parts/p04jcp-j-deck-upright-top-cap/p04jcp-j-deck-upright-top-cap.md>) — 120 | `cab45bfd8383f6ee81aa9a89fbccb69cd5a80937f82433e08968f160207063a0` | `{"position_mm":[250.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFT — Deck support horizontal foot | 1 | [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — 122 | `723d7e5f7b57c83177b432391eea337856569ec577c3cf41f9993382848559f2` | `{"position_mm":[-250.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFTV — Deck support vertical leg | 1 | [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — 123 | `94ee558b3e0da6c07a1628b77335daa8b9dde6a90dec62c82ec31c6077ef9298` | `{"position_mm":[-250.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04UPJ20 — Deck upright nominal 20 x 20 x 2 tube | 1 | [Deck side upright nominal section](<../../parts/p04upj20-j-deck-side-upright-20-tube/p04upj20-j-deck-side-upright-20-tube.md>) — 129 | `9c3de00c986b27d0b1eefed4d83a1423ae2118b23b30bef5957010ab979ead46` | `{"position_mm":[-250.0,-185.0,548.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JCP — Deck upright top cap | 1 | [Raised deck upright top cap](<../../parts/p04jcp-j-deck-upright-top-cap/p04jcp-j-deck-upright-top-cap.md>) — 120 | `cab45bfd8383f6ee81aa9a89fbccb69cd5a80937f82433e08968f160207063a0` | `{"position_mm":[-250.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFT — Deck support horizontal foot | 1 | [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — 122 | `723d7e5f7b57c83177b432391eea337856569ec577c3cf41f9993382848559f2` | `{"position_mm":[250.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JFTV — Deck support vertical leg | 1 | [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — 123 | `94ee558b3e0da6c07a1628b77335daa8b9dde6a90dec62c82ec31c6077ef9298` | `{"position_mm":[250.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04UPJ20 — Deck upright nominal 20 x 20 x 2 tube | 1 | [Deck side upright nominal section](<../../parts/p04upj20-j-deck-side-upright-20-tube/p04upj20-j-deck-side-upright-20-tube.md>) — 129 | `9c3de00c986b27d0b1eefed4d83a1423ae2118b23b30bef5957010ab979ead46` | `{"position_mm":[250.0,-185.0,548.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P04JCP — Deck upright top cap | 1 | [Raised deck upright top cap](<../../parts/p04jcp-j-deck-upright-top-cap/p04jcp-j-deck-upright-top-cap.md>) — 120 | `cab45bfd8383f6ee81aa9a89fbccb69cd5a80937f82433e08968f160207063a0` | `{"position_mm":[250.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. skf sy25tf sy30tf dimensions.
2. skf sy25tf sy30tf dimensions.
3. skf sy25tf sy30tf dimensions.
4. Square steel tube stock family — supplier reference.
5. Weldable steel plate stock family — supplier reference.

## References — local

120. [Raised deck upright top cap](<../../parts/p04jcp-j-deck-upright-top-cap/p04jcp-j-deck-upright-top-cap.md>) — library entry 120.
122. [Raised deck horizontal outrigger foot](<../../parts/p04jft-j-deck-upright-outrigger-foot/p04jft-j-deck-upright-outrigger-foot.md>) — library entry 122.
123. [Raised deck two-hole outrigger vertical leg](<../../parts/p04jftv-j-outboard-foot-vertical-leg/p04jftv-j-outboard-foot-vertical-leg.md>) — library entry 123.
129. [Deck side upright nominal section](<../../parts/p04upj20-j-deck-side-upright-20-tube/p04upj20-j-deck-side-upright-20-tube.md>) — library entry 129.

## Views

1. [deck side supports j3f isometric](<deck-side-supports-j3f-isometric.png>).
