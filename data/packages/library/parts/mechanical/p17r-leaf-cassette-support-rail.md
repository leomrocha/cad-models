THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Leaf cassette support rail

1. **Library number:** 180.
2. **Type:** part.
3. **CAD file:** [p17r-leaf-cassette-support-rail.dwg](<p17r-leaf-cassette-support-rail.dwg>).
4. **DWG SHA-256:** `6b18c90020fee09213e6eb25e69b01415b66b70891f525cac1f539809d4886b3`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Leaf cassette support rail — P17R.

**Design status:** Discussion nominal hollow-section reference.

## Technical specification

CAD input sheet; custom proposal. Group: battery. Route: Leaf. Quantity: Each rail shape separately.

### Geometry and provenance

Source main bank bare arrangement444×300×204; rail contacts follow module source support faces.

### Units and local datum

Units: mm. Datum A: module support plane; B: stack axis/end restraint reference.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates C021 modules, insulating contact layers, P17E end plates and frame.

### Space and access

Allow covers, sense wiring and cassette removal.

### Custom construction

Cut/finish rails, drill supports and fit insulation attachments.

### Supported battery construction proposal — 13 November 2026

See battery load cases and construction for explicitly proposed masses,2g/3g/1g scenarios and 1.5 strength multiplier.

Propose two independently retained six-module cassettes on a common bottom tray. Bare footprint444×300 mm plus proposed 10 mm central installation corridor gives454×300 mm occupied plan before external stops/returns and terminal service space. Put two supported rails under each stack at source-compatible contact regions; connect outer stops and divider to structural support members. Keep electrical string identities LF-A/LF-B and provide independently supported extraction. Proposed454 mm consumes10 mm more body length than the bare444 mm layout; carry that increment into panel packing.

### Defined rail geometry — 44 mm corridor floor variant

1. **Proposal:** four identical steel square-tube rails20×20×2 mm, cut length 300 mm. Tube size reuses the proposed stock family in P04UPJ20; local construction is a rectangular hollow section with actual stock corner radii and seam recorded during stock inspection. End faces are square to the length axis. This is one manufactured rail geometry with four instances.
2. **Floor-frame placement:** rail length follows N =−150…150 mm; top V =−3 mm contacts common-floor underside and bottom V =−23 mm. Rail U centres are−193,−73,+73,+193 mm, corresponding to each cassette centre Uc =±133 mm plus/minus60 mm. Each rail spans Uc_rail±10 mm. Proposed floor-to-rail attachment is a fabrication joint on those contact faces; source restraint forces determine its weld/fastener sizing.
3. **Stud passage screen:** reconstructed stud columns lie at U =−232,−34,+34,+232 mm. Nearest rail-centre distance is39 mm. Subtract rail half-width 10 and proposed opening radius9 for 39−10−9 =20 mm separation. The lower stud reserve V =−16…0 mm is therefore clear of the rail solids in this proposal.
4. **Transfer:** P17HF — common floor gives floor holes, stack placement and underside clearance. P04UPJ20 — existing20 mm tube proposal supplies the reused nominal stock size. Rail cuts and positions in this section are construction proposals for the 44 mm corridor variant.

### Nissan factory collar/alignment procedure reference

1. Nissan 2013 factory module-stack procedure, EVB-248–250 and 265–267, aligns inter-module collars, uses opposite-corner bolts and temporary Ø7 mm centring bars, then installs the remaining bolts. The rear-stack operation uses a lashing belt to square the stack and holds each bolt stationary while tightening its nut.
2. **Source contact condition:** Nissan identifies aligned collars as supports for the stack bolts. Preserve that supported contact path when comparing the proposed six-module end plates, threaded rods and insulation layers with the actual module collar faces. C021 retains the VT-Tech source bore claim Ø9.1 mm, reconstructed centre pattern276 ×198 mm and reconstructed boss diameter 22.4 mm; the factory7 mm bars describe temporary alignment tooling.
3. **Layered proposal:** six 34 mm seller-envelope modules, seven proposed 0.25 mm layers and two proposed 3 mm plates give211.75 mm nominal stack envelope. Check the layer outlines and actual collar bearing contacts in that specific layered arrangement. The cassette's separate inertia stops/bridges carry their recorded whole-bank loads.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed hollow tube body | PASS | [1, 1, 1, 1] | count |
| Section and cut-length vertex bounds | PASS | [[-10.0, 10.0], [-10.0, 10.0], [0.0, 300.0]] | mm |
| Nominal inner and outer corner radii | PASS | [2.0, 4.0] | mm |

## Sources — online

1. Leaf module item geometry.
2. VT-Tech module dimensions.
3. Square steel tube stock family — supplier reference.
4. Weldable steel plate stock family — supplier reference.

## References — local

110. [Nissan Leaf Gen2 battery module](<../electrical/nissan-leaf-gen2-module-300x222x34.md>) — library entry 110.
111. [Main frame longitudinal rail](<p01-main-frame-longitudinal-rail-reference.md>) — library entry 111.
