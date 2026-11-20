# Yuzuki Avaota-A1 v1.7 computer — installation proposal

**Local catalogue ID** `sowbot-avaota-a1-v17-installation-envelope-proposal` · revision 2

**Native CAD** [DWG 2018](avaota-a1-v17-installation-envelope-proposal-r2.dwg), 46,737 bytes, SHA-256 `83728dbaef0b1ce0aa0e3b2c567b41722aa3b1c83ba84765a90292742e24b7ac`.

## Geometry and installation

Millimetres. Manufacturer STEP right-handed XYZ in mm, with substrate bottom Z = 0.

- The substrate reuses the v1.7 outline, 1.183202438 mm thickness and five perimeter apertures.
- Exterior connector bodies represent occupied axis-aligned envelopes derived from placed v1.7 component geometry. Plug directions refer to the component frame.
- The TFT1 screen is a separate installed accessory. U15 is the board-mounted display connector.
- Revision 2 adds the two source-matched 2-pin connector envelopes used in the populated-enclosure fit screen.

## CAD verification

OpenCADStudio verified the current geometry at revision 496. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](avaota-a1-v17-installation-envelope-proposal-r2-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](avaota-a1-v17-installation-envelope-proposal-r2-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](avaota-a1-v17-installation-envelope-proposal-r2-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](avaota-a1-v17-installation-envelope-proposal-r2-isometric.png), plot generated from CAD boundary geometry.
- [Upper isometric](avaota-a1-v17-installation-envelope-proposal-r2-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [Avaota-A1 v1.7 installation substrate](../avaota-a1-installation-substrate-stage/avaota-a1-installation-substrate-stage.md), derived geometry, CAD SHA-256 `63673fe6db5a19989ca45015be168578d733db7fddccaef1bb9dfc6305eef28e`. The checked v1.7 substrate supplies the retained outline, thickness and five apertures.
- [Yuzuki Avaota-A1 v1.7 board with source connectors](../../../assemblies/reusable/subassemblies/avaota-a1-v17-board-source-connectors/avaota-a1-v17-board-source-connectors.md), derived geometry, CAD SHA-256 `99627762af6f0a796268cf33389a5ffd8ce8f6dfbcd0a1c155ae735ff3f28911`. The detailed v1.7 source placements supply the occupied exterior connector envelopes.

## Technical sources

- [Avaota-A1 hardware v1.7 manufacturer STEP](https://raw.githubusercontent.com/AvaotaSBC/Avaota-A1/master/hardware/v1.7/06_3D/3D_PCB1_2024-08-17.zip)
