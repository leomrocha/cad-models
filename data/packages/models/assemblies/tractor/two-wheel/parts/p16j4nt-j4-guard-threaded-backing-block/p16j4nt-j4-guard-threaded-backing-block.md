THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# J4 guard nominal M6 backing block

1. **Library number:** 175.
2. **Type:** part.
3. **CAD file:** [p16j4nt-j4-guard-threaded-backing-block.dwg](<p16j4nt-j4-guard-threaded-backing-block.dwg>).
4. **DWG SHA-256:** `b8dde6a3ba077709ab404c7e5d56732644d914b67c29d16fe370eca437196370`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** J4 guard nominal M6 backing block — P16J4NT.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: ten per guard, twenty per pair.

### Finite geometry and attachment

1. **Proposed stock:** steel block16 mm along local x ×12 mm along local z ×6 mm along axial Y. Local x/z centre is the matching A05 lid axis. Left body-rim inner face isY166.5 mm; block front face contacts it and block extends inward toY160.5 mm. Right instances mirrorY. Source/standard thread designation is M6×1; proposed through-tapped axis is normalY. Proposed entry/exit chamfers are0.5 mm axial length at45°, giving a nominal5 mm full-form thread interval within the6 mm block. Inspect the actual fully formed tapped thread and screw after welding.
2. **Instance centres:** use all ten axes in P16J4LD — matching lid. At each top-row axisZ489.036290 mm, block spansZ483.036290…495.036290 mm and fits the12 mm top land. Side and bottom blocks fit their20 mm lands. At corner axes10 mm from side edges, the16 mm block width leaves2 mm to the side edge. The block footprint remains on the fixed rim outside the planning cavity.
3. **Weld proposal:** locate each block using the lid hole pattern and removable alignment screws, then weld along its two local x end edges to the body-rim inner face. Proposed fillet legs are1 mm, extending outward inx and inward inY; their maximum plan extent isx =±9 mm from the fixing axis, leaving1 mm to the adjacent10 mm edge allowance. Keep the local z =±6 mm block limits as finished envelope boundaries at the12 mm top land. Inspect alignment and tapped thread after welding, then install the lid screws from outside.
4. **Mating screw:** C134 — proposed M6×30 button-head screw bears directly on the1.5 mm steel lid. The lid input gives actual-length, head projection, tip-gap and tool conditions. The full threaded block supplies the fixed mating interface for the removable lid.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed deck interface part | PASS | [1, 1, 1, 1] | count |
| Source stock bounds | PASS | [[-8.0, 8.0], [-6.0, 6.0], [0.0, 6.0]] | mm |
| Nominal thread-reference axes | PASS | [[0.0, 3.061616997868383e-17]] | mm |
| Nominal45-degree cone half-angles | PASS | [45.0, 45.0] | degrees |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
2. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.
