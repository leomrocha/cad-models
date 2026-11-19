THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Main frame crossmember

1. **Library number:** 114.
2. **Type:** part.
3. **CAD file:** [p02-main-frame-crossmember-reference.dwg](<p02-main-frame-crossmember-reference.dwg>).
4. **DWG SHA-256:** `f2cd4fdf0b6f1c7b2ddc58fbbe1f9680c92ecac4fee7365acececf92c55104c2`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Main frame crossmember — P02.

## Technical specification

CAD input sheet; custom proposal. Group: frame. Route: Common steel-frame proposal. Quantity: 3.

### Geometry and provenance

Existing proposal 40×40×3 tube, 260 cut length between rails; frame positions follow the assembly proposal.

### Units and local datum

Units: mm. Datum A: frame reference face; B: crossmember centre plane.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates P01 rail faces and structural support plates; keep weld/bolt variant hardware identified.

### Space and access

Reserve support attachment access and equipment routing.

### Custom construction

Saw, deburr, fixture and join to rail arrangement.

### Dimensioned structural proposal variant S — 13 November 2026

**PROPOSAL VARIANT; no design selection.** Units:mm. Geometry below is proposed unless expressly identified as a source dimension. Datum/placement uses existing X forward,Y left,Z up and layout-proposals.md. Proposed steel thicknesses/sections require the named joint/load checks.

Frame variant S: three 40×40×3 steel tubes 260 long between rail inner faces Y±130, Z 233…273. Proposed centre planes X−280,0,+280; each spans 40 in X. Ends meet P01 inner faces; front/rear outside faces are X±300. Result is 600×340; nominal cut sum 2×600+3×260=1980 mm. Proposed welded butt ends preserve 260 clear-span cut; a bracketed variant subtracts only its actual intervening joint thickness. Fixture outside rectangle and diagonals; nominal diagonal sqrt(600²+340²)=689.64 mm. Weld throat/sequence is a load-dependent drawing input.

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

111. [Main frame longitudinal rail](<p01-main-frame-longitudinal-rail-reference.md>) — library entry 111.
