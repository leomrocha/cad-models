THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# ISO4017 M4x16 screw nominal reference

1. **Library number:** 73.
2. **Type:** part.
3. **CAD file:** [c135-iso-4017-m4x16-screw-proposed-class-8-8.dwg](<c135-iso-4017-m4x16-screw-proposed-class-8-8.dwg>).
4. **DWG SHA-256:** `ac406ecf71abc8a438fe2b05da0039b6ab297e65debb5483a024d6424cdcdd93`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** ISO4017 M4x16 screw nominal reference — C135.

**Design status:** Discussion joint proposal; source nominal screw reference.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A: under-head bearing plane z=0; screw axis +z, tip at nominal z=16; head lies at negative z. Nominal CAD reference is a regular hexagon AF 7, head height 2.8, nominal M4 thread cylinder and length 16 mm. The regular-hex corner reference 8.0829 mm is calculated for an ideal regular hexagon.

| Feature | Source dimension, mm | Source/status |
|---|---|---|
| Coarse pitch | 0.7 | ISO 4017:2022, edition 5, Tables 1–2 |
| Head AF s | 6.78–7 | ISO grade A limits |
| Across corners e | ≥7.66 | Source minimum |
| Head height k | nominal 2.8; 2.675–2.925 | ISO grade A |
| First full-form thread distance a | 0.7–2.1 | ISO 225 symbol at bearing face |
| Washer-faced portion c | 0.1–0.4 | ISO 225 source symbol |
| Bearing face inner da / outer dw | da≤4.7; dw≥6.2 | Source bearing-face features |
| Under-head curvature r | ≥0.2 | Source minimum; exact supplied radius retained |
| Incomplete end thread u | ≤1.4 | Calculated 2P from source Figure 1 note |

Böllhoff class 8.8 product grid explicitly lists this diameter/length.  Source length is under-head; individual length acceptance uses the actual named joint stack. Source Figure 1 allows a chamfered end; rolled end also allowed through M4. Thread tolerance/profile and actual end chamfer/fillet must retain the source standard/product details; the nominal thread cylinder represents the thread envelope.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| C01 — BMW shield ears to Z uprights | BMW shield alternative | 1 | 4 | 4 |
| C02 — BMW shield upright feet to tray | BMW shield alternative | 1 | 4 | 4 |
| C03 — Leaf upright to cassette extension | LEAF hood alternative | 1 | 8 | 8 |
| C04 — Leaf extension to common floor | LEAF 44corridor alternative | 1 | 6 | 6 |
| C05 — Leaf support bridge root to upright | LEAF hood alternative | 1 | 8 | 8 |
| C08 — Victron extensions to shelves | VICTRON hood alternative | 1 | 8×N_cases | 1×(8×N_cases) |
| C09 — Split cable-opening strips | LEAF OR VICTRON | 1 | 2×N_actual_split_openings | 1×(2×N_actual_split_openings) |

| E23 — Receiver cradle seat to carrier | J receiver envelope-cradle PROPOSAL | 1 | 2 | 2 |
| E25 — Receiver lateral stops to seat | J receiver envelope-cradle PROPOSAL | 1 | 4 | 4 |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D073 / SF01: ISO 4017:2022 official sample PDF Tables 1–2 and Figures 1–2. Acquisition: viewed_online_original_not_downloaded.
- D074 / SF02: Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet. Acquisition: viewed_online_direct_retrieval_failed_dns.
- D098 / SF26: ISO 225:2010 official scope page for fastener dimension symbols. Acquisition: viewed_online_standard_scope.
- D099 / SF27: ISO 225 symbol-description table reproduced in Product Dimensions and Tolerances Standards for Threaded Fasteners. Acquisition: viewed_online_table_extracted.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.



### E28 — removable gland-insert fixing

1. **Installed quantity:** 4 per gland carrier in the thin-insert proposal. P23GThin — joint stack records nominal 4.5 mm grip and the actual-length criterion.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| six unique hex side planes and three axial planes | PASS | "" |  |
| exposed head/shaft shoulder at under-head datum | PASS | "" |  |
| one coaxial nominal-radius shaft cylinder | PASS | "" |  |
| no additional cone, sphere or torus surfaces | PASS | "" |  |
| axial vertex extrema equal head top and shaft tip stations | PASS | "" |  |
| one closed connected solid | PASS | "" |  |

## Sources — online

1. second BMW original.
2. source review.
