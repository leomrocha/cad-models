# Structural S chassis with T539 tyre clearance envelopes

**Catalogue draft ID** `structural-s-t539-wheel-clearance`. Revision 1.

**Design status** Discussion construction proposal.

[Native DWG 2018](structural-s-t539-wheel-clearance.dwg), SHA-256 `cf2514c857286fb17189814184d761a503fa4161a38758bef6d4fdc457b25243`.

## Geometry

Structural S chassis and two upper-tolerance T539 6PR tyre clearance cylinders. The axle centres are 578 mm apart.

Millimetres. X forward, Y left and Z up. Lower chassis and tyre clearance solids in the Structural S datum.

At the 578 mm nominal track the maximum width is 804.44 mm. There is 5.78 mm lateral clearance from each cylinder to the outside of the lower frame rail. The model holds the axle at Z = 233 mm. Actual loaded ride height and wheel hardware use separate geometry.

## Embedded model revisions

- [Structural S lower chassis frame](../structural-s-lower-chassis-frame/structural-s-lower-chassis-frame.md), 1 instances, SHA-256 `4f455311da878278610730e443f084df6fa012204faf7f1152405d66104b94bc`.
- [Trelleborg T539 18×8.50-8 6PR tyre clearance envelope](../../../../../interface-references/wheels-and-tyres/c001-t539-6pr-tyre-clearance-envelope/c001-t539-6pr-tyre-clearance-envelope.md), 2 instances, SHA-256 `6ddeca5c03dc429168df06e06314dd72428f7770c18232cce5d8c10c756b4af9`.

## Checks

OpenCADStudio verified the reference geometry at revision 7863. The final DWG save verified its hash and recorded zero dropped objects.

## Views

- [Plan](structural-s-t539-wheel-clearance-XY.png)
- [Elevation](structural-s-t539-wheel-clearance-XZ.png)
- [End](structural-s-t539-wheel-clearance-YZ.png)
- [Isometric](structural-s-t539-wheel-clearance-top-isometric.png)
