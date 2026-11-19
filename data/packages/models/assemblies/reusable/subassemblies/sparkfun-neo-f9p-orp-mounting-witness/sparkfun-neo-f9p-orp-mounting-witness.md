# SparkFun NEO-F9P four-hole ORP mounting witness

1. **Library number:** 319.
2. **Plan use:** Brain electronics assembly mounting projection, models 23 and 32.
3. **Native drawing:** [Receiver and ORP four-hole reference](<sparkfun-neo-f9p-orp-mounting-witness.dwg>).
4. **DWG SHA-256:** `c926378ba9cd1b423dfba9744ab03215c11c4c8c253d15a5c5f2c2a01616dbb1`.
5. **Actual execution model:** unavailable.

## Technical specification

1. The reference drawing contains the complete library 291 receiver exterior, library 314 ORP face and four Ø1.85 mm projected probe circles. The plate is at identity. The receiver uses rotation **-0.109471°** about Z and translation **(-21.427987, -21.420440, 0) mm** in plate coordinates.
2. The PCB underside and planar ORP face share Z = 0 mm for the projection check. Each probe centre moves independently within its matching Ø3.302 mm Eagle bore and the assigned ORP opening. The narrowest measured radial clearance is **0.004998 mm**.
3. The nominal equal-pin limit for the four named circular drill primitives is **Ø1.863555 mm**. The JP31–JP101 diagonal centre spacing differs by 3.074908 mm between the patterns. Aligning the diagonals and their midpoints attains the corresponding distance bound for those four circular primitives. The saved ORP openings include merged cuts around three of the four assigned drills.
4. The circles represent projected clearance probes. The witness fixes XY alignment for one receiver. Mounting height, standoffs and hardware tolerances require their own references.

## Checks

1. All 93 receiver geometry occurrences matched their source payloads and composed placements. The saved plate mesh matches library 314 and retains 28 openings.
2. All four saved probe circles clear the saved plate mesh and nominal receiver bores. Verified SAVE, [projected bore view](<sparkfun-neo-f9p-orp-mounting-witness.png>) and guarded closure passed.

## Sources — online

1. SparkFun NEO-F9P board product.
2. Sowbot Brain hardware.

## References

1. [SparkFun receiver source exterior, library 291](<../sparkfun-neo-f9p-source-connector-exterior-stage/sparkfun-neo-f9p-source-connector-exterior-stage.md>).
2. [ORP 28-opening source face, library 314](<../../../../mechanical-parts/components/brain-orp-mounting-plate-28-opening-source-face/brain-orp-mounting-plate-28-opening-source-face.md>).
