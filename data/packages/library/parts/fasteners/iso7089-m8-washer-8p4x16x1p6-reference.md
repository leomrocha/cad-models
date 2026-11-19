THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# ISO 7089 M8 plain washer, proposed 200 HV

1. **Library number:** 91.
2. **Type:** part.
3. **CAD file:** [iso7089-m8-washer-8p4x16x1p6-reference.dwg](<iso7089-m8-washer-8p4x16x1p6-reference.dwg>).
4. **DWG SHA-256:** `533eb9e8cd7f67ab3e4f3fdebdd2294d990d9d7a60e17067ed4a6e74602581e5`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** ISO 7089 M8 plain washer, proposed 200 HV — C147.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A is lower bearing plane z=0; axis normal to parallel faces. Source: Stafa zinc-plated steel 200HV nominal table; separate Westfield ISO 7089 tolerance table. Dimensions in mm: bore 8.4, OD16, thickness 1.6; nominal only. Nominal CAD reference: bore 8.4, OD16, thickness 1.6. Source limits remain attached to the named table/product; exact edge radii/bevel are not supplied by the extracted row. For M10/M12 the listed tolerance ranges belong to Westfield, while Stafa/Würth product rows supply nominal dimensions. Proposed hardness 200HV pairs with 8.8 screws/class 8 nuts under the cited guidance. C067 has geometric 13×24×2.5 reuse only; its seller record supplies no 200HV certification and is preserved separately.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| J07 — Removable brake wing to upstand | CURRENT conditionalbrakes | 2 | 8 | 16 |
| E03 — Kelly source controller mounting | CURRENT Kelly pair | 2 | 8 | 16 |
| B01 — BMW supported module tabs | BMW alternative | 2 | 4 | 8 |
| B02 — Battery common tray/frame support | BMW lowframe OR J boltedpad comparison | 2 | 4 | 8 |
| B04 — Leaf six-module stack restraint | LEAF alternative | 2 | 8 | 16 |
| B05 — Leaf cassette removable bridges | LEAF alternative | 2 | 2cassettes×2bridges×2endjoints | 2×(2cassettes×2bridges×2endjoints) |
| B06 — Victron shelves to frame | VICTRON alternative | 2 | 4×N_shelves | 2×(4×N_shelves) |
| B07 — Victron restraint bridges | VICTRON alternative | 2 | N_actual_bridge_axes | 2×(N_actual_bridge_axes) |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D080 / SF08: Stafa ISO 7089 zinc-plated steel 200 HV technical information. Acquisition: viewed_online_original_not_downloaded.
- D081 / SF09: Westfield Fasteners ISO 7089 washer dimensions and tolerances. Acquisition: viewed_online_original_not_downloaded.
- D082 / SF10: Würth ISO 7089 A4 stainless 200 HV washer datasheet. Acquisition: viewed_online_original_not_downloaded.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.

## Sources — online

1. Kelly KLS-N wiring diagram, §3.2.2, p.14.
2. second BMW original.
3. source review.
