# Main Sowbot layout with the corrected ORP plate and BT-560 antennas

1. **Plan identity:** Assembly 5, Main Sowbot hardware layout proposal.
2. **Native drawing:** [Main layout](<main-orp-and-antenna-layout-proposal.dwg>).
3. **DWG SHA-256:** `17b6c34ae18b66ff62dfbfce7039a6aaab78d065b5a370b9ad07f5650c6f4d4d`.
4. **Actual execution model:** unavailable.

## Technical specification

1. The revised Brain occupies the existing Main position (250, 726, 250) mm. Rotation is identity and scale is 1. The Brain contains the library 314 Rosmo ORP mounting plate face and two library 315 Beitian BT-560 antenna meshes.
2. The saved proposal contains 10 live roots and 1,177 geometry occurrences, including 1,080 inside the Brain. All 9 other roots retain their geometry and placements.

## Verification

1. Independent comparison matched each installed geometry type, payload and composed placement to its source. Incremental and final verified SAVE and guarded closure passed.
2. [Isometric view](<main-orp-and-antenna-layout-proposal-isometric.png>) was inspected. The occurrence BOM binds placed models, quantities, matrices and source hashes.
3. **Battery removal projection:** All 66 XY pair checks on the six battery exteriors returned positive separation. The minimum gaps are **16.441 mm** to another battery, **89.505 mm** to the source-visible track patches, **35.000 mm** to the controller outlines, **56.000 mm** to the ORP face and **222.372 mm** to the BT-560 antenna skins. The check uses the saved battery orientations and fixed XY during a straight +Z lift. Its obstacle set consists of the listed geometry. Actual calculation model unavailable. Pair measurements and source hashes.

4. **Battery stud access:** The straight +Z approach starts at each stud cap centre. Among the evaluated surfaces of 224 placed meshes, the adjacent knob on the same battery sets the radial limit at all 12 positions. The limits are **29.074 mm** at the six positive studs and **28.337 mm** at the six negative studs. A smaller approach radius gives separation from the evaluated surfaces. The terminal shapes come from the photo exterior. Other solid geometry, lug fit and physical tool dimensions fall outside the result. Actual calculation model unavailable. [Plan view](<main-battery-terminal-access.png>) · Stud locations, mesh witnesses and source hashes.

5. **Installed lower Avaota-A1 extraction:** The saved Brain placement retains the checked **174.615 mm** +X removal path. The nearest represented hardware outside Brain is VariCore photo exterior 3, at **70.142 mm** conservative box separation. The checked surroundings comprise six battery exteriors, two controller outlines and the source-visible track patches. Actual calculation model unavailable. [Source path and scope](<../../../brain/layouts/brain-orp-and-antenna-layout-proposal/brain-orp-and-antenna-layout-proposal.md>).

## References

1. [Revised Brain CAD](<../../../brain/layouts/brain-orp-and-antenna-layout-proposal/brain-orp-and-antenna-layout-proposal.md>).
2. [Prior Main CAD](<../main-updated-brain-layout-proposal/main-updated-brain-layout-proposal.md>).
3. Native save checks.

## Sources — online

1. Sowbot hardware description.
