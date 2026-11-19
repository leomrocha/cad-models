# SOW BRAIN C03 F9P PCB

1. **Library number:** 230.
2. **Type:** part.
3. **CAD file:** [SOW-BRAIN-C03-F9P-PCB.dwg](<SOW-BRAIN-C03-F9P-PCB.dwg>).
4. **DWG SHA-256:** `90215704fc55ac10187f426014e59d04e9fd3e811cedcaa5b6f55c9938eced8f`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

1. **Geometry input record:** source-job.json.
2. **Input record SHA-256:** `899b091e8095a116dca576e7880406bea7aa52f5c0d805228760a6577742d033`.

```json
{
  "part_id": "SOW-BRAIN-C03-F9P-PCB",
  "part_name": "SparkFun GPS-23288 v1.1 bare PCB body",
  "source_sha256": "106bf493f740f487743a6953b4e576c6a998716e89e8dea9d19227594aaa951b",
  "units": "mm",
  "representation": "native bare PCB body; exact Eagle outline, all pad/mount/via drill apertures; calculated source design-rule total thickness",
  "thickness": 1.57,
  "frame": "Eagle sourceX/Y retained; bare PCB bottomZ=0; topZ=1.57mm",
  "edge_chain": [
    {
      "source_locator": "plain/wire[0]",
      "x1": "0",
      "y1": "0",
      "x2": "0",
      "y2": "43.18",
      "width": "0.1524",
      "layer": "20",
      "reversed": false
    },
    {
      "source_locator": "plain/wire[1]",
      "x1": "0",
      "y1": "43.18",
      "x2": "43.18",
      "y2": "43.18",
      "width": "0.1524",
      "layer": "20",
      "reversed": false
    },
    {
      "source_locator": "plain/wire[2]",
      "x1": "43.18",
      "y1": "43.18",
      "x2": "43.18",
      "y2": "29.718",
      "width": "0.1524",
      "layer": "20",
      "reversed": false
    },
    {
      "source_locator": "plain/wire[7]",
      "x1": "43.18",
      "y1": "29.718",
      "x2": "41.656",
      "y2": "29.718",
      "width": "0.1524",
      "layer": "20",
      "reversed": false
    },
    {
      "source_locator": "plain/wire[8]",
      "x1": "41.656",
      "y1": "29.718",
      "x2": "41.656",
      "y2": "21.082",
      "width": "0.1524",
      "layer": "20",
      "reversed": false
    },
    {
      "source_locator": "plain/wire[9]",
      "x1": "41.656",
      "y1": "21.082",
      "x2": "43.18",
      "y2": "21.082",
      "width": "0.1524",
      "layer": "20",
      "reversed": false
    },
    {
      "source_locator": "plain/wire[3]",
      "x1": "43.18",
      "y1": "21.082",
      "x2": "43.18",
      "y2": "0",
      "width": "0.1524",
      "layer": "20",
      "reversed": false
    },
    {
      "source_locator": "plain/wire[4]",
      "x1": "43.18",
      "y1": "0",
      "x2": "0",
      "y2": "0",
      "width": "0.1524",
      "layer": "20",
      "reversed": false
    }
  ],
  "drills": [
    {
      "kind": "through_pad_or_mount",
      "center": [
        2.54,
        40.6146
      ],
      "diameter": 3.302,
      "source": {
        "reference": "JP31",
        "feature_type": "hole",
        "local_feature": {
          "x": "0",
          "y": "0",
          "drill": "3.302"
        },
        "element_rotation": "R0",
        "x_mm": 2.54,
        "y_mm": 40.6146,
        "drill_mm": 3.302,
        "source_locator": "elements/JP31 -> libraries/SparkFun/packages/STAND-OFF/hole[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        40.64,
        40.6146
      ],
      "diameter": 3.302,
      "source": {
        "reference": "JP41",
        "feature_type": "hole",
        "local_feature": {
          "x": "0",
          "y": "0",
          "drill": "3.302"
        },
        "element_rotation": "R0",
        "x_mm": 40.64,
        "y_mm": 40.6146,
        "drill_mm": 3.302,
        "source_locator": "elements/JP41 -> libraries/SparkFun/packages/STAND-OFF/hole[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        2.54,
        2.54
      ],
      "diameter": 3.302,
      "source": {
        "reference": "JP91",
        "feature_type": "hole",
        "local_feature": {
          "x": "0",
          "y": "0",
          "drill": "3.302"
        },
        "element_rotation": "R0",
        "x_mm": 2.54,
        "y_mm": 2.54,
        "drill_mm": 3.302,
        "source_locator": "elements/JP91 -> libraries/SparkFun/packages/STAND-OFF/hole[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        40.64,
        2.54
      ],
      "diameter": 3.302,
      "source": {
        "reference": "JP101",
        "feature_type": "hole",
        "local_feature": {
          "x": "0",
          "y": "0",
          "drill": "3.302"
        },
        "element_rotation": "R0",
        "x_mm": 40.64,
        "y_mm": 2.54,
        "drill_mm": 3.302,
        "source_locator": "elements/JP101 -> libraries/SparkFun/packages/STAND-OFF/hole[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        1.2550000000000008,
        17.018
      ],
      "diameter": 0.4,
      "source": {
        "reference": "J3",
        "feature_type": "pad",
        "local_feature": {
          "name": "SHLD3",
          "x": "-4.318",
          "y": "-5.095",
          "drill": "0.4",
          "diameter": "0.6",
          "shape": "long",
          "rot": "R90",
          "stop": "no"
        },
        "element_rotation": "R270",
        "x_mm": 1.2550000000000008,
        "y_mm": 17.018,
        "drill_mm": 0.4,
        "source_locator": "elements/J3 -> libraries/SparkFun-Connectors/packages/USB-C-16P-2LAYER-PADS/pad[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        1.254999999999999,
        8.382000000000001
      ],
      "diameter": 0.4,
      "source": {
        "reference": "J3",
        "feature_type": "pad",
        "local_feature": {
          "name": "SHLD4",
          "x": "4.318",
          "y": "-5.095",
          "drill": "0.4",
          "diameter": "0.6",
          "shape": "long",
          "rot": "R90",
          "stop": "no"
        },
        "element_rotation": "R270",
        "x_mm": 1.254999999999999,
        "y_mm": 8.382000000000001,
        "drill_mm": 0.4,
        "source_locator": "elements/J3 -> libraries/SparkFun-Connectors/packages/USB-C-16P-2LAYER-PADS/pad[1]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        5.434999999999999,
        8.382
      ],
      "diameter": 0.4,
      "source": {
        "reference": "J3",
        "feature_type": "pad",
        "local_feature": {
          "name": "SHLD2",
          "x": "4.318",
          "y": "-0.915",
          "drill": "0.4",
          "diameter": "0.6",
          "shape": "long",
          "rot": "R90",
          "stop": "no"
        },
        "element_rotation": "R270",
        "x_mm": 5.434999999999999,
        "y_mm": 8.382,
        "drill_mm": 0.4,
        "source_locator": "elements/J3 -> libraries/SparkFun-Connectors/packages/USB-C-16P-2LAYER-PADS/pad[2]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        5.4350000000000005,
        17.018
      ],
      "diameter": 0.4,
      "source": {
        "reference": "J3",
        "feature_type": "pad",
        "local_feature": {
          "name": "SHLD1",
          "x": "-4.318",
          "y": "-0.915",
          "drill": "0.4",
          "diameter": "0.6",
          "shape": "long",
          "rot": "R90",
          "stop": "no"
        },
        "element_rotation": "R270",
        "x_mm": 5.4350000000000005,
        "y_mm": 17.018,
        "drill_mm": 0.4,
        "source_locator": "elements/J3 -> libraries/SparkFun-Connectors/packages/USB-C-16P-2LAYER-PADS/pad[3]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        4.905,
        15.59
      ],
      "diameter": 0.65,
      "source": {
        "reference": "J3",
        "feature_type": "hole",
        "local_feature": {
          "x": "-2.89",
          "y": "-1.445",
          "drill": "0.65"
        },
        "element_rotation": "R270",
        "x_mm": 4.905,
        "y_mm": 15.59,
        "drill_mm": 0.65,
        "source_locator": "elements/J3 -> libraries/SparkFun-Connectors/packages/USB-C-16P-2LAYER-PADS/hole[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        4.9049999999999985,
        9.809999999999999
      ],
      "diameter": 0.65,
      "source": {
        "reference": "J3",
        "feature_type": "hole",
        "local_feature": {
          "x": "2.89",
          "y": "-1.445",
          "drill": "0.65"
        },
        "element_rotation": "R270",
        "x_mm": 4.9049999999999985,
        "y_mm": 9.809999999999999,
        "drill_mm": 0.65,
        "source_locator": "elements/J3 -> libraries/SparkFun-Connectors/packages/USB-C-16P-2LAYER-PADS/hole[1]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        1.27,
        21.59
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J5",
        "feature_type": "pad",
        "local_feature": {
          "name": "1",
          "x": "0",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R90",
        "x_mm": 1.27,
        "y_mm": 21.59,
        "drill_mm": 1.016,
        "source_locator": "elements/J5 -> libraries/SparkFun-Connectors/packages/1X06_NO_SILK/pad[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        1.2700000000000002,
        24.13
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J5",
        "feature_type": "pad",
        "local_feature": {
          "name": "2",
          "x": "2.54",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R90",
        "x_mm": 1.2700000000000002,
        "y_mm": 24.13,
        "drill_mm": 1.016,
        "source_locator": "elements/J5 -> libraries/SparkFun-Connectors/packages/1X06_NO_SILK/pad[1]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        1.2700000000000002,
        26.67
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J5",
        "feature_type": "pad",
        "local_feature": {
          "name": "3",
          "x": "5.08",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R90",
        "x_mm": 1.2700000000000002,
        "y_mm": 26.67,
        "drill_mm": 1.016,
        "source_locator": "elements/J5 -> libraries/SparkFun-Connectors/packages/1X06_NO_SILK/pad[2]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        1.2700000000000005,
        29.21
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J5",
        "feature_type": "pad",
        "local_feature": {
          "name": "4",
          "x": "7.62",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R90",
        "x_mm": 1.2700000000000005,
        "y_mm": 29.21,
        "drill_mm": 1.016,
        "source_locator": "elements/J5 -> libraries/SparkFun-Connectors/packages/1X06_NO_SILK/pad[3]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        1.2700000000000007,
        31.75
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J5",
        "feature_type": "pad",
        "local_feature": {
          "name": "5",
          "x": "10.16",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R90",
        "x_mm": 1.2700000000000007,
        "y_mm": 31.75,
        "drill_mm": 1.016,
        "source_locator": "elements/J5 -> libraries/SparkFun-Connectors/packages/1X06_NO_SILK/pad[4]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        1.270000000000001,
        34.29
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J5",
        "feature_type": "pad",
        "local_feature": {
          "name": "6",
          "x": "12.7",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R90",
        "x_mm": 1.270000000000001,
        "y_mm": 34.29,
        "drill_mm": 1.016,
        "source_locator": "elements/J5 -> libraries/SparkFun-Connectors/packages/1X06_NO_SILK/pad[5]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        13.97,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "1",
          "x": "0",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 13.97,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        16.51,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "2",
          "x": "2.54",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 16.51,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[1]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        19.05,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "3",
          "x": "5.08",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 19.05,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[2]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        21.59,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "4",
          "x": "7.62",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 21.59,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[3]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        24.130000000000003,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "5",
          "x": "10.16",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 24.130000000000003,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[4]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        26.67,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "6",
          "x": "12.7",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 26.67,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[5]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        29.21,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "7",
          "x": "15.24",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 29.21,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[6]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        31.75,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "8",
          "x": "17.78",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 31.75,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[7]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        34.29,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "9",
          "x": "20.32",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 34.29,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[8]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        36.83,
        41.91
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J7",
        "feature_type": "pad",
        "local_feature": {
          "name": "10",
          "x": "22.86",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 36.83,
        "y_mm": 41.91,
        "drill_mm": 1.016,
        "source_locator": "elements/J7 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[9]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        29.21,
        12.7
      ],
      "diameter": 0.95,
      "source": {
        "reference": "TP1",
        "feature_type": "pad",
        "local_feature": {
          "name": "1",
          "x": "0",
          "y": "0",
          "drill": "0.95",
          "diameter": "1.6",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 29.21,
        "y_mm": 12.7,
        "drill_mm": 0.95,
        "source_locator": "elements/TP1 -> libraries/SparkFun-Connectors/packages/1X01_NO_SILK/pad[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        11.43,
        29.21
      ],
      "diameter": 0.95,
      "source": {
        "reference": "TP2",
        "feature_type": "pad",
        "local_feature": {
          "name": "1",
          "x": "0",
          "y": "0",
          "drill": "0.95",
          "diameter": "1.6",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 11.43,
        "y_mm": 29.21,
        "drill_mm": 0.95,
        "source_locator": "elements/TP2 -> libraries/SparkFun-Connectors/packages/1X01_NO_SILK/pad[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        13.97,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "1",
          "x": "0",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 13.97,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[0]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        16.51,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "2",
          "x": "2.54",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 16.51,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[1]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        19.05,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "3",
          "x": "5.08",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 19.05,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[2]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        21.59,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "4",
          "x": "7.62",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 21.59,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[3]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        24.130000000000003,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "5",
          "x": "10.16",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 24.130000000000003,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[4]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        26.67,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "6",
          "x": "12.7",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 26.67,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[5]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        29.21,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "7",
          "x": "15.24",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 29.21,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[6]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        31.75,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "8",
          "x": "17.78",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 31.75,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[7]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        34.29,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "9",
          "x": "20.32",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 34.29,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[8]"
      }
    },
    {
      "kind": "through_pad_or_mount",
      "center": [
        36.83,
        1.27
      ],
      "diameter": 1.016,
      "source": {
        "reference": "J6",
        "feature_type": "pad",
        "local_feature": {
          "name": "10",
          "x": "22.86",
          "y": "0",
          "drill": "1.016",
          "diameter": "1.8796",
          "rot": "R90"
        },
        "element_rotation": "R0",
        "x_mm": 36.83,
        "y_mm": 1.27,
        "drill_mm": 1.016,
        "source_locator": "elements/J6 -> libraries/SparkFun-Connectors/packages/1X10_NO_SILK/pad[9]"
      }
    },
    {
      "kind": "via",
      "center": [
        6.985,
        25.4
      ],
      "diameter": 0.3,
      "source": {
        "signal": "3.3V",
        "x": "6.985",
        "y": "25.4",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.35,
        25.4
      ],
      "diameter": 0.3,
      "source": {
        "signal": "3.3V",
        "x": "6.35",
        "y": "25.4",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        12.769,
        13.404
      ],
      "diameter": 0.3,
      "source": {
        "signal": "3.3V",
        "x": "12.769",
        "y": "13.404",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        7.874,
        17.018
      ],
      "diameter": 0.3,
      "source": {
        "signal": "3.3V",
        "x": "7.874",
        "y": "17.018",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        8.89,
        3.175
      ],
      "diameter": 0.3,
      "source": {
        "signal": "3.3V",
        "x": "8.89",
        "y": "3.175",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        26.67,
        30.48
      ],
      "diameter": 0.3,
      "source": {
        "signal": "3.3V",
        "x": "26.67",
        "y": "30.48",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.098,
        29.21
      ],
      "diameter": 0.3,
      "source": {
        "signal": "3.3V",
        "x": "22.098",
        "y": "29.21",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        38.226996875,
        13.97
      ],
      "diameter": 0.381,
      "source": {
        "signal": "3.3V",
        "x": "38.226996875",
        "y": "13.97",
        "extent": "1-16",
        "drill": "0.381"
      }
    },
    {
      "kind": "via",
      "center": [
        21.336,
        14.732
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "21.336",
        "y": "14.732",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        14.986,
        27.432
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "14.986",
        "y": "27.432",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        26.924,
        27.432
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "26.924",
        "y": "27.432",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        24.892,
        24.384
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "24.892",
        "y": "24.384",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        28.575,
        24.384
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "28.575",
        "y": "24.384",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        32.258,
        27.686
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "32.258",
        "y": "27.686",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        29.845,
        24.384
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "29.845",
        "y": "24.384",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        31.115,
        24.384
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "31.115",
        "y": "24.384",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.909,
        24.13
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.909",
        "y": "24.13",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.83,
        24.13
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "36.83",
        "y": "24.13",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.83,
        22.86
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "36.83",
        "y": "22.86",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.83,
        21.59
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "36.83",
        "y": "21.59",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        38.1,
        21.59
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "38.1",
        "y": "21.59",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        39.37,
        21.59
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "39.37",
        "y": "21.59",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        40.64,
        21.59
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "40.64",
        "y": "21.59",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        24.892,
        26.543
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "24.892",
        "y": "26.543",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        24.892,
        25.4
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "24.892",
        "y": "25.4",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        29.21,
        26.67
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "29.21",
        "y": "26.67",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        30.734,
        26.67
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "30.734",
        "y": "26.67",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        32.258,
        26.67
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "32.258",
        "y": "26.67",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        34.671,
        23.114
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "34.671",
        "y": "23.114",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        35.56,
        26.67
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "35.56",
        "y": "26.67",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        35.56,
        28.0035
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "35.56",
        "y": "28.0035",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.83,
        26.67
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "36.83",
        "y": "26.67",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.83,
        27.94
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "36.83",
        "y": "27.94",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.83,
        29.21
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "36.83",
        "y": "29.21",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        38.1,
        29.21
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "38.1",
        "y": "29.21",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        39.37,
        29.21
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "39.37",
        "y": "29.21",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        40.64,
        29.21
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "40.64",
        "y": "29.21",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        10.414,
        35.56
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "10.414",
        "y": "35.56",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        10.414,
        39.497
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "10.414",
        "y": "39.497",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.985,
        9.398
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "6.985",
        "y": "9.398",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        1.27,
        6.35
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "1.27",
        "y": "6.35",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.987,
        11.176
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "22.987",
        "y": "11.176",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        24.638,
        11.176
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "24.638",
        "y": "11.176",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        17.653,
        15.367
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "17.653",
        "y": "15.367",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        18.923,
        16.637
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "18.923",
        "y": "16.637",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.193,
        17.907
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.193",
        "y": "17.907",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.86,
        19.05
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "22.86",
        "y": "19.05",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        19.304,
        12.446
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "19.304",
        "y": "12.446",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.574,
        13.716
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.574",
        "y": "13.716",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.86,
        15.621
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "22.86",
        "y": "15.621",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.86,
        21.59
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "22.86",
        "y": "21.59",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        24.765,
        15.621
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "24.765",
        "y": "15.621",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        32.512,
        19.177
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "32.512",
        "y": "19.177",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.274,
        17.399
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.274",
        "y": "17.399",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.274,
        15.621
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.274",
        "y": "15.621",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        7.366,
        3.937
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "7.366",
        "y": "3.937",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        2.286,
        11.557
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "2.286",
        "y": "11.557",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.985,
        15.875
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "6.985",
        "y": "15.875",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.32,
        2.54
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.32",
        "y": "2.54",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        7.62,
        1.27
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "7.62",
        "y": "1.27",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        11.303,
        4.064
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "11.303",
        "y": "4.064",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        13.97,
        7.62
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "13.97",
        "y": "7.62",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        42.545,
        14.859
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "42.545",
        "y": "14.859",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        9.525,
        13.208
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "9.525",
        "y": "13.208",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        9.271,
        15.875
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "9.271",
        "y": "15.875",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        12.7,
        39.497
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "12.7",
        "y": "39.497",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        15.24,
        39.497
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "15.24",
        "y": "39.497",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        11.43,
        36.83
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "11.43",
        "y": "36.83",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        15.5575,
        36.83
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "15.5575",
        "y": "36.83",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.86,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "22.86",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.86,
        36.83
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "22.86",
        "y": "36.83",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        27.94,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "27.94",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        27.94,
        32.004
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "27.94",
        "y": "32.004",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        30.48,
        35.56
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "30.48",
        "y": "35.56",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        35.56,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "35.56",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        35.56,
        36.83
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "35.56",
        "y": "36.83",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.02,
        35.56
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.02",
        "y": "35.56",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        21.59,
        25.4
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "21.59",
        "y": "25.4",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.32,
        22.86
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.32",
        "y": "22.86",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        17.78,
        25.4
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "17.78",
        "y": "25.4",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        17.78,
        22.86
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "17.78",
        "y": "22.86",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        17.78,
        20.32
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "17.78",
        "y": "20.32",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        17.78,
        17.78
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "17.78",
        "y": "17.78",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        15.24,
        20.32
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "15.24",
        "y": "20.32",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.35,
        22.86
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "6.35",
        "y": "22.86",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        10.16,
        30.48
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "10.16",
        "y": "30.48",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        16.51,
        26.67
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "16.51",
        "y": "26.67",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        16.51,
        30.48
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "16.51",
        "y": "30.48",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        16.51,
        33.02
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "16.51",
        "y": "33.02",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.35,
        27.94
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "6.35",
        "y": "27.94",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.35,
        30.48
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "6.35",
        "y": "30.48",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.35,
        35.56
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "6.35",
        "y": "35.56",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        10.16,
        41.91
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "10.16",
        "y": "41.91",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        7.62,
        41.91
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "7.62",
        "y": "41.91",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        21.59,
        33.02
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "21.59",
        "y": "33.02",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.32,
        36.83
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.32",
        "y": "36.83",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        35.56,
        20.32
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "35.56",
        "y": "20.32",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.83,
        20.32
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "36.83",
        "y": "20.32",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        38.1,
        12.7
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "38.1",
        "y": "12.7",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.02,
        3.81
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.02",
        "y": "3.81",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        30.48,
        3.81
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "30.48",
        "y": "3.81",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        27.94,
        3.81
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "27.94",
        "y": "3.81",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.4,
        3.81
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "25.4",
        "y": "3.81",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.86,
        2.54
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "22.86",
        "y": "2.54",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.4,
        6.35
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "25.4",
        "y": "6.35",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        27.94,
        6.35
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "27.94",
        "y": "6.35",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        30.48,
        10.16
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "30.48",
        "y": "10.16",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.86,
        5.715
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "22.86",
        "y": "5.715",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.02,
        8.89
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.02",
        "y": "8.89",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.02,
        12.319
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.02",
        "y": "12.319",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.35,
        33.02
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "6.35",
        "y": "33.02",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        30.48,
        6.35
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "30.48",
        "y": "6.35",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.02,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.02",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        30.48,
        32.766
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "30.48",
        "y": "32.766",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.02,
        6.35
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.02",
        "y": "6.35",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        10.16,
        1.27
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "10.16",
        "y": "1.27",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        35.179,
        3.175
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "35.179",
        "y": "3.175",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        17.78,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "17.78",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.32,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.32",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.4,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "25.4",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.4,
        36.83
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "25.4",
        "y": "36.83",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        30.48,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "30.48",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.274,
        14.224
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.274",
        "y": "14.224",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.32,
        20.32
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.32",
        "y": "20.32",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        16.51,
        14.097
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "16.51",
        "y": "14.097",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.35,
        24.13
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "6.35",
        "y": "24.13",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        35.56,
        34.29
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "35.56",
        "y": "34.29",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        34.29,
        33.02
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "34.29",
        "y": "33.02",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.02,
        31.75
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.02",
        "y": "31.75",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        35.179,
        29.464
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "35.179",
        "y": "29.464",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.703,
        32.258
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "36.703",
        "y": "32.258",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        38.1,
        39.37
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "38.1",
        "y": "39.37",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        38.1,
        36.83
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "38.1",
        "y": "36.83",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        33.02,
        29.21
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "33.02",
        "y": "29.21",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.019,
        32.4485
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "25.019",
        "y": "32.4485",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        12.7,
        30.48
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "12.7",
        "y": "30.48",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        12.954,
        37.465
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "12.954",
        "y": "37.465",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.32,
        33.02
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.32",
        "y": "33.02",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        17.399,
        7.239
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "17.399",
        "y": "7.239",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.043,
        9.144
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "20.043",
        "y": "9.144",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        10.668,
        9.271
      ],
      "diameter": 0.3,
      "source": {
        "signal": "GND",
        "x": "10.668",
        "y": "9.271",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        7.366,
        39.751
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SCL/SCK",
        "x": "7.366",
        "y": "39.751",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        15.494,
        5.08
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SCL/SCK",
        "x": "15.494",
        "y": "5.08",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.574,
        5.08
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SCL/SCK",
        "x": "20.574",
        "y": "5.08",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.019,
        34.163
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SCL/SCK",
        "x": "25.019",
        "y": "34.163",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        12.7,
        32.131
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SCL/SCK",
        "x": "12.7",
        "y": "32.131",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        12.7,
        34.417
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SCL/SCK",
        "x": "12.7",
        "y": "34.417",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        18.542,
        28.829
      ],
      "diameter": 0.3,
      "source": {
        "signal": "N$5",
        "x": "18.542",
        "y": "28.829",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.32,
        31.75
      ],
      "diameter": 0.3,
      "source": {
        "signal": "N$8",
        "x": "20.32",
        "y": "31.75",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.019,
        35.306
      ],
      "diameter": 0.3,
      "source": {
        "signal": "RXD1/PICO",
        "x": "25.019",
        "y": "35.306",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        23.114,
        34.925
      ],
      "diameter": 0.3,
      "source": {
        "signal": "TXD1/POCI",
        "x": "23.114",
        "y": "34.925",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.985,
        15.113
      ],
      "diameter": 0.3,
      "source": {
        "signal": "5V",
        "x": "6.985",
        "y": "15.113",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.985,
        10.287
      ],
      "diameter": 0.3,
      "source": {
        "signal": "5V",
        "x": "6.985",
        "y": "10.287",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        20.32,
        10.287
      ],
      "diameter": 0.3,
      "source": {
        "signal": "5V",
        "x": "20.32",
        "y": "10.287",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        27.94,
        13.97
      ],
      "diameter": 0.3,
      "source": {
        "signal": "D_SEL",
        "x": "27.94",
        "y": "13.97",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        32.5,
        18.0
      ],
      "diameter": 0.3,
      "source": {
        "signal": "D+",
        "x": "32.5",
        "y": "18",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        4.995828125,
        12.911171875
      ],
      "diameter": 0.3,
      "source": {
        "signal": "D+",
        "x": "4.995828125",
        "y": "12.911171875",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        6.985,
        12.434
      ],
      "diameter": 0.3,
      "source": {
        "signal": "D-",
        "x": "6.985",
        "y": "12.434",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        32.512,
        16.51
      ],
      "diameter": 0.3,
      "source": {
        "signal": "D-",
        "x": "32.512",
        "y": "16.51",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        40.005,
        14.859
      ],
      "diameter": 0.3048,
      "source": {
        "signal": "N$1",
        "x": "40.005",
        "y": "14.859",
        "extent": "1-16",
        "drill": "0.3048"
      }
    },
    {
      "kind": "via",
      "center": [
        2.54,
        10.541
      ],
      "diameter": 0.3,
      "source": {
        "signal": "N$7",
        "x": "2.54",
        "y": "10.541",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        4.572,
        5.715
      ],
      "diameter": 0.3,
      "source": {
        "signal": "N$7",
        "x": "4.572",
        "y": "5.715",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        2.54,
        14.097
      ],
      "diameter": 0.3,
      "source": {
        "signal": "N$9",
        "x": "2.54",
        "y": "14.097",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        1.27,
        18.669
      ],
      "diameter": 0.3,
      "source": {
        "signal": "N$9",
        "x": "1.27",
        "y": "18.669",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        32.639,
        14.986
      ],
      "diameter": 0.3,
      "source": {
        "signal": "EXT_INT",
        "x": "32.639",
        "y": "14.986",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.479,
        33.401
      ],
      "diameter": 0.3,
      "source": {
        "signal": "EXT_INT",
        "x": "22.479",
        "y": "33.401",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        4.064,
        24.13
      ],
      "diameter": 0.3,
      "source": {
        "signal": "TXD2",
        "x": "4.064",
        "y": "24.13",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        10.922,
        27.686
      ],
      "diameter": 0.3,
      "source": {
        "signal": "TXD2",
        "x": "10.922",
        "y": "27.686",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        3.175,
        24.13
      ],
      "diameter": 0.3,
      "source": {
        "signal": "RXD2",
        "x": "3.175",
        "y": "24.13",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        9.652,
        27.432
      ],
      "diameter": 0.3,
      "source": {
        "signal": "RXD2",
        "x": "9.652",
        "y": "27.432",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        8.382,
        39.751
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SDA/!CS!",
        "x": "8.382",
        "y": "39.751",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        14.859,
        5.5602
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SDA/!CS!",
        "x": "14.859",
        "y": "5.5602",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        19.912540625,
        5.561540625
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SDA/!CS!",
        "x": "19.912540625",
        "y": "5.561540625",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        22.987,
        33.909
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SDA/!CS!",
        "x": "22.987",
        "y": "33.909",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        13.97,
        29.21
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SDA/!CS!",
        "x": "13.97",
        "y": "29.21",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        14.986,
        33.909
      ],
      "diameter": 0.3,
      "source": {
        "signal": "SDA/!CS!",
        "x": "14.986",
        "y": "33.909",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.005828125,
        23.100828125
      ],
      "diameter": 0.3,
      "source": {
        "signal": "!RESET!",
        "x": "25.005828125",
        "y": "23.100828125",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        27.94,
        35.56
      ],
      "diameter": 0.3,
      "source": {
        "signal": "!RESET!",
        "x": "27.94",
        "y": "35.56",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        31.75,
        12.7
      ],
      "diameter": 0.3,
      "source": {
        "signal": "PULSE",
        "x": "31.75",
        "y": "12.7",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        34.29,
        10.16
      ],
      "diameter": 0.3,
      "source": {
        "signal": "PULSE",
        "x": "34.29",
        "y": "10.16",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        36.83,
        10.16
      ],
      "diameter": 0.3,
      "source": {
        "signal": "PULSE",
        "x": "36.83",
        "y": "10.16",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        25.146,
        28.702
      ],
      "diameter": 0.3,
      "source": {
        "signal": "RTK_STAT",
        "x": "25.146",
        "y": "28.702",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        40.64,
        38.1
      ],
      "diameter": 0.3,
      "source": {
        "signal": "RTK_STAT",
        "x": "40.64",
        "y": "38.1",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        41.275,
        33.02
      ],
      "diameter": 0.3,
      "source": {
        "signal": "N$19",
        "x": "41.275",
        "y": "33.02",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        13.335,
        27.559
      ],
      "diameter": 0.3,
      "source": {
        "signal": "LNA_EN",
        "x": "13.335",
        "y": "27.559",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        11.9791,
        13.208
      ],
      "diameter": 0.3,
      "source": {
        "signal": "BACKUP",
        "x": "11.9791",
        "y": "13.208",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        12.919671875,
        14.258328125
      ],
      "diameter": 0.3,
      "source": {
        "signal": "BACKUP",
        "x": "12.919671875",
        "y": "14.258328125",
        "extent": "1-16",
        "drill": "0.3"
      }
    },
    {
      "kind": "via",
      "center": [
        40.005,
        8.89
      ],
      "diameter": 0.3,
      "source": {
        "signal": "N$22",
        "x": "40.005",
        "y": "8.89",
        "extent": "1-16",
        "drill": "0.3"
      }
    }
  ]
}
```

## Sources — online

1. GNSS receiver boards.
