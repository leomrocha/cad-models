THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# DIN985 M10 nominal nut reference

1. **Library number:** 79.
2. **Type:** part.
3. **CAD file:** [c154-din-985-m10-nylon-insert-nut-proposed-class-8.dwg](<c154-din-985-m10-nylon-insert-nut-proposed-class-8.dwg>).
4. **DWG SHA-256:** `a393e75a73a8e4cc1dff911eb72ee76c6bf61cbc50f48bddb097b52746e81d50`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** DIN985 M10 nominal nut reference — C154.

**Design status:** Discussion joint proposal; source nominal regular-hex nut reference.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A is lower nut bearing plane z=0; thread axis +z. HBS DIN 985 table (live page, no edition shown) lists steel classes 8/10/12 and these dimensions: M10×1.5; AF 16.73–17; e≥18.9; total height 9.64–10; hex body m≥6.5; wrenching height m′≥5.5; bearing diameter dw≥15.6; transition da 10–10.8. Published e is a MINIMUM, not a maximum corner envelope. A regular hex based on AF maximum gives a calculated corner reference 19.6299; use actual supplied corners/driver for occupied-envelope verification. Nominal CAD reference uses AF 17, height 10, with thread/bore/insert profile referenced to the source drawing. The table does not fully locate the polymer insert/lead-in/radii; those remain supplied-part details. Proposed property class 8 is a product/class choice supported by the source range, a separate source class from the retained C068 seller identity. DIN 985 M10 AF 17 and M12 AF 19 must not be replaced by ISO 10511 AF 16/18. Full thread and insert engagement plus prevailing-torque installation conditions require the actual joint hardware.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| J01 — Motor moving plate to fixed backbone | CURRENT ME/J4 | 1 | 8 | 8 |
| J03 — 25 mm bearing through solid bar | ALTERNATIVE J4-25 ONLY | 1 | 8 | 8 |
| S01 — Deck and lifting foot through rail | Recorded four-hole foot error | 1 | 32 | 32 |
| A09 — PRO-M stationary housing to support | Current threaded-housing proposal | 0 | 8 | 0 |
| A13 — Sumitomo custom support feet through frame | SUMITOMO alternative | 1 | 8 | 8 |
| S01-2 — Two-hole deck and lifting foot connection | J two-hole foot proposal | 1 | 16 | 16 |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D083 / SF11: HBS Fasteners DIN 985 dimensions and product information. Acquisition: viewed_online_original_not_downloaded.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| Six regular-hex side planes at source AF/2 | PASS | "" |  |
| All unique planar surfaces match six side planes and two axial caps | PASS | "" |  |
| Lower and upper axial face stations | PASS | [0.0, 10.0] | mm |
| All unique cylinders match the optional sourced coaxial bore | PASS | "" |  |
| No additional conical or spherical surfaces | PASS | {} |  |
| Through-bore has an inner boundary loop at both cap stations | PASS | "" |  |
| One closed connected hexagonal body | PASS | [1, 1, 1, 1] | count |

## Sources — online

1. standard fastener geometry sources.
2. skf sy25tf sy30tf dimensions.
3. skf sy25tf sy30tf dimensions.
4. skf sy25tf sy30tf dimensions.
5. Kelly KLS-N wiring diagram, §3.2.2, p.14.
6. Exact-order manufacturer sheet.
7. manufacturer sheet.
8. manufacturer sheet.
9. Manufacturer instruction.
10. standard fastener geometry sources.
11. standard fastener geometry sources.
12. standard fastener geometry sources.
13. standard fastener geometry sources.
14. standard fastener geometry sources.
15. the retained original.
16. second BMW original.
17. source review.
18. standard fastener geometry sources.
19. standard fastener geometry sources.
20. standard fastener geometry sources.
21. standard fastener geometry sources.
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
