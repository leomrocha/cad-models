# Victron service hatch with fitted rails and twelve removable fasteners

**Catalogue draft ID** `victron-service-hatch-installed`. Revision 1.

**Design status** Discussion construction proposal.

[Native DWG 2018](victron-service-hatch-installed.dwg), SHA-256 `8fdb629ea8edc647155d51ff185a1d17d55096b2135dd0815189f741c6c4cfff`.

## Geometry

Fixed deck, removable cover and two removable rails with twelve M6 × 16 screws and twelve washers.

Shelf-local millimetres. X joins the two battery terminals, Y opposes the terminal normal, and Z points up from the shelf top.

The cover has 0.5 mm nominal gap at every opening edge. Each screw extends 5.4 mm below the rail. The nominal hex-head and washer stack projects 5.6 mm above the deck.

## Embedded model revisions

- [Victron service hatch drilled fixed deck](../../../../../mechanical/chassis/deck/victron-service-hatch-fixed-deck/victron-service-hatch-fixed-deck.md), 1 instances, SHA-256 `83743f7f66604800257e5e5d11cbf2c3ee21e6386da75076e2f852c63d40aff3`.
- [Victron service hatch drilled removable cover](../../../../../mechanical/chassis/deck/victron-service-hatch-removable-cover/victron-service-hatch-removable-cover.md), 1 instances, SHA-256 `67e718174880d267b60a7c1bc06b02c41623349b60b79c309e14d3677856799b`.
- [Victron service hatch removable support rail](../../../../../mechanical/chassis/deck/victron-service-hatch-support-rail/victron-service-hatch-support-rail.md), 2 instances, SHA-256 `859c8f94df7fb7d3a59508bc78b1dbde1d33f634923e22b01565e6985ef8d983`.
- [ISO4017 M6x16 screw nominal reference](../../../../../mechanical-parts/fasteners/screws/c130-iso-4017-m6x16-screw-proposed-class-8-8/c130-iso-4017-m6x16-screw-proposed-class-8-8.md), 12 instances, SHA-256 `0c8ca6b61cd26be2cc79642bab28684f302d798740ce33cab4da2479defd7a13`.
- [ISO 7089 M6 plain washer, proposed 200 HV](../../../../../mechanical-parts/fasteners/washers/iso7089-m6-washer-6p4x12x1p6-reference/iso7089-m6-washer-6p4x12x1p6-reference.md), 12 instances, SHA-256 `624e3bb3c0818f68d4cf020851b26e077ee0f073e70d0bde81014ee8dd199943`.

## Checks

OpenCADStudio verified the reference geometry at revision 10623. The final DWG save verified its hash and recorded zero dropped objects.

## Views

- [Plan](victron-service-hatch-installed-XY.png)
- [Elevation](victron-service-hatch-installed-XZ.png)
- [End](victron-service-hatch-installed-YZ.png)
- [Isometric](victron-service-hatch-installed-top-isometric.png)
