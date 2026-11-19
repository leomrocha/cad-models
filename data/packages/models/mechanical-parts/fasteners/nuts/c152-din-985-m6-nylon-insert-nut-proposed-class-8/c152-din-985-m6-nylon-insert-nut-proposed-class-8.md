THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# DIN985 M6 nominal nut reference

1. **Library number:** 77.
2. **Type:** part.
3. **CAD file:** [c152-din-985-m6-nylon-insert-nut-proposed-class-8.dwg](<c152-din-985-m6-nylon-insert-nut-proposed-class-8.dwg>).
4. **DWG SHA-256:** `b005197d6d63b19d28d1785191f25a1a7a8a07068289550796644a12ed197e08`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** DIN985 M6 nominal nut reference — C152.

**Design status:** Discussion joint proposal; source nominal regular-hex nut reference.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A is lower nut bearing plane z=0; thread axis +z. HBS DIN 985 table (live page, no edition shown) lists steel classes 8/10/12 and these dimensions: M6×1; AF 9.78–10; e≥11.05; total height 5.7–6; hex body m≥4; wrenching height m′≥3.3; bearing diameter dw≥8.9; transition da 6–6.75. Published e is a MINIMUM, not a maximum corner envelope. A regular hex based on AF maximum gives a calculated corner reference 11.5470; use actual supplied corners/driver for occupied-envelope verification. Nominal CAD reference uses AF 10, height 6, with thread/bore/insert profile referenced to the source drawing. The table does not fully locate the polymer insert/lead-in/radii; those remain supplied-part details. Proposed property class 8 is a product/class choice supported by the source range, a separate source class from the retained C068 seller identity. DIN 985 M10 AF 17 and M12 AF 19 must not be replaced by ISO 10511 AF 16/18. Full thread and insert engagement plus prevailing-torque installation conditions require the actual joint hardware.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| S02 — Deck sheet to ledge | CURRENT J ordinaryfasteneralternative | 1 | 6 | 6 |
| S03 — Splash lower angle to rail | CURRENT J | 1 | 12 | 12 |
| S04 — Splash sheet lower row | CURRENT J | 1 | 6 | 6 |
| S05 — Splash sheet upper split beams | CURRENT J | 1 | 6 | 6 |
| E01 — Kelly carrier through post ends | CURRENT Kelly pair | 1 | 8 | 8 |
| E02 — Kelly rail-gap-post access correction | CURRENT Kelly pair | 1 | 4 | 4 |
| E04 — Receiver bridge to rail | CURRENT J | 1 | 2 | 2 |
| E05 — Receiver carrier to bridge | CURRENT J | 1 | 2 | 2 |
| E08 — Source feet to R1 carrier | CURRENT R1 | 1 | 4 | 4 |
| B03 — J tray pad bolted alternative | J ALTERNATIVE to weldedpads | 1 | 4 | 4 |
| F01 — Functional insert independent support P23Battery | FUNCTIONAL bay alternative | 1 | 4×N_P23Battery | 1×(4×N_P23Battery) |
| F02 — Functional insert independent support P23Charge | FUNCTIONAL bay alternative | 1 | 4×N_P23Charge | 1×(4×N_P23Charge) |
| F03 — Functional insert independent support P23Disconnect | FUNCTIONAL bay alternative | 1 | 4×N_P23Disconnect | 1×(4×N_P23Disconnect) |
| F04 — Functional insert independent support P22FuseShoe | FUNCTIONAL bay alternative | 1 | 4×N_P22FuseShoe | 1×(4×N_P22FuseShoe) |
| F05 — Functional insert independent support P23Buttons | FUNCTIONAL bay alternative | 1 | 4×N_P23Buttons | 1×(4×N_P23Buttons) |
| F08 — SmallM6equipment carrier to angle shoes | ALTERNATIVE equipment families | 1 | 4×N_actual_equipment_carriers | 1×(4×N_actual_equipment_carriers) |
| F09 — Equipment shoe frame-side leg | ALTERNATIVE equipment families | 1 | 4×N_shoe_supported_carriers | 1×(4×N_shoe_supported_carriers) |
| F13 — Curtis controller to thermal plate | BT Curtis alternative | 1 | 3 | 3 |
| A05 — Generic guard lid to body lands | CURRENT J4 | 1 | 2×max(4,N_perimeter_fixings_per_guard) | 1×(2×max(4,N_perimeter_fixings_per_guard)) |
| A06 — Guard body to stationary support | CURRENT J4 | 1 | 2×N_actual_guard_body_axes | 1×(2×N_actual_guard_body_axes) |

| E24 — Receiver keeper bars to carrier | J receiver envelope-cradle PROPOSAL | 1 | 4 | 4 |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D083 / SF11: HBS Fasteners DIN 985 dimensions and product information. Acquisition: viewed_online_original_not_downloaded.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.



### E26 — Orion converter mounting proposal

1. **Installed quantity:** 4 per converter support in the BT auxiliary 12 V route. P22OR2412 — support and joint stack gives the source flange and proposed grip/length conditions.


### Rectangular J4 guard installation uses

1. **A06J4 — body to upper flange:** 8 pieces per guard pair in this discussion construction alternative.
2. **A07J4 — flange to rail:** 8 pieces per guard pair in this discussion construction alternative.

The installation register and guard flange input record the corresponding stack and installed access.

### Splash lower fixing alternative S04B

Six pieces per panel pair serve P24JP — one-washer lower fixing construction. The installation register records the source-limit stack, installed orientation and tool-space proposal.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| Six regular-hex side planes at source AF/2 | PASS | "" |  |
| All unique planar surfaces match six side planes and two axial caps | PASS | "" |  |
| Lower and upper axial face stations | PASS | [0.0, 6.0] | mm |
| All unique cylinders match the optional sourced coaxial bore | PASS | "" |  |
| No additional conical or spherical surfaces | PASS | {} |  |
| Through-bore has an inner boundary loop at both cap stations | PASS | "" |  |
| One closed connected hexagonal body | PASS | [1, 1, 1, 1] | count |

## Sources — online

1. Kelly KLS-N wiring diagram, §3.2.2, p.14.
