THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Albright SW80 end-pattern carrier

1. **Library number:** 193.
2. **Type:** part.
3. **CAD file:** [p22sw80e-sw80-end-pattern-carrier.dwg](<p22sw80e-sw80-end-pattern-carrier.dwg>).
4. **DWG SHA-256:** `db5e6ed8707474e3585124668b030608dc8c1310b50763c95c6eb48e8a2da581`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Albright SW80 end-pattern carrier — P22SW80E.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity one per end-mounted SW80 installation.

### Source pattern and plate constructor

1. **Source interface:** Albright SW80 family Data Sheet v6-01-20, page 1, end view: two M4 tapped mounting axes at 26.5 mm pitch. Retained source extraction identifies the view and retained original. C033 — SW80B-40 supplies the exact target identity and its separate family/exact-suffix attribution.
2. **Local datum:** origin at the midpoint of the two source end-mount axes. v follows their joining line; u lies in that source mounting face perpendicular to v; n points from the carrier contact face into the contactor. The source mounting axes are(u,v)=(0,−13.25),(0,+13.25), normal n. The half-pitch 13.25 is calculated from 26.5.
3. **Manufactured plate proposal:** steel 100u ×140v ×3n, u−50…50,v−70…70,n−3…0; four outside R3 mm corners. Two proposed Ø4.5 mm clearance holes at the two source axes. Four separate Ø6.5 mm carrier-support holes at(u,v)=(±40,±60). This reuses the existing P22 — removable equipment carrier grid and keeps source equipment mounting and frame support as separate hole groups.
4. **Calculated lands:** M4-hole-to-u-edge ligament is 50−2.25=47.75 mm; nearest v-edge ligament is 70−13.25−2.25=54.5 mm. Minimum straight-edge ligament is47.75 mm. M4 hole-to-hole ligament is 26.5−4.5=22 mm. The support-hole edge ligament is 10−3.25=6.75 mm. The nearest source-hole/support-hole distance is sqrt(40²+(60−13.25)²)=61.526925 mm; subtract radii 2.25+3.25 for 56.026925 mm material between their edges.

### Contact, fastener and service construction

1. **Equipment contact:** finished carrier face n 0 meets the named source end mounting face at the two source M4 holes. Preserve the supplied optional cap, coils, spades, contact housing and exact mounting-face protrusions at their source transform. Apply this local template to the source mounting face before positioning the carrier in the equipment bay.
2. **Source-thread length relationship:** an M4 mounting screw enters from n<−3 through the carrier. With actual washer thickness tW and under-head length L, penetration into the source face is p=L−3−tW. Require p to lie inside the source part's permitted tapped-hole engagement interval; use actual screw first/full-form end distances when computing overlap with the supplied tapped interval. The exact SW80B-40 tapped depth/engagement instruction is the component-specific source input for its screw length. The finite carrier holes above use the known family pattern.
3. **Carrier support:** four local M6 support axes reuse the P22 grid and its P22SH34 — equipment angle-shoe alternative. Preserve the carrier axes and assign the source-to-carrier transform independently from its carrier-to-frame placement. The existing frame-contact-plane comparison applies to those shoes.
4. **Physical sequence proposal:** match the actual source end face and two-hole pattern; attach the source contactor from the carrier rear using the source permitted engagement; fit the carrier supports and terminal harness. For service, isolate/disconnect the actual source terminals, support the contactor/carrier, release its four M6 support joints and withdraw the assembly along local+n before accessing the rear M4 screws on the bench. Required withdrawal distance follows the source component, source lugs and their actual bay pose. Albright permits horizontal mounting, or vertical mounting with its M8 main studs upward.
5. **Terminal interface:** source-family M8 main terminal pitch 29 mm and tightening range 8–9.5 N·m retain the source labels. Source lug/nut stack and exact suffix determine their installed volumes; those source features accompany the contactor rather than altering the two M4 carrier axes.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Albright SW80 end-pattern carrier | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-50.0, 50.0], [-70.0, 70.0], [-3.0, 0.0]] | mm |
| Source-sheet hole group 1 | PASS | [[0.0, -13.25], [0.0, 13.25]] | mm |
| Source-sheet hole group 2 | PASS | [[-40.0, -60.0], [-40.0, 60.0], [40.0, -60.0], [40.0, 60.0]] | mm |
| Outside corner radius | PASS | [3.0] | mm |

## Sources — online

1. albright sw80 family mount interface.
2. Albright SW80 drawing/specifications.
3. OEM Nordic's SW80B-40 listing.
4. Albright glossary.
5. Weldable steel plate stock family — supplier reference.

## References — local

191. [34 mm M6 equipment angle shoe](<../p22sh34-m6-equipment-angle-shoe-34mm/p22sh34-m6-equipment-angle-shoe-34mm.md>) — library entry 191.
