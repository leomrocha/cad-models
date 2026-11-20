# Victron frame seat carrier on the Structural S lower chassis

**Catalogue draft ID** `victron-frame-seat-carrier`. Revision 1.

**Design status** Discussion construction proposal.

[Native DWG 2018](victron-frame-seat-carrier.dwg), SHA-256 `12f7ceb44b3e71df4c067de3e82c632abfc4f1da91efa498c62e08f2f1a286d9`.

## Geometry

Two seat crossbars, four risers and four drilled flange seat tabs on the lower tractor frame.

Shelf-local millimetres. X joins the two battery terminals, Y opposes the terminal normal, and Z points up from the shelf top.

Each crossbar has two planar seats on the longitudinal frame rails. The four tabs have Ø8.5 mm open bores and 288 mm² of nominal footprint on each riser.

## Embedded model revisions

- [Structural S lower chassis frame](../structural-s-lower-chassis-frame/structural-s-lower-chassis-frame.md), 1 instances, SHA-256 `4f455311da878278610730e443f084df6fa012204faf7f1152405d66104b94bc`.
- [Victron frame seat transverse crossbar](../../../../../mechanical/chassis/battery-supports/victron-frame-seat-crossbar/victron-frame-seat-crossbar.md), 2 instances, SHA-256 `9a22d710398bd6647447b9d50080aa0d1db2ca8275ece1822f1c24f5deedaaa6`.
- [Victron frame flange seat riser](../../../../../mechanical/chassis/battery-supports/victron-frame-flange-seat-riser/victron-frame-flange-seat-riser.md), 4 instances, SHA-256 `91d43254c6a4dc21bde61a1148e858c1f82777b842b9822791ddb34bb38e3343`.
- [Victron frame flange seat tab](../../../../../mechanical/chassis/battery-supports/victron-frame-flange-seat-tab/victron-frame-flange-seat-tab.md), 4 instances, SHA-256 `0f5c7c7e8af40151ec31977425cc674a9b80f161785870ff51ef6ef61e265619`.

## Checks

OpenCADStudio verified the reference geometry at revision 10059. The final DWG save verified its hash and recorded zero dropped objects.

## Views

- [Plan](victron-frame-seat-carrier-XY.png)
- [Elevation](victron-frame-seat-carrier-XZ.png)
- [End](victron-frame-seat-carrier-YZ.png)
- [Isometric](victron-frame-seat-carrier-top-isometric.png)
