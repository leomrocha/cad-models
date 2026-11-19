THIS is a DISCUSSION IDEA DOCUMENT! things can go forward or REJECTED, there is NO ACCCEPTANCE IN THIS ITERATION AND NOTHING IS ALLOWED TO MARK AS ACCEPTED

# Splash stair top-clamp foot

1. **Library number:** 199.
2. **Type:** part.
3. **CAD file:** [p24jsft-j-splash-stair-top-clamp-foot.dwg](<p24jsft-j-splash-stair-top-clamp-foot.dwg>).
4. **DWG SHA-256:** `946c5a81a7d621082ba5b696b9cf114f243abc0b80692b37e43fbb7b26275ce4`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

**Existing component names and identifiers:** Splash stair top-clamp foot — P24JSFT.

**Design status:** Discussion construction proposal.

## Technical specification

Status: Discussion construction proposal. Units: mm. Quantity four per paired splash panels in S03T.
1. **Manufactured plate proposal:** steel 50 ×39 ×3 mm, local X −25…25, left Y 130…169,Z 540…543. Translate local X to centres−220,0,+220 and mirror Y for the right. One Ø6.5 mm hole normal Z at local X 18,Y 143. Quantity four in S03T: three left instances and right Xc−220.
2. **Calculated washer seat:** source C146 OD at most 12 gives footprint local X 12…24,Y 137…149. Edge gaps are 1 mm to X 25,37 mm to X −25,7 mm to Y 130 and 20 mm to Y 169. Hole-edge ligament toward X 25 is 25−18−3.25=3.75 mm.
3. **Contacts:** underside Z 540 contacts rail top 540. Upstand bottom Z 543 contacts the foot upper face over local X ±15,Y 166…169. Parent weld bounds Xc±15.5 fit this 50 mm blank.
4. **Separate guard-passage cuts:** the right-central and right-forward instances use P24JSFTC — central passage foot and P24JSFTF — forward passage foot. Each has its own manufactured input.
5. **Parent:** P24JSHS — stair support S03T gives actual screw length/full-form overlap, internal block and guard-fastener/tool comparisons. The parent analysis retains the 30 mm through-bolt comparison foot dimensions and its guard-material intersections.

1. **Manufactured plate proposal:** steel 50 ×39 ×3 mm, local X −25…25, left Y 130…169,Z 540…543. Translate local X to centres−220,0,+220 and mirror Y for the right. One Ø6.5 mm hole normal Z at local X 18,Y 143. Quantity four in S03T: three left instances and right Xc−220.
2. **Calculated washer seat:** source C146 OD at most 12 gives footprint local X 12…24,Y 137…149. Edge gaps are 1 mm to X 25,37 mm to X −25,7 mm to Y 130 and 20 mm to Y 169. Hole-edge ligament toward X 25 is 25−18−3.25=3.75 mm.
3. **Contacts:** underside Z 540 contacts rail top 540. Upstand bottom Z 543 contacts the foot upper face over local X ±15,Y 166…169. Parent weld bounds Xc±15.5 fit this 50 mm blank.
4. **Separate guard-passage cuts:** the right-central and right-forward instances use P24JSFTC — central passage foot and P24JSFTF — forward passage foot. Each has its own manufactured input.
5. **Parent:** P24JSHS — stair support S03T gives actual screw length/full-form overlap, internal block and guard-fastener/tool comparisons. The parent analysis retains the 30 mm through-bolt comparison foot dimensions and its guard-material intersections.

## Recorded construction checks

| Feature | Recorded result | Observed value | Unit |
|---|---|---|---|
| One closed Splash stair top-clamp foot | PASS | [1, 1, 1, 1] | count |
| Source-sheet coordinate extrema | PASS | [[-25.0, 25.0], [130.0, 169.0], [540.0, 543.0]] | mm |
| Source-sheet hole group 1 | PASS | [[18.0, 143.0]] | mm |

## Sources — online

1. Square steel tube stock family — supplier reference.
2. Weldable steel plate stock family — supplier reference.
3. Böllhoff ISO 4017 similar to DIN 933, steel 8.8, data sheet.
4. standard fastener geometry sources.
5. standard fastener geometry sources.

## References — local

90. [ISO 7089 M6 plain washer, proposed 200 HV](<../../fasteners/washers/iso7089-m6-washer-6p4x12x1p6-reference/iso7089-m6-washer-6p4x12x1p6-reference.md>) — library entry 90.
