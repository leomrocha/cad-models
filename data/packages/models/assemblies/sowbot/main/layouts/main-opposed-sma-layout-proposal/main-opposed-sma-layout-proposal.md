# Main Sowbot layout with opposed GNSS connectors

1. **Plan identity** Assembly 5, separate hardware placement proposal.
2. **Native drawing** [Main opposed-SMA layout proposal](<main-opposed-sma-layout-proposal.dwg>).
3. **DWG SHA-256** `a615757c3fc9476f401ca4ae39555e9b89fdb582f3c857e29b8026fdee2f51f3`.
4. **Actual execution and checking models** Unavailable.

## Technical specification

1. The Brain assembly retains its Main translation **(250, 726, 250) mm**. The two SparkFun NEO-F9P SMA connectors face outward in opposite X directions. The six VariCore battery exteriors, two planar ODrive v3.6 references and the source-visible track surfaces retain their saved placements.
2. The two **Ø2 mm** approach probes clear the nine other represented Main roots by at least **111.429 mm**. The lower bound is governed by the battery exteriors. The rotated receiver's closest conservative three-dimensional box gap to those nine roots is **97.426 mm**. Represented Main clearance.
3. The [Brain approach checks](<../../../brain/layouts/brain-opposed-sma-layout-proposal/brain-opposed-sma-layout-proposal.md>) cover the Brain solids, meshes and panel circle. The Main approach check covers the represented surfaces and the Ø2 mm probe.

## Verification

1. The independent geometry comparison matched all **1,177** geometry occurrences and their composed placements. The occurrence BOM identifies all ten roots and their sources.
2. Verified save, [isometric view](<main-opposed-sma-layout-proposal-isometric.png>) and guarded CAD closure passed.

## References

1. [Brain opposed-SMA source CAD](<../../../brain/layouts/brain-opposed-sma-layout-proposal/brain-opposed-sma-layout-proposal.md>).
2. [Prior Main layout](<../main-orp-and-antenna-layout-proposal/main-orp-and-antenna-layout-proposal.md>).

## Sources — online

1. Sowbot hardware configuration.
2. SparkFun NEO-F9P carrier.
