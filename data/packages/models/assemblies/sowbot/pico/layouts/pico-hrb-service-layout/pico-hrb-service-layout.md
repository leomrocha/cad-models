# Pico HRB battery service layout

1. **Plan identity:** Model 30 battery access, within Assembly 2 Pico tracked chassis.
2. **Native drawing:** [Pico HRB service layout](<pico-hrb-service-layout.dwg>).
3. **DWG SHA-256:** `9394b93932ce62710a17a73075573ae11d7ec0328f69a1905ba064aecc5e6788`.
4. **Actual execution model:** unavailable.

## Technical specification

1. The layout places the Pico lower frame and 138 × 46 × 39 mm HRB clearance solid at their checked chassis positions. The Hiwonder upper expansion plate 3026 and intermediate formed plate 3037 occupy their original source positions. Four live roots expand to six closed solids.
2. The source lift calculation traces a vertical travel of 88.995 mm. The volumes where the rigid battery path intersects plates 3026 and 3037 are 9,527.82 mm³ and 8,515.03 mm³, respectively.
3. With both plates removed in the full STEP check, the rigid battery path clears the 407 remaining stationary source bodies. Minimum finite separation is 0.0971 mm to lower formed plate 3108. The saved drawing displays the battery at rest and both plates in place. [Side-view service comparison](<pico-hrb-service-path.png>).

## Service positions

1. **Intermediate formed plate 3037:** After releasing the checked hardware and removing the upper expansion plate, lift the intermediate plate **42.544 mm** along chassis +Z. The battery clearance envelope stays at its installed pose. [Intermediate-plate position](<pico-hrb-intermediate-plate-endpoint.png>).
2. **Battery clearance envelope:** With both plates removed, lift the **138 × 46 × 39 mm** envelope **88.995 mm** along chassis +Z. The lower frame stays in its original position. [Battery removal position](<pico-hrb-battery-endpoint.png>).
3. Both views are orthographic projections of distinct manufacturer STEP-based service trial positions. The catalogue DWG shows the installed pose.

## Verification

1. All six solids passed source vertex, topology and composed placement checks. Maximum bidirectional vertex-set distance was 1.42e-14 mm.
2. Incremental and final verified SAVE, inspected [isometric view](<pico-hrb-service-layout-isometric.png>) and guarded closure passed. The occurrence BOM binds each root to its source drawing and transform.

## References

1. [Pico lightweight HRB bay](<../pico-lightweight-hrb-bay/pico-lightweight-hrb-bay.md>).
2. [Hiwonder upper expansion plate](<../../parts/pico-upper-expansion-plate-manufacturer-source/pico-upper-expansion-plate-manufacturer-source.md>).
3. Hiwonder intermediate formed plate.
4. Native checks.

## Sources — online

1. [Hiwonder manufacturer-linked STEP](https://drive.google.com/file/d/118zHyaMR6LU_DeXndFg6-FFH070BZfYu/view).
