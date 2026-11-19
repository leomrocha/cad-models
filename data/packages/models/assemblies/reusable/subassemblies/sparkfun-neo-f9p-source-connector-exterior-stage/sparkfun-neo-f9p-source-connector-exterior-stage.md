# SparkFun NEO-F9P carrier, module and source connector exterior stage

1. **Permanent library number:** 291.
2. **Plan identity:** existing receiver component job 23.
3. **Native drawing:** [Receiver exterior stage](<sparkfun-neo-f9p-source-connector-exterior-stage.dwg>).
4. **State:** PARTIAL_SOURCE_CONNECTOR_EXTERIOR_SAVED_CURRENT_GEOMETRY_CHECKED.
5. **DWG SHA-256:** `f76f6d8de63f91dc101b36226b1d3973e737cd48b7669bfe2037b8d162c7747e`.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Units and frame:** mm; original SparkFun v1.1 board XY coordinates; PCB bottom Z = 0, source PCB top Z = 1.57; connector source/reconstructed definitions retain exact board XY rotations and their declared Z registration.
2. **Existing carrier/module:** library 250 is reused at identity, retaining its exact source geometry and original component scope.
3. **Connector exterior:** one BSC A40-00119-C52-12 USB-C stage, one ChangHong SMA-02-101-TGG stage and two JST SM04B-SRSS side-entry stages retain their source drawing reconstructions and open surfaces. The USB-C representation is 4.17 mm overall from its 3.21 mm and 0.96 mm callouts; the printed overall nominal is 4.16 mm. The SMA axis height is a 2.205 mm registration proposal, with 0.125 mm upper and 0.035 mm lower ground-foot gaps. These values remain beside their component source qualifications.
4. **Geometry and placements:** five roots contain 31 Solid3D and 62 Mesh occurrences, 93 geometry occurrences. Complete source-property fingerprints, source hashes and composed nested matrices PASS. The PCB top source datum is Z = 1.57 mm; connector XY positions and rotations follow the retained board source.
5. **Persistence:** immediate and per-step checkpoints completed. Current geometry was captured before final SAVE. Original SAVE completion, correct path, file existence/size/SHA-256, save audit and zero dropped data PASS. Verification uses retained current records.
6. **Appearance and cleanup:** actual current-record XY and isometric views inspected PASS. All unique Mesh face edges and native solid boundaries use exact nested placements. Owned document 788 guarded closed after current checks and persistence.

## Installed source occurrences

| Component | Library number | Quantity | Source DWG SHA-256 | Root matrix, row-major |
|---|---:|---:|---|---|
| SparkFun NEO-F9P carrier/module source stage | 250 | 1 | `62b8861d041d8f51f2eda30518132d4666447606141520acbe2cb8ff37552672` | `1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1` |
| BSC A40-00119-C52-12 RevA USB-C female exterior — J3 | 288 | 1 | `8a46843370db9ae0c7abb661db3d64d9b9cfafb0b6c6aecaaa4e790c46a8691e` | `0, 1, 0, 6.35; -1, 0, 0, 12.7; 0, 0, 1, 1.57; 0, 0, 0, 1` |
| ChangHong SMA-02-101-TGG RevA femalePCBedge SMA exteriorstage — J1 | 289 | 1 | `d6108318bd05e1f25e3720a5a4239ddae191b9c1c38df420a9794f6891287b24` | `0, 1, 0, 39.37; -1, 0, 0, 25.4; 0, 0, 1, 2.205; 0, 0, 0, 1` |
| JST SM04B-SRSS-TB(LF)(SN) black horizontal Qwiic exteriorstage — J2 | 290 | 1 | `a939308b184768c8d67d818016e7746c6d66ae806391079d6bd7aa73b7925c21` | `-1, 0, 0, 8.89; 0, -1, 0, 38.1; 0, 0, 1, 1.57; 0, 0, 0, 1` |
| JST SM04B-SRSS-TB(LF)(SN) black horizontal Qwiic exteriorstage — J4 | 290 | 1 | `a939308b184768c8d67d818016e7746c6d66ae806391079d6bd7aa73b7925c21` | `1, 0, 0, 8.89; 0, 1, 0, 5.08; 0, 0, 1, 1.57; 0, 0, 0, 1` |

## Sources — online

1. SparkFun NEO-F9P Qwiic receiver and design files.
2. BSC USB-C Rev A drawing.
3. SMA female PCB-mount drawing.
4. JST SH connector family drawing.

## Views

1. [XY current-record view](<sparkfun-neo-f9p-source-connector-exterior-stage-XY.png>).
2. [XZ current-record view](<sparkfun-neo-f9p-source-connector-exterior-stage-XZ.png>).
3. [YZ current-record view](<sparkfun-neo-f9p-source-connector-exterior-stage-YZ.png>).
4. [isometric current-record view](<sparkfun-neo-f9p-source-connector-exterior-stage-isometric.png>).

## References

1. SparkFun NEO-F9P carrier/module source stage companion (earlier revision `model-250`; [current catalogue revision](<sparkfun-neo-f9p-source-connector-exterior-stage.md>)).
2. [BSC A40-00119-C52-12 RevA USB-C female exterior — J3 companion](<../../../../electronics/connectors/bsc-a40-00119-c52-12-usb-c-exterior-stage/bsc-a40-00119-c52-12-usb-c-exterior-stage.md>).
3. [ChangHong SMA-02-101-TGG RevA femalePCBedge SMA exteriorstage — J1 companion](<../../../../electronics/components/sparkfun-wrl00593-sma-exterior-stage/sparkfun-wrl00593-sma-exterior-stage.md>).
4. [JST SM04B-SRSS-TB(LF)(SN) black horizontal Qwiic exteriorstage — J2 companion](<../../../../electronics/connectors/jst-sm04b-srss-qwiic-exterior-stage/jst-sm04b-srss-qwiic-exterior-stage.md>).
5. [JST SM04B-SRSS-TB(LF)(SN) black horizontal Qwiic exteriorstage — J4 companion](<../../../../electronics/connectors/jst-sm04b-srss-qwiic-exterior-stage/jst-sm04b-srss-qwiic-exterior-stage.md>).
6. Project execution evidence: source-pinned caller job, source registration, SAVE/current-record checks and recovery history are retained at ``.

## Whole-receiver installation coordinates

1. **Drawing:** [Dimensioned whole-receiver installation coordinate sheet](<sparkfun-neo-f9p-installation-dimensioned.png>), 4800 × 3200 pixels. The Eagle outline, mounting centres and connector footprint origins accompany the reused whole-receiver isometric view. Existing 93 geometry occurrences and four views are preserved.
2. **Board outline:** original Eagle XY = 0…43.180 mm on both axes. Right-edge notch X = 41.656 mm, Y = 21.082…29.718 mm.
3. **PCB thickness:** 1.570 mm, calculated from source design rules: 1.500 mm first isolation plus two 0.035 mm outer copper layers. PCB bottom Z = 0; top Z = 1.570 mm.
4. **Mounting pattern:** four source STAND-OFF holes, Ø3.302 mm. Eagle X pitch = 38.100 mm; Eagle Y pitch = 38.0746 mm. Lower and side insets = 2.5400 mm; upper inset = 2.5654 mm. The source drawing nominal pitch is 38.10 mm (1.50 in) and nominal inset is 2.54 mm (0.10 in).

| Source mounting reference | X [mm] | Y [mm] | Source drill [mm] |
| --- | ---: | ---: | ---: |
| JP31 | 2.5400 | 40.6146 | 3.302 |
| JP41 | 40.6400 | 40.6146 | 3.302 |
| JP91 | 2.5400 | 2.5400 | 3.302 |
| JP101 | 40.6400 | 2.5400 | 3.302 |

5. **Connector coordinates:** X/Y and rotations identify original Eagle footprint origins; Z identifies the retained exterior-model registration origin. J3 USB-C = [6.350, 12.700, 1.570] mm, R270; J1 SMA = [39.370, 25.400, 2.205] mm, R270; J2 Qwiic = [8.890, 38.100, 1.570] mm, R180; J4 Qwiic = [8.890, 5.080, 1.570] mm, R0. The SMA Z = 2.205 mm registration proposal retains upper/lower ground-foot gaps of 0.125/0.035 mm.
6. **USB-C source dimensions:** the exterior reconstruction sums the 3.21 mm and 0.96 mm drawing callouts to 4.17 mm; the printed overall nominal is 4.16 mm.
7. **Source attribution:** SparkFun GPS-23288 NEO-F9P Qwiic receiver, retained v1.1 Eagle board and the connector drawings cited above. The installation coordinate sheet preserves the existing source qualifications and partial connector surfaces.
