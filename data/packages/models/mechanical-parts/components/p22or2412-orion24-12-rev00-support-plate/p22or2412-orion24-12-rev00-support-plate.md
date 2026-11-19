THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Orion24/12 Rev00 source-pattern support plate

1. **Library number:** 190.
2. **Type:** part.
3. **CAD file:** [p22or2412-orion24-12-rev00-support-plate.dwg](<p22or2412-orion24-12-rev00-support-plate.dwg>).
4. **DWG SHA-256:** `4cf64ec259d0a747089e948a7f359b8a72cc82a73be060d41689c1018d88578a`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Orion24/12 Rev00 source-pattern support plate — P22OR2412.

**Design status:** Discussion construction proposal.

## Technical specification

Discussion construction proposal. Route: BT auxiliary 12 V supply using C045 — Victron Orion24-12 converter. Quantity: one plate per converter. Parent: P22Converter — DC/DC support family.

### Source, dimensions and local frame

1. **Source interface:** C045 retained STEP Rev00, heat-sink solid #42102. Four source radius 4 mm notch axes have source-native (x,z) = (±87.15,25) and (±87.15,96) mm. Flange planes y = 34.5 and 37.5 mm give calculated flange thickness 3 mm. C045 source-entity extraction records the original path, hash and entity identities.
2. **Local support frame:** u = source x; v = source z − 60.5 mm; n = 37.5 mm − source y. The source support-contact faces are n = 0 mm. The converter flange occupies n = 0…3 mm. The plate front contacts these faces. Installed orientation uses the manufacturer terminal-down requirement.
3. **Proposed plate:** 3 mm steel, width 227 mm along u and height 173 mm along v. Closed rectangular outline u = −113.5…113.5 mm, v = −86.5…86.5 mm, corner radius 5 mm. Extrude n = −3…0 mm. Steel is the proposed non-flammable mounting surface; finish and material grade follow the structural stock record.
4. **Converter fixing holes:** four through Ø6.6 mm axes normal n at (u,v) = (±87.15,±35.5) mm, matching source STEP Rev00 pitches 174.3 × 71 mm. Proposed hole diameter 6.6 mm gives 0.6 mm nominal diametral clearance around an M6 nominal shank.
5. **Support fixing holes:** four through Ø6.6 mm axes normal n at (u,v) = (±103.5,±60) mm. These are proposed carrier-interface axes. They place the support fasteners outside the source heat-sink width ±93.3 mm.
6. **Source revision:** this plate uses STEP Rev00 and the existing converter DWG's 174.3 mm pitch. The manufacturer's Rev01 drawing pitch is 174 mm; its mounting-pattern record is separately labelled in C045.

### Converter-to-plate joint E26

1. **Joint proposal:** four source flange-to-plate fixings. Nominal solid grip G = 3 mm source flange + 3 mm proposed plate = 6 mm. Hardware per fixing: one C128 — ISO 4017 M6×20 screw, proposed class 8.8, two C146 — ISO 7089 M6 plain washer, proposed 200 HV and one C152 — DIN 985 M6 nylon-insert nut, proposed class 8. Four fixings use four screws, eight washers and four nuts.
2. **Length criterion:** source washer maximum thickness 1.8 mm each, nut maximum height 6 mm and source M6 pitch 1 mm. Proposed exposed thread = two pitches = 2 mm. Required actual screw length L ≥ G + 2 × 1.8 + 6 + 2 × 1 = G + 11.6 mm. At nominal G = 6 mm, minimum actual L = 17.6 mm. Proposed M6 × 20 mm nominal length gives 2.4 mm nominal arithmetic margin. Actual plate/flange grip and supplied screw length enter the same criterion.
3. **Assembly direction:** place the screw head and one washer against the source flange's head-side face, pass the shank through the mounting notch and plate, and install rear washer and nut. Set all four screws before applying the source converter to its supported position. Tightening torque for these custom mounting joints derives from their material/fastener joint specification.
4. **Tool-space proposal:** reserve a Ø15 mm cylinder about each converter screw axis on the head side for socket access, and the source M6 nut/tool envelope behind the carrier. Inspect the placed manufacturer model against these tool cylinders.

### Written-geometry checks

1. **Converter-hole straight-edge ligaments:** minimum along u = 113.5 − 87.15 − 3.3 = 23.05 mm; along v = 86.5 − 35.5 − 3.3 = 47.7 mm.
2. **Support-hole straight-edge ligaments:** minimum along u = 113.5 − 103.5 − 3.3 = 6.7 mm; along v = 86.5 − 60 − 3.3 = 23.2 mm.
3. **Support-washer source-envelope gap:** maximum M6 washer radius 6 mm. Its inner edge at |u| = 103.5 − 6 = 97.5 mm gives 97.5 − 93.3 = 4.2 mm nominal horizontal gap from the source heat-sink vertex span. Outer plate-edge margin = 113.5 − 103.5 − 6 = 4 mm.
4. **Converter washer at source flange edge:** source heat-sink outer x = ±93.3 mm, notch x = ±87.15 mm and washer maximum radius 6 mm give 93.3 − 87.15 − 6 = 0.15 mm nominal straight-edge allowance. The open notch receives the washer across its source 8 mm width. Preserve the actual source notch/fillet profile in the mounting check.

### Cooling and CAD construction record

1. **Manufacturer installation:** the retained Victron manual Rev 14 — 02/2026, section 4.1, printed page 4, requires vertical mounting, terminals down and 100 mm clear space above and below the converter. C045 contains the exact manual path/hash and source conditions.
2. **Model construction:** create the proposed rounded plate outline, extrude 3 mm, cut the eight Ø6.6 mm through holes, and record their source/proposal axis groups separately. Preserve the STEP Rev00 converter and its component transforms as the mating reference.
3. **Inspection record:** record plate thickness, outline dimensions, corner radius, all hole centres/diameters, flange contacts, actual grip, screw lengths and head/tool access. Record the source-local-to-installed transform with the terminal-down orientation and cooling spaces.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Orion24/12 Rev00 source-pattern support plate | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-113.5, 113.5], [-86.5, 86.5], [-3.0, 0.0]] | mm |
| Source-sheet hole group 1 | PASS | [[-103.5, -60.0], [-103.5, 60.0], [-87.15, -35.5], [-87.15, 35.5], [87.15, -35.5], [87.15, 35.5], [103.5, -60.0], [103.5, 60.0]] | mm |
| Outside corner radius | PASS | [5.0] | mm |

## Sources — online

1. manufacturer dimension drawing.
2. Weldable steel plate stock family — supplier reference.
3. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.
4. HBS Fasteners DIN 985 dimensions and product information.
