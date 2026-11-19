# Pico lower-frame and HRB battery clearance layout proposal

1. **Plan identity:** Model 30 battery fit, within Assembly 2 Pico tracked chassis.
2. **Native drawing:** [Pico battery-bay layout](<pico-lightweight-hrb-bay.dwg>).
3. **DWG SHA-256:** `2c061f67a3653fd868167914c72a4ce54d406d8a8242b0e1d76801dd0ec178ab`.
4. **Actual execution model:** unavailable.

## Technical specification

1. Library 298 contributes the lower formed plate and left and right side carriers. The source group rotates −90° about chassis Z and translates (−14.125076, 9.027626, −5.839633) mm. This transform comes from the checked manufacturer-to-chassis frame in the fit contract.
2. Library 313 contributes one 138 × 46 × 39 mm HRB hard-case clearance solid. Its checked pose is built into the library drawing. The bottom centre is (19.287945, 0.078085, 33.842676) mm in the chassis frame.
3. The source STEP static check gives 0.0971 mm minimum separation to lower formed plate body 3108 at the tested position. That value applies to the rigid battery clearance solid at rest. The source clearance and service study uses the full manufacturer assembly.

## Verification

1. The two native roots expand to four closed solids. The placement and solid topology match the retained source references. The maximum bidirectional vertex-set error was 1.42e-14 mm.
2. Incremental and final verified SAVE, inspected [isometric view](<../../../../images/sowbot/pico-lightweight-hrb-bay-isometric.png>) and guarded closure passed. The occurrence BOM records both source drawings, quantities and transformations.

## References

1. [Library 298 lower frame](<../../../../library/subassemblies/pico-lower-plate-carriers-source-group.md>).
2. [Library 313 battery clearance](<../../../../library/standards/hrb-3s-6000mah-hard-case-pico-clearance.md>).
3. Native geometry and final save.

## Sources — online

1. Sowbot hardware description.
