THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# ISO4017 M6x16 screw nominal reference

1. **Library number:** 70.
2. **Type:** part.
3. **CAD file:** [c130-iso-4017-m6x16-screw-proposed-class-8-8.dwg](<c130-iso-4017-m6x16-screw-proposed-class-8-8.dwg>).
4. **DWG SHA-256:** `0c8ca6b61cd26be2cc79642bab28684f302d798740ce33cab4da2479defd7a13`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** ISO4017 M6x16 screw nominal reference — C130.

**Design status:** Discussion joint proposal; source nominal screw reference.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A: under-head bearing plane z=0; screw axis +z, tip at nominal z=16; head lies at negative z. Nominal CAD reference is a regular hexagon AF 10, head height 4, nominal M6 thread cylinder and length 16 mm. The regular-hex corner reference 11.5470 mm is calculated for an ideal regular hexagon.

| Feature | Source dimension, mm | Source/status |
|---|---|---|
| Coarse pitch | 1 | ISO 4017:2022, edition 5, Tables 1–2 |
| Head AF s | 9.78–10 | ISO grade A limits |
| Across corners e | ≥11.05 | Source minimum |
| Head height k | nominal 4; 3.85–4.15 | ISO grade A |
| First full-form thread distance a | 1–3 | ISO 225 symbol at bearing face |
| Washer-faced portion c | 0.15–0.5 | ISO 225 source symbol |
| Bearing face inner da / outer dw | da≤6.8; dw≥8.88 | Source bearing-face features |
| Under-head curvature r | ≥0.25 | Source minimum; exact supplied radius retained |
| Incomplete end thread u | ≤2 | Calculated 2P from source Figure 1 note |

Böllhoff class 8.8 product grid explicitly lists this diameter/length.  Source length is under-head; individual length acceptance uses the actual named joint stack. Source Figure 1 allows a chamfered end; rolled end also allowed through M4. Thread tolerance/profile and actual end chamfer/fillet must retain the source standard/product details; the nominal thread cylinder represents the thread envelope.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| S04 — Splash sheet lower row | CURRENT J | 1 | 6 | 6 |
| A05 — Generic guard lid to body lands | CURRENT J4 | 1 | 2×max(4,N_perimeter_fixings_per_guard) | 1×(2×max(4,N_perimeter_fixings_per_guard)) |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D073 / SF01: ISO 4017:2022 official sample PDF Tables 1–2 and Figures 1–2. Acquisition: viewed_online_original_not_downloaded.
- D074 / SF02: Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet. Acquisition: viewed_online_direct_retrieval_failed_dns.
- D098 / SF26: ISO 225:2010 official scope page for fastener dimension symbols. Acquisition: viewed_online_standard_scope.
- D099 / SF27: ISO 225 symbol-description table reproduced in Product Dimensions and Tolerances Standards for Threaded Fasteners. Acquisition: viewed_online_table_extracted.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.



### Splash lower fixing alternative S04B

Six pieces per panel pair serve P24JP — one-washer lower fixing construction. The installation register records the source-limit stack, installed orientation and tool-space proposal.

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

1. standard fastener geometry sources.
2. standard fastener geometry sources.
3. standard fastener geometry sources.
4. standard fastener geometry sources.
5. skf sy25tf sy30tf dimensions.
6. skf sy25tf sy30tf dimensions.
7. skf sy25tf sy30tf dimensions.
8. Kelly KLS-N wiring diagram, §3.2.2, p.14.
9. Exact-order manufacturer sheet.
10. manufacturer sheet.
11. manufacturer sheet.
12. Manufacturer instruction.
13. standard fastener geometry sources.
14. standard fastener geometry sources.
15. standard fastener geometry sources.
16. standard fastener geometry sources.
17. standard fastener geometry sources.
18. standard fastener geometry sources.
19. the retained original.
20. second BMW original.
21. source review.
22. standard fastener geometry sources.
23. standard fastener geometry sources.
24. standard fastener geometry sources.
25. standard fastener geometry sources.
26. standard fastener geometry sources.
27. standard fastener geometry sources.
28. standard fastener geometry sources.
29. standard fastener geometry sources.
30. standard fastener geometry sources.
31. standard fastener geometry sources.
32. standard fastener geometry sources.
33. standard fastener geometry sources.
34. standard fastener geometry sources.
35. standard fastener geometry sources.
36. standard fastener geometry sources.
