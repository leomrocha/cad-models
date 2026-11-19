# Mini Sowbot battery clearance layout proposal

1. **Plan identity:** Assembly 6, Mini Sowbot.
2. **Native drawing:** [Mini battery clearance layout](<mini-hardware-battery-envelope-layout-proposal.dwg>).
3. **DWG SHA-256:** `d537c446c290479419ce7457e738ea3fe647c3240a44f6121b9a2e3066dcbdc2`.
4. **Actual execution model:** unavailable.

## Technical specification

1. **Battery reference:** one Propow CPN24050, 24 V 50 Ah clearance solid at the saved Mini footprint position. Its native bounds in millimetres are X = −153 to 153, Y = −210 to −36 and Z = 0 to 220. The 200 mm supplier height reference occupies the same horizontal projection.
2. **Placement:** the existing Mini base, shared Brain hardware and Open BTS7960 placement matrices are retained. The clearance solid replaces the battery footprint root. The assembly has four live roots.
3. **Clearance:** the battery projection stays 5 mm from the represented Brain exterior and 136 mm from the represented driver during a straight +Z lift. Both height cases use the same 306 × 174 mm footprint. The base remains a planar source installation reference.
4. **Verification:** the transferred clearance solid retains all eight expected installed vertices, six planar faces and reciprocal closed topology. The saved source check reads SAT and the installed check reads SAB. The base, Brain and driver root placements match the saved baseline. Incremental saves, final file hash, zero dropped entities and both owned-document closures passed.

## Sources — online

1. Propow CPN24050 technical data, the 306 × 174 × 200/220 mm size field.
2. Sowbot hardware table, Mini base and the separately described 24 V 30 Ah battery.

## References

1. [Previous Mini layout](<mini-receiver-exterior-hardware-layout-proposal.md>).
2. [Propow clearance solids](<../../../../library/standards/propow-cpn24050-size-field-envelopes.md>).
3. [Isometric view](<../../../../images/sowbot/mini-hardware-battery-envelope-layout-proposal-isometric.png>).
4. [Assembly occurrence BOM](<../../../../docs/sowbot/bom/mini-battery-envelope-occurrences.csv>).
