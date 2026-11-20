# Open Core Brain populated split-tier assembly — assembly proposal

**Local catalogue ID** `assembly-brain-populated-split-tier-installation-proposal` · revision 1

**Native CAD** [DWG 2018](brain-populated-split-tier-installation-proposal.dwg), 2,084,712 bytes, SHA-256 `f70c7bca8714163edd93bc0e84b332d4fb01d0ca89cbaa6631eba633da4ac36c`.

## Geometry and installation

Millimetres. Brain enclosure body enclosure XYZ millimetres.

- The body carries the exact-profile 28-opening ORP plate, two Avaota computers, two source SparkFun receivers with opposed SMA openings, one source LEVIA control board, the estimated original power board and separate attachment supports.
- The two antenna seals seat at Z = 51 mm. Their antenna origins are Z = 51.4 mm. The Ø7.583 mm shaft allowance clears the Ø8 mm passages. Access separates the 8 mm feed-through bore from the larger plug body.
- The 22 mm E-stop barrel is coaxial with the fourth front bore, a 22.4 mm assembled receiving-hole proposal. Independent exact native-bound geometry comparison gives zero common volume for the switch and receiving body.
- Board envelopes retain a conservative minimum interboard distance of 3.920 mm. With the trial Ø12 by 16 mm SMA plug reserves, minimum board gaps are 1.344 mm and 25.664 mm. Nominal wall gaps are 7.730 mm and 1.542 mm. These checks cover the stated AABB board and compact-plug reserves.
- The service view releases the removable lid, hinge pins, fixings and antenna leads before board access. The right shelf leaves 23.5 mm above the upper C25 screw-block mouths. Remove the shelf before using the 25 mm tool variant. The LEVIA rests and Avaota offset rails are proposed mechanical support geometry.

## CAD verification

OpenCADStudio verified the current geometry at revision 907. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](brain-populated-split-tier-installation-proposal-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](brain-populated-split-tier-installation-proposal-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](brain-populated-split-tier-installation-proposal-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](brain-populated-split-tier-installation-proposal-top-isometric.png), plot generated from CAD boundary geometry.
- [Service lift +115 mm · XY](brain-populated-split-tier-installation-proposal-lid-lift-115mm-XY.png), plot generated from CAD boundary geometry.
- [Service lift +115 mm · XZ](brain-populated-split-tier-installation-proposal-lid-lift-115mm-XZ.png), plot generated from CAD boundary geometry.
- [Service lift +115 mm · YZ](brain-populated-split-tier-installation-proposal-lid-lift-115mm-YZ.png), plot generated from CAD boundary geometry.
- [Service lift +115 mm · top-isometric](brain-populated-split-tier-installation-proposal-lid-lift-115mm-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [Brain GNSS receivers with opposed SMA access](../brain-opposed-sma-layout-proposal/brain-opposed-sma-layout-proposal.md), derived, CAD SHA-256 `d26c6f86f5a3e8d6431ec9681ce22ca3733803f1597c7282d13154a3d1910198`.
- [Open Core Brain removable enclosure — assembly proposal](../../subassemblies/brain-enclosure-seated-lid-assembly-proposal/brain-enclosure-seated-lid-assembly-proposal.md), embedded, CAD SHA-256 `9e0d7442e4a6dcdb874a591d962fac7f1c5900bb9194ba90d2fac8baf3d5e7c8`. Occurrences ENCLOSURE-CLOSED.
- [Open Core Brain electronics installation supports — installation proposal](../../subassemblies/brain-installation-supports-proposal/brain-installation-supports-proposal.md), embedded, CAD SHA-256 `d28965310481459906f800c6754c789b7210931cfea0dba1bf4102f265d791ab`. Occurrences MOUNTING-SUPPORTS.
- [Rosmo ORP Brain mounting plate — installation proposal](../../../../../mechanical-parts/components/brain-orp-mounting-plate-source-profile-proposal/brain-orp-mounting-plate-source-profile-proposal.md), embedded, CAD SHA-256 `13552d7ce70edab40c2ad9f0502bdcb4dbe01f05161a4b42fcafb85e9456ecca`. Occurrences SOW-BRAIN-C06-1.
- [Yuzuki Avaota-A1 v1.7 computer — installation proposal](../../../../../electronics/components/avaota-a1-v17-installation-envelope-proposal-r2/avaota-a1-v17-installation-envelope-proposal-r2.md), embedded, CAD SHA-256 `83728dbaef0b1ce0aa0e3b2c567b41722aa3b1c83ba84765a90292742e24b7ac`. Occurrences SOW-BRAIN-C01-1, SOW-BRAIN-C01-2.
- [SparkFun NEO-F9P receiver with connector exteriors](../../../../reusable/subassemblies/sparkfun-neo-f9p-source-connector-exterior-stage/sparkfun-neo-f9p-source-connector-exterior-stage.md), embedded, CAD SHA-256 `f76f6d8de63f91dc101b36226b1d3973e737cd48b7669bfe2037b8d162c7747e`. Occurrences SOW-BRAIN-C03-F9P-1, SOW-BRAIN-C03-F9P-2.
- [LEVIA-H7 board exterior stage](../../../../../electronics/components/levia-h7-board-exterior-stage/levia-h7-board-exterior-stage.md), embedded, CAD SHA-256 `fa1cc46d5326ef9edf11cdc8d5b4454032bc9b467fc6bd8b1c5537bb983aa8c7`. Occurrences SOW-BRAIN-C02-1.
- [Sowbot original power regulation board — installation proposal](../../../../../electronics/components/brain-power-board-installation-reconstruction/brain-power-board-installation-reconstruction.md), embedded, CAD SHA-256 `d489e258bf75bef1b2883a3f54a4104ecdf6df5487b9d246c0cd1d78989b7466`. Occurrences SOW-BRAIN-C05-1.
- [Sowbot source-linked 22 mm emergency-stop switch — installation proposal](../../../../../electronics/components/physical-estop-22mm-installation-reconstruction/physical-estop-22mm-installation-reconstruction.md), embedded, CAD SHA-256 `101c0635453048e0fc8a9f0ac2f7864cccb7d283855d01d91a1d978233209023`. Occurrences SOW-BRAIN-C08-1.
- [Beitian BT-560 GNSS antenna — installation proposal](../../../../../electronics/components/beitian-bt560-installation-reconstruction/beitian-bt560-installation-reconstruction.md), embedded, CAD SHA-256 `10cbaf920743217c1c398a62118b4babdeea3a885f72b1529089be02c0941454`. Occurrences SOW-BRAIN-C04-1, SOW-BRAIN-C04-2.

## Technical sources

- [Sowbot hardware](https://sowbot.co.uk/hardware/)
