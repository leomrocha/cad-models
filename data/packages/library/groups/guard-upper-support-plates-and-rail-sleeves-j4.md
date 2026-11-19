THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# guard upper support plates and rail sleeves j4

1. **Library number:** 34.
2. **Type:** group.
3. **CAD file:** [guard-upper-support-plates-and-rail-sleeves-j4.dwg](<guard-upper-support-plates-and-rail-sleeves-j4.dwg>).
4. **DWG SHA-256:** `b44b9c470b19965de6fd0742a7dcf1e6d3c6f418440f15d2af1914bfd2d47fdf`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: four per guard, eight per pair.

### Finite geometry and joints


1. **Finished pieces and contact:** each upper mounting flange is a proposed 3 mm steel welded angle, width30 mm along X. At its centre X = xF, vertical sheet occupies X = xF±15, Y =132.7…135.7, Z =465…497 mm. Horizontal foot occupies X = xF±15, Y =132.7…162.7, Z =497…500 mm. The vertical sheet upper face Z497 contacts the foot underside Z497. Join that corner with a proposed continuous 1 mm-leg fillet at the inner corner; its vertical extent starts at Z496, 0.963710 mm above the guard-row washer maximum495.036290. Keep the outer contact faces planar; finished surfaces define the contact planes. The vertical front face Y =135.7 contacts the guard back sheet outer face135.7. The horizontal upper face Z =500 contacts the raised-rail underside500. Mirror Y on the right. These are proposed support contacts derived from the retained J4 rail pose.
2. **Guard-side axes:** one Ø6.5 mm bore normal Y at (X,Z) = (xF,489.036290) mm. Left xF = −110, −40, 40, 110 mm; right xF = −110, 0, 110, 210 mm. Four flanges per guard. At source Ø12 mm washer maximum, highest edge Z495.036290 leaves1.963710 mm below horizontal-foot underside497 mm. Free side distance15−6 =9 mm. These body fixing axes match P16J4BD — back sheet.
3. **Guard-to-flange joint:** proposed four C128 — M6×20 screws, eight C146 — M6 washers and four C152 — M6 nuts per guard. Grip is1.5 mm body+3 mm flange =4.5 mm. With source washer ceilings1.8 mm each, nut ceiling6 mm and proposed2 mm protrusion, required actual length is4.5+3.6+6+2 =16.1 mm. Nominal20 mm gives3.9 mm allowance. Put heads inside the guard, screws pointing inward, and nuts behind the flange. At maximum source washer thickness, head bearing plane Y139 mm, tipY119 mm, rear nut minimumY124.9 mm. Source motor end-faceY115 mm leaves nominal4 mm to that screw tip; actual inequality Y_head_bearing−L>Y_motor_end applies at this upper row. The source motor boxes at this row end atY115; exact protrusions retain their source geometry.
4. **Guard-joint access:** install the flange nuts using radial AF10 open-ended wrench access before refitting the lid. Proposed wrench thickness≤4 mm occupies Y125…129 mm, outward of source motor end115 and inward of raised-rail inner face130. Proposed wrench plan radius≤10 mm around the guard axis gives maximumZ499.036290 mm,0.963710 mm below rail underside500. This is a tool-space proposal for the actual wrench shape and installed hardware; heads are accessed through the removed lid.
5. **Rail joint:** one Ø6.5 mm bore normal Z at (X,Y) = (xF,150) mm through horizontal foot and both40×40×3 mm rail walls. Reuse P22CT34 — Ø12/Ø6.6×34 mm rail sleeve, rotated to axis Z, between the inner rail wallsZ503…537 mm. Install sleeves before rail-end closure. Four sleeves per guard. Proposed rail fixing uses four C129 — M6×55 screws, eight C146 washers and four C152 nuts per guard. Grip is3 mm foot+40 mm rail=43 mm; sleeve is inside that grip. Source maximum stack with two1.8 mm washers,6 mm nut and2 mm protrusion gives54.6 mm required actual length. Nominal55 mm leaves0.4 mm arithmetic allowance; actual supplied length must satisfy L≥43+tW1+tW2+hN+2 mm.
6. **Rail-joint pose and access:** place hex heads below the foot and nuts above the rail. At source washer/head height ceilings, head bottom isZ497−1.8−4.15 =491.05 mm. Guard top wall maximum isT+1.5 =484.536290 mm, giving6.513710 mm vertical separation at Y150. Upper washer occupiesZ540…541.8 mm, nut reaches547.8 mm and nominal tip reaches550.2 mm. The raised battery tray underside575 mm leaves24.8 mm to that tip. Fit the flanges to the rails before installing the guard body and battery tray; for rail-joint service, remove the guard body first. In that assembly state, reserve a proposedØ20 mm socket cylinder at each rail axis with30 mm axial access above the nut and below the head. Local socket maximum radius10 mm atY150 stays inside the rail band130…170. Source/supplied head corners and socket shape control actual access.
7. **Construction identity:** this P16MTJ4 welded upper flange is a J4 proposal distinct from the earlier20×20 mm folded Structural S flange. Its two sheet pieces and weld are individual fabrication children; four instances repeat per guard. The guard-to-flange group and flange-to-rail group are separate connections.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P16MTJ4V — Guard vertical mounting sheet | 1 | [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — 177 | `9c4222325c1a43381495deef3fa1fdf8f2c1e26dccfa6bb3607e3682efd5ad08` | `{"position_mm":[-110.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4F — Guard mounting rail foot | 1 | [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — 176 | `32e9ee73040728b988bf8c1efd2f93c7e8eee7a2c5b0ed52272847137faeafab` | `{"position_mm":[-110.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P22CT34 — Guard vertical rail compression sleeve | 1 | [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — 187 | `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f` | `{"position_mm":[-110.0,150.0,503.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4V — Guard vertical mounting sheet | 1 | [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — 177 | `9c4222325c1a43381495deef3fa1fdf8f2c1e26dccfa6bb3607e3682efd5ad08` | `{"position_mm":[-40.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4F — Guard mounting rail foot | 1 | [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — 176 | `32e9ee73040728b988bf8c1efd2f93c7e8eee7a2c5b0ed52272847137faeafab` | `{"position_mm":[-40.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P22CT34 — Guard vertical rail compression sleeve | 1 | [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — 187 | `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f` | `{"position_mm":[-40.0,150.0,503.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4V — Guard vertical mounting sheet | 1 | [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — 177 | `9c4222325c1a43381495deef3fa1fdf8f2c1e26dccfa6bb3607e3682efd5ad08` | `{"position_mm":[40.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4F — Guard mounting rail foot | 1 | [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — 176 | `32e9ee73040728b988bf8c1efd2f93c7e8eee7a2c5b0ed52272847137faeafab` | `{"position_mm":[40.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P22CT34 — Guard vertical rail compression sleeve | 1 | [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — 187 | `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f` | `{"position_mm":[40.0,150.0,503.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4V — Guard vertical mounting sheet | 1 | [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — 177 | `9c4222325c1a43381495deef3fa1fdf8f2c1e26dccfa6bb3607e3682efd5ad08` | `{"position_mm":[110.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4F — Guard mounting rail foot | 1 | [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — 176 | `32e9ee73040728b988bf8c1efd2f93c7e8eee7a2c5b0ed52272847137faeafab` | `{"position_mm":[110.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P22CT34 — Guard vertical rail compression sleeve | 1 | [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — 187 | `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f` | `{"position_mm":[110.0,150.0,503.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4V — Guard vertical mounting sheet | 1 | [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — 177 | `9c4222325c1a43381495deef3fa1fdf8f2c1e26dccfa6bb3607e3682efd5ad08` | `{"position_mm":[-110.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4F — Guard mounting rail foot | 1 | [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — 176 | `32e9ee73040728b988bf8c1efd2f93c7e8eee7a2c5b0ed52272847137faeafab` | `{"position_mm":[-110.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P22CT34 — Guard vertical rail compression sleeve | 1 | [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — 187 | `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f` | `{"position_mm":[-110.0,-150.0,503.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4V — Guard vertical mounting sheet | 1 | [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — 177 | `9c4222325c1a43381495deef3fa1fdf8f2c1e26dccfa6bb3607e3682efd5ad08` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4F — Guard mounting rail foot | 1 | [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — 176 | `32e9ee73040728b988bf8c1efd2f93c7e8eee7a2c5b0ed52272847137faeafab` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P22CT34 — Guard vertical rail compression sleeve | 1 | [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — 187 | `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f` | `{"position_mm":[0.0,-150.0,503.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4V — Guard vertical mounting sheet | 1 | [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — 177 | `9c4222325c1a43381495deef3fa1fdf8f2c1e26dccfa6bb3607e3682efd5ad08` | `{"position_mm":[110.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4F — Guard mounting rail foot | 1 | [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — 176 | `32e9ee73040728b988bf8c1efd2f93c7e8eee7a2c5b0ed52272847137faeafab` | `{"position_mm":[110.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P22CT34 — Guard vertical rail compression sleeve | 1 | [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — 187 | `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f` | `{"position_mm":[110.0,-150.0,503.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4V — Guard vertical mounting sheet | 1 | [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — 177 | `9c4222325c1a43381495deef3fa1fdf8f2c1e26dccfa6bb3607e3682efd5ad08` | `{"position_mm":[210.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P16MTJ4F — Guard mounting rail foot | 1 | [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — 176 | `32e9ee73040728b988bf8c1efd2f93c7e8eee7a2c5b0ed52272847137faeafab` | `{"position_mm":[210.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P22CT34 — Guard vertical rail compression sleeve | 1 | [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — 187 | `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f` | `{"position_mm":[210.0,-150.0,503.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
3. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.

## References — local

176. [J4 guard mounting rail foot](<../parts/mechanical/p16mtj4f-j4-guard-flange-rail-foot.md>) — library entry 176.
177. [J4 guard vertical mounting sheet](<../parts/mechanical/p16mtj4v-j4-guard-flange-vertical-sheet.md>) — library entry 177.
187. [M6 rail compression sleeve](<../parts/mechanical/p22ct34-m6-rail-compression-sleeve.md>) — library entry 187.

## Views

1. [guard upper support plates and rail sleeves j4 isometric](<../images/guard-upper-support-plates-and-rail-sleeves-j4-isometric.png>).
