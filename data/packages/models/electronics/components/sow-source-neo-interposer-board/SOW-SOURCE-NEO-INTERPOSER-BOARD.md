# SOW SOURCE NEO INTERPOSER BOARD

1. **Library number:** 240.
2. **Type:** part.
3. **CAD file:** [SOW-SOURCE-NEO-INTERPOSER-BOARD.dwg](<SOW-SOURCE-NEO-INTERPOSER-BOARD.dwg>).
4. **DWG SHA-256:** `992bb6e7fd492b4e2a3626a0956e88d71a47b00e98ca04a94a108a879f8ce903`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

1. **Geometry input record:** interposer-source-job.json.
2. **Input record SHA-256:** `3037a2d21698494d19cc377eb96ca0d1e6e9992e7585787d175655be0b8b90e1`.

```json
{
  "part_id": "SOW-SOURCE-NEO-INTERPOSER-BOARD",
  "part_name": "NEO_WITH_INTERPOSER_BOT INTERPOSER_BOT physical PCB and24PINsubparts",
  "source_assembly_name": "NEO_WITH_INTERPOSER_BOT",
  "source_url": "
  "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
  "units": "mm",
  "frame": "NativeworldXYZ=sourceassemblyXYZ;alloriginalbodyplacementsretained",
  "representation": "separatenativeanalyticextrusionsoftheexactsourceconstantYphysicalparts",
  "instances": [
    {
      "source_body_id": 5136,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0907307860741096,
      "high_y": 2.404730786074109,
      "height": 1.3139999999999996,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 5136,
        "types": {
          "ORIENTED_EDGE": 384,
          "CARTESIAN_POINT": 386,
          "ADVANCED_FACE": 66,
          "VERTEX_POINT": 128,
          "DIRECTION": 396,
          "AXIS2_PLACEMENT_3D": 138,
          "PLANE": 30,
          "CIRCLE": 72,
          "CYLINDRICAL_SURFACE": 36,
          "VECTOR": 120,
          "FACE_OUTER_BOUND": 66,
          "EDGE_LOOP": 66,
          "LINE": 120,
          "EDGE_CURVE": 192,
          "CLOSED_SHELL": 1,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            -8.008281837700412,
            7.9917181622995885
          ],
          [
            1.0907307860741096,
            2.404730786074109
          ],
          [
            -12.200000000003547,
            -3.5475095083725705e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 785,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 785,
        "types": {
          "PLANE": 7,
          "VECTOR": 17,
          "CARTESIAN_POINT": 44,
          "ORIENTED_EDGE": 42,
          "ADVANCED_FACE": 9,
          "DIRECTION": 43,
          "AXIS2_PLACEMENT_3D": 13,
          "CYLINDRICAL_SURFACE": 2,
          "EDGE_LOOP": 9,
          "EDGE_CURVE": 21,
          "LINE": 17,
          "VERTEX_POINT": 14,
          "FACE_OUTER_BOUND": 9,
          "CLOSED_SHELL": 1,
          "CIRCLE": 4,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            -7.40828183770042,
            -6.608281837700411
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035476,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 15052,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 15052,
        "types": {
          "EDGE_CURVE": 21,
          "ORIENTED_EDGE": 42,
          "DIRECTION": 43,
          "AXIS2_PLACEMENT_3D": 13,
          "VECTOR": 17,
          "FACE_OUTER_BOUND": 9,
          "CARTESIAN_POINT": 44,
          "VERTEX_POINT": 14,
          "LINE": 17,
          "ADVANCED_FACE": 9,
          "PLANE": 7,
          "EDGE_LOOP": 9,
          "CIRCLE": 4,
          "MANIFOLD_SOLID_BREP": 1,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            -6.308281837700419,
            -5.5082818377004115
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.000000000003548,
            -3.539920093165172e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 5624,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 5624,
        "types": {
          "DIRECTION": 43,
          "EDGE_CURVE": 21,
          "FACE_OUTER_BOUND": 9,
          "CARTESIAN_POINT": 44,
          "AXIS2_PLACEMENT_3D": 13,
          "VERTEX_POINT": 14,
          "ORIENTED_EDGE": 42,
          "CIRCLE": 4,
          "LINE": 17,
          "VECTOR": 17,
          "PLANE": 7,
          "ADVANCED_FACE": 9,
          "EDGE_LOOP": 9,
          "CLOSED_SHELL": 1,
          "CYLINDRICAL_SURFACE": 2,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            -5.208281837700419,
            -4.408281837700411
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035478,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 262,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 262,
        "types": {
          "AXIS2_PLACEMENT_3D": 13,
          "CARTESIAN_POINT": 44,
          "DIRECTION": 43,
          "PLANE": 7,
          "VECTOR": 17,
          "VERTEX_POINT": 14,
          "ADVANCED_FACE": 9,
          "EDGE_CURVE": 21,
          "ORIENTED_EDGE": 42,
          "FACE_OUTER_BOUND": 9,
          "CIRCLE": 4,
          "LINE": 17,
          "CYLINDRICAL_SURFACE": 2,
          "EDGE_LOOP": 9,
          "MANIFOLD_SOLID_BREP": 1,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            -4.108281837700419,
            -3.3082818377004104
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035478,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 10006,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 10006,
        "types": {
          "AXIS2_PLACEMENT_3D": 13,
          "ORIENTED_EDGE": 42,
          "CARTESIAN_POINT": 44,
          "EDGE_CURVE": 21,
          "PLANE": 7,
          "DIRECTION": 43,
          "ADVANCED_FACE": 9,
          "VERTEX_POINT": 14,
          "VECTOR": 17,
          "FACE_OUTER_BOUND": 9,
          "EDGE_LOOP": 9,
          "CYLINDRICAL_SURFACE": 2,
          "LINE": 17,
          "CIRCLE": 4,
          "MANIFOLD_SOLID_BREP": 1,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            -3.0082818377004186,
            -2.20828183770041
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.000000000003548,
            -3.539920093165172e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 14999,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 14999,
        "types": {
          "DIRECTION": 43,
          "VECTOR": 17,
          "AXIS2_PLACEMENT_3D": 13,
          "CARTESIAN_POINT": 44,
          "ORIENTED_EDGE": 42,
          "LINE": 17,
          "VERTEX_POINT": 14,
          "CYLINDRICAL_SURFACE": 2,
          "FACE_OUTER_BOUND": 9,
          "EDGE_LOOP": 9,
          "ADVANCED_FACE": 9,
          "EDGE_CURVE": 21,
          "MANIFOLD_SOLID_BREP": 1,
          "CIRCLE": 4,
          "PLANE": 7,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            -0.008281837700418428,
            0.7917181622995899
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035478,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 1272,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 1272,
        "types": {
          "PLANE": 7,
          "FACE_OUTER_BOUND": 9,
          "ADVANCED_FACE": 9,
          "CARTESIAN_POINT": 44,
          "ORIENTED_EDGE": 42,
          "LINE": 17,
          "VECTOR": 17,
          "VERTEX_POINT": 14,
          "EDGE_CURVE": 21,
          "AXIS2_PLACEMENT_3D": 13,
          "DIRECTION": 43,
          "EDGE_LOOP": 9,
          "CIRCLE": 4,
          "MANIFOLD_SOLID_BREP": 1,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            1.091718162299582,
            1.8917181622995902
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035476,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 5099,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 5099,
        "types": {
          "AXIS2_PLACEMENT_3D": 13,
          "DIRECTION": 43,
          "ORIENTED_EDGE": 42,
          "CARTESIAN_POINT": 44,
          "LINE": 17,
          "VECTOR": 17,
          "VERTEX_POINT": 14,
          "EDGE_LOOP": 9,
          "ADVANCED_FACE": 9,
          "CIRCLE": 4,
          "EDGE_CURVE": 21,
          "FACE_OUTER_BOUND": 9,
          "PLANE": 7,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            2.191718162299582,
            2.9917181622995903
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035476,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 6249,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 6249,
        "types": {
          "CARTESIAN_POINT": 44,
          "DIRECTION": 43,
          "VERTEX_POINT": 14,
          "FACE_OUTER_BOUND": 9,
          "ORIENTED_EDGE": 42,
          "EDGE_LOOP": 9,
          "AXIS2_PLACEMENT_3D": 13,
          "VECTOR": 17,
          "LINE": 17,
          "PLANE": 7,
          "EDGE_CURVE": 21,
          "ADVANCED_FACE": 9,
          "CIRCLE": 4,
          "CYLINDRICAL_SURFACE": 2,
          "MANIFOLD_SOLID_BREP": 1,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            3.2917181622995835,
            4.091718162299592
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035476,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 2354,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 2354,
        "types": {
          "VECTOR": 17,
          "AXIS2_PLACEMENT_3D": 13,
          "EDGE_CURVE": 21,
          "CARTESIAN_POINT": 44,
          "DIRECTION": 43,
          "LINE": 17,
          "ORIENTED_EDGE": 42,
          "FACE_OUTER_BOUND": 9,
          "CIRCLE": 4,
          "PLANE": 7,
          "VERTEX_POINT": 14,
          "ADVANCED_FACE": 9,
          "EDGE_LOOP": 9,
          "CYLINDRICAL_SURFACE": 2,
          "MANIFOLD_SOLID_BREP": 1,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            4.391718162299582,
            5.1917181622995905
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035476,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 7900,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 7900,
        "types": {
          "CARTESIAN_POINT": 44,
          "DIRECTION": 43,
          "VECTOR": 17,
          "ORIENTED_EDGE": 42,
          "EDGE_CURVE": 21,
          "VERTEX_POINT": 14,
          "EDGE_LOOP": 9,
          "AXIS2_PLACEMENT_3D": 13,
          "LINE": 17,
          "CIRCLE": 4,
          "CYLINDRICAL_SURFACE": 2,
          "FACE_OUTER_BOUND": 9,
          "PLANE": 7,
          "CLOSED_SHELL": 1,
          "ADVANCED_FACE": 9,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            5.491718162299584,
            6.291718162299592
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035472,
            -3.5392695718616807e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 6291,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 6291,
        "types": {
          "DIRECTION": 43,
          "CARTESIAN_POINT": 44,
          "ORIENTED_EDGE": 42,
          "VECTOR": 17,
          "VERTEX_POINT": 14,
          "EDGE_LOOP": 9,
          "PLANE": 7,
          "ADVANCED_FACE": 9,
          "LINE": 17,
          "FACE_OUTER_BOUND": 9,
          "AXIS2_PLACEMENT_3D": 13,
          "EDGE_CURVE": 21,
          "CLOSED_SHELL": 1,
          "MANIFOLD_SOLID_BREP": 1,
          "CIRCLE": 4,
          "CYLINDRICAL_SURFACE": 2
        },
        "vertex_bounds": [
          [
            6.591718162299584,
            7.3917181622995916
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -1.0000000000035476,
            -3.539703252730675e-12
          ]
        ]
      }
    },
    {
      "source_body_id": 14527,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 14527,
        "types": {
          "DIRECTION": 43,
          "LINE": 17,
          "VECTOR": 17,
          "PLANE": 7,
          "VERTEX_POINT": 14,
          "ORIENTED_EDGE": 42,
          "ADVANCED_FACE": 9,
          "CARTESIAN_POINT": 44,
          "FACE_OUTER_BOUND": 9,
          "AXIS2_PLACEMENT_3D": 13,
          "EDGE_CURVE": 21,
          "EDGE_LOOP": 9,
          "CYLINDRICAL_SURFACE": 2,
          "CIRCLE": 4,
          "MANIFOLD_SOLID_BREP": 1,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            -7.408281837700412,
            -6.608281837700403
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003552,
            -11.200000000003543
          ]
        ]
      }
    },
    {
      "source_body_id": 3957,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 3957,
        "types": {
          "VECTOR": 17,
          "CARTESIAN_POINT": 44,
          "VERTEX_POINT": 14,
          "PLANE": 7,
          "DIRECTION": 43,
          "AXIS2_PLACEMENT_3D": 13,
          "ORIENTED_EDGE": 42,
          "FACE_OUTER_BOUND": 9,
          "EDGE_LOOP": 9,
          "EDGE_CURVE": 21,
          "CIRCLE": 4,
          "ADVANCED_FACE": 9,
          "LINE": 17,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            -6.308281837700412,
            -5.508281837700404
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    },
    {
      "source_body_id": 3510,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 3510,
        "types": {
          "LINE": 17,
          "VECTOR": 17,
          "EDGE_CURVE": 21,
          "ORIENTED_EDGE": 42,
          "CARTESIAN_POINT": 44,
          "PLANE": 7,
          "DIRECTION": 43,
          "VERTEX_POINT": 14,
          "AXIS2_PLACEMENT_3D": 13,
          "EDGE_LOOP": 9,
          "FACE_OUTER_BOUND": 9,
          "ADVANCED_FACE": 9,
          "CIRCLE": 4,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            -5.208281837700412,
            -4.408281837700404
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003554,
            -11.200000000003545
          ]
        ]
      }
    },
    {
      "source_body_id": 10659,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 10659,
        "types": {
          "EDGE_CURVE": 21,
          "AXIS2_PLACEMENT_3D": 13,
          "DIRECTION": 43,
          "PLANE": 7,
          "CARTESIAN_POINT": 44,
          "ORIENTED_EDGE": 42,
          "FACE_OUTER_BOUND": 9,
          "VECTOR": 17,
          "VERTEX_POINT": 14,
          "ADVANCED_FACE": 9,
          "EDGE_LOOP": 9,
          "LINE": 17,
          "CIRCLE": 4,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            -4.108281837700411,
            -3.308281837700403
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    },
    {
      "source_body_id": 7804,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 7804,
        "types": {
          "VECTOR": 17,
          "CYLINDRICAL_SURFACE": 2,
          "DIRECTION": 43,
          "AXIS2_PLACEMENT_3D": 13,
          "PLANE": 7,
          "ORIENTED_EDGE": 42,
          "CARTESIAN_POINT": 44,
          "ADVANCED_FACE": 9,
          "EDGE_CURVE": 21,
          "LINE": 17,
          "EDGE_LOOP": 9,
          "FACE_OUTER_BOUND": 9,
          "VERTEX_POINT": 14,
          "MANIFOLD_SOLID_BREP": 1,
          "CIRCLE": 4,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            -3.008281837700409,
            -2.2082818377004005
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    },
    {
      "source_body_id": 13900,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 13900,
        "types": {
          "DIRECTION": 43,
          "CARTESIAN_POINT": 44,
          "CIRCLE": 4,
          "ORIENTED_EDGE": 42,
          "EDGE_LOOP": 9,
          "LINE": 17,
          "VERTEX_POINT": 14,
          "FACE_OUTER_BOUND": 9,
          "ADVANCED_FACE": 9,
          "VECTOR": 17,
          "PLANE": 7,
          "EDGE_CURVE": 21,
          "AXIS2_PLACEMENT_3D": 13,
          "MANIFOLD_SOLID_BREP": 1,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            -0.008281837700410515,
            0.7917181622995977
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    },
    {
      "source_body_id": 1896,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 1896,
        "types": {
          "CARTESIAN_POINT": 44,
          "DIRECTION": 43,
          "VECTOR": 17,
          "EDGE_CURVE": 21,
          "ORIENTED_EDGE": 42,
          "LINE": 17,
          "ADVANCED_FACE": 9,
          "PLANE": 7,
          "AXIS2_PLACEMENT_3D": 13,
          "VERTEX_POINT": 14,
          "EDGE_LOOP": 9,
          "CYLINDRICAL_SURFACE": 2,
          "FACE_OUTER_BOUND": 9,
          "CIRCLE": 4,
          "MANIFOLD_SOLID_BREP": 1,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            1.0917181622995888,
            1.891718162299597
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003554,
            -11.200000000003545
          ]
        ]
      }
    },
    {
      "source_body_id": 12766,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 12766,
        "types": {
          "CARTESIAN_POINT": 44,
          "VERTEX_POINT": 14,
          "AXIS2_PLACEMENT_3D": 13,
          "DIRECTION": 43,
          "ADVANCED_FACE": 9,
          "EDGE_CURVE": 21,
          "ORIENTED_EDGE": 42,
          "LINE": 17,
          "VECTOR": 17,
          "EDGE_LOOP": 9,
          "FACE_OUTER_BOUND": 9,
          "CIRCLE": 4,
          "PLANE": 7,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            2.191718162299589,
            2.9917181622995974
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    },
    {
      "source_body_id": 2863,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 2863,
        "types": {
          "ORIENTED_EDGE": 42,
          "CARTESIAN_POINT": 44,
          "AXIS2_PLACEMENT_3D": 13,
          "VERTEX_POINT": 14,
          "DIRECTION": 43,
          "VECTOR": 17,
          "EDGE_LOOP": 9,
          "LINE": 17,
          "ADVANCED_FACE": 9,
          "EDGE_CURVE": 21,
          "PLANE": 7,
          "FACE_OUTER_BOUND": 9,
          "CIRCLE": 4,
          "MANIFOLD_SOLID_BREP": 1,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            3.291718162299591,
            4.0917181622996
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    },
    {
      "source_body_id": 114,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 114,
        "types": {
          "VECTOR": 17,
          "LINE": 17,
          "PLANE": 7,
          "VERTEX_POINT": 14,
          "CARTESIAN_POINT": 44,
          "EDGE_CURVE": 21,
          "EDGE_LOOP": 9,
          "DIRECTION": 43,
          "ORIENTED_EDGE": 42,
          "AXIS2_PLACEMENT_3D": 13,
          "CYLINDRICAL_SURFACE": 2,
          "FACE_OUTER_BOUND": 9,
          "ADVANCED_FACE": 9,
          "MANIFOLD_SOLID_BREP": 1,
          "CIRCLE": 4,
          "CLOSED_SHELL": 1
        },
        "vertex_bounds": [
          [
            4.3917181622995916,
            5.191718162299599
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    },
    {
      "source_body_id": 3561,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 3561,
        "types": {
          "CIRCLE": 4,
          "CARTESIAN_POINT": 44,
          "VERTEX_POINT": 14,
          "EDGE_CURVE": 21,
          "DIRECTION": 43,
          "ORIENTED_EDGE": 42,
          "EDGE_LOOP": 9,
          "VECTOR": 17,
          "ADVANCED_FACE": 9,
          "AXIS2_PLACEMENT_3D": 13,
          "LINE": 17,
          "PLANE": 7,
          "FACE_OUTER_BOUND": 9,
          "CYLINDRICAL_SURFACE": 2,
          "CLOSED_SHELL": 1,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            5.49171816229959,
            6.291718162299598
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    },
    {
      "source_body_id": 12257,
      "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
      "units": "mm",
      "frame": "source localXYZ;constructioncanonical[x,-z,y]rotatesX(-90deg)toexactsourceXYZ",
      "low_y": 1.0807307860741096,
      "high_y": 1.0907307860741096,
      "height": 0.010000000000000009,
      "source_placement": {
        "relationship_id": 10709,
        "parent_shape_id": 5252,
        "child_shape_id": 10378,
        "child_shape_entity": "SHAPE_REPRESENTATION ( 'INTERPOSER_BOT', ( #11148 ), #8980 )",
        "placement": {
          "source_id": 13295,
          "frame_ids": [
            13517,
            11148
          ],
          "matrix": [
            [
              1.0,
              0.0,
              0.0,
              -12.268142179940495
            ],
            [
              0.0,
              1.0,
              0.0,
              -5.229220100774739
            ],
            [
              0.0,
              0.0,
              1.0,
              -18.564717367862542
            ],
            [
              0.0,
              0.0,
              0.0,
              1.0
            ]
          ]
        }
      },
      "source_geometry_summary": {
        "body_id": 12257,
        "types": {
          "ORIENTED_EDGE": 42,
          "VECTOR": 17,
          "DIRECTION": 43,
          "CLOSED_SHELL": 1,
          "FACE_OUTER_BOUND": 9,
          "AXIS2_PLACEMENT_3D": 13,
          "ADVANCED_FACE": 9,
          "CARTESIAN_POINT": 44,
          "LINE": 17,
          "VERTEX_POINT": 14,
          "EDGE_LOOP": 9,
          "EDGE_CURVE": 21,
          "CYLINDRICAL_SURFACE": 2,
          "PLANE": 7,
          "CIRCLE": 4,
          "MANIFOLD_SOLID_BREP": 1
        },
        "vertex_bounds": [
          [
            6.59171816229959,
            7.391718162299599
          ],
          [
            1.0807307860741096,
            1.0907307860741096
          ],
          [
            -12.200000000003556,
            -11.200000000003547
          ]
        ]
      }
    }
  ]
}
```

## Sources — online

1. u-blox NEO-F9P STEP — NEO_WITH_INTERPOSER_BOT source geometry.
