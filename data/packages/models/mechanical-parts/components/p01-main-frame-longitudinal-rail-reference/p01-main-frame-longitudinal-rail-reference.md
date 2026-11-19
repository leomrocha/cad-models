THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Main frame longitudinal rail

1. **Library number:** 111.
2. **Type:** part.
3. **CAD file:** [p01-main-frame-longitudinal-rail-reference.dwg](<p01-main-frame-longitudinal-rail-reference.dwg>).
4. **DWG SHA-256:** `e7bd8c78f2bd07126b170becccc9475d9b9c80becde387d458dc048c2c755e90`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Main frame longitudinal rail — P01.

## Technical specification

CAD input sheet; custom proposal. Group: frame. Route: Common steel-frame proposal. Quantity: 2.

### Geometry and provenance

Existing proposal 40×40×3 square steel tube, 600 cut length. Material grade follows actual stock record.

### Units and local datum

Units: mm. Datum A: rail top/side reference faces; B: front end.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates P02 crossmembers, drive-support group, caster/hitch supports and upper supports. Mark tube orientation and joint faces.

### Space and access

Keep internal attachment/tool access and central underside at axle height or above.

### Custom construction

Saw, deburr, fixture, join using structural drawing, finish exposed surfaces.

### Dimensioned structural proposal variant S — 13 November 2026

**PROPOSAL VARIANT; no design selection.** Units:mm. Geometry below is proposed unless expressly identified as a source dimension. Datum/placement uses existing X forward,Y left,Z up and layout-proposals.md. Proposed steel thicknesses/sections require the named joint/load checks.

Frame variant S: two 40×40×3 steel tubes, length 600, square ends; X−300…300, left Y 130…170/right Y−170…−130, Z 233…273. Local longitudinal coordinate starts at rear cut face. Material grade is a proposed stock-selection parameter; strength uses actual certificate. Clear between inner faces 260; total frame width 340. Proposed welded route has no generic bolt holes in rail walls. Through-bolted support variants use their own axes and compression sleeves through the 34 mm nominal internal tube width; sleeve OD/bore/weld detail follows fastener loads. Existing ITEM route remains a separate material/joint variant.

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
