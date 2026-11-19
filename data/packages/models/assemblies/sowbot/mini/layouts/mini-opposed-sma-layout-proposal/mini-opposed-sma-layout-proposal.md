# Mini Sowbot layout with opposed GNSS connectors

1. **Plan identity** Assembly 6, separate installation layout proposal.
2. **Native drawing** [Mini opposed-SMA layout proposal](<mini-opposed-sma-layout-proposal.dwg>).
3. **DWG SHA-256** `91bc9166ab7d0253521e020f7d6d0db50a593cc0dd595999b7bfdfb3007cee9c`.
4. **Actual execution and checking models** Unavailable.

## Technical specification

1. The Brain assembly retains its Mini translation **(0, 20, 0) mm**. The two SparkFun NEO-F9P receiver SMA connectors face outward in opposite X directions. The 220 mm battery envelope, Open BTS7960 driver and planar base retain their source geometry and placements.
2. The saved model contains **4 live roots** and **1,134 geometry occurrences**. The occurrence BOM records the four installed groups and their source hashes and matrices.
3. The two **Ø2 mm** approach probes have a minimum **48.270 mm** separation from the Mini base footprint, battery envelope and conservative bounds of the represented driver. The planar base governs that value. The corresponding [Brain clearance check](<../../../brain/layouts/brain-opposed-sma-layout-proposal/brain-opposed-sma-layout-proposal.md>) covers the installed Brain solids, meshes and panel circle. Mini approach calculation.

## Verification

1. Independent comparison matched all placed geometry and the composed placements to the source records.
2. Verified save, [isometric view](<mini-opposed-sma-layout-proposal-isometric.png>) and guarded closure passed.

## References

1. [Brain opposed-SMA source CAD](<../../../brain/layouts/brain-opposed-sma-layout-proposal/brain-opposed-sma-layout-proposal.md>).
2. [Prior Mini layout](<../mini-orp-and-antenna-layout-proposal/mini-orp-and-antenna-layout-proposal.md>).

## Sources — online

1. Sowbot hardware configuration.
2. SparkFun NEO-F9P carrier.
