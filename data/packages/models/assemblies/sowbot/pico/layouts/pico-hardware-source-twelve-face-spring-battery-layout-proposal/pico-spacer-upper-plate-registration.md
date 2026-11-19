# Pico spacer registration at the upper expansion plate

1. **Plan** — Assembly 2, step 7. Compare the four Hiwonder Pico spacer upper cap planes and axes with the upper expansion plate underside and openings at their saved source positions.
2. **Parts** — Hiwonder upper expansion plate, library 265, STEP body 3026, and hex spacer, library 276, with source occurrences 3032–3035. Opening identifiers come from the dimensioned upper plate drawing. [Plate](<../../parts/pico-upper-expansion-plate-manufacturer-source/pico-upper-expansion-plate-manufacturer-source.md>) · [Spacer](<../../parts/pico-spacer-manufacturer-source/pico-spacer-manufacturer-source.md>) · [Drawing](<../../parts/pico-upper-expansion-plate-manufacturer-source/pico-upper-expansion-plate-manufacturer-source-dimensioned.png>).
3. **Chassis coordinates** — X longitudinal, Y transverse, Z up. Each spacer's calculated upper cap centre is at Z **117.265800 mm**. The source plate underside is at Z **117.389892 mm**, giving a **0.124092 mm** axial separation at each spacer.
4. **Spacer 3032** — X −103.504213 mm, Y −34.110366 mm. Nearest opening H38, Ø4.300 mm. XY centre offset 0.043690 mm.
5. **Spacer 3033** — X 83.309358 mm, Y 31.421683 mm. Nearest opening H36, Ø4.300 mm. XY centre offset 0.043690 mm.
6. **Spacer 3034** — X 83.309358 mm, Y −31.325731 mm. Nearest opening H35, Ø4.300 mm. XY centre offset 0.043690 mm.
7. **Spacer 3035** — X −103.504213 mm, Y 34.206318 mm. Nearest opening H37, Ø4.300 mm. XY centre offset 0.043690 mm.
8. **Method** — Transform the upper cap centre from the spacer origin using its saved chassis occurrence matrix. Cross-check the elevations against independent source vertex extrema. Project into the upper plate frame and compare distances to all 66 recorded opening centres. Retain both source offsets in the placement. Calculation and input hashes.
9. **Source** — Values are calculated from the retained manufacturer CAD geometry. The calculating model was `gpt-6.2-sol`. Hiwonder Pico chassis STEP.
10. **Independent check** — Direct reading of the STEP planes and Ø4.3 mm cylindrical surfaces reproduced the four axial gaps and XY centre offsets within 0.000000001 mm. The independent checking model identity is unavailable. Direct STEP check.
