THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# J Kelly carrier upright

1. **Library number:** 189.
2. **Type:** part.
3. **CAD file:** [p22kjr-j-kelly-carrier-frame-upright.dwg](<p22kjr-j-kelly-carrier-frame-upright.dwg>).
4. **DWG SHA-256:** `bc17d38867c7063f4dba4727fa8257ef9978d584011cbf46869af0bf48987688`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** J Kelly carrier upright — P22KJR.

**Design status:** Discussion nominal hollow-section reference.

## Technical specification

Status: Discussion proposal. Units: mm. Route:Structural S discussion variant. Quantity: 4 per J controller pair. Assembly/reference family:P22Kelly. Repeated identical pieces use instances.

### Geometry, datum and interfaces

Proposed 20×20×2 steel box tube 188 long, Z 480…668. Left Y 177…197, right mirrored; centres X−137/77. Outer face Y 197 contacts carrier inner face 197. TwoØ6.6 cross bores axis Y at Z 490/658 match carrier frame holes; compression sleeve P22CT14 spans16 mm internal tube gap. At Z 520 one further bore joins raised rail through P22SP7 gap spacer. Tube lowest 480 stays 9 above expanded crown 471; tray outer 165 to post inner 177 gap 12. Four identical tube instances per controller pair. Rail connection bore placement is separate from carrier end holes.

### Construction and dimensional check

Cut, turn or form the stated proposed shape. Deburr edges and inspect the named hole axes, end faces and mating contacts before assembly. Source component interfaces retain their source labels.

### Rail-bolt carrier exit — correction proposal

At Z = 520 mm, the post's existing Ø6.6 mm rail-joint bore aligns with a new Ø6.6 mm exit in the 3 mm P22KJ carrier. The bolt clamps the 40 mm rail, 7 mm gap spacer, 20 mm post and 3 mm carrier, giving 70 mm grip before washers. Both side assemblies use X = −137/77 mm; right-side Y coordinates mirror the left. The carrier access-hole proposal gives the finite stack, hardware assumptions and assembly sequence.


### Source-backed clamp cross-reference

The current P22KJ source-limit proposal uses M6×85 through the70 mm rail/spacer/post/carrier grip at Z520, with two carrier access holes. Each post retains its three16 mm P22CT14 sleeves and the rail has its separate34 mm sleeve. Both side post X axes remain−137/77; right mirrors Y. Four rail clamps use4 bolts,8 washers and4 nuts; the separate eight carrier-end clamps retain their own grip23 mm.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed hollow tube body | PASS | [1, 1, 1, 1] | count |
| Section and cut-length vertex bounds | PASS | [[-10.0, 10.0], [-10.0, 10.0], [0.0, 188.0]] | mm |
| Nominal inner and outer corner radii | PASS | [2.0, 4.0] | mm |
| Source transverse bore axes | PASS | [[0.0, 10.0], [0.0, 40.0], [0.0, 178.0]] | mm |

## Sources — online

1. source review r02.
2. source review r02.
3. Kelly KLS-N wiring diagram, §3.2.2, p.14.
4. Square steel tube stock family — supplier reference.
5. Weldable steel plate stock family — supplier reference.
6. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.
