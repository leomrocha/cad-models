# ODrive v3.6 controller — installation proposal

**Local catalogue ID** `sowbot-odrive-v36-installation-reconstruction` · revision 1

**Native CAD** [DWG 2018](odrive-v36-installation-reconstruction.dwg), 40,979 bytes, SHA-256 `87fbf335f1211c0378ed7d50155de053ff2ab19f4d737df99b7db14688c862ec`.

## Geometry and installation

Millimetres. Catalogue model-283 PCB rectangle, origin at PCB bottom and XY footprint centre. +X along 135 mm dimension. +Z toward terminals.

- ODrive specifies a 135 × 50 mm footprint for v3.6. The purchased reference is ODv36-56V with connectors. Mounting, connector, thermal zone and 1.6 mm board thickness are proposals registered to the retained older artwork.
- The proposed mounting aperture diameter is 3.2 mm with range 2.8–3.6 mm and transferred location allowance ±1.5 mm. USB service approaches from +Y. Terminal and cooling space is above the board along +Z.

## CAD verification

OpenCADStudio verified the current geometry at revision 331. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](odrive-v36-installation-reconstruction-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](odrive-v36-installation-reconstruction-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](odrive-v36-installation-reconstruction-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](odrive-v36-installation-reconstruction-isometric.png), plot generated from CAD boundary geometry.
- [Upper isometric](odrive-v36-installation-reconstruction-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [ODrive v3.6 manufacturer size reference](../odrive-v36-135x50-source-dimension-reference/odrive-v36-135x50-source-dimension-reference.md), derived geometry, CAD SHA-256 `ea06fee77de0dc0e196a6521bb397a76531db4418699aafdcf6cc8eeac35547a`. The exact manufacturer footprint reference supplies the 135 × 50 mm substrate outline.

## Technical sources

- [Source reference](https://docs.odriverobotics.com/v/latest/hardware/odrive-comparison.html)
