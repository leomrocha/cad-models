# Main Sowbot layout with updated Brain

1. **Plan identity** Assembly 5, Main Sowbot, partial hardware layout proposal.
2. **Native drawing** [Main layout with updated Brain](<main-updated-brain-layout-proposal.dwg>).
3. **DWG SHA-256:** `4e67d456027df4d7b00db9276bf264122cdf3bb75711fd5044b0c3953e6eb77e`. DWG 2018, 9,321,400 bytes.
4. **Execution model** Actual identity unavailable.

## Technical specification

1. **Brain placement** The [updated Brain](<brain-avaota-source-connectors-layout-proposal.md>) is installed at root `8C1`. The placement is X = 250 mm, Y = 726 mm and Z = 250 mm with identity rotation in the saved Main frame.
2. **Other roots** One source-visible track patch group, six VariCore VC-1280Na+ photo-exterior battery instances and two ODrive v3.6 planar outline references retain their previous placements and represented geometry.
3. **Live geometry** Ten roots expand to 1,181 occurrences: 952 solids, 228 meshes and one circle. The updated Brain expands to 1,084 of those occurrences.

## Verification

1. Independent current-record comparison matched all nine other roots to their previous geometry and placements. The updated Brain and both nested 309-solid Avaota boards matched their composed assembly positions. The previous Brain handle `4A5` is erased.
2. Incremental and final SAVE receipts confirmed the geometry epoch, path, byte count, hash and zero dropped entities. The [isometric view](<../../../../images/sowbot/main-updated-brain-layout-proposal-isometric.png>) was inspected before guarded closure.

## References

1. [Ten-root occurrence BOM](<../../../../docs/sowbot/bom/main-updated-brain-occurrences.csv>).
2. [Previous Main layout proposal](<main-receiver-exterior-hardware-layout-proposal.md>).
3. Independent saved drawing check.

## Sources — online

1. Sowbot Main hardware table.
2. VariCore VC-1280Na+ battery specification.
3. ODrive controller comparison.
