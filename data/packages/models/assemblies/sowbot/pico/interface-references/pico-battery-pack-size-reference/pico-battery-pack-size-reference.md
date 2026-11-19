# Pico Hiwonder battery — pack-size reference

1. **Library number:** 248.
2. **Plan component:** model 30, Pico lithium-polymer battery.
3. **CAD file:** [Battery reference volume](<pico-battery-pack-size-reference.dwg>).
4. **DWG SHA-256:** `9f2526d4e4e95acb53663f4ec98494e711570712e4035f6eae24bb8d10b44c19`.
5. **Representation:** reference envelope, one native closed solid.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Manufacturer dimensions:** 86 × 60 × 21 mm, from the Hiwonder battery Parameters table for the advanced chassis bundle.
2. **Manufacturer pack identity:** 11.1 V, 6,000 mAh lithium battery; Hiwonder lists DC5.5 × 2.5 female / SM-2P male plugs for this pack.
3. **Represented volume:** pack-size rectangular volume; local X=86 mm, Y=60 mm, Z=21 mm. Bottom-face centre is the origin and +Z points through pack thickness. These axes are the local construction convention.
4. **Geometry checks:** native XYZ bounds X=−43…43 mm, Y=−30…30 mm, Z=0…21 mm; one closed body PASS. Comparison tolerance 0.000001 mm checks numeric geometry agreement with the input values.
5. **Persistence:** saved after creation and each feature step; final native save/reopen and SHA-256 checks PASS.
6. **Views and cleanup:** four native boundary drawings inspected; both owned tabs closed, pre-existing documents preserved.

## References — library

1. [Isometric boundary drawing](<pico-battery-pack-size-reference-isometric.png>).
2. [Top boundary drawing](<pico-battery-pack-size-reference-XY.png>).

## Sources — online

1. Hiwonder advanced chassis, LiPo battery and charger bundle, battery Parameters table: dimensions, voltage, capacity and plug names.
