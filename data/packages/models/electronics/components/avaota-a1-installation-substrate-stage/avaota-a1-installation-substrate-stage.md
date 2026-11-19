# Yuzuki Avaota-A1 v1.7 — installation substrate stage

1. **Library number:** 251.
2. **Plan component:** model 21, Avaota-A1 computer.
3. **CAD file:** [Native installation substrate](<avaota-a1-installation-substrate-stage.dwg>).
4. **DWG SHA-256:** `63673fe6db5a19989ca45015be168578d733db7fddccaef1bb9dfc6305eef28e`.
5. **State:** PARTIAL_SAVED_REOPENED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Included hardware:** manufacturer source solid 2035 perimeter with five source perimeter apertures; one closed native body with 21 faces and 114 coedges. Circuit-detail apertures are outside this installation stage.
2. **Coordinate frame:** original manufacturer STEP XYZ in millimetres; lower face Z = 0 mm, upper face Z = 1.183202438405 mm. Thickness is source geometry.
3. **Construction:** reused the existing exact-perimeter native checkpoint; each of the five aperture cutters and cuts was individually saved. Thirteen persistent checkpoints retained.
4. **Checks:** all five source aperture centres/radii, source Z limits and reciprocal closed-body topology PASS after reopening. Save audit, reopened hash and owned-document closure PASS.
5. **Views:** saved-model-derived isometric boundary drawing inspected.

## Source aperture geometry

1. **Source aperture 14775:** centre [2.894081788164, 10.595951231902] mm, radius 1.650003810008 mm, manufacturer STEP geometry.
2. **Source aperture 14779:** centre [3.122682245364, 79.582489204978] mm, radius 1.650003810008 mm, manufacturer STEP geometry.
3. **Source aperture 15293:** centre [60.679197358395, 79.531689103378] mm, radius 1.650003810008 mm, manufacturer STEP geometry.
4. **Source aperture 15481:** centre [96.89966979934, 79.430088900178] mm, radius 1.650003810008 mm, manufacturer STEP geometry.
5. **Source aperture 15485:** centre [97.05207010414, 10.621351282703] mm, radius 1.650003810008 mm, manufacturer STEP geometry.

## Dimensioned source substrate drawing

1. [Dimensioned installation-substrate drawing](<avaota-a1-installation-substrate-dimensioned.png>): 4800 × 3200 PNG; source XY, XZ, YZ and isometric projections, with five source perimeter-aperture coordinates and diameters. Measurements are calculated CAD values from retained source-native geometry.
2. **Source substrate outline:** analytic X/Y spans **99.975 × 74.975 mm** (unrounded 99.97480060960095 × 74.97474980949902 mm). Source thickness **1.183 mm** (unrounded 1.183202438405 mm). Lower/upper source planes Z = 0.000/1.183202438405 mm.
3. **Source coordinate frame:** original manufacturer STEP XYZ in millimetres. Outline bounds X = 0.011176022352039183…99.985976631953 mm and Y = 7.6114452628909985…82.58619507239001 mm. The five aperture centres/radii above retain this frame and their source loop identities; each source diameter is 3.300007620016 mm, displayed as **3.300 mm**.
4. **Measurement method:** 57 supported native boundary curves, comprising 35 straight and 22 ellipse edges. Exact stationary coordinate parameters within each ellipse trim interval and straight endpoints establish the outline extrema. Three decimal places are displayed.
5. Existing substrate geometry, numeric source frame and the whole-computer exterior source model remain unchanged.

## References — library

1. [Separate manufacturer source solid 16229 — library 228](<../sow-brain-c01-source-16229/SOW-BRAIN-C01-SOURCE-16229.md>).
2. [Isometric boundary drawing](<avaota-installation-substrate-stage-isometric.png>).
3. [XY boundary drawing](<avaota-installation-substrate-stage-XY.png>).

## Sources — online

1. Avaota-A1 manufacturer v1.7 3D archive, member `3D_PCB1_2024-08-17.step`, SHA-256 `80560b3471ae01130e5d671fd85837e824fd1c22fbfe5bae4b5f4bbc36f9ac41`: original board product, perimeter, aperture geometry and thickness.
