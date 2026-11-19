# SOW BRAIN C02 PCB

1. **Library number:** 229.
2. **Type:** part.
3. **CAD file:** [SOW-BRAIN-C02-PCB.dwg](<SOW-BRAIN-C02-PCB.dwg>).
4. **DWG SHA-256:** `fb30e55eff99c0d95896018fd88b316ef0af00b96f858d3ce8f9e7eddb0e2559`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

1. **Geometry input record:** source-job.json.
2. **Input record SHA-256:** `0def5982ecf299d5e9667e025b345125731ae7cfeb4bbfc94e6e411868480aad`.

```json
{
  "part_id": "SOW-BRAIN-C02-PCB",
  "part_name": "LEVIA-H7 Rev0_1 physical PCB substrate",
  "source_sha256": "d062589e44d26a5f2cb64105fb9a7df71a42984a45275a46d0ad600f0405f767",
  "representation": "native solid substrate; source Edge.Cuts, thickness and pad drills",
  "units": "mm",
  "frame": {
    "source_to_native": "[x,y,z] -> [x,-y,z]",
    "native_bottom_z": 0,
    "native_top_z": 1.6,
    "source_pad_angle_convention": "pad at angle is board absolute; footprint-local pad position rotates by footprint angle in KiCad screen coordinates"
  },
  "thickness": 1.6,
  "edge_chain": [
    {
      "source_index": 0,
      "uuid": "8d5cec02-6ea2-4621-8685-bdb5c9a7bae4",
      "source_type": "gr_line",
      "start": [
        118.945923,
        -82.425292
      ],
      "end": [
        118.945879,
        -83.886178
      ],
      "reversed": false
    },
    {
      "source_index": 6,
      "uuid": "c6aea401-0e60-433c-aff1-3bb0876c5582",
      "source_type": "gr_arc",
      "start": [
        118.945879,
        -83.886178
      ],
      "end": [
        119.278009,
        -84.688061
      ],
      "reversed": true,
      "center": [
        120.07987728962591,
        -83.88621352806919
      ],
      "radius": 1.133998290182453,
      "theta": 0.7854165123985011,
      "bulge": 0.19891713613401232
    },
    {
      "source_index": 7,
      "uuid": "8d7f6f73-cc0a-4ac2-ae37-422d47d41584",
      "source_type": "gr_line",
      "start": [
        119.278009,
        -84.688061
      ],
      "end": [
        120.315414,
        -85.725493
      ],
      "reversed": false
    },
    {
      "source_index": 12,
      "uuid": "62ab3b48-ddce-4e74-bbc5-a325c7207a4c",
      "source_type": "gr_arc",
      "start": [
        120.315414,
        -85.725493
      ],
      "end": [
        121.384559,
        -85.725507
      ],
      "reversed": true,
      "center": [
        120.84999350000804,
        -85.19092688688679
      ],
      "radius": 0.7560001131731474,
      "theta": 1.5707951798730782,
      "bulge": 0.4142132264475118
    },
    {
      "source_index": 13,
      "uuid": "dd622010-3715-474e-be71-47c7af3a1dc6",
      "source_type": "gr_line",
      "start": [
        121.384559,
        -85.725507
      ],
      "end": [
        121.660002,
        -85.450072
      ],
      "reversed": false
    },
    {
      "source_index": 16,
      "uuid": "ddeba68b-99ab-4457-9355-9fb69737a94b",
      "source_type": "gr_arc",
      "start": [
        121.660002,
        -85.450072
      ],
      "end": [
        121.860605,
        -84.739245
      ],
      "reversed": true,
      "center": [
        121.12543734031398,
        -84.91549246349966
      ],
      "radius": 0.7559991112628117,
      "theta": 1.020709106412512,
      "bulge": 0.26086410318309955
    },
    {
      "source_index": 17,
      "uuid": "a5955323-1517-4198-914a-4a353b56950b",
      "source_type": "gr_arc",
      "start": [
        121.860605,
        -84.739245
      ],
      "end": [
        123.078009,
        -85.955087
      ],
      "reversed": false,
      "center": [
        123.45919704448434,
        -84.3560042374407
      ],
      "radius": 1.643888684423503,
      "theta": -5.181696615226289,
      "bulge": -3.5391908591020154
    },
    {
      "source_index": 23,
      "uuid": "b6cc9d0f-009b-42e4-9a71-f1fa7f883db9",
      "source_type": "gr_arc",
      "start": [
        123.078009,
        -85.955087
      ],
      "end": [
        122.368141,
        -86.155902
      ],
      "reversed": true,
      "center": [
        122.90270587459884,
        -86.69047799071149
      ],
      "radius": 0.7559967559421308,
      "theta": 1.0194012137983568,
      "bulge": 0.26051490925244386
    },
    {
      "source_index": 22,
      "uuid": "262b3ef2-564c-4719-9303-b5e79ec285db",
      "source_type": "gr_line",
      "start": [
        122.368141,
        -86.155902
      ],
      "end": [
        122.091534,
        -86.432501
      ],
      "reversed": false
    },
    {
      "source_index": 20,
      "uuid": "c558811a-43e4-4508-91e6-84d7a1575c22",
      "source_type": "gr_arc",
      "start": [
        122.091534,
        -86.432501
      ],
      "end": [
        122.09152,
        -87.501646
      ],
      "reversed": true,
      "center": [
        122.6261001131274,
        -86.96708050001064
      ],
      "radius": 0.7560001131850248,
      "theta": 1.5707951798465203,
      "bulge": 0.4142132264397332
    },
    {
      "source_index": 21,
      "uuid": "b77c77b3-fa80-49b4-8171-c5484eaa459a",
      "source_type": "gr_line",
      "start": [
        122.09152,
        -87.501646
      ],
      "end": [
        123.126088,
        -88.536242
      ],
      "reversed": false
    },
    {
      "source_index": 28,
      "uuid": "34c54764-ef89-4c38-8ba1-1a687928cba5",
      "source_type": "gr_arc",
      "start": [
        123.126088,
        -88.536242
      ],
      "end": [
        123.927923,
        -88.868393
      ],
      "reversed": true,
      "center": [
        123.92795814581754,
        -87.73439066924789
      ],
      "radius": 1.1340023312949534,
      "theta": 0.7853789028046063,
      "bulge": 0.19890736171946227
    },
    {
      "source_index": 29,
      "uuid": "46bfad36-b2ae-4fef-b6c6-e7b4f8e5dde1",
      "source_type": "gr_line",
      "start": [
        123.927923,
        -88.868393
      ],
      "end": [
        125.399313,
        -88.868438
      ],
      "reversed": false
    },
    {
      "source_index": 32,
      "uuid": "002ac6fe-8903-48a3-adf2-0b52fbafb3f4",
      "source_type": "gr_arc",
      "start": [
        125.399313,
        -88.868438
      ],
      "end": [
        126.149392,
        -88.584961
      ],
      "reversed": true,
      "center": [
        125.3993475197647,
        -87.73443783299554
      ],
      "radius": 1.1340001675298617,
      "theta": 0.7227339690594478,
      "bulge": 0.18267574166757192
    },
    {
      "source_index": 33,
      "uuid": "68e54703-b48c-452c-9a6a-f4507093bc75",
      "source_type": "gr_arc",
      "start": [
        126.149392,
        -88.584961
      ],
      "end": [
        127.899577,
        -87.923515
      ],
      "reversed": false,
      "center": [
        127.8994957241302,
        -90.56951622272665
      ],
      "radius": 2.64600122397288,
      "theta": -0.7227339354043254,
      "bulge": -0.1826757329730199
    },
    {
      "source_index": 35,
      "uuid": "337d28f8-504e-4365-9e42-cbf0096e1ae4",
      "source_type": "gr_line",
      "start": [
        127.899577,
        -87.923515
      ],
      "end": [
        149.532053,
        -87.924175
      ],
      "reversed": false
    },
    {
      "source_index": 36,
      "uuid": "e561cba9-8080-4663-9faa-cedd93a29a66",
      "source_type": "gr_arc",
      "start": [
        149.532053,
        -87.924175
      ],
      "end": [
        151.282197,
        -88.585728
      ],
      "reversed": false,
      "center": [
        149.53197295340243,
        -90.57017356602248
      ],
      "radius": 2.645998567233253,
      "theta": -0.7227344835809459,
      "bulge": -0.18267587459040005
    },
    {
      "source_index": 40,
      "uuid": "a665d65b-ed84-4e53-80b0-d6bd894f184d",
      "source_type": "gr_arc",
      "start": [
        151.282197,
        -88.585728
      ],
      "end": [
        152.032259,
        -88.869251
      ],
      "reversed": true,
      "center": [
        152.03229748086702,
        -87.73524067026479
      ],
      "radius": 1.1340103303925724,
      "theta": 0.7227275352295586,
      "bulge": 0.182674079535676
    },
    {
      "source_index": 41,
      "uuid": "c20e09e1-196c-43cd-9617-ec7a5170df02",
      "source_type": "gr_line",
      "start": [
        152.032259,
        -88.869251
      ],
      "end": [
        153.493072,
        -88.869295
      ],
      "reversed": false
    },
    {
      "source_index": 44,
      "uuid": "e00c337e-770b-4ecc-a579-8738e9ab16ba",
      "source_type": "gr_arc",
      "start": [
        153.493072,
        -88.869295
      ],
      "end": [
        154.295035,
        -88.537085
      ],
      "reversed": true,
      "center": [
        153.49311002680307,
        -87.73530272811975
      ],
      "radius": 1.1339922725178326,
      "theta": 0.7855206791105417,
      "bulge": 0.19894420837008633
    },
    {
      "source_index": 45,
      "uuid": "9811115f-5fac-4ccd-afc5-f96495c3a5ac",
      "source_type": "gr_line",
      "start": [
        154.295035,
        -88.537085
      ],
      "end": [
        155.332442,
        -87.4995
      ],
      "reversed": false
    },
    {
      "source_index": 53,
      "uuid": "9159c7b4-3741-44c6-86b2-55b83a62a228",
      "source_type": "gr_arc",
      "start": [
        155.332442,
        -87.4995
      ],
      "end": [
        155.332349,
        -86.430354
      ],
      "reversed": true,
      "center": [
        154.79782288684302,
        -86.96497349997192
      ],
      "radius": 0.7560001159953659,
      "theta": 1.5707970504438156,
      "bulge": 0.4142137743249721
    },
    {
      "source_index": 52,
      "uuid": "98bbbce7-9bdf-4509-88b7-3d14909a6709",
      "source_type": "gr_line",
      "start": [
        155.332349,
        -86.430354
      ],
      "end": [
        155.057055,
        -86.155108
      ],
      "reversed": false
    },
    {
      "source_index": 46,
      "uuid": "a5df9243-4340-4a96-8e25-fd88c0dd0b65",
      "source_type": "gr_arc",
      "start": [
        155.057055,
        -86.155108
      ],
      "end": [
        154.346261,
        -85.954562
      ],
      "reversed": true,
      "center": [
        154.5225269184418,
        -86.68972823136598
      ],
      "radius": 0.7560020249708947,
      "theta": 1.0206331808417324,
      "bulge": 0.26084383020548746
    },
    {
      "source_index": 47,
      "uuid": "5d4c81db-4e3e-435d-98da-faa0f9a6030a",
      "source_type": "gr_arc",
      "start": [
        154.346261,
        -85.954562
      ],
      "end": [
        155.562074,
        -84.737121
      ],
      "reversed": false,
      "center": [
        153.96297565617982,
        -84.35597510876838
      ],
      "radius": 1.643894067026499,
      "theta": -5.181696576836151,
      "bulge": -3.5391907292869966
    },
    {
      "source_index": 56,
      "uuid": "e0040e45-2c2b-484d-8538-0d22e44d5cc3",
      "source_type": "gr_arc",
      "start": [
        155.562074,
        -84.737121
      ],
      "end": [
        155.762947,
        -85.447022
      ],
      "reversed": true,
      "center": [
        156.29747068999225,
        -84.91240368965508
      ],
      "radius": 0.7559975614671556,
      "theta": 1.0194720694111608,
      "bulge": 0.26053382545044035
    },
    {
      "source_index": 57,
      "uuid": "b5ff6575-c918-4d5c-8683-d58abb309d07",
      "source_type": "gr_line",
      "start": [
        155.762947,
        -85.447022
      ],
      "end": [
        156.039277,
        -85.723305
      ],
      "reversed": false
    },
    {
      "source_index": 60,
      "uuid": "b833d10a-ac84-4761-ae80-3be96f99e337",
      "source_type": "gr_arc",
      "start": [
        156.039277,
        -85.723305
      ],
      "end": [
        157.108422,
        -85.723213
      ],
      "reversed": true,
      "center": [
        156.57380349994594,
        -85.18868588674039
      ],
      "radius": 0.7560001160098773,
      "theta": 1.5707951795992146,
      "bulge": 0.414213226367299
    },
    {
      "source_index": 61,
      "uuid": "15aa7b35-6174-42ca-953d-58b1598b3379",
      "source_type": "gr_line",
      "start": [
        157.108422,
        -85.723213
      ],
      "end": [
        158.143293,
        -84.688164
      ],
      "reversed": false
    },
    {
      "source_index": 68,
      "uuid": "60a8f512-1624-4d30-b72a-54600fc89c86",
      "source_type": "gr_arc",
      "start": [
        158.143293,
        -84.688164
      ],
      "end": [
        158.475364,
        -83.886407
      ],
      "reversed": true,
      "center": [
        157.3413621676744,
        -83.88637406680263
      ],
      "radius": 1.1340018328076404,
      "theta": 0.7852812641802563,
      "bulge": 0.19888198643955804
    },
    {
      "source_index": 69,
      "uuid": "8f68ee8b-c94d-41a7-8f16-7e980b1b2e45",
      "source_type": "gr_line",
      "start": [
        158.475364,
        -83.886407
      ],
      "end": [
        158.475408,
        -82.415371
      ],
      "reversed": false
    },
    {
      "source_index": 67,
      "uuid": "00c38526-334b-4153-af23-cf8ef2ea0629",
      "source_type": "gr_arc",
      "start": [
        158.475408,
        -82.415371
      ],
      "end": [
        158.19193,
        -81.665292
      ],
      "reversed": true,
      "center": [
        157.34139497079684,
        -82.41534247517923
      ],
      "radius": 1.1340130295619009,
      "theta": 0.7227257285550605,
      "bulge": 0.1826736127949896
    },
    {
      "source_index": 66,
      "uuid": "cda70487-cb9c-4c6c-ac2c-de95d9f3fdc8",
      "source_type": "gr_arc",
      "start": [
        158.19193,
        -81.665292
      ],
      "end": [
        157.530482,
        -79.915108
      ],
      "reversed": false,
      "center": [
        160.17648515787135,
        -79.91518527673679
      ],
      "radius": 2.6460031590012894,
      "theta": -0.7227332903238803,
      "bulge": -0.18267556632126164
    },
    {
      "source_index": 62,
      "uuid": "cdfa413f-731f-4191-8d6d-61b35a88248b",
      "source_type": "gr_line",
      "start": [
        157.530482,
        -79.915108
      ],
      "end": [
        157.53112,
        -58.293127
      ],
      "reversed": false
    },
    {
      "source_index": 63,
      "uuid": "ce0a540d-1066-4d78-bd2f-335f145ef0c6",
      "source_type": "gr_arc",
      "start": [
        157.53112,
        -58.293127
      ],
      "end": [
        158.192671,
        -56.542982
      ],
      "reversed": false,
      "center": [
        160.1771217513252,
        -58.293204982844415
      ],
      "radius": 2.6460017524743544,
      "theta": -0.7227336658120826,
      "bulge": -0.18267566332585825
    },
    {
      "source_index": 70,
      "uuid": "cca6677d-8f38-438b-a6c1-6420d612b5ec",
      "source_type": "gr_arc",
      "start": [
        158.192671,
        -56.542982
      ],
      "end": [
        158.476194,
        -55.79292
      ],
      "reversed": true,
      "center": [
        157.34220233892077,
        -55.79288857587067
      ],
      "radius": 1.1339916615213474,
      "theta": 0.722739979954548,
      "bulge": 0.1826772945383067
    },
    {
      "source_index": 71,
      "uuid": "d04b1357-2bd9-400e-bded-4ff6e164fa68",
      "source_type": "gr_line",
      "start": [
        158.476194,
        -55.79292
      ],
      "end": [
        158.476237,
        -54.321965
      ],
      "reversed": false
    },
    {
      "source_index": 65,
      "uuid": "0037fe10-b164-4643-b950-b618e33f6232",
      "source_type": "gr_arc",
      "start": [
        158.476237,
        -54.321965
      ],
      "end": [
        158.144107,
        -53.520083
      ],
      "reversed": true,
      "center": [
        157.34223871053715,
        -54.321930471805906
      ],
      "radius": 1.1339982899885124,
      "theta": 0.7854156306968987,
      "bulge": 0.19891690698682354
    },
    {
      "source_index": 64,
      "uuid": "c96d98cd-eaf2-4ed3-80f7-a470a9f77531",
      "source_type": "gr_line",
      "start": [
        158.144107,
        -53.520083
      ],
      "end": [
        157.106738,
        -52.482687
      ],
      "reversed": false
    },
    {
      "source_index": 59,
      "uuid": "4f9f8548-98fa-4a29-bdd4-687ff8fd99a6",
      "source_type": "gr_arc",
      "start": [
        157.106738,
        -52.482687
      ],
      "end": [
        156.037593,
        -52.482673
      ],
      "reversed": true,
      "center": [
        156.5721584999951,
        -53.0172531131174
      ],
      "radius": 0.7560001131738859,
      "theta": 1.5707951798652693,
      "bulge": 0.4142132264452246
    },
    {
      "source_index": 58,
      "uuid": "5b572172-98f0-48b1-b399-56b1b1ca97ee",
      "source_type": "gr_line",
      "start": [
        156.037593,
        -52.482673
      ],
      "end": [
        155.762136,
        -52.758123
      ],
      "reversed": false
    },
    {
      "source_index": 55,
      "uuid": "76337f9e-cfbb-47c2-a8d2-a5c1d46fcf09",
      "source_type": "gr_arc",
      "start": [
        155.762136,
        -52.758123
      ],
      "end": [
        155.561529,
        -53.468934
      ],
      "reversed": true,
      "center": [
        156.29669934545228,
        -53.2927023356145
      ],
      "radius": 0.7559980399228431,
      "theta": 1.0206889970500335,
      "bulge": 0.2608587337385886
    },
    {
      "source_index": 54,
      "uuid": "9a281f24-aa75-4e01-bf6c-32fc4640494e",
      "source_type": "gr_arc",
      "start": [
        155.561529,
        -53.468934
      ],
      "end": [
        154.344141,
        -52.253091
      ],
      "reversed": false,
      "center": [
        153.96297515533286,
        -53.85213018261032
      ],
      "radius": 1.6438411445961718,
      "theta": -5.181668671311199,
      "bulge": -3.5390963699839966
    },
    {
      "source_index": 48,
      "uuid": "d3842c14-7d8b-4e32-a04e-c0ca4f310013",
      "source_type": "gr_arc",
      "start": [
        154.344141,
        -52.253091
      ],
      "end": [
        155.054005,
        -52.052276
      ],
      "reversed": true,
      "center": [
        154.51943849472622,
        -51.51769075318288
      ],
      "radius": 0.7560044541376448,
      "theta": 1.0193839976905277,
      "bulge": 0.2605103131248613
    },
    {
      "source_index": 49,
      "uuid": "02e10954-fd09-4834-9a3f-89097d96a00f",
      "source_type": "gr_line",
      "start": [
        155.054005,
        -52.052276
      ],
      "end": [
        155.330613,
        -51.775674
      ],
      "reversed": false
    },
    {
      "source_index": 51,
      "uuid": "a54fa459-8af3-43e4-ae0e-30b4705d2a4f",
      "source_type": "gr_arc",
      "start": [
        155.330613,
        -51.775674
      ],
      "end": [
        155.330627,
        -50.706529
      ],
      "reversed": true,
      "center": [
        154.7960468868926,
        -51.2410944999949
      ],
      "radius": 0.7560001131669525,
      "theta": 1.5707951798839843,
      "bulge": 0.41421322645070613
    },
    {
      "source_index": 50,
      "uuid": "b6c14e93-ad4d-4876-ae5c-cc0c050c90c8",
      "source_type": "gr_line",
      "start": [
        155.330627,
        -50.706529
      ],
      "end": [
        154.296079,
        -49.671954
      ],
      "reversed": false
    },
    {
      "source_index": 43,
      "uuid": "abc48727-bc7e-4524-ad52-06961867c4ed",
      "source_type": "gr_arc",
      "start": [
        154.296079,
        -49.671954
      ],
      "end": [
        153.494245,
        -49.339802
      ],
      "reversed": true,
      "center": [
        153.4942117022505,
        -50.473795041118585
      ],
      "radius": 1.1339930416110113,
      "theta": 0.7853851725701663,
      "bulge": 0.1989089911758286
    },
    {
      "source_index": 42,
      "uuid": "8f2b5d54-6a6a-4efa-a123-99ade6372015",
      "source_type": "gr_line",
      "start": [
        153.494245,
        -49.339802
      ],
      "end": [
        152.033301,
        -49.339757
      ],
      "reversed": false
    },
    {
      "source_index": 39,
      "uuid": "a7ade030-acfb-4bfe-b188-6c50a50f15a3",
      "source_type": "gr_arc",
      "start": [
        152.033301,
        -49.339757
      ],
      "end": [
        151.283221,
        -49.623234
      ],
      "reversed": true,
      "center": [
        152.03326741547778,
        -50.47376228751681
      ],
      "radius": 1.134005288014131,
      "theta": 0.7227314375811629,
      "bulge": 0.18267508767894874
    },
    {
      "source_index": 38,
      "uuid": "dd40ee6e-652b-44de-be09-19f18dca3bf0",
      "source_type": "gr_arc",
      "start": [
        151.283221,
        -49.623234
      ],
      "end": [
        149.533036,
        -50.28468
      ],
      "reversed": false,
      "center": [
        149.533117275865,
        -47.63867877727653
      ],
      "radius": 2.646001223973665,
      "theta": -0.7227339354046665,
      "bulge": -0.18267573297310802
    },
    {
      "source_index": 37,
      "uuid": "9d756de2-52d6-414b-a652-b728a7c36d55",
      "source_type": "gr_line",
      "start": [
        149.533036,
        -50.28468
      ],
      "end": [
        127.890075,
        -50.284014
      ],
      "reversed": false
    },
    {
      "source_index": 34,
      "uuid": "f4c5c2c4-7194-41fa-8ebc-1f995385ba62",
      "source_type": "gr_arc",
      "start": [
        127.890075,
        -50.284014
      ],
      "end": [
        126.139931,
        -49.62246
      ],
      "reversed": false,
      "center": [
        127.8901539857986,
        -47.638021239997684
      ],
      "radius": 2.6459927611812217,
      "theta": -0.7227362851581685,
      "bulge": -0.18267634001461597
    },
    {
      "source_index": 31,
      "uuid": "5000829b-0233-4fca-8edf-33ff76a3f726",
      "source_type": "gr_arc",
      "start": [
        126.139931,
        -49.62246
      ],
      "end": [
        125.389869,
        -49.338937
      ],
      "reversed": true,
      "center": [
        125.38983757585173,
        -50.47292866113921
      ],
      "radius": 1.1339916615788694,
      "theta": 0.72273997991538,
      "bulge": 0.1826772945281879
    },
    {
      "source_index": 30,
      "uuid": "ed25900e-6cf3-452e-8c5b-0fb3457f0992",
      "source_type": "gr_line",
      "start": [
        125.389869,
        -49.338937
      ],
      "end": [
        123.928944,
        -49.338892
      ],
      "reversed": false
    },
    {
      "source_index": 27,
      "uuid": "ca98f8eb-10c0-479e-9dfa-53b39f7a5987",
      "source_type": "gr_arc",
      "start": [
        123.928944,
        -49.338892
      ],
      "end": [
        123.127055,
        -49.671028
      ],
      "reversed": true,
      "center": [
        123.92891198949181,
        -50.47289878197182
      ],
      "radius": 1.134006782423613,
      "theta": 0.7854177909273681,
      "bulge": 0.1989174684134664
    },
    {
      "source_index": 26,
      "uuid": "2d13b56b-a537-4aa8-be6b-d65f306f23ad",
      "source_type": "gr_line",
      "start": [
        123.127055,
        -49.671028
      ],
      "end": [
        122.089642,
        -50.708428
      ],
      "reversed": false
    },
    {
      "source_index": 18,
      "uuid": "f52a195c-a8fe-4d84-9840-30ac9c3a7918",
      "source_type": "gr_arc",
      "start": [
        122.089642,
        -50.708428
      ],
      "end": [
        122.089635,
        -51.777574
      ],
      "reversed": true,
      "center": [
        122.62421111308134,
        -51.243004499998065
      ],
      "radius": 0.7560001131023467,
      "theta": 1.5707970505852806,
      "bulge": 0.4142137743664063
    },
    {
      "source_index": 19,
      "uuid": "f79648b4-f951-421e-9307-a5290fd0c0ef",
      "source_type": "gr_line",
      "start": [
        122.089635,
        -51.777574
      ],
      "end": [
        122.365083,
        -52.053025
      ],
      "reversed": false
    },
    {
      "source_index": 25,
      "uuid": "69311a7d-b697-40e8-88cd-efdf9d333ed8",
      "source_type": "gr_arc",
      "start": [
        122.365083,
        -52.053025
      ],
      "end": [
        123.075913,
        -52.253623
      ],
      "reversed": true,
      "center": [
        122.89965983863698,
        -51.518454211876
      ],
      "radius": 0.756001536984299,
      "theta": 1.02070783209422,
      "bulge": 0.2608637629241893
    },
    {
      "source_index": 24,
      "uuid": "0b47ce70-77a6-45b8-86e9-7e0dc49dbd17",
      "source_type": "gr_arc",
      "start": [
        123.075913,
        -52.253623
      ],
      "end": [
        121.860072,
        -53.471039
      ],
      "reversed": false,
      "center": [
        123.45917187556346,
        -53.85222806325857
      ],
      "radius": 1.643905567231316,
      "theta": -5.181703672592671,
      "bulge": -3.539214723509507
    },
    {
      "source_index": 15,
      "uuid": "24559fd4-7532-425f-a7e3-db897794c429",
      "source_type": "gr_arc",
      "start": [
        121.860072,
        -53.471039
      ],
      "end": [
        121.659254,
        -52.761168
      ],
      "reversed": true,
      "center": [
        121.12467784648138,
        -53.29573676936521
      ],
      "radius": 0.7559996250626771,
      "theta": 1.0194025830353821,
      "bulge": 0.26051527479358355
    },
    {
      "source_index": 14,
      "uuid": "45751d60-6b68-40fd-a68f-b821ea2a8f95",
      "source_type": "gr_line",
      "start": [
        121.659254,
        -52.761168
      ],
      "end": [
        121.382644,
        -52.484555
      ],
      "reversed": false
    },
    {
      "source_index": 11,
      "uuid": "73b71f2c-931c-4636-b640-88851232e621",
      "source_type": "gr_arc",
      "start": [
        121.382644,
        -52.484555
      ],
      "end": [
        120.313499,
        -52.484548
      ],
      "reversed": true,
      "center": [
        120.84806799998674,
        -53.01912632021101
      ],
      "radius": 0.7560013202252471,
      "theta": 1.5707919864931204,
      "bulge": 0.41421229112870855
    },
    {
      "source_index": 10,
      "uuid": "e93e3d39-00c7-4b32-a37e-e38c404e6ee1",
      "source_type": "gr_line",
      "start": [
        120.313499,
        -52.484548
      ],
      "end": [
        119.27892,
        -53.519115
      ],
      "reversed": false
    },
    {
      "source_index": 3,
      "uuid": "0d3a64aa-d2e6-4a08-bc8c-cda2f4554b94",
      "source_type": "gr_arc",
      "start": [
        119.27892,
        -53.519115
      ],
      "end": [
        118.946774,
        -54.320945
      ],
      "reversed": true,
      "center": [
        120.08076783834642,
        -54.32097662805499
      ],
      "radius": 1.1339938387874198,
      "theta": 0.7853788711775063,
      "bulge": 0.19890735349986255
    },
    {
      "source_index": 2,
      "uuid": "c0620874-732e-4e38-b450-fae05779dccd",
      "source_type": "gr_line",
      "start": [
        118.946774,
        -54.320945
      ],
      "end": [
        118.946729,
        -55.792348
      ],
      "reversed": false
    },
    {
      "source_index": 4,
      "uuid": "b6e4e6f3-78a7-40fc-8365-826a72f13a44",
      "source_type": "gr_arc",
      "start": [
        118.946729,
        -55.792348
      ],
      "end": [
        119.230206,
        -56.542427
      ],
      "reversed": true,
      "center": [
        120.08072916702122,
        -55.7923825197587
      ],
      "radius": 1.134000167546616,
      "theta": 0.7227339690483587,
      "bulge": 0.18267574166470715
    },
    {
      "source_index": 5,
      "uuid": "daed4745-7908-48c6-8dee-cceff09654e7",
      "source_type": "gr_arc",
      "start": [
        119.230206,
        -56.542427
      ],
      "end": [
        119.891653,
        -58.292612
      ],
      "reversed": false,
      "center": [
        117.24565758369751,
        -58.29252966362477
      ],
      "radius": 2.645995417583941,
      "theta": -0.7227357370517993,
      "bulge": -0.18267619841536142
    },
    {
      "source_index": 9,
      "uuid": "ed37bbf3-d302-45b9-a900-b37e2e73765c",
      "source_type": "gr_line",
      "start": [
        119.891653,
        -58.292612
      ],
      "end": [
        119.890999,
        -79.925085
      ],
      "reversed": false
    },
    {
      "source_index": 8,
      "uuid": "c2d7b72a-3e71-4923-9020-269a3795d304",
      "source_type": "gr_arc",
      "start": [
        119.890999,
        -79.925085
      ],
      "end": [
        119.229446,
        -81.67523
      ],
      "reversed": false,
      "center": [
        117.24499531319681,
        -79.92500401779719
      ],
      "radius": 2.646003688042433,
      "theta": -0.7227333985557793,
      "bulge": -0.18267559428217095
    },
    {
      "source_index": 1,
      "uuid": "305e2c17-325b-4afa-8b13-0a572ffe6f21",
      "source_type": "gr_arc",
      "start": [
        119.229446,
        -81.67523
      ],
      "end": [
        118.945923,
        -82.425292
      ],
      "reversed": true,
      "center": [
        120.07991466115901,
        -82.42532342415568
      ],
      "radius": 1.1339916615986185,
      "theta": 0.7227399799021965,
      "bulge": 0.18267729452478207
    }
  ],
  "drills": [
    {
      "reference": "H2",
      "footprint": "_pico:MountingHole_3.2mm_M3_ISO14580_Pad_TopBottom",
      "pad": "1",
      "source_footprint_at": [
        "at",
        "153.963",
        "84.356"
      ],
      "source_pad_at": [
        "at",
        "0",
        "0"
      ],
      "source_drill": [
        "drill",
        "3.15"
      ],
      "center": [
        153.963,
        -84.356
      ],
      "size": [
        3.15,
        3.15
      ],
      "angle_deg": 0,
      "shape": "circle"
    },
    {
      "reference": "H3",
      "footprint": "_pico:MountingHole_3.2mm_M3_ISO14580_Pad_TopBottom",
      "pad": "1",
      "source_footprint_at": [
        "at",
        "123.4592",
        "84.356"
      ],
      "source_pad_at": [
        "at",
        "0",
        "0"
      ],
      "source_drill": [
        "drill",
        "3.15"
      ],
      "center": [
        123.4592,
        -84.356
      ],
      "size": [
        3.15,
        3.15
      ],
      "angle_deg": 0,
      "shape": "circle"
    },
    {
      "reference": "H4",
      "footprint": "_pico:MountingHole_3.2mm_M3_ISO14580_Pad_TopBottom",
      "pad": "1",
      "source_footprint_at": [
        "at",
        "123.47",
        "53.85"
      ],
      "source_pad_at": [
        "at",
        "0",
        "0"
      ],
      "source_drill": [
        "drill",
        "3.15"
      ],
      "center": [
        123.47,
        -53.85
      ],
      "size": [
        3.15,
        3.15
      ],
      "angle_deg": 0,
      "shape": "circle"
    },
    {
      "reference": "H1",
      "footprint": "_pico:MountingHole_3.2mm_M3_ISO14580_Pad_TopBottom",
      "pad": "1",
      "source_footprint_at": [
        "at",
        "153.97",
        "53.775"
      ],
      "source_pad_at": [
        "at",
        "0",
        "0"
      ],
      "source_drill": [
        "drill",
        "3.15"
      ],
      "center": [
        153.97,
        -53.775
      ],
      "size": [
        3.15,
        3.15
      ],
      "angle_deg": 0,
      "shape": "circle"
    },
    {
      "reference": "USB1",
      "footprint": "EasyEDA:USB-C-SMD_HCTL_HC-TYPE-C-16P-01M",
      "pad": "25",
      "source_footprint_at": [
        "at",
        "124.1875",
        "61.26",
        "-90"
      ],
      "source_pad_at": [
        "at",
        "4.32",
        "-1.72",
        "270"
      ],
      "source_drill": [
        "drill",
        "oval",
        "0.599999",
        "1.400023"
      ],
      "center": [
        125.9075,
        -65.58
      ],
      "size": [
        0.599999,
        1.400023
      ],
      "angle_deg": 270.0,
      "shape": "oval"
    },
    {
      "reference": "USB1",
      "footprint": "EasyEDA:USB-C-SMD_HCTL_HC-TYPE-C-16P-01M",
      "pad": "26",
      "source_footprint_at": [
        "at",
        "124.1875",
        "61.26",
        "-90"
      ],
      "source_pad_at": [
        "at",
        "4.32",
        "2.28",
        "270"
      ],
      "source_drill": [
        "drill",
        "oval",
        "0.599999",
        "1.799996"
      ],
      "center": [
        121.9075,
        -65.58
      ],
      "size": [
        0.599999,
        1.799996
      ],
      "angle_deg": 270.0,
      "shape": "oval"
    },
    {
      "reference": "USB1",
      "footprint": "EasyEDA:USB-C-SMD_HCTL_HC-TYPE-C-16P-01M",
      "pad": "27",
      "source_footprint_at": [
        "at",
        "124.1875",
        "61.26",
        "-90"
      ],
      "source_pad_at": [
        "at",
        "-4.32",
        "2.28",
        "270"
      ],
      "source_drill": [
        "drill",
        "oval",
        "0.599999",
        "1.799996"
      ],
      "center": [
        121.9075,
        -56.94
      ],
      "size": [
        0.599999,
        1.799996
      ],
      "angle_deg": 270.0,
      "shape": "oval"
    },
    {
      "reference": "USB1",
      "footprint": "EasyEDA:USB-C-SMD_HCTL_HC-TYPE-C-16P-01M",
      "pad": "28",
      "source_footprint_at": [
        "at",
        "124.1875",
        "61.26",
        "-90"
      ],
      "source_pad_at": [
        "at",
        "-4.32",
        "-1.72",
        "270"
      ],
      "source_drill": [
        "drill",
        "oval",
        "0.599999",
        "1.400023"
      ],
      "center": [
        125.9075,
        -56.94
      ],
      "size": [
        0.599999,
        1.400023
      ],
      "angle_deg": 270.0,
      "shape": "oval"
    }
  ]
}
```

## Sources — online

1. Control board.
