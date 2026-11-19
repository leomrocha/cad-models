# Brain GNSS receivers with opposed SMA access

1. **Plan identity** Assembly 4, separate placement proposal.
2. **Native drawing** [Brain opposed-SMA layout proposal](<brain-opposed-sma-layout-proposal.dwg>).
3. **DWG SHA-256:** `d26c6f86f5a3e8d6431ec9681ce22ca3733803f1597c7282d13154a3d1910198`.
4. **Actual execution and checking models** Unavailable.
5. **Occurrence BOM** Nine roots with the same quantities as the parent layout. Model sources, matrices and quantities.

## Technical specification

1. The lower-X SparkFun NEO-F9P receiver rotates 180° around its substrate centre, at Brain XY **(22.202200, 27.734798) mm**. Its board height and source block are retained. The other eight roots retain their exact native records.
2. The rotated receiver's SMA faces −X. The second receiver faces +X. The same Ø2 mm straight-probe check that found an obstruction in the parent layout finds zero hits among the **127** represented meshes with the trial placement.
3. Nearest gaps between the rotated receiver's vertex bounds and the other board bounds are **5.000 mm** to LEVIA-H7, **5.000 mm** vertically to the upper Avaota-A1 and **9.726 mm** to the other receiver. These are vertex-envelope measurements. Mating plug clearance and enclosure entry remain physical installation checks.

## Verification

1. The changed native matrix matches the offline placement trial. The guard verified all eight other roots and the unchanged receiver definition. Incremental and final verified SAVE and owned-tab closure passed.
2. [Plan view showing both SMA directions](<../../../../images/sowbot/brain-opposed-sma-plan-view.png>).
3. Clearance trial and scope.

4. **Solid clearance at both SMA approaches:** Conservative bounds from the original Avaota, LEVIA and u-blox STEP solids and the source PCB extrusions exclude all **952** placed solid occurrences from the two Ø2 mm probes. The panel-interface circle also clears. On the −X approach, the nearest solid bound lies **5.470 mm** behind the entry plane. On the +X approach, the upper Avaota bounding box leaves at least **6.181 mm** between the box and the probe surface. The bounds include source shape tolerances. This check uses the represented source geometry at the saved poses. Actual calculation model unavailable. Source bounds, matrices and hash checks.

## References

1. [Parent Brain layout](<brain-orp-and-antenna-layout-proposal.md>).
2. [Library 291 SparkFun NEO-F9P receiver](<../../../../library/subassemblies/sparkfun-neo-f9p-source-connector-exterior-stage.md>).

## Sources — online

1. Sowbot Brain hardware configuration.
2. SparkFun NEO-F9P carrier.
