# Main Sowbot reducer exterior — installation proposal

**Local catalogue ID** `sowbot-main-reducer-reconstruction` · revision 2

**Native CAD** [DWG 2018](main-reducer-reconstruction-r2.dwg), 34,694 bytes, SHA-256 `988a33d062110b5bc31b9695879d16f06e60cd01f967a1710081ede2d45dfae2`.

## Geometry and installation

Millimetres. X forward, Y inward from the motor mating plane, Z upward. Motor axis passes through the flange origin.

- Housing, motor mating face and separate Ø32 mm output shaft. Ø10.7 mm input relief and eight Ø4.5 mm mounting passages.
- The millimetre definitions use retained source images and mating dimensions for installation and clearance work.
- This drawing represents nominal reconstructed geometry. The mating and manufacturing dimensions need physical measurement.

## CAD verification

OpenCADStudio verified the current geometry at revision 118. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](main-reducer-reconstruction-r2-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](main-reducer-reconstruction-r2-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](main-reducer-reconstruction-r2-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](main-reducer-reconstruction-r2-isometric.png), plot generated from CAD boundary geometry.
- [Upper isometric](main-reducer-reconstruction-r2-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [ODrive D6374 manufacturer motor](../../../../../electronics/motors/odrive-d6374-manufacturer-motor/odrive-d6374-manufacturer-motor.md), derived geometry, CAD SHA-256 `4e1d5d250367d32e1ec3c890f83bb885b950b12c868a25c09b2a1c329c6714e7`. The D6374 motor provides the motor mating plane, shaft and eight mounting axes used for the proposed reducer interface.

## Technical sources

- [Sowbot hardware](https://sowbot.co.uk/hardware/)
