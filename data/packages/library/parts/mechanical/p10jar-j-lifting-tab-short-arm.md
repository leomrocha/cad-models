THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# J lifting short arm nominal section

1. **Library number:** 159.
2. **Type:** part.
3. **CAD file:** [p10jar-j-lifting-tab-short-arm.dwg](<p10jar-j-lifting-tab-short-arm.dwg>).
4. **DWG SHA-256:** `eff79ccdee729311f7e011e6909594575ec648f981493be22a14c0d728d44f6f`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** J lifting short arm nominal section — P10JAR.

**Design status:** Discussion nominal hollow-section reference.

## Technical specification

Status: Discussion proposal. Units: mm. Quantity: 4 per J lifting support.

### Geometry and contacts

Proposed40X×40Z×3 steel tube15 long alongY, leftY195…210/rightmirror,Z707…747; centresX±180. Inner faceY195 contacts20 mm-wide stanchion face over20×40 central area. OuterfaceY210 contacts P10ROOT innerface over40×40. RootY210…218 and tabY218…226 remain source-S geometry in this J transform. Arm width40 overhangs20 mm post face by10 each side; full40×40 weld contact is not claimed. Reuse foot/template atX±180 so the foot60 mm width avoids the deck foot centred±250 by10 mm.

### Construction

Parent P10 — Side lifting tab; combined installation. Cut/form the proposed geometry, inspect joint contact and hole axes, then check the stated load path.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed hollow tube body | PASS | [1, 1, 1, 1] | count |
| Section and cut-length vertex bounds | PASS | [[-20.0, 20.0], [-20.0, 20.0], [0.0, 15.0]] | mm |
| Nominal inner and outer corner radii | PASS | [3.0, 6.0] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
