THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Nissan Leaf six-module stack end-restraint plate

1. **Library number:** 178.
2. **Type:** part.
3. **CAD file:** [p17e-leaf-stack-end-restraint-plate.dwg](<p17e-leaf-stack-end-restraint-plate.dwg>).
4. **DWG SHA-256:** `7673c28ef5e8a62864030d96a13caedf00ae309a08c5c8f99b69cc38e3197e4b`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Nissan Leaf six-module stack end-restraint plate — P17E.

**Design status:** Discussion construction proposal.

## Technical specification

CAD input sheet; custom proposal. Group: battery. Route: Leaf. Quantity: Each distinct end geometry separately.

### Geometry and provenance

End plate geometry follows module stack restraint/service procedure; include source-compatible contact and clamping features.

### Units and local datum

Units: mm. Datum A: stack end contact face; B: module stack axis.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates C021 and P17R through source-guided restraint hardware and insulating layers.

### Space and access

Keep terminal/tap service access and cover fixing.

### Custom construction

Cut/machine plate; drill clamp features; finish contact edges.

### Engineering transfer — 13 November 2026

1. **Input and status:** Leaf Gen 2 reconstruction; local origin at can centre on lower broad face; X=300 mm can length, Y=222 mm width, Z=34 mm thickness. Source bore diameter Ø9.1 mm; reconstructed bore centres (X,Y)=(±138,±99) mm.
2. **Dimensioned proposal:** transfer these four axes to each end-restraint plate facing a six-module broad-face stack. Calculated pattern spans are 276×198 mm. Six bare 34 mm modules give 6×34=204 mm between the two bare stack-end planes. End plates, intermediate insulation and compression interfaces add their own thicknesses to the restraint stack.
3. **Mating reference:** this pattern uses module-local axes; it requires a recorded rotation/translation into the 444×300×204 bank layout. The 444 mm bank dimension is two 222 mm module widths. Keep each six-module string individually identified.
4. **Construction dependency:** the four centres are a reconstruction template. Confirm donor-hole alignment and the module-specific restraint procedure before transferring a fabrication pattern or setting clamp preload. No clamp force is calculated from bore geometry.

### Supported battery construction proposal — 13 November 2026

Propose3 mm end plates as a structural calculation candidate. Six34 mm modules plus seven 0.25 mm barriers and two 3 mm plates give204+1.75+6=211.75 mm nominal stack-axis envelope; proposed 220 mm packaging space allows8.25 mm before hardware/tolerance/compression details. Preserve276×198 mm reconstruction pattern and donor confirmation.

Separate two functions: module stack hardware establishes source-specified contact/compression; the cassette stops/bridges transfer whole-stack inertia into the chassis. External restraint loads in P20H supply no manufacturer compression preload. Record source compression procedure independently; do not tighten module plates to the cassette inertia force. Plate ribs and source-compatible contact outlines follow plate-bending and module-procedure checks.

### Explicit module placement reference

P17HF — common floor, module-to-bank transform gives the proper rotation, cassette centres and each module's bare/layered height. Transfer the reconstructed four-bore axes through that transform. Nominal lower and upper end-plate faces for the layered alternative are V =0…3 mm and 208.75…211.75 mm in the common-floor frame; these are proposed positions for the existing3 mm plate alternative.

### Finite end-plate outline — layered cassette construction proposal

1. **Shape proposal:**3 mm steel plate,300 mm along module-local x and 222 mm along module-local y, outside corner radius12 mm. Centre in x/y at the retained module datum. Four Ø9.1 mm through holes use the reconstructed axes(x,y)=(±138,±99) mm. The proposed outer outline follows the retained can reconstruction. Corner-circle centres coincide with the reconstructed hole axes; nominal radial material from each hole to the curved outside edge is12−9.1/2 =7.45 mm.
2. **Instances:** two identical end plates per six-module cassette, four per two-cassette bank. In the nominal layered placement their V ranges are0…3 mm and 208.75…211.75 mm. The seven 0.25 mm insulation layers preserve the existing nominal 211.75 mm stack. Contact areas, actual material properties, plate bending and clamping force follow the module restraint procedure and structural calculation inputs.
3. **Lower hardware passage:** the lower nut/washer stack passes through the proposed Ø18 mm common-floor openings. Assemble the module restraint outside the floor, then seat the complete cassette. P17HF — floor-opening construction records the 8 opening axes, receiving envelope, stud tips and rail reserve. The plate's shape, thickness and bore transfer retain proposal/reconstruction labels.

### Nissan factory collar/alignment procedure reference

1. Nissan 2013 factory module-stack procedure, EVB-248–250 and 265–267, aligns inter-module collars, uses opposite-corner bolts and temporary Ø7 mm centring bars, then installs the remaining bolts. The rear-stack operation uses a lashing belt to square the stack and holds each bolt stationary while tightening its nut.
2. **Source contact condition:** Nissan identifies aligned collars as supports for the stack bolts. Preserve that supported contact path when comparing the proposed six-module end plates, threaded rods and insulation layers with the actual module collar faces. C021 retains the VT-Tech source bore claim Ø9.1 mm, reconstructed centre pattern276 ×198 mm and reconstructed boss diameter 22.4 mm; the factory7 mm bars describe temporary alignment tooling.
3. **Layered proposal:** six 34 mm seller-envelope modules, seven proposed 0.25 mm layers and two proposed 3 mm plates give211.75 mm nominal stack envelope. Check the layer outlines and actual collar bearing contacts in that specific layered arrangement. The cassette's separate inertia stops/bridges carry their recorded whole-bank loads.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Nissan Leaf six-module stack end-restraint plate | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-150.0, 150.0], [-111.0, 111.0], [0.0, 3.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-138.0, -99.0], [-138.0, 99.0], [138.0, -99.0], [138.0, 99.0]] | mm |
| Outside corner radius | PASS | [12.0] | mm |

## Sources — online

1. EVShop module listing.
2. VT-Tech module article.
3. Jay Summet, Battery Bay Plan: Nissan Leaf Cells six group.
4. EcoTrust module without additional mounting points.
5. EcoTrust module with additional mounting points.
6. Square steel tube stock family — supplier reference.
7. Weldable steel plate stock family — supplier reference.

## References — local

110. [Nissan Leaf Gen2 battery module](<../electrical/nissan-leaf-gen2-module-300x222x34.md>) — library entry 110.
180. [Leaf cassette support rail](<p17r-leaf-cassette-support-rail.md>) — library entry 180.
