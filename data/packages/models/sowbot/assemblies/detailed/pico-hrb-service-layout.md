# Pico HRB battery service layout

1. **Plan identity:** Model 30 battery access, within Assembly 2 Pico tracked chassis.
2. **Native drawing:** [Pico HRB service layout](<pico-hrb-service-layout.dwg>).
3. **DWG SHA-256:** `9394b93932ce62710a17a73075573ae11d7ec0328f69a1905ba064aecc5e6788`.
4. **Actual execution model:** unavailable.

## Technical specification

1. The layout places the Pico lower frame and 138 × 46 × 39 mm HRB clearance solid at their checked chassis positions. The Hiwonder upper expansion plate 3026 and intermediate formed plate 3037 occupy their original source positions. Four live roots expand to six closed solids.
2. The source lift calculation traces a vertical travel of 88.995 mm. The volumes where the rigid battery path intersects plates 3026 and 3037 are 9,527.82 mm³ and 8,515.03 mm³, respectively.
3. With both plates removed in the full STEP check, the rigid battery path clears the 407 remaining stationary source bodies. Minimum finite separation is 0.0971 mm to lower formed plate 3108. The saved drawing displays the battery at rest and both plates in place. [Side-view service comparison](<../../../../images/sowbot/pico-hrb-service-path.png>).

## Verification

1. All six solids passed source vertex, topology and composed placement checks. Maximum bidirectional vertex-set distance was 1.42e-14 mm.
2. Incremental and final verified SAVE, inspected [isometric view](<../../../../images/sowbot/pico-hrb-service-layout-isometric.png>) and guarded closure passed. The [occurrence BOM](<../../../../docs/sowbot/bom/pico-hrb-service-layout-occurrences.csv>) binds each root to its source drawing and transform.

## References

1. [Pico lightweight HRB bay](<pico-lightweight-hrb-bay.md>).
2. [Hiwonder upper expansion plate](<../../../../library/parts/mechanical/pico-upper-expansion-plate-manufacturer-source.md>).
3. Hiwonder intermediate formed plate.
4. Native checks.

## Sources — online

1. Hiwonder manufacturer-linked STEP.
