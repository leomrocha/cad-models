# Main Sowbot reconstructed hardware installation — assembly proposal

**Local catalogue ID** `assembly-main-sowbot-reconstructed-hardware-layout-proposal` · revision 1

**Native CAD** [DWG 2018](main-sowbot-reconstructed-hardware-layout-proposal.dwg), 2,314,988 bytes, SHA-256 `6067d0b66076e430868a87c2f60aa8086954518fae710b5f8fab26355375808a`.

## Geometry and installation

Millimetres. Main tracked chassis X fore-aft, Y left, Z up, in millimetres.

- The model contains the verified Main chassis subassembly and counts its two ODrive D6374 motors there. Six VariCore cases retain the saved XY arrangement and sit at Z = 7 mm on the nominal deck.
- The removable front Brain mounting proposal rotates the housing +90° about Z and places its origin at (38, 133, 24) mm. A 7 mm conservative X gap separates the case from the first battery lift projection.
- The two ODrive v3.6 controller board bases are (175, 40, 13) and (450, 40, 13) mm. Their +Y service plugs and +Z tools approach on the external sides. Deck ears carry the near-side supports. The first controller moved 25 mm to clear the middle crossmember end flange.
- Two Kee Lite fittings use the proposed Front Brain support tube pairs. Ø33.7 mm nominal tubes pass through proposal Ø34.4 mm bores. Their two axes and other placed parts are dimensioned in the parent occurrence evidence.
- Independent exact envelope comparisons found zero positive interference across 48 tested cross-group pairs. The 24 seating-distance checks, six continuous 250 mm upward battery lifts, twelve terminal tool approaches, two USB approaches and two controller cooling reserves passed.

## CAD verification

OpenCADStudio verified the current geometry at revision 1591. The final save verified the DWG hash and recorded zero dropped entities. The saved document was closed.

## Views

- [XY plan](main-sowbot-reconstructed-hardware-layout-proposal-XY.png), plot generated from CAD boundary geometry.
- [XZ elevation](main-sowbot-reconstructed-hardware-layout-proposal-XZ.png), plot generated from CAD boundary geometry.
- [YZ end](main-sowbot-reconstructed-hardware-layout-proposal-YZ.png), plot generated from CAD boundary geometry.
- [Isometric](main-sowbot-reconstructed-hardware-layout-proposal-top-isometric.png), plot generated from CAD boundary geometry.

## CAD references

- [Main Sowbot reconstructed tracked chassis — assembly proposal](../main-chassis-reconstructed-assembly-proposal/main-chassis-reconstructed-assembly-proposal.md), embedded, CAD SHA-256 `4b691a1df2a334c57b268c7506ddbe2af287e8f77ae7ecd51e68455a32710c5c`. Occurrences MAIN-CHASSIS.
- [Main deck with front extension and controller ears — installation proposal](../../parts/main-joined-deck-and-controller-ears-r2/main-joined-deck-and-controller-ears-r2.md), embedded, CAD SHA-256 `0a4b9848f5708a57ab405913ebd2c95614d400a8114ed2ba397dd9107b76467c`. Occurrences MAIN-DECK.
- [Main deck tube and controller supports — installation proposal](../../subassemblies/main-deck-tube-and-controller-supports-r2/main-deck-tube-and-controller-supports-r2.md), embedded, CAD SHA-256 `5c73959c413097abcd56557c631edf55d203ab98516ff64426d2ce768392f1af`. Occurrences MAIN-DECK-SUPPORTS.
- [VariCore VC1280NA battery exterior — installation proposal](../../../../../electronics/batteries/varicore-vc1280na-exterior-reconstruction/varicore-vc1280na-exterior-reconstruction.md), embedded, CAD SHA-256 `412c23bc45061d98866ad877e0f1c6efa025111466be1bc56bf737151d0ae06a`. Occurrences BATTERY-1, BATTERY-2, BATTERY-3, BATTERY-4, BATTERY-5, BATTERY-6.
- [ODrive v3.6 controller — installation proposal](../../../../../electronics/components/odrive-v36-installation-reconstruction/odrive-v36-installation-reconstruction.md), embedded, CAD SHA-256 `87fbf335f1211c0378ed7d50155de053ff2ab19f4d737df99b7db14688c862ec`. Occurrences ODRIVE-1, ODRIVE-2.
- [Open Core Brain populated split-tier assembly — assembly proposal](../../../brain/layouts/brain-populated-split-tier-installation-proposal/brain-populated-split-tier-installation-proposal.md), embedded, CAD SHA-256 `f70c7bca8714163edd93bc0e84b332d4fb01d0ca89cbaa6631eba633da4ac36c`. Occurrences BRAIN.
- [Kee Lite L45-6 crossover fitting — installation proposal](../../../../../mechanical-parts/components/kee-lite-l45-6-exterior-reconstruction/kee-lite-l45-6-exterior-reconstruction.md), embedded, CAD SHA-256 `f30c52fc567fe9951c08df183c8a1f8c75125c159f846c009354cd6154d3ac58`. Occurrences KEE-LITE-1, KEE-LITE-2.

## Technical sources

- [Sowbot hardware](https://sowbot.co.uk/hardware/)
