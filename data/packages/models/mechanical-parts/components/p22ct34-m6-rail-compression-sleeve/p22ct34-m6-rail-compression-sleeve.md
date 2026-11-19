THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# M6 rail compression sleeve

1. **Library number:** 187.
2. **Type:** part.
3. **CAD file:** [p22ct34-m6-rail-compression-sleeve.dwg](<p22ct34-m6-rail-compression-sleeve.dwg>).
4. **DWG SHA-256:** `5cdb33e56fea83e7adf5df809bb23ebb7ded8032b0692beb564e2c670025161f`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** M6 rail compression sleeve — P22CT34.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion proposal. Units: mm. Route:J3f raised-frame discussion proposal. Quantity: 4 per J controller pair plus 2 per J receiver bridge pair.

### Geometry, datum and interfaces

Turned steel OD 12,bore 6.6,length 34 through 40×40×3 raised rail. Sleeve ends meet internal walls; source tube seam/corner profile is checked at mounting location. At X−137/77,Z 520, joint axis Y passes rail 40 +gap 7+post 20 plus washers/nut. Insert sleeve before frame end closure or through explicitly detailed service access.

### Source and construction

Parent P22Kelly — Kelly KLS 7240 N support bracket; current J3f/J4 arrangement. All custom dimensions here are proposed inputs. Cut/turn/form, deburr and inspect stated contact faces, axes and length before assembly.

### Carrier-inclusive rail-joint proposal

The rail sleeve retains its 34 mm cut length and Y = 133…167 mm inside-wall contact. The proposed carrier exit holes extend the external clamp path through the 3 mm carrier: rail 40 + gap spacer 7 + post 20 + carrier 3 = 70 mm. This stack uses one rail sleeve and one separate 16 mm post sleeve per axis; both lie inside their hollow sections. Four rail sleeves serve the paired controllers.

### Receiver bridge instances — E04 proposal

Two additional identical sleeves occupy Y =133…167 mm at (X,Z) = (−315,520) and (−175,520) mm inside the left rail. Each sleeve has the same Ø12 mm outside, Ø6.6 mm bore and 34 mm length as the controller instances. Install these sleeves before rail end closure. The combined controller-pair and receiver-bridge proposal uses 4 +2 =6 sleeves. P22RXB — receiver bridge input defines its two-joint clamp stack and length criterion.


### Vertical guard-support instances — A07J4 proposal

Eight additional identical Ø12 mm / Ø6.6 mm / 34 mm sleeves serve the guard-support construction alternative. Their axes are vertical Z, between rail inner faces Z503 and Z537 mm. Left positions are (X,Y) = (−110,150), (−40,150), (40,150), (110,150) mm; right positions are (−110,−150), (0,−150), (110,−150), (210,−150) mm. Install before rail-end closure. These proposed tube dimensions are reused with a different rigid transform. P16MTJ4 — guard flange input defines the actual grip and service sequence for these eight instances.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed sleeve | PASS | [1, 1, 1, 1] | count |
| Nominal outside diameter | PASS | [[0.0, 0.0]] | mm |
| Nominal bore diameter | PASS | [[0.0, 2.0818995585505003e-15]] | mm |
| Square cut end planes and cut length | PASS | [0.0, 34.0] | mm |

## Sources — online

1. Kelly KLS-N wiring diagram, §3.2.2, p.14.
2. source review r02.
3. source review r02.
4. Square steel tube stock family — supplier reference.
5. Weldable steel plate stock family — supplier reference.
