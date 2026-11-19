THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Motenergy right fixed motor backbone

1. **Library number:** 116.
2. **Type:** part.
3. **CAD file:** [p03jbr-j-right-motor-fixed-backbone.dwg](<p03jbr-j-right-motor-fixed-backbone.dwg>).
4. **DWG SHA-256:** `675373e05f38ce8f8be5975ec8cdb113ad80d19074953c8898453bb3a24b2d52`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Motenergy right fixed motor backbone — P03JBR.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:J3f raised-frame discussion proposal. Quantity: 1 per right J3f motor.

### Geometry, datum and interfaces

Proposed 5 mm steel plate X 55…300,Z 285…565,Y−130…−125. FourØ11 slide-joint axes X 80/280,Z 380/480. Motor centre X 180/Z 430, source pilot/source screw-head swept clearance capsules same as P03JIN left pattern. Right edge 300 gives 5 mm gap to front beam starting 305; slot-hole axis 280 has14.5 mm nominal ligament afterØ11 hole. Outer face Y−130 contacts rail inner face over Z 500…540; moving plate outer face−125 contacts backbone inner face. Welded support connection avoids shifting source motor-hole pattern. Keep proposed clearance cutouts and frame weld contact outside slide-joint washers.

### Source and construction

Parent P03M — ME0907 motor support plate variant; current J3f/J4 arrangement. All custom dimensions here are proposed inputs. Cut/turn/form, deburr and inspect stated contact faces, axes and length before assembly.

### Source-screw adjustment envelope

The source upper mounting screw moves through Z = 489.6…519.6 mm in the J motor pose. Plate outer face and rail inner face are 5 mm apart in Y. The P11 — motor plate head-space calculation gives the source axis, local-to-assembly transform and flush-seat construction proposal. Evaluate the actual screw/washer swept geometry throughout the 30 mm adjustment travel at this rail interface.


### Source-backed flush-head clearance revision

Retain the existing motor, rail and backbone transform. The four source-axis clearance capsules use proposed radius 10.5 mm through the 5 mm backbone over motor travel±15 mm. C161 — ASME B18.3 flat-head 3/8-16×1 in is seated in P11; the ideal theoretical sharp reference radius9.9187 mm is0.5813 mm inside the capsule; actual head/capsule clearance is determined from the supplied profile and seated position. Flush to 1.0 mm inspected recess heads preserve the 5 mm rail gap. Source pilot-clearance capsule andØ11 slide axes are unchanged. Motor-to-plate tightening precedes installation on this backbone; the P11 constructor gives the lower-position tool approach and full plate/seat/thread calculation.


Source correction: ASME Table 8 A maximum is a theoretical sharp 82° flush reference. Radius10.5 mm is the proposed capsule, with actual head/seat receiving condition in P11 — motor plate. The source protrusion inspection uses straight GP bore16.5608…16.5862 mm and head-top height1.2700…2.2352 mm above a flat lapped-sharp-edge gage; its datum is separate from the plate seat.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed motor backbone | PASS | [1, 1, 1, 1] | count |
| Source backbone bounds | PASS | [[55.0, 300.0], [-129.99999999999997, -124.99999999999997], [285.0, 565.0]] | mm |
| Four slide-joint axes | PASS | [[79.9999999999999, 480.0], [80.00000000000023, 380.00000000000006], [280.0, 479.99999999999994], [280.0000000000001, 379.9999999999999]] | mm |
| Visible pilot travel-end arcs | PASS | [[179.99999999999991, 414.99999999999994], [180.00000000000043, 444.99999999999983]] | mm |
| Six exposed screw-head sweep end arcs | PASS | [[105.4, 415.00000000000006], [105.4, 445.00000000000006], [179.9999999999999, 519.6000000000001], [180.00000000000003, 340.40000000000003], [254.60000000000005, 415.0], [254.60000000000008, 445.0]] | mm |

## Sources — online

1. ME0907 outline drawing0JWT.301.073.
2. ME0907 specification and drawing downloads.
3. Kobe EV ME0907 data.
4. Motenergy ME0907 family page.
5. EV Europe ME0907 specification.
6. Kelly ME0907 page.
7. KellyController.eu ME0907 offer.
8. Square steel tube stock family — supplier reference.
9. Weldable steel plate stock family — supplier reference.
