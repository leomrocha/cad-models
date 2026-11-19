THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# M10 deck/lift foot compression sleeve

1. **Library number:** 121.
2. **Type:** part.
3. **CAD file:** [p04jct34-j-foot-m10-rail-compression-sleeve.dwg](<p04jct34-j-foot-m10-rail-compression-sleeve.dwg>).
4. **DWG SHA-256:** `a9a23cb627b4148f5ff608207e074aa65e90652ab83aebb00de0115f93643ede`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** M10 deck/lift foot compression sleeve — P04JCT34.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Quantity: 2 per foot in the two-hole proposal; 4 per foot in the recorded four-hole error.

### Earlier four-hole geometry — error record

Proposed turned steelOD14,bore11,length34. Sleeve axes normalY atfootlocalX±15,Z513/527. Outer circles occupyZ506…520 and520…534, tangent atmidplane520. Nominal40×40×3 rail has internalZ503…537; with3 mm innercorner radius, straight side-wall contact spansZ506…534, matching these end circles. This uses the nominal stock corner geometry; inspect actual radius/seam before making the block/rail joint. Full annular end contact area isπ(14²−11²)/4=58.905 mm², before any deburr edge; retain that contact area when setting clamp preload/material. This replaces the earlierOD16 sleeves/510,530 rows that crossed the inner wall.

### Construction

Parent P04L — Deck support ledge; combined installation. Cut/form the proposed geometry, inspect joint contact and hole axes, then check the stated load path.

### Two-hole foot alternative — sleeve instances

1. **Proposed sleeve geometry:** retain steel outside diameter 14 mm, bore 11 mm and cut length 34 mm. Use two instances per foot with axes along Y at local X = −15/+15 mm and global Z = 520 mm. Nominal left rail interior is Y = 133…167 mm; the right installation mirrors Y.
2. **Calculated wall contact:** each sleeve end spans Z = 513…527 mm. The assumed R3 internal rail corners leave the straight wall interval Z = 506…534 mm, giving 7 mm from each circular end extremity to the corresponding straight-wall end. Axial contact uses the 34 mm inner-wall separation. The nominal annular end area is π(14²−11²)/4 = 58.905 mm² before edge deburring; actual rail radius, seam and wall separation control fitted contact.
3. **Proposed quantity:** 2 sleeves per foot, 8 per four-foot deck and 8 per four-foot lifting set; 16 for both sets. The foot vertical-leg correction gives the external hardware stack and joint evaluation.


### Current two-hole source-limit connection

Two sleeves per foot lie at Xc±15,Z520, axes Y. OD14 mm end circles occupy Z513…527, 7 mm inside the nominal straight-wall limits506…534. Eight feet use16 sleeves in the two-hole proposal. The original four-per-foot arrangement remains the recorded alternative; external hardware clearance is defined by the current P04JFTV source-limit proposal.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed sleeve | PASS | [1, 1, 1, 1] | count |
| Nominal outside diameter | PASS | [[0.0, 0.0]] | mm |
| Nominal bore diameter | PASS | [[0.0, 2.0818995585505003e-15]] | mm |
| Square cut end planes and cut length | PASS | [0.0, 34.0] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
