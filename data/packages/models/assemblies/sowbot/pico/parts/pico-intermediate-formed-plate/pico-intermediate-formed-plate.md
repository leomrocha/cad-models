# Pico intermediate formed plate

1. **Library number:** 316.
2. **Plan use:** Pico HRB battery service reference, model 30.
3. **Native drawing:** [Hiwonder intermediate formed plate](<pico-intermediate-formed-plate.dwg>).
4. **DWG SHA-256:** `c9a45bd74fb248799a0952397aaf4e2f898d988cd026ef487f4cc20f6e752355`.
5. **Actual execution model:** unavailable.

## Technical specification

1. Manufacturer STEP body 3037 supplies one closed 215-face formed plate. The DWG retains original manufacturer XYZ coordinates in millimetres. The native topological-vertex bounds are X −41.778 to 59.692 mm, Y −123.921 to 119.617 mm and Z 81.629 to 98.121 mm.
2. The selected-body STEP derivative retains 7,391 source entities. Only the source shape-representation member list changes. The selected body's geometry is byte-identical to the retained original STEP.

3. **Formed dimensions from the native boundary:** X = 101.470 mm, Y = 243.537 mm and Z = 16.492 mm in manufacturer coordinates. The main sheet is **2.000 mm** thick between its two broad faces at Z = 96.121 and 98.121 mm. The flanges extend toward lower Z. Each main face has 77 opening loops, including 68 circular mouths and nine other profiles. Source geometry measurements describe the saved formed plate. [Dimensioned drawing](<pico-intermediate-formed-plate-dimensioned.png>).

## Checks

1. The native body matched the original source vertex set with a measured bidirectional error of 0.0 mm. Face count, reciprocal closed topology, original placement and verified SAVE passed.
2. The [isometric view](<pico-intermediate-formed-plate-isometric.png>) was inspected. Guarded closure of the saved construction document passed.

## Sources — online

1. [Hiwonder manufacturer-linked STEP](https://drive.google.com/file/d/118zHyaMR6LU_DeXndFg6-FFH070BZfYu/view).
2. Hiwonder suspended tracked chassis.

## References

1. [Hiwonder upper expansion plate, body 3026](<../../../../../../library/parts/mechanical/pico-upper-expansion-plate-manufacturer-source.md>).
2. [Hiwonder lower formed plate, body 3108](<../../../../../../library/parts/mechanical/pico-lower-plate-manufacturer-source.md>).
3. [HRB clearance reference in Pico chassis coordinates](<../../../../../../library/standards/hrb-3s-6000mah-hard-case-pico-clearance.md>).
