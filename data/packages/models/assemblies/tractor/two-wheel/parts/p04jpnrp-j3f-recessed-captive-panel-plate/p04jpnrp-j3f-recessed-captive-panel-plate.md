THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Recessed-captive deck panel plate

1. **Library number:** 125.
2. **Type:** part.
3. **CAD file:** [p04jpnrp-j3f-recessed-captive-panel-plate.dwg](<p04jpnrp-j3f-recessed-captive-panel-plate.dwg>).
4. **DWG SHA-256:** `d67e2500b095729c0bab237127a3ce09c8a24f6f4e6f23ef6e269eba966611e1`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Recessed-captive deck panel plate — P04JPNRP.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: one per P04JPNR assembly, two per deck.
1. **Cut blank:** steel 299×400×3 mm, localu 0…299,v±200,n 0…3; corner radius 3 mm. Rear transform(X,Y,Z)=(−300+u,v,770+n); front(X,Y,Z)=(300−u,−v,770+n). The two identical blanks span the original 600×400 mm footprint with 2 mm centre gap.
2. **Cup apertures:** fourØ22 mm through holes normaln at(u,v)=(85,±187.5),(175,±187.5). Weld the matching turned cup flanges into those apertures, with flange bottomZ770/top 773 flush to the parent plate. The matchingØ22 aperture andØ22 flange share a vertical cylindrical contact surface throughZ770…773; their solids have zero volume overlap. Use a full-depth circumferential butt-weld preparation, then finish both panel faces withinZ770…773 and keep the side edgeY±200 intact. Aperture-to-side-edge ligament is 200−187.5−11=1.5 mm. Finished weld material remains within that plate/cup union and the 1.5 mm outer edge land; source closed heads sit within the recessed cup bore. Hole-to-hole axes alongu are 90 mm apart. Each cup flange underside seats on the matching fixed ledge.
3. **Support and sources:** P04JPNR — assembly gives source fastener positions, actual engagement criteria, fixed-body clearances and the manual removal sequence. P04JRC — cup carries the source mounting template.

1. **Cut blank:** steel 299×400×3 mm, localu 0…299,v±200,n 0…3; corner radius 3 mm. Rear transform(X,Y,Z)=(−300+u,v,770+n); front(X,Y,Z)=(300−u,−v,770+n). The two identical blanks span the original 600×400 mm footprint with 2 mm centre gap.
2. **Cup apertures:** fourØ22 mm through holes normaln at(u,v)=(85,±187.5),(175,±187.5). Weld the matching turned cup flanges into those apertures, with flange bottomZ770/top 773 flush to the parent plate. The matchingØ22 aperture andØ22 flange share a vertical cylindrical contact surface throughZ770…773; their solids have zero volume overlap. Use a full-depth circumferential butt-weld preparation, then finish both panel faces withinZ770…773 and keep the side edgeY±200 intact. Aperture-to-side-edge ligament is 200−187.5−11=1.5 mm. Finished weld material remains within that plate/cup union and the 1.5 mm outer edge land; source closed heads sit within the recessed cup bore. Hole-to-hole axes alongu are 90 mm apart. Each cup flange underside seats on the matching fixed ledge.
3. **Support and sources:** P04JPNR — assembly gives source fastener positions, actual engagement criteria, fixed-body clearances and the manual removal sequence. P04JRC — cup carries the source mounting template.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Recessed-captive deck panel plate | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[0.0, 299.0], [-200.0, 200.0], [0.0, 3.0]] | mm |
| Source-sheet hole group 1 | PASS | [[85.0, -187.5], [85.0, 187.5], [175.0, -187.5], [175.0, 187.5]] | mm |
| Outside corner radius | PASS | [3.0] | mm |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
