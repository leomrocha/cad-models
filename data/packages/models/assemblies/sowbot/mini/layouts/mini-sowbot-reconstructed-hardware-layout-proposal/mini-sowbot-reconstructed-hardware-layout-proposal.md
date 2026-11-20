# Mini Sowbot reconstructed hardware installation — assembly proposal

**Local catalogue ID** `assembly-mini-sowbot-reconstructed-hardware-layout-proposal` · revision 1

**Native CAD** [DWG 2018](mini-sowbot-reconstructed-hardware-layout-proposal.dwg), 2,117,184 bytes, SHA-256 `248175429448c8d571f4b3e528912c0b86e967e2b3e3b1192235c017fb40aaf0`.

## Geometry and installation

Millimetres. Current Mini layout XYZ, XY platform, +Z upward.

- Brain body enclosure footprint X−53…207, Y−15…152, so Mini 450×490 footprint X−225…225, Y−245…245 leaves 18 mm at the governing right edge. Brain case floor sits at Z0. Battery holds parent position X−153…153, Y−210…−36, with 21 mm gap from enclosure minimum Y. Driver global Z12 top leaves ≥2 mm over nominal platform even at 10 mm underside extent. Check Brain hinge and antenna pads as separate geometry, battery lift and terminal tools, and platform stiffness and attachment geometry.
- The Propow 50 Ah battery is the linked candidate and keeps its previously saved XY location. The described 30 Ah source identity remains a separate alternative.
- Four 10.4 mm driver support sockets seat its 1.6 mm nominal board with board top Z = 12 mm. The 450 × 490 mm source base footprint retains its native position and definition.
- Independent exterior comparison found 21 mm battery-to-Brain and 136 mm battery-to-driver XY gaps for continuous +Z lift. The Brain-to-driver projection gap is 62.896 mm. The proposed Ø45 mm E-stop actuation reserve leaves 0.6 mm above the platform datum.

## CAD verification

OpenCADStudio verified the current geometry at revision 1171. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](mini-sowbot-reconstructed-hardware-layout-proposal-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](mini-sowbot-reconstructed-hardware-layout-proposal-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](mini-sowbot-reconstructed-hardware-layout-proposal-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](mini-sowbot-reconstructed-hardware-layout-proposal-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [Mini Sowbot layout with opposed GNSS connectors](../mini-opposed-sma-layout-proposal/mini-opposed-sma-layout-proposal.md), derived, CAD SHA-256 `91bc9166ab7d0253521e020f7d6d0db50a593cc0dd595999b7bfdfb3007cee9c`.
- [Sowbot Mini chassis footprint reference](../../interface-references/sowbot-mini-chassis-footprint-reference/sowbot-mini-chassis-footprint-reference.md), embedded, CAD SHA-256 `d890c11303d90da0a029a2d23cf11c64a82e084c68e4411910c0921f7ff66b3d`. Occurrences SOW-MINI-C03-OPT1.
- [Propow CPN24050 24 V 50 Ah battery — installation proposal](../../../../../electronics/batteries/propow-cpn24050-installation-reconstruction/propow-cpn24050-installation-reconstruction.md), embedded, CAD SHA-256 `6439d57a890aa8778a8bd8a3284992f91a075928c81ce9972693c2f022de8ad9`. Occurrences SOW-MINI-C04.
- [Open BTS7960 Mini motor driver — installation proposal](../../../../../electronics/components/open-bts7960-mini-installation-reconstruction/open-bts7960-mini-installation-reconstruction.md), embedded, CAD SHA-256 `2e20ff5ebecb3ad75689da7fd14a3f7aa9c77bc4688da26ec6497c4b06c8fcb2`. Occurrences SOW-MINI-C02-OPT1.
- [Open Core Brain populated split-tier assembly — assembly proposal](../../../brain/layouts/brain-populated-split-tier-installation-proposal/brain-populated-split-tier-installation-proposal.md), embedded, CAD SHA-256 `f70c7bca8714163edd93bc0e84b332d4fb01d0ca89cbaa6631eba633da4ac36c`. Occurrences SOW-MINI-C01.
- [Mini Open BTS7960 driver supports — installation proposal](../../subassemblies/mini-driver-supports-proposal/mini-driver-supports-proposal.md), embedded, CAD SHA-256 `7789c3f43130881efe1db36a38bba1103f0b243b9e516c842a6e4ab724d068c5`. Occurrences MINI-DRIVER-STANDOFFS.

## Technical sources

- [Sowbot hardware](https://sowbot.co.uk/hardware/)
