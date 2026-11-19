THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# DIN985 M8 nominal nut reference

1. **Library number:** 78.
2. **Type:** part.
3. **CAD file:** [c153-din-985-m8-nylon-insert-nut-proposed-class-8.dwg](<c153-din-985-m8-nylon-insert-nut-proposed-class-8.dwg>).
4. **DWG SHA-256:** `f1c0db1417a3afad9cabf855b33e49fd6088925b41e4f428a4039006ed754019`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** DIN985 M8 nominal nut reference — C153.

**Design status:** Discussion joint proposal; source nominal regular-hex nut reference.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A is lower nut bearing plane z=0; thread axis +z. HBS DIN 985 table (live page, no edition shown) lists steel classes 8/10/12 and these dimensions: M8×1.25; AF 12.73–13; e≥14.38; total height 7.64–8; hex body m≥5.5; wrenching height m′≥4.4; bearing diameter dw≥11.6; transition da 8–8.75. Published e is a MINIMUM, not a maximum corner envelope. A regular hex based on AF maximum gives a calculated corner reference 15.0111; use actual supplied corners/driver for occupied-envelope verification. Nominal CAD reference uses AF 13, height 8, with thread/bore/insert profile referenced to the source drawing. The table does not fully locate the polymer insert/lead-in/radii; those remain supplied-part details. Proposed property class 8 is a product/class choice supported by the source range, a separate source class from the retained C068 seller identity. DIN 985 M10 AF 17 and M12 AF 19 must not be replaced by ISO 10511 AF 16/18. Full thread and insert engagement plus prevailing-torque installation conditions require the actual joint hardware.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| J07 — Removable brake wing to upstand | CURRENT conditionalbrakes | 1 | 8 | 8 |
| E03 — Kelly source controller mounting | CURRENT Kelly pair | 1 | 8 | 8 |
| B01 — BMW supported module tabs | BMW alternative | 1 | 4 | 4 |
| B02 — Battery common tray/frame support | BMW lowframe OR J boltedpad comparison | 1 | 4 | 4 |
| B04 — Leaf six-module stack restraint | LEAF alternative | 2 | 8 | 16 |
| B05 — Leaf cassette removable bridges | LEAF alternative | 1 | 2cassettes×2bridges×2endjoints | 1×(2cassettes×2bridges×2endjoints) |
| B06 — Victron shelves to frame | VICTRON alternative | 1 | 4×N_shelves | 1×(4×N_shelves) |
| B07 — Victron restraint bridges | VICTRON alternative | 1 | N_actual_bridge_axes | 1×(N_actual_bridge_axes) |

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
| Lower and upper axial face stations | PASS | [0.0, 8.0] | mm |
| All unique cylinders match the optional sourced coaxial bore | PASS | "" |  |
| No additional conical or spherical surfaces | PASS | {} |  |
| Through-bore has an inner boundary loop at both cap stations | PASS | "" |  |
| One closed connected hexagonal body | PASS | [1, 1, 1, 1] | count |

## Sources — online

1. Kelly KLS-N wiring diagram, §3.2.2, p.14.
2. second BMW original.
3. source review.
