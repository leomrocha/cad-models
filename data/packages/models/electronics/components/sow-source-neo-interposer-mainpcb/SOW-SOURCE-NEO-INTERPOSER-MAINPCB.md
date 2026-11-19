# SOW SOURCE NEO INTERPOSER MAINPCB

1. **Library number:** 242.
2. **Type:** part.
3. **CAD file:** [SOW-SOURCE-NEO-INTERPOSER-MAINPCB.dwg](<SOW-SOURCE-NEO-INTERPOSER-MAINPCB.dwg>).
4. **DWG SHA-256:** `512718589217c73c60afc7e388dde3786202fd98e5c748f265460e280a2f77ab`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

1. **Geometry input record:** mainpcb-source-job.json.
2. **Input record SHA-256:** `afba8b491cec7722c3860a6422a4c07993ea038dbe840e65432157b730ce25ed`.

```json
{
  "part_id": "SOW-SOURCE-NEO-INTERPOSER-MAINPCB",
  "part_name": "NEO_WITH_INTERPOSER_BOT main_PCB_NEO_BOT physical subpart",
  "source_assembly_name": "NEO_WITH_INTERPOSER_BOT",
  "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
  "source_body_id": 10692,
  "units": "mm",
  "representation": "exact source rectangular physical subpart;6planes/8vertices/12straightedges",
  "source_faces": [
    {
      "source_face_id": 637,
      "plane_id": 12995,
      "local_origin": [
        8.000000000000007,
        0.7049999999999998,
        6.100000000000001
      ],
      "local_normal": [
        -1.0,
        0.0,
        0.0
      ],
      "assembly_origin": [
        -4.276424017640908,
        -2.1194893147006306,
        -18.564717367866084
      ],
      "assembly_normal": [
        -1.0,
        0.0,
        0.0
      ]
    },
    {
      "source_face_id": 1886,
      "plane_id": 11293,
      "local_origin": [
        -7.999999999999993,
        0.7049999999999998,
        6.100000000000001
      ],
      "local_normal": [
        0.0,
        0.0,
        -1.0
      ],
      "assembly_origin": [
        -20.276424017640906,
        -2.1194893147006306,
        -18.564717367866084
      ],
      "assembly_normal": [
        0.0,
        0.0,
        -1.0
      ]
    },
    {
      "source_face_id": 4547,
      "plane_id": 10599,
      "local_origin": [
        -7.999999999999993,
        0.7049999999999998,
        6.100000000000001
      ],
      "local_normal": [
        -1.0,
        0.0,
        0.0
      ],
      "assembly_origin": [
        -20.276424017640906,
        -2.1194893147006306,
        -18.564717367866084
      ],
      "assembly_normal": [
        -1.0,
        0.0,
        0.0
      ]
    },
    {
      "source_face_id": 6795,
      "plane_id": 1918,
      "local_origin": [
        0.0,
        0.7049999999999998,
        0.0
      ],
      "local_normal": [
        0.0,
        -1.0,
        0.0
      ],
      "assembly_origin": [
        -12.276424017640915,
        -2.1194893147006306,
        -24.664717367866086
      ],
      "assembly_normal": [
        0.0,
        -1.0,
        0.0
      ]
    },
    {
      "source_face_id": 9535,
      "plane_id": 1599,
      "local_origin": [
        0.0,
        0.0,
        0.0
      ],
      "local_normal": [
        0.0,
        -1.0,
        0.0
      ],
      "assembly_origin": [
        -12.276424017640915,
        -2.8244893147006307,
        -24.664717367866086
      ],
      "assembly_normal": [
        0.0,
        -1.0,
        0.0
      ]
    },
    {
      "source_face_id": 12085,
      "plane_id": 1650,
      "local_origin": [
        -7.999999999999993,
        0.7049999999999998,
        -6.100000000000001
      ],
      "local_normal": [
        0.0,
        0.0,
        -1.0
      ],
      "assembly_origin": [
        -20.276424017640906,
        -2.1194893147006306,
        -30.764717367866087
      ],
      "assembly_normal": [
        0.0,
        0.0,
        -1.0
      ]
    }
  ],
  "source_placement": {
    "relationship_id": 8299,
    "parent_shape_id": 5252,
    "child_shape_id": 5274,
    "child_shape_entity": "SHAPE_REPRESENTATION ( 'main_PCB_NEO_BOT', ( #11148 ), #11042 )",
    "placement": {
      "source_id": 3997,
      "frame_ids": [
        9478,
        11148
      ],
      "matrix": [
        [
          1.0,
          0.0,
          0.0,
          -12.276424017640915
        ],
        [
          0.0,
          1.0,
          0.0,
          -2.8244893147006307
        ],
        [
          0.0,
          0.0,
          1.0,
          -24.664717367866086
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
  "frame": "Native worldXYZ exactly equals source assemblyXYZ; PCB thickness along+Y; no assembly reorientation",
  "source_geometry_summary": {
    "body_id": 10692,
    "types": {
      "VECTOR": 12,
      "DIRECTION": 24,
      "CARTESIAN_POINT": 26,
      "ORIENTED_EDGE": 24,
      "LINE": 12,
      "EDGE_LOOP": 6,
      "PLANE": 6,
      "AXIS2_PLACEMENT_3D": 6,
      "VERTEX_POINT": 8,
      "EDGE_CURVE": 12,
      "FACE_OUTER_BOUND": 6,
      "ADVANCED_FACE": 6,
      "MANIFOLD_SOLID_BREP": 1,
      "CLOSED_SHELL": 1
    },
    "vertex_bounds": [
      [
        -7.999999999999993,
        8.000000000000007
      ],
      [
        0.0,
        0.7049999999999998
      ],
      [
        -6.100000000000001,
        6.100000000000001
      ]
    ]
  }
}
```

## Sources — online

1. u-blox NEO-F9P STEP — NEO_WITH_INTERPOSER_BOT source geometry.
