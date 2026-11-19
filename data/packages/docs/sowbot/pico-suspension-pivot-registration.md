# Pico suspension pivots and roller axes

1. **Plan check** — Assembly 2 step 5. Compare the eight arm-to-carrier pivots and eight arm-to-roller axes in the manufacturer static pose. The left carrier is STEP body 3234 and the right carrier is body 3368. Manufacturer STEP · Installed wheel-axis register.
2. **Left arm and roller pairs** — Source bodies 3186/3180, 3206/3205, 3220/3219 and 3237/3233. [Left source group](<../../library/subassemblies/pico-left-suspension-arm-roller-source-group.md>).
3. **Right arm and roller pairs** — Source bodies 3320/3314, 3340/3339, 3354/3353 and 3371/3367. [Right source group](<../../library/subassemblies/pico-right-suspension-arm-roller-source-group.md>).
4. **Pivot and axle geometry** — Each **Ø4.3 mm** carrier pivot and **Ø7.2 mm** arm pivot share an axis in the source pose. Each **Ø5.2 mm** arm axle opening shares an axis with its corresponding **Ø15 mm** roller bore. The arm pivot-to-axle centre spacing is **15.004404 mm**. The calculations use cylindrical support surfaces and the retained wheel-axis transforms. Exact source face and axis records.
5. **Transverse spacing** — Each arm and its carrier have **5.180000 mm** between their transverse topological-vertex envelopes in the original source pose. This is the separation along the pivot axis between the measured envelopes. Source envelope and axis check.
6. **Independent verification** — Direct STEP axis intercepts at source X = 0 reproduce each alignment within 0.00000001 mm and reproduce the transverse vertex separation within 0.00000001 mm. Root calculation model `gpt-6.2-sol`. Independent checking model identity unavailable. Independent source verification.

## Tension-spring end contacts

1. **Left springs and moving arms** — STEP body pairs 3182/3186, 3236/3206, 3235/3220 and 3238/3237. All four upper loops meet left side carrier 3234.
2. **Right springs and moving arms** — STEP body pairs 3316/3320, 3370/3340, 3369/3354 and 3372/3371. All four upper loops meet right side carrier 3368.
3. **Static contact** — The finite spring faces meet the corresponding arm and carrier faces at both ends of each spring. Across **16** body pairs the largest minimum separation was **4.3 × 10⁻¹⁴ mm**, calculated from the original STEP. Arm contact points are at source Z **38.394–38.733 mm** and carrier contact points at **72.080–72.727 mm**.
4. **Mount geometry and check scope** — The source arm and carrier have open hook profiles. Their partial cylindrical faces include radii near **3.1 mm** and **7 mm**. The lower spring-hook axis on left arm 3186 is at source Y **84.159082 mm**, Z **35.394652 mm**. Its separate suspension pivot is at Y **76.306174 mm** on the same Z level. The check covers finite surfaces in the published static pose. Actual model identities unavailable. Source hook geometry and bindings · Sixteen finite-face checks.

## Helical coil clearance

1. **Suspension arms** — Minimum coil-to-arm separation across all eight positions is **1.454044 mm**, with spring 3235 and left suspension arm 3220 among the governing pairs. Individual minima range from 1.454044 to 1.466856 mm.
2. **Side carriers** — Minimum coil-to-carrier separation is **1.319538 mm** at left spring 3182 and left carrier 3234. Individual minima range from 1.319538 to 1.443543 mm.
3. **Source geometry** — The check uses two finite helical faces per spring, including left seed faces 18547/18553 and right seed faces 24335/24341. The imported faces match original STEP control points and trim endpoints, with a separate source check of the two seed supports. The distances use the corresponding complete arm or carrier boundary in the manufacturer’s static pose. End-loop contacts are documented separately above. Actual checking model identities unavailable. All 16 clearance calculations · Independent coil-face identification.
