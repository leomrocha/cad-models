# Brain mounting plate source openings

The current [28-opening face, library 314](<../../../../../mechanical-parts/components/brain-orp-mounting-plate-28-opening-source-face/brain-orp-mounting-plate-28-opening-source-face.md>) incorporates the 39 holes nested in the original ORP footprint. The source map below records the earlier ten-opening libraries. Complete source map.

Model 32, SOW-BRAIN-C06. This register locates the ten openings in the ORP mounting plate source pattern for interface IF-003. The saved analytic pattern is library 254. The faceted source face is library 285. [Analytic pattern](<../../interface-references/brain-mounting-plate-source-pattern-reference/brain-mounting-plate-source-pattern-reference.md>) [Open source face](<../../parts/brain-mounting-plate-source-open-face/brain-mounting-plate-source-open-face.md>)

All coordinates and dimensions below are in millimetres, in the library XY frame at Z = 0. The origin is the plate centre. From EasyEDA coordinates, X = 0.254 × (source X − 4216.85) and Y = 0.254 × (3177.15 − source Y). The outline is 99.9998 × 99.9998 mm with a 3.499993 mm corner radius. The source-derived circle grid pitch is 19.99996 mm. EasyEDA ORP source, revision `1ff7250ebd4c4571b7af0292bb667b55`

## Connected openings

Bounds are the minimum and maximum X and Y of the sampled union. The union uses 1,024 segments per source circle and the exact vertices of the two non-plated cutout contours. Opening identifiers follow the order in the checked union receipt. The mapped records are the five board-level HOLE primitives, 24 layer-10 circle records and two non-plated cutout contours used by libraries 254 and 285.

| Opening | Geometry | Minimum (X, Y) | Maximum (X, Y) | Source record IDs |
| --- | --- | --- | --- | --- |
| ORP-01 | Single circle | (-48.955909, 44.516091) | (-45.455891, 48.016109) | `gge15338` |
| ORP-02 | Compound cutout | (-42.251884, 30.646116) | (-17.817135, 46.646084) | `gge332080`, `gge332101`, `gge39871`, `gge39898`, `gge39913`, `gge39931`, `gge23944` |
| ORP-03 | Two overlapping circles | (-1.495806, 38.551104) | (1.765046, 41.792906) | `gge39865`, `gge39895`, `gge39910`, `gge39934` |
| ORP-04 | Two overlapping circles | (-21.495766, 18.551144) | (-18.234914, 21.792946) | `gge39877`, `gge39889`, `gge39907`, `gge39922` |
| ORP-05 | Two overlapping circles | (-1.495806, 18.551144) | (1.765046, 21.792946) | `gge39874`, `gge39886`, `gge39904`, `gge39925` |
| ORP-06 | Single circle | (-48.574909, -48.320909) | (-45.074891, -44.820891) | `gge5767` |
| ORP-07 | Single circle | (45.151091, 44.897091) | (48.651109, 48.397109) | `gge15353` |
| ORP-08 | Two overlapping circles | (18.504154, 38.551104) | (21.765006, 41.792906) | `gge39868`, `gge39892`, `gge39916`, `gge39928` |
| ORP-09 | Two overlapping circles | (18.504154, 18.551144) | (21.765006, 21.792946) | `gge39880`, `gge39883`, `gge39901`, `gge39919` |
| ORP-10 | Single circle | (45.405091, -48.447909) | (48.905109, -44.947891) | `gge5782` |

## Analytic circle primitives

Each row describes one exact-distinct source circle. Multiple IDs in a row share the same centre and diameter. The large circle in ORP-02 is one primitive of the compound cutout.

| Opening | Centre (X, Y) | Diameter | Source record IDs |
| --- | --- | ---: | --- |
| ORP-01 | (-47.205900, 46.266100) | 3.5000184 | `gge15338` |
| ORP-02 | (-34.251900, 38.646100) | 15.9999680 | `gge23944` |
| ORP-02 | (-19.895820, 40.192960) | 3.1998920 | `gge39871`, `gge39898`, `gge39913` |
| ORP-02 | (-19.834860, 40.151050) | 3.1998920 | `gge39931` |
| ORP-03 | (0.104140, 40.192960) | 3.1998920 | `gge39865`, `gge39895`, `gge39910` |
| ORP-03 | (0.165100, 40.151050) | 3.1998920 | `gge39934` |
| ORP-04 | (-19.895820, 20.193000) | 3.1998920 | `gge39877`, `gge39889`, `gge39907` |
| ORP-04 | (-19.834860, 20.151090) | 3.1998920 | `gge39922` |
| ORP-05 | (0.104140, 20.193000) | 3.1998920 | `gge39874`, `gge39886`, `gge39904` |
| ORP-05 | (0.165100, 20.151090) | 3.1998920 | `gge39925` |
| ORP-06 | (-46.824900, -46.570900) | 3.5000184 | `gge5767` |
| ORP-07 | (46.901100, 46.647100) | 3.5000184 | `gge15353` |
| ORP-08 | (20.104100, 40.192960) | 3.1998920 | `gge39868`, `gge39892`, `gge39916` |
| ORP-08 | (20.165060, 40.151050) | 3.1998920 | `gge39928` |
| ORP-09 | (20.104100, 20.193000) | 3.1998920 | `gge39880`, `gge39883`, `gge39901` |
| ORP-09 | (20.165060, 20.151090) | 3.1998920 | `gge39919` |
| ORP-10 | (47.155100, -46.697900) | 3.5000184 | `gge5782` |

## Compound opening contours

ORP-02 includes the two overlapping non-plated cutout contours below, two distinct layer-10 circles represented by four source records and the Ø15.999968 mm HOLE primitive. Vertices follow the source traversal order and each contour closes to its first vertex.

- `gge332080` — (-30.2667670, 37.9045470), (-30.2667670, 43.2385470), (-17.9223670, 43.2639470), (-17.8715670, 37.9299470).

- `gge332101` — (-30.2123348, 33.2648052), (-30.2123348, 38.5988052), (-17.8679348, 38.6242052), (-17.8171348, 33.2902052).

Three nonjoining source outline tracks are retained in library 254 as separate curves. The register is a planar source interface for the existing plate geometry.

The ten sampled union bounds were matched one-to-one to the ten inner loops independently derived from the recorded native Mesh triangles. The maximum absolute difference across X and Y extrema was 0.001989 mm. Library 285’s source faceting chord error bound was 0.002 mm. [Open-face source and checks](<../../parts/brain-mounting-plate-source-open-face/brain-mounting-plate-source-open-face.md>)
