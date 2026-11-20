# Structural S side lifting supports

**Catalogue draft ID** `structural-s-side-lifting-supports`. Revision 1.

**Design status** Discussion construction proposal.

[Native DWG 2018](structural-s-side-lifting-supports.dwg), SHA-256 `223b3fa21cc8d58ed24102fbe736d22926f9c04d4178cdb501305067354c2d91`.

## Geometry

Four Structural S side lifting supports. Each uses one stanchion, one horizontal arm, one root doubler and one lifting tab.

Millimetres. X forward, Y left and Z up. Four lifting supports in the Structural S chassis frame.

The four Ø20 mm eye centres are at Z = 540 mm. The arm, root doubler and tab contact planes are at 170, 210 and 218 mm outboard on each side. The nominal arm end contacts the stanchion flat over 168 mm² and the root doubler over the rounded tube wall footprint. The doubler and tab overlap over 3,000 mm². Weld sizing and lifting capacity are separate engineering checks.

## Embedded model revisions

- [Structural S lifting tab stanchion](../../../../../mechanical/chassis/lifting-supports/p10st-lift-tab-stanchion/p10st-lift-tab-stanchion.md), 4 instances, SHA-256 `05452f8be8e5cd31b3ebf1d6a52c8ffd0f94d0d0a1d1881826fda0ff4bd01829`.
- [Structural S lifting tab horizontal arm](../../../../../mechanical/chassis/lifting-supports/p10ar-lift-tab-horizontal-arm/p10ar-lift-tab-horizontal-arm.md), 4 instances, SHA-256 `6b7336a425318dfcc503c8b4d5bed4b68449cf76e7b0109d6107433fcf5e00e2`.
- [Side lifting-tab root doubler](../../../../../mechanical-parts/components/p10root-lift-tab-root-doubler/p10root-lift-tab-root-doubler.md), 4 instances, SHA-256 `2f39ac7c65689cdcffb11a1f9c4679b7975ff60b7177afcf0b0d5ad051ff62d3`.
- [J lifting tab](../../../../../mechanical-parts/components/p10jt-j-lifting-tab/p10jt-j-lifting-tab.md), 4 instances, SHA-256 `32707443c7df3a1b1dcd3bb520e5fadd9ad2e9e5ec814509f9d8718f1fde4fe0`.

## Checks

OpenCADStudio verified the reference geometry at revision 6994. The final DWG save verified its hash and recorded zero dropped objects.

## Views

- [Plan](structural-s-side-lifting-supports-XY.png)
- [Elevation](structural-s-side-lifting-supports-XZ.png)
- [End](structural-s-side-lifting-supports-YZ.png)
- [Isometric](structural-s-side-lifting-supports-top-isometric.png)
