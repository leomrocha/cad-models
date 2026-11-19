THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Splash stair panel-support plate

1. **Library number:** 203.
2. **Type:** part.
3. **CAD file:** [p24jsv-j-splash-stair-panel-plate.dwg](<p24jsv-j-splash-stair-panel-plate.dwg>).
4. **DWG SHA-256:** `c977433cd3504f91aa0abbf3e8cb0ab5f4f2b02a9af2b73e1a0b88c5035c0b07`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Splash stair panel-support plate — P24JSV.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm.
1. **Manufactured plate proposal:** steel, bounds local X −15…15, Y 175…178, Z 555…583. Quantity six per panel pair. Translate X by Xc−220/0/+220 per side and mirror Y for the right side. All dimensions are custom construction proposals derived from the retained support contacts.
2. **Holes and lands:** One Ø6.5 through hole normal Y at local X 0,Z 570. Source Ø12 washer spans Z 564…576; nominal end gaps are 9 mm below and 7 mm above.
3. **Contact:** Lower end 555 contacts bridge top 555; inner face Y 175 contacts panel outer face 175, with that contact face finished flush after welding.
4. **Parent:** P24JSHS — four-piece stair support gives weld positions, source hardware, exact guard-foot intersections, sleeve condition and named load inputs. Preserve those joint conditions when using this child shape.

1. **Manufactured plate proposal:** steel, bounds local X −15…15, Y 175…178, Z 555…583. Quantity six per panel pair. Translate X by Xc−220/0/+220 per side and mirror Y for the right side. All dimensions are custom construction proposals derived from the retained support contacts.
2. **Holes and lands:** One Ø6.5 through hole normal Y at local X 0,Z 570. Source Ø12 washer spans Z 564…576; nominal end gaps are 9 mm below and 7 mm above.
3. **Contact:** Lower end 555 contacts bridge top 555; inner face Y 175 contacts panel outer face 175, with that contact face finished flush after welding.
4. **Parent:** P24JSHS — four-piece stair support gives weld positions, source hardware, exact guard-foot intersections, sleeve condition and named load inputs. Preserve those joint conditions when using this child shape.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Splash stair panel-support plate | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-15.0, 15.0], [175.0, 178.0], [555.0, 583.0]] | mm |
| Source-sheet hole group 1 | PASS | [[0.0, 570.0]] | mm |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
