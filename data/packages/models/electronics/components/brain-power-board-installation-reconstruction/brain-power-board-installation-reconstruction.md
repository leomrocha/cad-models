# Sowbot original power regulation board — installation proposal

**Local catalogue ID** `sowbot-brain-power-board-installation-reconstruction` · revision 1

**Native CAD** [DWG 2018](brain-power-board-installation-reconstruction.dwg), 38,892 bytes, SHA-256 `d489e258bf75bef1b2883a3f54a4104ecdf6df5487b9d246c0cd1d78989b7466`.

## Geometry and installation

Millimetres. Origin on PCB lower-left straight-edge datum viewed from above. +X right, +Y up in source image. Z=0 board bottom, +Z toward components.

- The original power-board raster supplies four aperture and connector landmarks. The inferred 5.08 mm screw-terminal pitch gives the proposed 98.49 mm nominal square board with the estimated size range 96.60–98.91 mm. Board thickness is proposed as 1.6 mm with range 1.4–2.0 mm.
- USB-A, 5 V and 3.3 V connections approach from +Y. The 12 V connection approaches from +X. Input screw, XT60-style and barrel connections approach from −X. Terminal tool access is along +Z. Proposed tool space is 15–25 mm.

## CAD verification

OpenCADStudio verified the current geometry at revision 279. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](brain-power-board-installation-reconstruction-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](brain-power-board-installation-reconstruction-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](brain-power-board-installation-reconstruction-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](brain-power-board-installation-reconstruction-isometric.png), plot generated from CAD boundary geometry.
- [Upper isometric](brain-power-board-installation-reconstruction-top-isometric.png), plot generated from CAD boundary geometry.

## Technical sources

- [Source reference](https://oshwlab.com/rosmo/pcb12v-reroute)
