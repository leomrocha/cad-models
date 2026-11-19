THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# DIN985 M4 nominal nut reference

1. **Library number:** 76.
2. **Type:** part.
3. **CAD file:** [c150-din-985-m4-nylon-insert-nut-proposed-class-8.dwg](<c150-din-985-m4-nylon-insert-nut-proposed-class-8.dwg>).
4. **DWG SHA-256:** `214a38ab471d60c7ee6fa4b4e3d2274ffa8b27b5a866c9cd05ad0fffc66c9058`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** DIN985 M4 nominal nut reference — C150.

**Design status:** Discussion joint proposal; source nominal regular-hex nut reference.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A is lower nut bearing plane z=0; thread axis +z. HBS DIN 985 table (live page, no edition shown) lists steel classes 8/10/12 and these dimensions: M4×0.7; AF 6.78–7; e≥7.66; total height 4.7–5; hex body m≥2.9; wrenching height m′≥2.2; bearing diameter dw≥5.9; transition da 4–4.6. Published e is a MINIMUM, not a maximum corner envelope. A regular hex based on AF maximum gives a calculated corner reference 8.0829; use actual supplied corners/driver for occupied-envelope verification. Nominal CAD reference uses AF 7, height 5, with thread/bore/insert profile referenced to the source drawing. The table does not fully locate the polymer insert/lead-in/radii; those remain supplied-part details. Proposed property class 8 is a product/class choice supported by the source range, a separate source class from the retained C068 seller identity. DIN 985 M10 AF 17 and M12 AF 19 must not be replaced by ISO 10511 AF 16/18. Full thread and insert engagement plus prevailing-torque installation conditions require the actual joint hardware.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| C01 — BMW shield ears to Z uprights | BMW shield alternative | 1 | 4 | 4 |
| C02 — BMW shield upright feet to tray | BMW shield alternative | 1 | 4 | 4 |
| C03 — Leaf upright to cassette extension | LEAF hood alternative | 1 | 8 | 8 |
| C04 — Leaf extension to common floor | LEAF 44corridor alternative | 1 | 6 | 6 |
| C05 — Leaf support bridge root to upright | LEAF hood alternative | 1 | 8 | 8 |
| C06 — Leaf hood ears through insulating blocks | LEAF hood alternative | 1 | 8 | 8 |
| C07 — Victron hoods through reference posts | VICTRON hood alternative | 1 | 4×N_cases | 1×(4×N_cases) |
| C08 — Victron extensions to shelves | VICTRON hood alternative | 1 | 8×N_cases | 1×(8×N_cases) |
| C09 — Split cable-opening strips | LEAF OR VICTRON | 1 | 2×N_actual_split_openings | 1×(2×N_actual_split_openings) |
| F06 — SurLok receptacles to service inserts | BATTERY service | 1 | 8 | 8 |

| E23 — Receiver cradle seat to carrier | J receiver envelope-cradle PROPOSAL | 1 | 2 | 2 |
| E25 — Receiver lateral stops to seat | J receiver envelope-cradle PROPOSAL | 1 | 4 | 4 |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D083 / SF11: HBS Fasteners DIN 985 dimensions and product information. Acquisition: viewed_online_original_not_downloaded.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.



### E28 — removable gland-insert fixing

1. **Installed quantity:** 4 per gland carrier in the thin-insert proposal. P23GThin — joint stack records nominal 4.5 mm grip and the actual-length criterion.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| Six regular-hex side planes at source AF/2 | PASS | "" |  |
| All unique planar surfaces match six side planes and two axial caps | PASS | "" |  |
| Lower and upper axial face stations | PASS | [0.0, 5.0] | mm |
| All unique cylinders match the optional sourced coaxial bore | PASS | "" |  |
| No additional conical or spherical surfaces | PASS | {} |  |
| Through-bore has an inner boundary loop at both cap stations | PASS | "" |  |
| One closed connected hexagonal body | PASS | [1, 1, 1, 1] | count |

## Sources — online

1. second BMW original.
2. source review.
