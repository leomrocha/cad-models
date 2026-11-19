THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# SKF SY20TF bearing unit

1. **Library number:** 209.
2. **Type:** part.
3. **CAD file:** [skf-sy20tf-checked.dwg](<skf-sy20tf-checked.dwg>).
4. **DWG SHA-256:** `94dd235468e260ba90537fd4dffc664e20f9c64460a25ad7786170c8d991d91c`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** SKF SY20TF bearing unit — C009.

## Technical specification

CAD input sheet; manufacturer dimensions in existing record. Group: drive. Route: ME0907 supported-shaft candidate. Quantity: 4 for two bearings per side.

### Geometry and provenance

Source 20 mm bore, 127×32×64.5 envelope, shaft height 33.3, nominal bolt centres 97, slots88–106. YAR204-2F insert/set-screw locking; source set-screw torque4 N·m.

### Units and local datum

Units: mm. Origin: housing base at shaft-axis projection; axis through20 mm bore.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates candidate20 mm shaft P12 and bearing support P13. Model slots, locking screws, seal faces and grease fitting.

### Space and access

Provide set-screw, mounting bolt and grease access.

### Source-feature table 13 November 2026

SKF SY20TF housing local datum: mounting plane Z=0; shaft axis parallel to Y at Z=33.3 mm. Manufacturer dimensions in the cited drawing: housing L=127 mm, A=32 mm, A1=21 mm, H=64.5 mm; foot thickness 14 mm; two slots 20.5×11.5 mm centred at X=±48.5 mm. YAR204-2F insert: Ø20 mm bore, 31 mm width, approx Ø28.2 mm shoulder; two M6×0.75 set screws, AF3, 120° apart, screw centres 4.5 mm from locking face. The retained source/check record flags a comparison where expected top width A1=21 mm and observed reconstruction width=32 mm; preserve this as an audit discrepancy, not a changed manufacturer value. Sources: SKF drawing  pp.3–5; SKF PUB BU/P1 13728 EN pp.92,122–123; retained records under `engineering/module-development/cad/work/component-led-2026-11-12/c009-reuse-01/`.

### Component dimensions and installation interfaces

| Feature | Specification | Datum / installation | Source |
|---|---|---|---|
| Housing body and mounting slots | L127 mm; A32 mm; A1 21 mm; H64.5 mm; shaft centre height33.3 mm; foot14 mm; slots20.5×11.5 mm at X±48.5 mm | Local datum base mounting plane Z=0, bearing axis Y; hole pattern is measured along housing length | SKF SY20TF manufacturer drawing,  pp.3–5; retained CAD check record `engineering/module-development/cad/checks/component-results/component-led-2026-11-12/c009-reuse-01/source-findings.json`. Manufacturer drawing A1=21 mm; separate retained CAD audit reports a 32 mm top-width comparison and flags mismatch. |
| Bore, insert width, shoulder, lock screws | Ø20 mm bore; 31 mm insert width; approx Ø28.2 mm shoulder; 2×M6×0.75 set screws, 120° apart, AF3; centers4.5 mm from locking face | Shaft axis through bearing centre; dimensions from bearing catalog drawing and retained reconstruction | SKF PUB BU/P1 13728 EN pp.92,122–123; existing CAD record. CAD reconstruction records screws 4.1 mm length from ring wall and 1.5 mm socket depth; these are reconstruction values, not separate SKF callouts. |

## Sources — online

1. SKF technical drawing.
