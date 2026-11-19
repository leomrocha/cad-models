THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# ISO 7089 M6 plain washer, proposed 200 HV

1. **Library number:** 90.
2. **Type:** part.
3. **CAD file:** [iso7089-m6-washer-6p4x12x1p6-reference.dwg](<iso7089-m6-washer-6p4x12x1p6-reference.dwg>).
4. **DWG SHA-256:** `624e3bb3c0818f68d4cf020851b26e077ee0f073e70d0bde81014ee8dd199943`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** ISO 7089 M6 plain washer, proposed 200 HV — C146, C156.

## Technical specification

Status: source-dimensional input; length, property class, finish/material and joint use retain PROPOSAL status where stated. Units: mm. Quantity follows the named route and source-pattern multiplicity below; alternatives are counted separately.

### Geometry, datums and source limits

Datum A is lower bearing plane z=0; axis normal to parallel faces. Source: JC Fasteners B6iD02 page 1, AISI316/200HV. Dimensions in mm: bore 6.4–6.62, OD11.57–12, thickness 1.4–1.8. Nominal CAD reference: bore 6.4, OD12, thickness 1.6. Source limits remain attached to the named table/product; exact edge radii/bevel are not supplied by the extracted row. For M10/M12 the listed tolerance ranges belong to Westfield, while Stafa/Würth product rows supply nominal dimensions. Proposed hardness 200HV pairs with 8.8 screws/class 8 nuts under the cited guidance. C067 has geometric 13×24×2.5 reuse only; its seller record supplies no 200HV certification and is preserved separately.

### Occupied space, installation and quantity

Assembly checks use the source-limit head, washer, nut and actual tool insertion/extraction envelopes at the installed transform. Record full thread/insert engagement, locking/preload and material contact at each named joint.

| Joint | Route / alternative | Per joint | Repeated joints | Quantity / formula |
|---|---|---:|---:|---:|
| S02 — Deck sheet to ledge | CURRENT J ordinaryfasteneralternative | 2 | 6 | 12 |
| S03 — Splash lower angle to rail | CURRENT J | 2 | 12 | 24 |
| S04 — Splash sheet lower row | CURRENT J | 2 | 6 | 12 |
| S05 — Splash sheet upper split beams | CURRENT J | 2 | 6 | 12 |
| E01 — Kelly carrier through post ends | CURRENT Kelly pair | 2 | 8 | 16 |
| E02 — Kelly rail-gap-post access correction | CURRENT Kelly pair | 2 | 4 | 8 |
| E04 — Receiver bridge to rail | CURRENT J | 2 | 2 | 4 |
| E05 — Receiver carrier to bridge | CURRENT J | 2 | 2 | 4 |
| E07 — R1 carrier to threaded rail end blocks | CURRENT R1 | 1 | 4 | 4 |
| E08 — Source feet to R1 carrier | CURRENT R1 | 2 | 4 | 8 |
| B03 — J tray pad bolted alternative | J ALTERNATIVE to weldedpads | 2 | 4 | 8 |
| F01 — Functional insert independent support P23Battery | FUNCTIONAL bay alternative | 2 | 4×N_P23Battery | 2×(4×N_P23Battery) |
| F02 — Functional insert independent support P23Charge | FUNCTIONAL bay alternative | 2 | 4×N_P23Charge | 2×(4×N_P23Charge) |
| F03 — Functional insert independent support P23Disconnect | FUNCTIONAL bay alternative | 2 | 4×N_P23Disconnect | 2×(4×N_P23Disconnect) |
| F04 — Functional insert independent support P22FuseShoe | FUNCTIONAL bay alternative | 2 | 4×N_P22FuseShoe | 2×(4×N_P22FuseShoe) |
| F05 — Functional insert independent support P23Buttons | FUNCTIONAL bay alternative | 2 | 4×N_P23Buttons | 2×(4×N_P23Buttons) |
| F08 — SmallM6equipment carrier to angle shoes | ALTERNATIVE equipment families | 2 | 4×N_actual_equipment_carriers | 2×(4×N_actual_equipment_carriers) |
| F09 — Equipment shoe frame-side leg | ALTERNATIVE equipment families | 2 | 4×N_shoe_supported_carriers | 2×(4×N_shoe_supported_carriers) |
| F13 — Curtis controller to thermal plate | BT Curtis alternative | 2 | 3 | 6 |
| A05 — Generic guard lid to body lands | CURRENT J4 | 2 | 2×max(4,N_perimeter_fixings_per_guard) | 2×(2×max(4,N_perimeter_fixings_per_guard)) |
| A06 — Guard body to stationary support | CURRENT J4 | 2 | 2×N_actual_guard_body_axes | 2×(2×N_actual_guard_body_axes) |

| E24 — Receiver keeper bars to carrier | J receiver envelope-cradle PROPOSAL | 2 | 4 | 8 |

The authoritative fastener installation register gives the actual source grip, orientation, interface parameters and evidence lines. Numeric quantities belong to their named proposal routes. Variable-length parent families use their actual source grip.

### Sources and provenance

- D079 / SF07: JC Fasteners ISO 7089 AISI 316 plain washer, 200 HV, catalogue datasheet B6iD02. Acquisition: viewed_online_original_not_downloaded.

- Standard geometry extraction: source standards/pages, symbols, acquisition limits and source-class distinctions.
- Source register.



### E26 — Orion converter mounting proposal

1. **Installed quantity:** 8 per converter support in the BT auxiliary 12 V route. P22OR2412 — support and joint stack gives the source flange and proposed grip/length conditions.


### Rectangular J4 guard installation uses

1. **A06J4 — body to upper flange:** 16 pieces per guard pair in this discussion construction alternative.
2. **A07J4 — flange to rail:** 16 pieces per guard pair in this discussion construction alternative.

The installation register and guard flange input record the corresponding stack and installed access.

### Splash lower fixing alternative S04B

Six pieces per panel pair serve P24JP — one-washer lower fixing construction. The installation register records the source-limit stack, installed orientation and tool-space proposal.

## Sources — online

1. Kelly KLS-N wiring diagram, §3.2.2, p.14.
