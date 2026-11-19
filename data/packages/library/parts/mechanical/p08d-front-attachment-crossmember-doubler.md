THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Front/rear S attachment crossmember doubler

1. **Library number:** 154.
2. **Type:** part.
3. **CAD file:** [p08d-front-attachment-crossmember-doubler.dwg](<p08d-front-attachment-crossmember-doubler.dwg>).
4. **DWG SHA-256:** `645598f3e87d77648c51099f842c40fc23ca47c276a8db263314b05b1646a708`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Front/rear S attachment crossmember doubler — P08D.

**Design status:** Discussion construction proposal.

## Technical specification

CAD input sheet; custom proposal. Group: attachments. Route: Front interface support proposal. Quantity: 1.

### Geometry and provenance

Existing support stock proposal 8 mm plate; shape follows front frame and attachment plate.

### Units and local datum

Units: mm. Datum A: crossmember seating face; B: front interface plane.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates P08 front plate and P01/P02 structural members.

### Space and access

Reserve joining, fastening and tool/pin access.

### Custom construction

Cut, drill, fixture and join to structural drawing.

### Dimensioned structural proposal variant S — 13 November 2026

**PROPOSAL VARIANT; no design selection.** Units:mm. Geometry below is proposed unless expressly identified as a source dimension. Datum/placement uses existing X forward,Y left,Z up and layout-proposals.md. Proposed steel thicknesses/sections require the named joint/load checks.

Attachment support variant S: steel 260 Y×80 Z×8 plate on front crossmember outside face X 300, extending X 300…308, Y±130, Z 233…313. Proposed fourØ13 axes(Y,Z)=(±100,253),(±100,293). Upper row Z 293 is above 40 mm tube; provide paired 40×40×3 uprights from rail top 273 to 313 or use a welded variant with load path explicitly shown. Lower row through hollow tube requires compression sleeve; this layout is not four holes directly through an 80 mm-high tube. P08 attach es to this support with separate fastener/weld definition.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Front/rear S attachment crossmember doubler | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[300.0, 308.0], [-130.0, 130.0], [233.0, 313.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-100.0, 253.00000000000003], [-100.0, 293.0], [100.0, 253.00000000000003], [100.0, 293.0]] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

114. [Main frame crossmember](<p02-main-frame-crossmember-reference.md>) — library entry 114.
