# Beitian BT-560 rear mounting interface reference

1. **Library number** 306.
2. **Plan job** 24, BT-560 antenna.
3. **Native drawing** [Rear mounting interface reference](<beitian-bt560-rear-mounting-interface-reference.dwg>).
4. **DWG SHA-256:** `863d5380d78c5753269d85ab09acb9a2014301ef37684c8905553a9acd9b9910`. DWG 2018, 27,891 bytes.
5. **State** SAVED_SOURCE_INTERFACE_CHECKED.
6. **Execution models** gpt-6.2-sol for source registration and package verification. The model that built the native drawing is unavailable.

## Technical specification

The interface uses the model 281 frame in millimetres. The origin is the rear housing plane on the SMA-J axis. Positive Z points toward the antenna tip.

1. **Rear housing reference** nominal Ø27.3 mm circle in the XY plane at Z = 0. The manufacturer's diameter tolerance is ±0.3 mm.
2. **Axial seal reference** 0.4 mm along the SMA-J axis. The body-side station is Z = 0. The outer seal station is Z = −0.4 mm. The manufacturer drawing identifies the two planes and the 0.4 mm span.

## Verification

1. The manufacturer drawing's rear body dimension line and library 281's rear datum use the same raster columns 683–684. The seal silhouette lies outside this line, toward negative Z.
2. The native circle diameter, plane, axis and axial span passed against the registered source. Both entities retain geometry provenance. The millimetre header and SAVE audit passed with zero dropped entities.
3. The current-record reference view was inspected. The owned document passed guarded closure.

## References

1. BT-560 exterior, library 281 (earlier revision `model-281`; [current catalogue revision](<../../../electronics/components/beitian-bt560-joined-source-skin/beitian-bt560-joined-source-skin.md>)).
2. [Rear collar and axial seal view](<beitian-bt560-rear-mounting-interface-reference.png>).

## Sources — online

1. Beitian BT-560 manufacturer drawing revision 5.53, January 2023. Source SHA-256 `27df818a9ffd3ce25bb07207d98fff6a5fa6b0e2bd512917a9cc182dd6d6e707`.
