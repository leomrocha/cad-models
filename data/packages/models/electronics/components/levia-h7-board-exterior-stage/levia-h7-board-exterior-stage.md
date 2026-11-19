# LEVIA-H7 board exterior — substrate and 12 external connectors

1. **Library number:** 249.
2. **Plan component:** model 22, LEVIA-H7 Rev0_1 control board.
3. **CAD file:** [Native board exterior stage](<levia-h7-board-exterior-stage.dwg>).
4. **DWG SHA-256:** `fa1cc46d5326ef9edf11cdc8d5b4454032bc9b467fc6bd8b1c5537bb983aa8c7`.
5. **State:** SAVED_REOPENED_CHECKED — whole-board installation exterior.
6. **Actual execution model:** unavailable.

## Technical specification

1. **Included hardware:** one PCB substrate, one U11 Megastar ZX-SH1.0-3PWT connector, one U21 Megastar ZX-SH1.0-3PWT connector and one USB1 HCTL HC-TYPE-C-16P-01M connector, six Megastar ZX-SH1.0-4PWT connectors (U10, U13, U18, U24, U3, U8), one ZX-SH1.0-8PWT connector (U22), and two ZX-SH1.0-6PWT connectors (U19, U20). Seven top-level roots reuse the source geometry; their nested geometry contains 272 construction-solid occurrences representing one PCB and 12 external connector units.
2. **Coordinate frame:** original LEVIA STEP root XYZ, millimetres. The native substrate retains KiCad X,−Y coordinates translated by [−123.469995, +84.350004, 0] mm. These translation values come from the KiCad source aux_axis_origin. U11 and U21 footprint centres independently match their STEP occurrence XY values within 0.000001 mm after this transform.
3. **Connector placements:** all saved source-placed connector groups are inserted at [0, 0, 0] mm with unit scale and zero additional rotation. Their original source placements remain embedded.
4. **Source planes:** the KiCad substrate thickness is 1.6 mm; the retained STEP U11 front-side mounting-origin Z is 1.595 mm. The plane difference is 0.005 mm. Each source value is preserved.
5. **Checks:** all seven root insertion matrices and metadata PASS after reopening; full native ACIS/noncommon properties and original metadata match their reused source models. All nested source-placement matrices match within 0.000000001. Save/reopen manifest and SHA-256 PASS. Both owned documents closed; pre-existing documents preserved.
6. **Views:** XY, XZ, YZ and isometric boundary drawings inspected. 3,066 unsupported trim edges are represented by their native endpoint points.

## References — library

1. [PCB substrate — library 229](<../sow-brain-c02-pcb/SOW-BRAIN-C02-PCB.md>), quantity 1.
2. [U11 connector — library 222](<../../../assemblies/reusable/subassemblies/levia-u11-source-placed-complete-connector/LEVIA-U11-source-placed-complete-connector.md>), quantity 1.
3. [U21 connector — library 223](<../../../assemblies/reusable/subassemblies/levia-u21-source-placed-complete-connector/LEVIA-U21-source-placed-complete-connector.md>), quantity 1.
4. [USB1 connector — library 224](<../../../assemblies/reusable/subassemblies/levia-usb1-source-placed-complete-connector/LEVIA-USB1-source-placed-complete-connector.md>), quantity 1.
5. [Isometric boundary drawing](<levia-h7-board-exterior-stage-isometric.png>).
6. [Top boundary drawing](<levia-h7-board-exterior-stage-XY.png>).

## Sources — online

1. LEVIA-H7 source repository, retained Rev0_1 KiCad design and STEP assembly: board outline, thickness, export origin, named connectors and original placements.

## Installation substrate drawing

1. **Drawing:** [Dimensioned installation substrate](<levia-h7-installation-substrate-dimensioned.png>), 4800 × 3200 pixels. Four projections reuse the saved library 229 substrate boundary in the unchanged library 249 whole-board source frame. Existing whole-board connector views remain above.
2. **Calculated CAD analytic substrate extents:** X = 39.530358 mm; Y = 39.530403 mm; Z = 1.600 mm. Bounds: X = −4.524116…35.006242 mm, Y = −4.519291…35.011112 mm, Z = 0…1.600 mm. Display curves use retained samples of 162 straight and 108 ellipse boundary curves.
3. **Source mounting-footprint references:** the original KiCad footprint name is `MountingHole_3.2mm_M3_ISO14580_Pad_TopBottom`; its source drill is Ø3.150 mm. Crosshairs identify source reference centres in the original LEVIA STEP root XYZ frame. The table records the source drill disk relative to the KiCad Edge.Cuts contour.

| Source reference | X [mm] | Y [mm] | Centre vs contour | Ø3.150 mm source drill disk vs contour |
| --- | ---: | ---: | --- | --- |
| H1 | 30.500005 | 30.575004 | Outside | Intersects outer boundary |
| H2 | 30.493005 | −0.005996 | Outside | Wholly outside |
| H3 | −0.010795 | −0.005996 | Outside | Wholly outside |
| H4 | 0.000005 | 30.500004 | Outside | Wholly outside |

4. **Source planes:** PCB Z = 0…1.600 mm; STEP front mounting-origin Z = 1.595 mm; preserved source-plane difference = 0.005 mm.
5. **Source comparison:** the retained strict native/source vertex comparison reports 22 FAIL results. The finite-boundary diagnostic places 21 of those 22 source vertices on the retained native boundary within 3.18 × 10⁻¹⁴ mm at both caps. Source perimeter vertex 43, native-substrate XY = [154.344141, −52.253091] mm, has nearest finite-boundary distance 0.007776821201906426 mm at Z = 0 and 1.600 mm; the original numerical criterion is 0.0000002 mm. The original strict receipt remains unchanged. The drawing represents the saved native substrate boundary; the H-reference table represents the original KiCad source coordinates and contour disposition.
