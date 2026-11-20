# Open BTS7960 Mini motor driver — installation proposal

**Local catalogue ID** `sowbot-open-bts7960-mini-installation-reconstruction` · revision 1

**Native CAD** [DWG 2018](open-bts7960-mini-installation-reconstruction.dwg), 41,836 bytes, SHA-256 `2e20ff5ebecb3ad75689da7fd14a3f7aa9c77bc4688da26ec6497c4b06c8fcb2`.

## Geometry and installation

Millimetres. Catalogue model-312 frame. PCB original face Z=0. X right and Y up from mapped EasyEDA layout.

- The exact EasyEDA outline and four 2.1999956 mm mounting diameters are retained at the source centres. The occupied board uses a proposed 1.6 mm thickness with 1.2–2.54 mm range, below the PCB top datum.
- Five exterior connector envelopes follow the source placement and approximate wire approach. Six source-registered screwdriver mouths are modelled with proposed axial entry depth. Upper heatsink and underside Mini360 envelopes support clearance checks.

## CAD verification

OpenCADStudio verified the current geometry at revision 362. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](open-bts7960-mini-installation-reconstruction-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](open-bts7960-mini-installation-reconstruction-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](open-bts7960-mini-installation-reconstruction-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](open-bts7960-mini-installation-reconstruction-isometric.png), plot generated from CAD boundary geometry.
- [Upper isometric](open-bts7960-mini-installation-reconstruction-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [Open BTS7960 Mini driver with Mini360 mounting slots](../../../assemblies/reusable/subassemblies/open-bts7960-mini-driver-21-opening-source-face/open-bts7960-mini-driver-21-opening-source-face.md), derived geometry, CAD SHA-256 `88cbee0a4a3df39fc11ff2cb7d22cd0e01e367c356c29db145b028f9801fd808`. The source 21-opening board and its connector geometry supply the PCB outline, four bore centres and five connector placements.
- [Open BTS7960 Mini driver screw-tool entries](../../../interface-references/mechanical/open-bts7960-terminal-tool-entry-reference/open-bts7960-terminal-tool-entry-reference.md), derived geometry, CAD SHA-256 `e089830b6136b8c31b5c8d4cf564762df64adfcdf5835b413ec6a3cdbe4a95be`. The six source screw-tool opening axes locate the proposed terminal tool access.

## Technical sources

- [Source reference](https://sowbot.co.uk/hardware/)
