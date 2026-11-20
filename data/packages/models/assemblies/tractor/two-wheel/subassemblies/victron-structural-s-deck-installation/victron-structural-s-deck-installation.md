# Victron service deck mounted on the Structural S lower chassis

**Catalogue draft ID** `victron-structural-s-deck-installation`. Revision 1.

**Design status** Discussion construction proposal.

[Native DWG 2018](victron-structural-s-deck-installation.dwg), SHA-256 `ecf26c342f354c4db61176746bbc89add8641a63644411473d3a5f927439fd43`.

## Geometry

Structural S lower frame, Victron battery support and removable service hatch on four uprights and two flat ledges, with six deck-to-ledge M6 joints.

Shelf-local millimetres. X joins the two battery terminals, Y opposes the terminal normal, and Z points up from the shelf top.

The deck seats at Z = 537 mm, with 16.784 mm of nominal headroom above the upper battery restraint. Six M6 × 20 ledge screws have a 6 mm solid grip and project 4.8 mm beyond their locknuts.

## Embedded model revisions

- [Victron single supported shelf fastened to the Structural S chassis](../victron-single-shelf-frame-installation/victron-single-shelf-frame-installation.md), 1 instances, SHA-256 `c90ca6520efdcf0ca715dcfa10f9f612eeb00a11271995371fdabe83b238e39b`.
- [Structural S side lifting supports](../structural-s-side-lifting-supports/structural-s-side-lifting-supports.md), 1 instances, SHA-256 `223b3fa21cc8d58ed24102fbe736d22926f9c04d4178cdb501305067354c2d91`.
- [Victron service hatch with fitted rails and twelve removable fasteners](../victron-service-hatch-installed/victron-service-hatch-installed.md), 1 instances, SHA-256 `8fdb629ea8edc647155d51ff185a1d17d55096b2135dd0815189f741c6c4cfff`.
- [Structural S deck upright](../../../../../mechanical/chassis/deck/p04up-deck-upright-s/p04up-deck-upright-s.md), 4 instances, SHA-256 `668824b23041ae1e4a5295468a8bdc9588420d49a7f5733dcd36ce4b5bee04cf`.
- [Deck upright ledge bridge cap](../../../../../mechanical/chassis/deck/p04cap-deck-upright-ledge-bridge-cap/p04cap-deck-upright-ledge-bridge-cap.md), 4 instances, SHA-256 `df1730869618767e1657cecd19b729f7b3458c26edf7a986b0cd5f48641154eb`.
- [Structural S Victron service deck flat ledge](../../../../../mechanical/chassis/deck/victron-structural-s-service-deck-flat-ledge/victron-structural-s-service-deck-flat-ledge.md), 2 instances, SHA-256 `48fa07be2e478c417266e1dd374fb56853dfd836005498bef91f7a36cd848520`.
- [ISO4017 M6x20 screw nominal reference](../../../../../mechanical-parts/fasteners/screws/c128-iso-4017-m6x20-screw-proposed-class-8-8/c128-iso-4017-m6x20-screw-proposed-class-8-8.md), 6 instances, SHA-256 `32dcc1ddeecddfa8687901a913f6a6aa1e6cb574c311daa8cc1f59ebc896eb4d`.
- [ISO 7089 M6 plain washer, proposed 200 HV](../../../../../mechanical-parts/fasteners/washers/iso7089-m6-washer-6p4x12x1p6-reference/iso7089-m6-washer-6p4x12x1p6-reference.md), 12 instances, SHA-256 `624e3bb3c0818f68d4cf020851b26e077ee0f073e70d0bde81014ee8dd199943`.
- [DIN985 M6 nominal nut reference](../../../../../mechanical-parts/fasteners/nuts/c152-din-985-m6-nylon-insert-nut-proposed-class-8/c152-din-985-m6-nylon-insert-nut-proposed-class-8.md), 6 instances, SHA-256 `b005197d6d63b19d28d1785191f25a1a7a8a07068289550796644a12ed197e08`.

## Checks

OpenCADStudio verified the reference geometry at revision 10843. The final DWG save verified its hash and recorded zero dropped objects.

## Views

- [Plan](victron-structural-s-deck-installation-XY.png)
- [Elevation](victron-structural-s-deck-installation-XZ.png)
- [End](victron-structural-s-deck-installation-YZ.png)
- [Isometric](victron-structural-s-deck-installation-top-isometric.png)
