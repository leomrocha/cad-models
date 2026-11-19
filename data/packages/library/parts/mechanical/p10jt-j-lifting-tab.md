THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# J lifting tab

1. **Library number:** 161.
2. **Type:** part.
3. **CAD file:** [p10jt-j-lifting-tab.dwg](<p10jt-j-lifting-tab.dwg>).
4. **DWG SHA-256:** `32707443c7df3a1b1dcd3bb520e5fadd9ad2e9e5ec814509f9d8718f1fde4fe0`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** J lifting tab — P10JT.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity: four per J lifting-support arrangement.

### Shape and source dimensions

1. **Blank:** proposed steel plate, 60 mm along local X, 120 mm along local Z and 8 mm thickness along local Y. The 120 mm blank and separate root connection follow P10ROOT — lifting-tab root doubler.
2. **Eye and corners:** proposed diameter 20 mm eye, centred on local X = 0 mm, Z = 100 mm. Two upper outside corner radii are 15 mm. These features follow P10 — side lifting tab.
3. **Local datum:** origin at the centre of the lower edge on the inner mounting face. Bounds X = −30…30 mm, Y = 0…8 mm, Z = 0…120 mm. Eye axis is normal to Y.

### J arrangement and contact

1. **Left placement:** add X = −180 mm or +180 mm, Y = 218 mm, Z = 707 mm to the local coordinates. The plate spans Y = 218…226 mm, Z = 707…827 mm; the eye centre is Z = 807 mm. Mirror Y for the right-hand instances.
2. **Root contact:** the raised root doubler spans Z = 697…757 mm and Y = 210…218 mm on the left. The tab inner face contacts its outer face over Z = 707…757 mm, a 50 mm vertical contact interval. These placements follow P10JST — J lifting stanchion and the explicit J transform in the side-lifting-tab sheet.
3. **Support chain:** the tab connects through the root doubler, P10JAR — J lifting short arm, J lifting stanchion and its frame feet.

### CAD checks

1. Check the closed solid, 60 × 120 × 8 mm overall bounds, 20 mm eye diameter and eye axis, two 15 mm corner radii, source labels and saved/reopened geometry.
2. In the group, check the four placements, root contact interval and side location relative to the usable deck.

Geometry dependencies: P10ROOT, P10JAR, P10JST. All dimensions above retain discussion-proposal status.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed J lifting tab | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-30.0, 30.0], [0.0, 8.000000000000007], [0.0, 120.0]] | mm |
| Source-sheet hole group 1 | PASS | [[0.0, 100.0]] | mm |
| Native outside corner radius 15 mm | PASS | [[-15.0, 105.0], [15.0, 105.0]] | mm |

## Sources — online

1. Weldable steel plate stock family — supplier reference.

## References — local

159. [J lifting short arm nominal section](<p10jar-j-lifting-tab-short-arm.md>) — library entry 159.
160. [J lifting stanchion nominal section](<p10jst-j-outboard-lifting-stanchion.md>) — library entry 160.
162. [Side lifting-tab root doubler](<p10root-lift-tab-root-doubler.md>) — library entry 162.
