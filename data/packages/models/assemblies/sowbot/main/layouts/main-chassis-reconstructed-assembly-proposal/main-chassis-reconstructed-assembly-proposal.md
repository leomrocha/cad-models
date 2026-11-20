# Main Sowbot reconstructed tracked chassis — assembly proposal

**Local catalogue ID** `assembly-main-chassis-reconstructed-assembly-proposal` · revision 1

**Native CAD** [DWG 2018](main-chassis-reconstructed-assembly-proposal.dwg), 179,149 bytes, SHA-256 `4b691a1df2a334c57b268c7506ddbe2af287e8f77ae7ecd51e68455a32710c5c`.

## Geometry and installation

Millimetres. X travels towards distant end, Y left, Z up. Existing top-tread reference Z=0; proposed ground Z=-227 mm and highest cleat Z=3 mm.

- Eleven physical occurrences. Two carriers, two track loops, three removable crossmembers, two reducers and two manufacturer-source D6374 motors.
- Nominal axle fore-aft centres X = −20 and 850 mm, common Z = −112 mm. Track lateral centre planes Y = −80 and 855 mm. Nominal carrier-to-belt axial clearance is 10 mm.
- Source-bound analytic OCC evaluation reported zero overlaps above 0.01 mm³ across all 55 installed occurrence pairs. Native readback verified the corresponding eleven placements and body face counts.

## CAD verification

OpenCADStudio verified the current geometry at revision 226. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](main-chassis-reconstructed-assembly-proposal-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](main-chassis-reconstructed-assembly-proposal-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](main-chassis-reconstructed-assembly-proposal-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](main-chassis-reconstructed-assembly-proposal-isometric.png), plot generated from CAD boundary geometry.
- [Upper isometric](main-chassis-reconstructed-assembly-proposal-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [Main Sowbot left side carrier — installation proposal](../../parts/main-left-carrier-reconstruction/main-left-carrier-reconstruction.md), embedded, CAD SHA-256 `1c7daf9cb6d36ef6d2096bf8b08b165e0f7f89c1948d1e502f08f8625ab006e4`. Occurrences frame-left.
- [Main Sowbot right side carrier — installation proposal](../../parts/main-right-carrier-reconstruction/main-right-carrier-reconstruction.md), embedded, CAD SHA-256 `1f7c200df7f0fd71e4d7286e83b7292b40b6474f9147973f8d873339fe8fa881`. Occurrences frame-right.
- [Main Sowbot reconstructed track loop — installation proposal](../../parts/main-track-loop-reconstruction/main-track-loop-reconstruction.md), embedded, CAD SHA-256 `025fdb9065ad07f7e47bf509b7d7a370ba4288cc81b7f804b246894525a5220a`. Occurrences track-left, track-right.
- [Main Sowbot crossmember — installation proposal](../../parts/main-crossmember-reconstruction/main-crossmember-reconstruction.md), embedded, CAD SHA-256 `291f49f3d946ff6a5a2bb2eee01699879005f86a28b1305fbc7c244540da3ad9`. Occurrences crossmember-front, crossmember-removable-middle, crossmember-rear.
- [Main Sowbot reducer exterior — installation proposal](../../parts/main-reducer-reconstruction-r2/main-reducer-reconstruction-r2.md), embedded, CAD SHA-256 `988a33d062110b5bc31b9695879d16f06e60cd01f967a1710081ede2d45dfae2`. Occurrences reducer-left, reducer-right.
- [ODrive D6374 manufacturer motor](../../../../../electronics/motors/odrive-d6374-manufacturer-motor/odrive-d6374-manufacturer-motor.md), embedded, CAD SHA-256 `4e1d5d250367d32e1ec3c890f83bb885b950b12c868a25c09b2a1c329c6714e7`. Occurrences motor-left, motor-right.

## Technical sources

- [Sowbot hardware](https://sowbot.co.uk/hardware/)
