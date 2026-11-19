THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Splash stair bridge

1. **Library number:** 198.
2. **Type:** part.
3. **CAD file:** [p24jsb-j-splash-stair-bridge.dwg](<p24jsb-j-splash-stair-bridge.dwg>).
4. **DWG SHA-256:** `99d5225918028de447645c9a403bdd849aab8b649da4601a63c75d7559900f77`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Splash stair bridge — P24JSB.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm.
1. **Manufactured plate proposal:** steel, bounds local X −15…15, Y 166…178, Z 552…555. Quantity six per panel pair. Translate X by Xc−220/0/+220 per side and mirror Y for the right side. All dimensions are custom construction proposals derived from the retained support contacts.
2. **Holes and lands:** Solid rectangular plate; cut size 30 × 12 × 3.
3. **Contact:** Bottom over Y 166…169 contacts upstand top 552. Upper face over Y 175…178 contacts panel plate end 555. Underside 552 leaves 4 mm to deck-foot top 548.
4. **Parent:** P24JSHS — four-piece stair support gives weld positions, source hardware, exact guard-foot intersections, sleeve condition and named load inputs. Preserve those joint conditions when using this child shape.
5. **Sheet-plane crossing:** bridge material passes through Y 173.5…175,Z 552…555. Pair this part with P24JPT — notched trimmed panel, whose full-thickness central cut X ±16 and outer corner-open cuts X −237.1…−204 /204…237.1, all Z 550…555.5, clear the proposed bridge/end-weld bounds by 0.5 mm.

1. **Manufactured plate proposal:** steel, bounds local X −15…15, Y 166…178, Z 552…555. Quantity six per panel pair. Translate X by Xc−220/0/+220 per side and mirror Y for the right side. All dimensions are custom construction proposals derived from the retained support contacts.
2. **Holes and lands:** Solid rectangular plate; cut size 30 × 12 × 3.
3. **Contact:** Bottom over Y 166…169 contacts upstand top 552. Upper face over Y 175…178 contacts panel plate end 555. Underside 552 leaves 4 mm to deck-foot top 548.
4. **Parent:** P24JSHS — four-piece stair support gives weld positions, source hardware, exact guard-foot intersections, sleeve condition and named load inputs. Preserve those joint conditions when using this child shape.
5. **Sheet-plane crossing:** bridge material passes through Y 173.5…175,Z 552…555. Pair this part with P24JPT — notched trimmed panel, whose full-thickness central cut X ±16 and outer corner-open cuts X −237.1…−204 /204…237.1, all Z 550…555.5, clear the proposed bridge/end-weld bounds by 0.5 mm.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Splash stair bridge | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-15.0, 15.0], [166.0, 178.0], [552.0, 555.0]] | mm |

## Sources — online

1. Weldable steel plate stock family — supplier reference.
