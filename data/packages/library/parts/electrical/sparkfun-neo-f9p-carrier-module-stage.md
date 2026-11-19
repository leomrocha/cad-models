# SparkFun GPS-23288 v1.1 receiver — carrier and NEO-F9P module

1. **Library number:** 250.
2. **Plan component:** model 23, SparkFun NEO-F9P Qwiic receiver.
3. **CAD file:** [Native carrier and module stage](<sparkfun-neo-f9p-carrier-module-stage.dwg>).
4. **DWG SHA-256:** `62b8861d041d8f51f2eda30518132d4666447606141520acbe2cb8ff37552672`.
5. **State:** PARTIAL_SAVED_REOPENED.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Included hardware:** one source carrier substrate and one 30-body manufacturer NEO-F9P module, inserted as two existing native models. Total nested construction bodies: 31.
2. **Coordinate frame:** Eagle board XY in millimetres, carrier bottom Z = 0 mm and top Z = 1.57 mm, retained from source-native substrate. Eagle U1 centre is X = 20.32 mm, Y = 19.558 mm, rotation 0°.
3. **Module placement:** source XYZ maps to [−Z, −X, +Y], followed by translation [−4.34471736786609, +7.28157598235909, +5.71848931470063] mm. Source contact-plane minimum Y = −4.14848931470063 mm seats at board Z = 1.57 mm. All 24 physical contact rectangles are matched to Eagle pads; longitudinal residual is below 0.000001 mm and transverse centre offsets are ±0.4 mm inside the copper-pad rectangles. The asymmetric 3 mm contact gap fixes orientation.
4. **Retained external-interface locations:** J3 USB-C at [6.35, 12.7] mm, R270; J1 SMA at [39.37, 25.4] mm, R270; J2 Qwiic at [8.89, 38.1] mm, R180; J4 Qwiic at [8.89, 5.08] mm, R0. This saved stage contains the carrier and receiver module.
5. **Checks:** source-contact matching, native insertion matrices and metadata before/after reopening PASS; eight incremental checkpoints retained; save/reopen and file hash PASS; owned documents 611 and 612 closed.
6. **Views:** isometric and XY boundary drawings inspected from saved native geometry.

## References — library

1. [Source carrier substrate — library 230](<SOW-BRAIN-C03-F9P-PCB.md>), quantity 1.
2. [NEO-F9P source module — library 227](<../../subassemblies/NEO_WITH_INTERPOSER_BOT.md>), quantity 1.
3. [Isometric boundary drawing](<../../images/sparkfun-neo-f9p-carrier-module-stage-isometric.png>).
4. [XY boundary drawing](<../../images/sparkfun-neo-f9p-carrier-module-stage-XY.png>).

## Sources — online

1. SparkFun GPS-23288 NEO-F9P Qwiic receiver, retained v1.1 Eagle board: U1 contact footprints, connector footprints and placements.
2. u-blox NEO-F9P manufacturer STEP, retained manufacturer module geometry.
