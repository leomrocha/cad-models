THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# ISO 4017 M10×35 screw, proposed class 8.8

1. **Library number:** 86.
2. **Type:** part.
3. **CAD file:** [iso4017-m10x35-nominal-reference.dwg](<iso4017-m10x35-nominal-reference.dwg>).
4. **DWG SHA-256:** `9d66440e7c2f23df1806ebe33f606fb13d283f9251e9d0b52b003d69bd5952e8`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** ISO 4017 M10×35 screw, proposed class 8.8 — C124.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A: under-head bearing plane z=0; screw axis +z, tip at nominal z=35; head lies at negative z. Nominal CAD reference is a regular hexagon AF 16 mm, head height 6.4 mm, nominal M10 thread cylinder and length 35 mm. The regular-hex corner reference 18.4752 mm is calculated for an ideal regular hexagon.

| Feature | Source dimension, mm | Source/status |
|---|---|---|
| Coarse pitch | 1.5 | ISO 4017:2022, edition 5, Tables 1–2 |
| Head AF s | 15.73–16 | ISO grade A limits |
| Across corners e | ≥17.77 | Source minimum |
| Head height k | nominal 6.4; 6.22–6.58 | ISO grade A |
| First full-form thread distance a | 1.5–4.5 | ISO 225 symbol at bearing face |
| Washer-faced portion c | 0.15–0.6 | ISO 225 source symbol |
| Bearing face inner da / outer dw | da≤11.2; dw≥14.63 | Source bearing-face features |
| Under-head curvature r | ≥0.4 | Source minimum; exact supplied radius retained |
| Incomplete end thread u | ≤3.0 | Calculated 2P from source Figure 1 note |

Böllhoff class 8.8 product grid explicitly lists this diameter/length.  Böllhoff product limits differ: M10 k max 6.69/AF min 15.57; M12 k max 7.79/AF min 17.57. Keep these product envelopes separate from ISO 2022 grade A. Source length is under-head; individual length acceptance uses the actual named joint stack. Source Figure 1 allows a chamfered end; rolled end also allowed through M4. Thread tolerance/profile and actual end chamfer/fillet must retain the source standard/product details; the nominal thread cylinder represents the thread envelope.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| J01 — Motor moving plate to fixed backbone | CURRENT ME/J4 | 1 | 8 | 8 |
| A09 — PRO-M stationary housing to support | Sumitomo PRO-M alternative | 1 | 8 | 8 |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D073 / SF01: ISO 4017:2022 official sample PDF Tables 1–2 and Figures 1–2. Acquisition: viewed_online_original_not_downloaded.
- D074 / SF02: Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet. Acquisition: viewed_online_direct_retrieval_failed_dns.
- D098 / SF26: ISO 225:2010 official scope page for fastener dimension symbols. Acquisition: viewed_online_standard_scope.
- D099 / SF27: ISO 225 symbol-description table reproduced in Product Dimensions and Tolerances Standards for Threaded Fasteners. Acquisition: viewed_online_table_extracted.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.

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
