# NEO WITH INTERPOSER BOT

1. **Library number:** 227.
2. **Type:** subassembly.
3. **CAD file:** [NEO_WITH_INTERPOSER_BOT.dwg](<NEO_WITH_INTERPOSER_BOT.dwg>).
4. **DWG SHA-256:** `eb9f56b869e9bd4409c7701bd5c2052c31d20c59ddf8f2fedba5a87c7fc63e31`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

1. **Geometry input record:** assembly-source-contract.json.
2. **Input record SHA-256:** `1c0bae4789c713593f8e61dd13f5cc1b40f3b5014f2f85b1e6d0acc971afe6d6`.

```json
{
  "source_assembly_name": "NEO_WITH_INTERPOSER_BOT",
  "source_sha256": "be35ebd8a1b4f57e0b93f239879642951560ddd67c93f60f33ff4573ef3d9ba9",
  "units": "mm",
  "frame": "NativeworldXYZexactlyretainssourceassemblyXYZ;nomodeltransformoradaptationappliedduringassembly",
  "representation": "30separatephysicalnativeSolid3Dbodies;originalsourcepartplacements",
  "input_parts": [
    {
      "prefix": "mainpcb",
      "part_id": "SOW-SOURCE-NEO-INTERPOSER-MAINPCB",
      "native_model": "
      "sha256": "512718589217c73c60afc7e388dde3786202fd98e5c748f265460e280a2f77ab",
      "physical_bodies": 1,
      "source_check_path": "
    },
    {
      "prefix": "contacts",
      "part_id": "SOW-SOURCE-NEO-INTERPOSER-CONTACTS",
      "native_model": "
      "sha256": "71fcdb08f0d09f23c940fd623b13514d3cecc5b4e9b84c1192a10eb4931c54c2",
      "physical_bodies": 3,
      "source_check_path": "
    },
    {
      "prefix": "interposer",
      "part_id": "SOW-SOURCE-NEO-INTERPOSER-BOARD",
      "native_model": "
      "sha256": "992bb6e7fd492b4e2a3626a0956e88d71a47b00e98ca04a94a108a879f8ce903",
      "physical_bodies": 25,
      "source_check_path": "
    },
    {
      "prefix": "shield",
      "part_id": "SOW-SOURCE-NEO-INTERPOSER-SHIELD",
      "native_model": "
      "sha256": "54390e78f8b45c93f7f6f66b27a8bb496e7c54596de04bcbc7fa25e3c1257940",
      "physical_bodies": 1,
      "source_check_path": "
    }
  ],
  "expected_physical_body_count": 30
}
```

## Sources — online

1. u-blox NEO-F9P STEP — NEO_WITH_INTERPOSER_BOT source geometry.

## References — local

240. [SOW SOURCE NEO INTERPOSER BOARD](<../../../../electronics/components/sow-source-neo-interposer-board/SOW-SOURCE-NEO-INTERPOSER-BOARD.md>) — library entry 240.
241. [SOW SOURCE NEO INTERPOSER CONTACTS](<../../../../electronics/components/sow-source-neo-interposer-contacts/SOW-SOURCE-NEO-INTERPOSER-CONTACTS.md>) — library entry 241.
242. [SOW SOURCE NEO INTERPOSER MAINPCB](<../../../../electronics/components/sow-source-neo-interposer-mainpcb/SOW-SOURCE-NEO-INTERPOSER-MAINPCB.md>) — library entry 242.
243. [SOW SOURCE NEO INTERPOSER SHIELD](<../../../../electronics/components/sow-source-neo-interposer-shield/SOW-SOURCE-NEO-INTERPOSER-SHIELD.md>) — library entry 243.
