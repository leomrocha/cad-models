THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# front attachment lower cheeks and mast s

1. **Library number:** 33.
2. **Type:** group.
3. **CAD file:** [front-attachment-lower-cheeks-and-mast-s.dwg](<front-attachment-lower-cheeks-and-mast-s.dwg>).
4. **DWG SHA-256:** `f5f56e5e9d26cacdfa00a94afe2a4691d5e82be31641a537abec231808e2b738`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Represented geometry

Seven source-proposal support solids: doubler, two upper tabs, mast seat, mast tube and two lower cheeks. Structural S coordinates; crossmember face X300 mm and top Z273 mm.

## Technical specification

CAD input sheet; custom proposal. Group: attachments. Route: Front mount proposal. Quantity: Each distinct front plate separately.

### Geometry and provenance

Existing stock proposal 10 mm pin plates/8 mm support doubler. Exact front mating geometry follows project front-interface source; keep front linkage context explicit.

### Units and local datum

Units: mm. Datum A: front mounting plane; B: lower interface axis; C: base centreline.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates front structural support and actual tool pins/linkage. Preserve exact standard category/edition andsource drawing.

### Space and access

Keep top deck usable, side-mounted services accessible and tool/pin removal clear.

### Custom construction

Cut, fixture, drill/ream source interface, fit pin retention.

### Chassis-side attachment support variant S — 13 November 2026

**PROPOSAL**, mm: two 10 mm steel lower carrier cheeks, each 120 X×100 Z, proposed chassis-side boreØ22.5 centred 50 mm above lower edge and 60 mm from either X edge. Lower edge Z 273; local bore Z 323. Locate pair at Y±100 on matching doubler; nominal cheek inner separation 190 if plates centred Y±100. Add 6 mm triangular 100×80 braces to frame/doubler. Front plate bounds X 308…428; rear mirror X−428…−308. Proposed chassis bore axes are Y; local centre X±368. Upper support blank 10 mm thick,100 Y×120 Z, source-mating hole diameter/position retained as parameter dTOP/(uTOP,vTOP); mount at frame-centre Y 0 on separately drawn mast. These are chassis support datums, with linkage members continuing to implement-side datums.

Source reference in existing mechanical-connections/README.md: ISO 730:2009; ISO 8759-4:2018 front power-lift scope excludes two-direction tractors and directs those cases to ISO 730. Existing rear reference retains Cat 1 shoulder span 683±1.5 and mast 460±1.5 with C063/C064 component references. Preserve exact standard shoulder/ball datums; do not apply 683 to these 190 mm chassis cheek spacing. Implement-side linkage transformation is a separate proposed parameter set. For a direct rigid frame carrying that standard reference, lower shoulder planes Y±341.5 and upper mast reference 460 above lower axis put it outside 340 mm body width and far above deck; model the actual links/carrier extension explicitly. Proposed linkage pivot bores 22.5 are custom clearances, not a claim of standard ball/hole dimensions. Pin grip, articulation, withdrawal and keeper geometry follow exact C063/C064 mating parts. No category or standard-conformity claim is assigned to the custom support. Rear support conflicts with caster/hitch region unless a distinct combined arrangement resolves it.

### Separate manufactured shapes and quantity basis — 13 November 2026

Reference assembly: manufacture applicable children, not an extra duplicate parent solid.
- P08LC — Front lower attachment cheek: 2 per corresponding interface; Structural S discussion variant.
- P08UB — Front upper attachment blank: 1 per corresponding interface; Structural S discussion variant.
- P08MS — Front attachment mast: 1 per corresponding interface; Structural S discussion variant.
- P08BS — Front attachment mast base seat: 1 per corresponding interface; Structural S discussion variant.
- P08BR — Front attachment support triangle: 4 per corresponding interface; Structural S discussion variant.
- P08DU — Front doubler upper support tab: 2 per corresponding interface; Structural S discussion variant.

### Explicit J connection transform

J front chassis transform: take S mounting planeX300 toJ325 (+25X), and rail underside233 to500 (+267Z). P08D/P08LC/P08BS/P08MS/P08UB/P08BR shapes retain their own local dimensions; front mount startsX325, outside the650 mainframe and source batterytrayX≤290. Custom chassis pivots remain distinct from the source ISO shoulder/ball datum. Upper mast reaches above deck outside its usableX bounds; this is a support alternative, not a new implement mechanism.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P08D — S front crossmember doubler | 1 | [Front/rear S attachment crossmember doubler](<../../../../mechanical-parts/components/p08d-front-attachment-crossmember-doubler/p08d-front-attachment-crossmember-doubler.md>) — 154 | `645598f3e87d77648c51099f842c40fc23ca47c276a8db263314b05b1646a708` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P08BS — S mast base seat | 1 | [Front/rear S attachment mast base seat](<../../../../mechanical-parts/components/p08bs-front-attachment-mast-base-seat/p08bs-front-attachment-mast-base-seat.md>) — 153 | `b983773fa06b46a3d8974cca8598791ac256564160c5ae017d07395904d77545` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P08MS — S mast nominal hollow tube | 1 | [S attachment mast tube](<../../../../mechanical-parts/components/p08ms-front-attachment-mast/p08ms-front-attachment-mast.md>) — 157 | `44165d0aad89e92329afe90cac4dc1fb3e897d22d3370a4f810e54cf627db68a` | `{"position_mm":[328.0,0.0,283.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P08DU — S upper support tab | 1 | [Front/rear S doubler upper support tab](<../../../../mechanical-parts/components/p08du-front-doubler-upper-support-tab/p08du-front-doubler-upper-support-tab.md>) — 155 | `48d694750185bcbf2d064a538e3da7482f9d73ff5ba9f678855f96df4052efc1` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P08LC — S lower attachment cheek | 1 | [Front/rear S lower attachment cheek](<../../../../mechanical-parts/components/p08lc-front-lower-attachment-cheek/p08lc-front-lower-attachment-cheek.md>) — 156 | `99da10623773b0432ee2460bd3891262d9c6891226234d5ffc052b84a7030aa5` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P08DU — S upper support tab | 1 | [Front/rear S doubler upper support tab](<../../../../mechanical-parts/components/p08du-front-doubler-upper-support-tab/p08du-front-doubler-upper-support-tab.md>) — 155 | `48d694750185bcbf2d064a538e3da7482f9d73ff5ba9f678855f96df4052efc1` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |
| P08LC — S lower attachment cheek | 1 | [Front/rear S lower attachment cheek](<../../../../mechanical-parts/components/p08lc-front-lower-attachment-cheek/p08lc-front-lower-attachment-cheek.md>) — 156 | `99da10623773b0432ee2460bd3891262d9c6891226234d5ffc052b84a7030aa5` | `{"position_mm":[0.0,0.0,0.0],"scale":[1.0,-1.0,1.0],"rotation_radians":0.0,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

153. [Front/rear S attachment mast base seat](<../../../../mechanical-parts/components/p08bs-front-attachment-mast-base-seat/p08bs-front-attachment-mast-base-seat.md>) — library entry 153.
154. [Front/rear S attachment crossmember doubler](<../../../../mechanical-parts/components/p08d-front-attachment-crossmember-doubler/p08d-front-attachment-crossmember-doubler.md>) — library entry 154.
155. [Front/rear S doubler upper support tab](<../../../../mechanical-parts/components/p08du-front-doubler-upper-support-tab/p08du-front-doubler-upper-support-tab.md>) — library entry 155.
156. [Front/rear S lower attachment cheek](<../../../../mechanical-parts/components/p08lc-front-lower-attachment-cheek/p08lc-front-lower-attachment-cheek.md>) — library entry 156.
157. [S attachment mast tube](<../../../../mechanical-parts/components/p08ms-front-attachment-mast/p08ms-front-attachment-mast.md>) — library entry 157.

## Views

1. [front attachment lower cheeks and mast s isometric](<front-attachment-lower-cheeks-and-mast-s-isometric.png>).

1. [front attachment lower cheeks and mast s orthographic](<front-attachment-lower-cheeks-and-mast-s-orthographic.png>).

1. [front attachment lower cheeks and mast s orthographic](<front-attachment-lower-cheeks-and-mast-s-orthographic.svg>).
