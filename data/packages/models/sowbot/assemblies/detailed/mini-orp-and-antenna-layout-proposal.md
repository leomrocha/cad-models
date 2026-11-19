# Mini Sowbot layout with the corrected ORP plate and BT-560 antennas

1. **Plan identity:** Assembly 6, Mini Sowbot hardware layout proposal.
2. **Native drawing:** [Mini layout](<mini-orp-and-antenna-layout-proposal.dwg>).
3. **DWG SHA-256:** `613502a3a1e68ce27987bd420267710d49e29f9ecb29f448bf58f9d8b31989e9`.
4. **Actual execution model:** unavailable.

## Technical specification

1. The revised Brain occupies the existing Mini position (0, 20, 0) mm. Rotation is identity and scale is 1. The Brain contains the library 314 Rosmo ORP mounting plate face and two library 315 Beitian BT-560 antenna meshes.
2. The saved proposal contains 4 live roots and 1,134 geometry occurrences, including 1,080 inside the Brain. All 3 other roots retain their geometry and placements.

## Verification

1. Independent comparison matched each installed geometry type, payload and composed placement to its source. Incremental and final verified SAVE and guarded closure passed.
2. [Isometric view](<../../../../images/sowbot/mini-orp-and-antenna-layout-proposal-isometric.png>) was inspected. The occurrence BOM binds placed models, quantities, matrices and source hashes.

## References

1. [Revised Brain CAD](<brain-orp-and-antenna-layout-proposal.md>).
2. [Prior Mini CAD](<mini-battery-driver-and-brain-layout-proposal.md>).
3. Native save checks.
4. [Library 318 Propow 220 mm battery clearance source](<../../../../library/standards/propow-cpn24050-220mm-source-selection.md>).

## Sources — online

1. Sowbot hardware description.
