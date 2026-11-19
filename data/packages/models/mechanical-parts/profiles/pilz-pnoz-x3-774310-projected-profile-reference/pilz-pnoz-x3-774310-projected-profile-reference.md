THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Pilz PNOZX3 774310 relay

1. **Library number:** 204.
2. **Type:** part.
3. **CAD file:** [pilz-pnoz-x3-774310-projected-profile-reference.dwg](<pilz-pnoz-x3-774310-projected-profile-reference.dwg>).
4. **DWG SHA-256:** `05ee9fcc76284d4c22e0672880647f73706d252a275c2e1d54d50c63ec32a268`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Pilz PNOZX3 774310 relay — C048.

## Technical specification

CAD input sheet; manufacturer component reference. Group: electrical. Route: Stop equipment. Quantity: 1.

### Geometry and provenance

Source PNOZ X3 774310: width 45 mm, height 87 mm and drawing depth 120.6 mm; product-page rounded depth 121 mm; mass 375 g; DIN-rail mount.

### Units and local datum

Units: mm. Origin: rail engagement face; mark terminal rows.
Assembly placement uses X forward, Y left, Z up. Record the local-to-assembly transform.

### Mating interfaces and hardware

Mates DIN rail, source terminals and correctly terminated wires.

### Space and access

Reserve terminal tools, withdrawal and adjacent spacing.

### Component dimensions and installation interfaces

| Feature | Specification | Datum / installation | Source |
|---|---|---|---|
| Relay housing and rail fit | Front width 45 mm, height 87 mm, outermost drawing depth 120.6 mm; product-page rounded depth 121 mm. 35 mm DIN-rail mounting. | Source front/side drawing views; installation orientation is a separate placement transform | Retained manufacturer drawing P97/45, drawing 2009094, 30 June 2011; exact-product acquisition and dimension associations. |

### Retained drawing-view correction

1. **Inspected original:** Pilz P97/45 drawing2009094/model2006038, dated30 June2011, one page, all dimensions in millimetres. The retained source preview was visually inspected. Front-view dimension leaders give45 mm width and87 mm height; side-view outermost dimension gives120.6 mm depth. The side view's separate115.4 mm span connects the inner front reference extension to the rear extreme as drawn. Preserve those witness-line associations.
2. **Earlier input error:** the earlier table called121 mm the height and87 mm the depth. Correct associations are width45 mm, height87 mm and depth120.6 mm in the drawing. Product-page depth121 mm is its rounded value, as recorded by the exact-product source acquisition.
3. **Placement:** retained acquisition metadata records the manufacturer field “mounting position any”. A horizontal or vertical rail layout is a project placement proposal; source rail-engagement and catch geometry define the relay's actual rail-to-body transform. Use the front view's45×87 mm body projection for the horizontal-rail proposal in P22Relay.

Original source URL:  SHA-256: `0c9ba5e48ab95734026c94cc883a524ef993027f1a0fd375ef688700940b4b83`. Retained acquisition record maps this drawing to exact product774310. Drawing depth is the complete outermost component span; rail plane offset is its own mating feature.


### Direct-on-included-plate relay construction alternative

C166 —100 mm rail cut and F10R1 —two M5×12 rail joints define the finite direct-on-MPS3020 route. C163 —75 mm cut/P22Relay independent plate is retained as its separate alternative. rail/end-stop topology extraction gives source-native rail/end-stop frames, candidate mating faces, the 0.8 mm installed-depth discrepancy and source source-based body-envelope bound 128.1 mm. Pilz clip/release geometry remains the exact source dependency after HTTP403; actual receiving checks preserve the rear wall, door/wiring and contact geometry.

## Sources — online

1. Pilz774310 component documentation.
2. c048 pilz pnozx3 774310 relay.
3. relay rail interface.
4. relay rail interface.
5. relay rail interface.
