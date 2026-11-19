# SOW BRAIN LEVIA CONNECTOR SIDES

1. **Library number:** 232.
2. **Type:** part.
3. **CAD file:** [SOW-BRAIN-LEVIA-CONNECTOR-SIDES.dwg](<SOW-BRAIN-LEVIA-CONNECTOR-SIDES.dwg>).
4. **DWG SHA-256:** `8c7747a8a62b0b85c8fa2736a4f1f1a3f1a2e93b773317921db8db084430bdb0`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

1. **Geometry input record:** source-job.json.
2. **Input record SHA-256:** `198b4d7d4ab29e24dbca447380cc1b1c4e369c931860486c24beacf253c155ec`.

```json
{
  "part_id": "SOW-BRAIN-LEVIA-CONNECTOR-SIDES",
  "part_name": "LEVIA-H7 U11/U21 Megastar ZX-SH1.0-3PWT physical connector side subparts",
  "source_configuration": "LEVIA-H7 Rev0_1 STEPassembly",
  "units": "mm",
  "representation": "Fourseparatephysicalnativeanalyticprofileextrusionsfromsourcebodies#136895/#149971withoriginalU11/U21placements",
  "frame": "NativeXYZ=originalSTEPassemblyXYZ;virtualprofileXYZ=sourceZXYinvertedbeforeplacement",
  "instances": [
    {
      "component_name": "LEVIA U11 ZX-SH1.0-3PWT physical side body#136895",
      "source_body_id": 136895
    },
    {
      "component_name": "LEVIA U21 ZX-SH1.0-3PWT physical side body#136895",
      "source_body_id": 136895
    },
    {
      "component_name": "LEVIA U11 ZX-SH1.0-3PWT physical side body#149971",
      "source_body_id": 149971
    },
    {
      "component_name": "LEVIA U21 ZX-SH1.0-3PWT physical side body#149971",
      "source_body_id": 149971
    }
  ]
}
```

## Sources — online

1. LEVIA-H7 Rev0_1 board and STEP source.
