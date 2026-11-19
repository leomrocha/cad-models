# Main Sowbot track straight-run brightness ridges

1. **Library number** 321.
2. **Plan item** 03, Main chassis track, conditional photo reference.
3. **Native drawing** [Eleven projected tread ridge lines](<main-track-straight-ridge-reference.dwg>).
4. **DWG SHA-256:** `8be1f4743310bb1f1b3e53c305492c9ae45711823ef80b2baa1160bd547573ef`. DWG 2018, 28,315 bytes.
5. **Actual execution and checking model identities** Unavailable.

## Technical specification

1. Eleven open two-vertex polylines project visible brightness ridges onto the near track's straight-run reference plane. The library 280 frame uses millimetres, X along travel, Y across the belt toward image-left and Z up. Each line spans the analysis window Y = −90 to −40 mm at Z = 0.
2. Conditional ridge X positions are 110.5, 163.5, 216.5, 270.5, 321.5, 372, 430, 484.5, 543, 595.5, 656.25 mm. The projected adjacent gaps range from 50.50 to 60.75 mm. The photograph supplies projected brightness positions within the fixed camera and plane assumptions.
3. Source extraction sampled seven transverse positions in the 436 × 250 px photograph. Three positions established the fit. The remaining four used separate original pixels and associated peaks within ±15 mm of the training seeds. They matched 39 of 44 possible ridge comparisons, with a 2.326 px maximum perpendicular residual among the matches. [Source overlay](<../images/main-track-straight-ridge-source-overlay.png>).

## Checks

1. OCS returned exactly 11 open polylines, each with two source-matched endpoints and zero bulge, in a millimetre drawing. Incremental verified SAVE and final save confirmed the intended path and hash, with zero dropped entities.
2. The projected endpoints and line positions were inspected against the original photograph. The saved native arrays matched the measured endpoints. Guarded closure passed.

## Sources — online

1. Sowbot hardware and Main chassis photo.

## References

1. [Library 280 straight-tread patch and three visible-cleat band meshes](<../parts/mechanical/main-chassis-visible-tread-photo-reference.md>). The lines use its conditional camera and tread plane.
