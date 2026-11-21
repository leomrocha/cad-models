# Fibox MPS 3020 direct Phoenix relay rail mount

**Catalogue draft ID** `fibox-mps3020-phoenix-direct-relay-mount`. Revision 1.

**Design status** Discussion construction proposal.

[Native DWG 2018](fibox-mps3020-phoenix-direct-relay-mount.dwg), SHA-256 `ae5c445997370f87e912ab11e93983336362f0f9d688b5ba46118bde4f946195`.

## Geometry

Machined MPS 3020 plate, 100 mm Phoenix rail, two 0804271 end stops and two nominal M5 × 12 mounting stacks.

Millimetres. U along the rail, V down, N toward the cabinet door. Rail bearing plane N = 0.

The rail seats on the plate at N = 0 mm. Its outer slots align with the plate bores on 75 mm pitch. Both screws project 2 mm beyond their locknuts in the nominal stack. The installed positions place eight end-stop clamp vertices per side on the rail lip underside plane N = 6.5 mm. The Ø12 mm socket envelope overlaps the final end-stop bounds by 0.5 mm. The proposed 2 mm inward stop slide gives a 1.5 mm nominal gap before relay placement.

## Embedded model revisions

- [Fibox MPS 3020 plate with direct relay rail drilling](../../../../../electrical/enclosure-mounts/fibox-mps3020-direct-relay-rail-plate/fibox-mps3020-direct-relay-rail-plate.md), 1 instances, SHA-256 `61bf406394fc5efe964cdb4f7f8fc1571230b963149c8e5f01d5569ca8eb93e7`.
- [Phoenix Contact NS 35/7.5 rail, 100 mm cut](../../../../../electrical/din-rails/phoenix-0807012-ns35-100mm-relay-rail/phoenix-0807012-ns35-100mm-relay-rail.md), 1 instances, SHA-256 `4a2e38d77f705c6140002d44ea7f65f0902641e1eb3a042ab97b354184c7bfd6`.
- [Phoenix Contact E/NS 35 N BK rail end stop](../../../../../electrical/din-rails/phoenix-0804271-ens35-end-stop/phoenix-0804271-ens35-end-stop.md), 2 instances, SHA-256 `f72728da15248c0661b3ff5abc3b643e86872eb49ea2c2d07dd8f6656062221b`.
- [ISO 4017 M5 × 12 screw nominal reference](../../../../../mechanical-parts/fasteners/screws/c167-iso4017-m5x12-screw-proposed-class88/c167-iso4017-m5x12-screw-proposed-class88.md), 2 instances, SHA-256 `90ff7a63e2e589a295025fb89b8c8d6cc2f2bcf46ecfb1f95ea28ba2d0e9f9eb`.
- [ISO 7089 M5 plain washer, proposed 200 HV](../../../../../mechanical-parts/fasteners/washers/iso7089-m5-washer-5p3x10x1p0-reference/iso7089-m5-washer-5p3x10x1p0-reference.md), 4 instances, SHA-256 `88c192a893deb24923e114cbf767284cbe5a8f9243b3fe74885932d94a7051c7`.
- [DIN 985 M5 nylon-insert nut nominal reference](../../../../../mechanical-parts/fasteners/nuts/c151-din-985-m5-nylon-insert-nut-proposed-class-8/c151-din-985-m5-nylon-insert-nut-proposed-class-8.md), 2 instances, SHA-256 `93539a49f7eed7c133ef5072ec82333e2377af68cd56428d7ad6686ca2251e64`.

## Checks

OpenCADStudio verified the reference geometry at revision 33281. The final DWG save verified its hash and recorded zero dropped objects.

## Views

- [Plan](fibox-mps3020-phoenix-direct-relay-mount-XY.png)
- [Elevation](fibox-mps3020-phoenix-direct-relay-mount-XZ.png)
- [End](fibox-mps3020-phoenix-direct-relay-mount-YZ.png)
- [Isometric](fibox-mps3020-phoenix-direct-relay-mount-top-isometric.png)
