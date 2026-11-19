THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# rear attachment lower cheeks and mast j3f

1. **Library number:** 48.
2. **Type:** group.
3. **CAD file:** [rear-attachment-lower-cheeks-and-mast-j3f.dwg](<rear-attachment-lower-cheeks-and-mast-j3f.dwg>).
4. **DWG SHA-256:** `e2fd52522474013d09854a34a111a76f9a40bbe54d7c0dec5e06fa153d37bb56`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Design status:** Discussion construction proposal.

## Represented geometry

Seven existing S support solids transformed into the recorded raised J frame

## Technical specification

CAD input sheet; custom proposal. Group: attachments. Route: Rear ISO730 reference proposal. Quantity: Each distinct rear plate separately.

### Geometry and provenance

Source rear referenceCat.1 shoulder span683±1.5, mast460±1.5, lowerØ22 andupperØ19 pin references. Retain standard-derivedinterface metadata.

### Units and local datum

Units: mm. Datum A: rear linkage plane; B: lower pin axis; C: robot centreline.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates rear structural support, lower/upper linkage interfaces and retained pins.

### Space and access

Keep hitch, caster, upper deck and pin withdrawal clear across actual mechanism.

### Custom construction

Cut, machine pin interfaces and attach to structural support drawing.

### Chassis-side attachment support variant S — 13 November 2026

**PROPOSAL**, mm: two 10 mm steel lower carrier cheeks, each 120 X×100 Z, proposed chassis-side boreØ22.5 centred 50 mm above lower edge and 60 mm from either X edge. Lower edge Z 273; local bore Z 323. Locate pair at Y±100 on matching doubler; nominal cheek inner separation 190 if plates centred Y±100. Add 6 mm triangular 100×80 braces to frame/doubler. Front plate bounds X 308…428; rear mirror X−428…−308. Proposed chassis bore axes are Y; local centre X±368. Upper support blank 10 mm thick,100 Y×120 Z, source-mating hole diameter/position retained as parameter dTOP/(uTOP,vTOP); mount at frame-centre Y 0 on separately drawn mast. These are chassis support datums, with linkage members continuing to implement-side datums.

Source reference in existing mechanical-connections/README.md: ISO 730:2009; ISO 8759-4:2018 front power-lift scope excludes two-direction tractors and directs those cases to ISO 730. Existing rear reference retains Cat 1 shoulder span 683±1.5 and mast 460±1.5 with C063/C064 component references. Preserve exact standard shoulder/ball datums; do not apply 683 to these 190 mm chassis cheek spacing. Implement-side linkage transformation is a separate proposed parameter set. For a direct rigid frame carrying that standard reference, lower shoulder planes Y±341.5 and upper mast reference 460 above lower axis put it outside 340 mm body width and far above deck; model the actual links/carrier extension explicitly. Proposed linkage pivot bores 22.5 are custom clearances, not a claim of standard ball/hole dimensions. Pin grip, articulation, withdrawal and keeper geometry follow exact C063/C064 mating parts. No category or standard-conformity claim is assigned to the custom support. Rear support conflicts with caster/hitch region unless a distinct combined arrangement resolves it.

### Separate manufactured shapes and quantity basis — 13 November 2026

Reference assembly: manufacture applicable children, not an extra duplicate parent solid.
- P09LC — Rear lower attachment cheek: 2 per corresponding interface; Structural S discussion variant.
- P09UB — Rear upper attachment blank: 1 per corresponding interface; Structural S discussion variant.
- P09MS — Rear attachment mast: 1 per corresponding interface; Structural S discussion variant.
- P09BS — Rear attachment mast base seat: 1 per corresponding interface; Structural S discussion variant.
- P09BR — Rear attachment support triangle: 4 per corresponding interface; Structural S discussion variant.
- P09DU — Rear doubler upper support tab: 2 per corresponding interface; Structural S discussion variant.

### Explicit J connection transform

J rear support alternative mirrors front translation−25X/+267Z. P09-family solids attach the raised rear frame with exact local source-S geometry. Rotated rear cabinet occupies the same rear support volume, so rear linkage and that cabinet are alternative modules until a distinct combined pose is specified. Preserve source ISO datum and custom chassis pivot separation.

## Installed members

Each row is one recorded occurrence. Position units: mm; rotation units: radians; scale and normal components: dimensionless. Matrices retain the recorded 4 × 4 row-major convention, with translation in mm.

| Member | Quantity | Model reference | Source DWG SHA-256 | Recorded placement |
|---|---|---|---|---|
| P09 — Rear attachment support existing seven-solid support | 1 | [front attachment lower cheeks and mast s](<../../../../reusable/groups/front-attachment-lower-cheeks-and-mast-s/front-attachment-lower-cheeks-and-mast-s.md>) — 33 | `f5f56e5e9d26cacdfa00a94afe2a4691d5e82be31641a537abec231808e2b738` | `{"position_mm":[-25.0,0.0,267.0],"scale":[1.0,1.0,1.0],"rotation_radians":3.141592653589793,"normal":[0.0,0.0,1.0]}` |

## Sources — online

1. Weldable steel plate stock family — supplier reference.

## References — local

33. [front attachment lower cheeks and mast s](<../../../../reusable/groups/front-attachment-lower-cheeks-and-mast-s/front-attachment-lower-cheeks-and-mast-s.md>) — library entry 33.

## Views

1. [rear attachment lower cheeks and mast j3f isometric](<rear-attachment-lower-cheeks-and-mast-j3f-isometric.png>).

1. [rear attachment lower cheeks and mast j3f orthographic](<rear-attachment-lower-cheeks-and-mast-j3f-orthographic.png>).

1. [rear attachment lower cheeks and mast j3f orthographic](<rear-attachment-lower-cheeks-and-mast-j3f-orthographic.svg>).
