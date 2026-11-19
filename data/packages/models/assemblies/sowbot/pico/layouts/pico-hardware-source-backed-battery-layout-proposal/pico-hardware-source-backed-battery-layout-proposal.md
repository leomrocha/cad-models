# Pico source chassis and central battery-case partial assembly

1. **State:** PARTIAL_SAVED_REOPENED_SOURCE_GEOMETRY_AND_PLACEMENTS_CHECKED.
2. **Native drawing:** [Pico source-backed partial assembly](<pico-hardware-source-backed-battery-layout-proposal.dwg>).
3. **DWG SHA-256:** `ead0b4a0aa11bf90a0deba4335f5b40662f20ac9db7baa73d001a97450b0d367`.
4. **Plan identity:** assembly 7, complete Pico Sowbot; saved partial construction stage.
5. **Actual execution model:** unavailable.

## Installed source geometry

1. **Chassis occurrence:** manufacturer-source chassis stage, SHA-256 `0c89ca8a5355edde81d26bf57032eeba9649874055d6aefea3957e1aa9d0aa2d`; installed with the identity matrix. Its checked source geometry and component placements remain recorded in its companion.
2. **Central case occurrence:** [manufacturer source central battery-case geometry](<../../../../../electronics/batteries/hiwonder-manufacturer-central-battery-case-source-stage/hiwonder-manufacturer-central-battery-case-source-stage.md>), library 284, SHA-256 `306b0bea34286d402fdd2add377ef0c95253f852d83397929358ac04606ac66d`; source solid 3036, measured 76.8 × 66.8 × 24 mm. The battery-case role follows the labeled manufacturer exploded view. The supplier's 86 × 60 × 21 mm pack reference remains separately attributed in library 248.
3. **Frame:** millimetres; X follows source Y and travel, Y follows negative source X, Z is up. The chassis companion supplies the common source-to-assembly origin.
4. **Central-case placement:** the source-to-assembly transform composes with the case's recorded inverse local transform. The installed matrix, row-major, is:

```text
 0  1  0  19.287944944981604
-1  0  0   0.07808514033535374
 0  0  1  33.84267639045569
 0  0  0   1
```

## Persistence and checks

1. **Checkpoints:** empty document, millimetre units, chassis insertion, chassis metadata, case insertion, case placement and case metadata were saved separately.
2. **Insertion recovery:** both original file requests returned response timeouts and subsequently recovered to insertion-point prompts. The completed file requests were preserved; placement stages used their subsequent inputs. Neither file request was replayed.
3. **Canonical save:** 12,261,228 bytes, AC1032 DWG; verified save and zero dropped entities PASS. The saved file hash is listed above.
4. **Fresh reopen:** original request `pico-hardware-battery-final-r1:reopen` completed and identified document 763. Exact canonical path, SHA-256 and reopened audit PASS. Both timeout histories remain retained.
5. **Geometry and placements:** two root occurrences, 193 solid occurrences and two supplemental open Mesh occurrences PASS exact source-native noncommon geometry fingerprints and all composed nested matrices. World topological vertex bounds match original source geometry within 0.000001 mm; maximum observed bound error 0.00000000000001421 mm.
6. **Appearance and cleanup:** reopened-record XY and isometric boundary views inspected PASS; 45,895 boundary edges, including 2,834 unsupported trim edges represented by endpoints. Owned documents 762 and 763 guarded closed; unrelated Start 1 preserved.
7. **Source-stage scope:** the chassis companion retains source plate 3037 as its plan-scope finding and the original spring display failure beside the supplemental open coil patches. Charger identity remains recorded in plan job 31.

## Sources — online

1. Manufacturer-linked chassis STEP, original SHA-256 `b82d132ced4c00b245f4a38b96ea3f5ccdbc8318fbf45ed12118964f4cefb65a`.
2. Hiwonder suspended tracked chassis and product-structure illustration.

## References

1. Current plan, assembly 7 and component job 30.
2. Exact recovery receipt, including original request IDs, source hashes, placement matrices, checkpoint hashes and the last observed native state.
3. Saved occurrence and checkpoint records.
4. Canonical save audit.
5. Source central-case geometry checks.

## Saved-model views

1. [Top boundary view](<pico-hardware-source-backed-battery-layout-proposal-XY.png>).
2. [Isometric boundary view](<pico-hardware-source-backed-battery-layout-proposal-isometric.png>).
3. Reopened nested geometry checks.
4. Source/world placement checks.
5. Guarded document cleanup.
