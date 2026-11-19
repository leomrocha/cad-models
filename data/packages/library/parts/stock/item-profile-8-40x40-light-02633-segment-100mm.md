THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# ITEM Profile 8 40×40 light 0.0.026.33

1. **Library number:** 93.
2. **Type:** part.
3. **CAD file:** [item-profile-8-40x40-light-02633-segment-100mm.dwg](<item-profile-8-40x40-light-02633-segment-100mm.dwg>).
4. **DWG SHA-256:** `eeebae1dcff61a08c94a157c1dbc01d4f81cf4c7c6b5a9be80fd3b4222d725b8`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** ITEM Profile 8 40×40 light 0.0.026.33 — C084.

## Technical specification

Date: 13 November 2026. Inventory input; discussion proposal. Route: Bolted-frame alternative M01. Quantity: Derived cut lengths by rail/crossmember instance; repeated stock shape.

### Geometry and provenance

Copy section geometry from retained manufacturer PDF and linked CAD reference. Profile is an extrusion; assign cut length as instance parameter sourced from frame layout drawing.

### Units and local datum

Units: mm unless the source designation states inch. Model the source component geometry from the cited standard, drawing or product record. For custom features, use the mating component datums and label dimensions as proposal values. Origin and axes: establish from the mating face or source component axis; assembly placement uses X forward, Y left, Z up.

### Mating interfaces and hardware

Mates Angle Bracket Set 8 40×40 and T-slot Nut 8 St M8.

### Installation and access

Use source bracket kit with profile grooves; cut, deburr and protect open ends according to frame assembly drawing.

### CAD measurements

Measure source-critical mating features, fastener access, installation envelope and removal direction. Record measurement values, source revision, datum, units and CAD file revision.

### Remaining construction alternatives — 13 November 2026

**Cut-instance proposal:** reuse P01 rail and P02 crossmember IDs as the two derived stock roles for the existing600×340 frame layout, with source40×40 ITEM section. Two rails600 mm and three crossmembers260 mm give total nominal cut length2×600+3×260=1980 mm, excluding kerf, end cleanup and rejects. Across-width relation40+260+40=340 mm follows the existing between-rails arrangement. Keep steel-tube and ITEM-profile routes as alternatives; bracket thickness and actual joint orientation determine whether the same nominal cuts remain valid in the bolted arrangement. Record route-specific finished cut length, end datum, cut ID/instance and source profile0.0.026.33 before cutting.

## Sources — online

1. c084 item profile 8 40x40 light.

## References — local

111. [Main frame longitudinal rail](<../mechanical/p01-main-frame-longitudinal-rail-reference.md>) — library entry 111.
114. [Main frame crossmember](<../mechanical/p02-main-frame-crossmember-reference.md>) — library entry 114.
