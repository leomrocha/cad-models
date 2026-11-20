# Propow CPN24050 24 V 50 Ah battery — installation proposal

**Local catalogue ID** `sowbot-propow-cpn24050-installation-reconstruction` · revision 1

**Native CAD** [DWG 2018](propow-cpn24050-installation-reconstruction.dwg), 33,466 bytes, SHA-256 `6439d57a890aa8778a8bd8a3284992f91a075928c81ce9972693c2f022de8ad9`.

## Geometry and installation

Millimetres. Reuse catalogue model-318 frame. X along 306 mm from 350 to 656. +Y from printed label edge toward case rear. Z up from base.

- Propow CPN24050 listing, CPS24050 gallery marking and 306 × 174 mm footprint identify the 24 V 50 Ah candidate. The reconstructed main case height is 200 mm and proposed post top is 220 mm. The case includes the recessed handle and pictorial hold-down ledge.
- The post X positions are image-based estimates with ±8 mm allowance. The suggested Y range is 22–56 mm and post base diameter range is 17–24 mm. Clamps and case removal are accessed from +Z.
- Sowbot separately describes a 24 V 30 Ah sodium-ion pack. The 50 Ah and 30 Ah identities have separate evidence.

## CAD verification

OpenCADStudio verified the current geometry at revision 415. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](propow-cpn24050-installation-reconstruction-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](propow-cpn24050-installation-reconstruction-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](propow-cpn24050-installation-reconstruction-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](propow-cpn24050-installation-reconstruction-isometric.png), plot generated from CAD boundary geometry.
- [Upper isometric](propow-cpn24050-installation-reconstruction-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [Propow CPN24050 three-dimensional clearance references](../../../interface-references/mechanical/propow-cpn24050-size-field-envelopes/propow-cpn24050-size-field-envelopes.md), derived geometry, CAD SHA-256 `03b2af173b90db3fb42654a53c4fab8388457a0028008c38e61837f1886f2768`. The source size-field envelopes supply the separate 200 mm case and 220 mm overall height fields.
- [Propow CPN24050 220 mm Mini placement envelope](../../../interface-references/mechanical/propow-cpn24050-220mm-source-selection/propow-cpn24050-220mm-source-selection.md), derived geometry, CAD SHA-256 `7cf2bb95e21603bfcfa77e786d0604c7721d9f7527203ab0811c17583674197c`. The selected 220 mm placement envelope supplies the installed coordinate frame and footprint.

## Technical sources

- [Source reference](https://sowbot.co.uk/hardware/)
