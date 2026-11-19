THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# ISO 7089 M4 plain washer, proposed 200 HV

1. **Library number:** 88.
2. **Type:** part.
3. **CAD file:** [iso7089-m4-washer-4p3x9x0p8-reference.dwg](<iso7089-m4-washer-4p3x9x0p8-reference.dwg>).
4. **DWG SHA-256:** `82c8bfae0411486bf95807b11f7cd235c1d6af3a40b3e88fc3a6a5658fca8575`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** ISO 7089 M4 plain washer, proposed 200 HV — C144.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A is lower bearing plane z=0; axis normal to parallel faces. Source: JC Fasteners B6iD02 page 1, AISI316/200HV. Dimensions in mm: bore 4.3–4.48, OD8.64–9, thickness 0.7–0.9. Nominal CAD reference: bore 4.3, OD9, thickness 0.8. Source limits remain attached to the named table/product; exact edge radii/bevel are not supplied by the extracted row. For M10/M12 the listed tolerance ranges belong to Westfield, while Stafa/Würth product rows supply nominal dimensions. Proposed hardness 200HV pairs with 8.8 screws/class 8 nuts under the cited guidance. C067 has geometric 13×24×2.5 reuse only; its seller record supplies no 200HV certification and is preserved separately.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| C01 — BMW shield ears to Z uprights | BMW shield alternative | 2 | 4 | 8 |
| C02 — BMW shield upright feet to tray | BMW shield alternative | 2 | 4 | 8 |
| C03 — Leaf upright to cassette extension | LEAF hood alternative | 2 | 8 | 16 |
| C04 — Leaf extension to common floor | LEAF 44corridor alternative | 2 | 6 | 12 |
| C05 — Leaf support bridge root to upright | LEAF hood alternative | 2 | 8 | 16 |
| C06 — Leaf hood ears through insulating blocks | LEAF hood alternative | 2 | 8 | 16 |
| C07 — Victron hoods through reference posts | VICTRON hood alternative | 2 | 4×N_cases | 2×(4×N_cases) |
| C08 — Victron extensions to shelves | VICTRON hood alternative | 2 | 8×N_cases | 2×(8×N_cases) |
| C09 — Split cable-opening strips | LEAF OR VICTRON | 2 | 2×N_actual_split_openings | 2×(2×N_actual_split_openings) |
| F06 — SurLok receptacles to service inserts | BATTERY service | 2 | 8 | 16 |

| E23 — Receiver cradle seat to carrier | J receiver envelope-cradle PROPOSAL | 2 | 2 | 4 |
| E25 — Receiver lateral stops to seat | J receiver envelope-cradle PROPOSAL | 2 | 4 | 8 |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D079 / SF07: JC Fasteners ISO 7089 AISI 316 plain washer, 200 HV, catalogue datasheet B6iD02. Acquisition: viewed_online_original_not_downloaded.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.



### E28 — removable gland-insert fixing

1. **Installed quantity:** 8 per gland carrier in the thin-insert proposal. P23GThin — joint stack records nominal 4.5 mm grip and the actual-length criterion.

## Sources — online

1. second BMW original.
2. source review.
