THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Nissan Leaf Gen2 battery module

1. **Library number:** 110.
2. **Type:** part.
3. **CAD file:** [nissan-leaf-gen2-module-300x222x34.dwg](<nissan-leaf-gen2-module-300x222x34.dwg>).
4. **DWG SHA-256:** `4eabb05101f181a9ab8fbf29bd0e6f8f45b823c273eecd2e684e3e870053b13c`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Nissan Leaf Gen2 battery module — C021.

## Technical specification

CAD input sheet; source component/model reference. Group: battery. Route: Leaf bank or BT-L alternative. Quantity: 12 for main bank; 3 for BT-L.

### Geometry and provenance

Source module300×222×34; nominal7.4 V60 Ah. Existing model shows shells, mounting bores and three terminal assemblies.

### Units and local datum

Units: mm. Retained model origin: can centre in X/Y on its lower broad face, Z = 0. Local X follows the 300 mm can length toward the terminals, local Y the 222 mm can width, and local Z the 34 mm thickness. Source and reconstruction features use this datum.
Assembly placement uses X forward, Y left, Z up. Preserve this part's local datum and record its placement transform.

### Mating interfaces and hardware

Mates P17R support rail, P17E end restraint, insulation and busbar/sense harness. Preserve original terminal and mounting geometry.

### Space and access

Provide terminal covers, voltage-tap access and source restraint faces.

### Component dimensions and installation interfaces

| Feature | Specification | Datum / installation | Source |
|---|---|---|---|
| Case envelope; mount-hole diameter and centres; terminal pitch/height | 300×222×34 mm; 4×Ø9.1 mm holes at X±138,Y±99 mm; terminal positions Y−38,0,+38 mm at Z17 mm; M6 power terminals and M4 centre tap | Existing model origin at module centre; Z=0 case bottom support plane. Hole coordinates are retained CAD reconstruction; hole diameter and terminal threads are source-record claims. | Retained `engineering/module-development/parts/dimension-evidence/leaf-gen2-geometry.md`, C021 CAD check records and project source list EVShop module listing, VT-Tech module dimensions. The exact per-module dimensions/hole coordinates are not all Nissan OEM drawing callouts; source/provenance distinction retained. |

## Sources — online

1. Leaf module item geometry.
2. VT-Tech module dimensions.
