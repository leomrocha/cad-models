THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Caster S frame doubler

1. **Library number:** 133.
2. **Type:** part.
3. **CAD file:** [p05d-caster-frame-doubler.dwg](<p05d-caster-frame-doubler.dwg>).
4. **DWG SHA-256:** `f1d95f68b341765953fdca8a77c76c4b2c754884fe99e4c6d9841984a4de411b`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Caster S frame doubler — P05D.

**Design status:** Discussion construction proposal.

## Technical specification

Date: 12 November 2026. CAD input sheet; custom proposal. Group: caster. Route: Removable caster support proposal. Quantity: 1.

### Geometry and provenance

Existing proposal 10 mm plate connecting clevis to rear crossmember/rails; prior layout uses fourM12 joints.

### Units and local datum

Units: mm. Datum A: crossmember attachment face; B: base centreline.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates P05A cheeks and P02/P01; bolt lengths follow full stack and access.

### Space and access

Reserve socket access and arm removal.

### Custom construction

Cut, drill, fixture and attach as structural drawing specifies.

### Dimensioned structural proposal variant S — 13 November 2026

**PROPOSAL VARIANT; no design selection.** Units:mm. Geometry below is proposed unless expressly identified as a source dimension. Datum/placement uses existing X forward,Y left,Z up and layout-proposals.md. Proposed steel thicknesses/sections require the named joint/load checks.

Caster variant S: horizontal steel doubler 340 Y×120 X×10, bounds X−300…−180,Y±170,Z 273…283. Proposed fourØ13 axes at X−280/−200,Y±150 join both rails through 40 mm depth, with compression sleeves in the tubes. Set bolt under-head length from 10 plate+40 tube+sourced washers/nut/protrusion; keep the sleeve supporting the clamp. Two local cheek-support webs 6 thick join plate to P05A at Y±38, rising to cheek lower Z 273 and upper Z 393, with contact profile trimmed to the cheek rectangle. Frame/caster reaction flows through webs/doubler into both rails. Plate or webs may obstruct pin extraction; reserve the C018/C019 axial withdrawal cylinder before final web placement.

### Separate manufactured shapes and quantity basis — 13 November 2026

Existing parent plate/body retains its own manufacturing role; helpers are separate applicable pieces.
- P05W250 — Caster frame cheek web 250: 2 per C017 variant; Structural S discussion variant.
- P05W300 — Caster frame cheek web 300: 2 per C016 height alternative; Structural S discussion variant.
- P05CT — M12 frame compression sleeve: 4 per caster doubler; reuse instances for matching frame joints; Structural S discussion variant.
- P05JBR — Rearward caster raised frame bridge: 2 per rearward caster alternative; Rearward caster J4 placement alternative.
- P05JROOT — Rearward caster bridge root plate: 4 per rearward caster bridge; Rearward caster J4 placement alternative.
- P05JDP250 — Rearward caster bridge drop 250: 2 per C017 rearward alternative; Rearward caster J4 placement alternative.
- P05JDP300 — Rearward caster bridge drop 300: 2 per C016 rearward alternative; Rearward caster J4 placement alternative.
- P05JCT — Rearward caster cheek upper tie: 1 per rearward caster alternative; Rearward caster J4 placement alternative.
- P05JCT0 — Same-axis caster raised frame upper tie: 1 per retained-axis J3f caster; J3f raised frame and raised cabinet discussion variant.

### Raised-cabinet J3f support reconciliation

J3f retained-axis mount usesP05JCT0 high tie and four P05JDP250 orP05JDP300 translated post instances. Existinglowdoubler 273…283 is a separate Svariant. J3fcabinet 550…750 clears caster upper cheek 443/head plate 365. Prior cabinet 295…495 collides with caster head plates; that low cabinet pose is not combined with this caster.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Caster S frame doubler | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-300.0, -180.0], [-170.0, 170.0], [273.0, 283.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-280.0, -150.0], [-280.0, 150.0], [-200.0, -150.0], [-200.0, 150.0]] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.

## References — local

114. [Main frame crossmember](<../../components/p02-main-frame-crossmember-reference/p02-main-frame-crossmember-reference.md>) — library entry 114.
