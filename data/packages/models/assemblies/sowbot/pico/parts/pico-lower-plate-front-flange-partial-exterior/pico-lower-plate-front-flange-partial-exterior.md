# Pico lower plate front flange partial exterior

1. **Library number:** 263.
2. **Plan component:** model 09, Hiwonder Pico lower plate; partial front-flange stage.
3. **CAD file:** [Native flange solid](<pico-lower-plate-front-flange-partial-exterior.dwg>).
4. **DWG SHA-256:** `808b126b1a10c0e0bdac4ebf0e3516d576d43d749ab4c57cd9fe20dcbad89a35`.
5. **State:** PARTIAL_FRONT_FLANGE_SAVED_REOPENED_GEOMETRY_CHECKED.
6. **Actual construction and checking models:** unavailable.

## Technical specification

1. **Represented geometry:** one closed solid extruded from a six-segment approximation of the visible lower front flange. The detached lower plate's upward lip is matched to the lower front panel in the manufacturer drawing.
2. **Source width:** 101.58 mm, manufacturer drawing callout, extension intersections X = 838 and 1082 pixels in the original 1,200 × 1,200 pixel image.
3. **Reconstructed height:** nominal 15.863006993 mm; worst-case raster interval 13.997448276–17.781489362 mm. Vertical calibration uses the manufacturer 119.39 mm overall-height callout at Y = 426 and 712 pixels. Feature picking uses ±2 pixel inputs; per-point uncertainty is retained in the source trace.
4. **Source thickness and material claims:** 2 mm, aluminium alloy, Hiwonder's retained whole-chassis specification. The plan applies this plate thickness to the lower-plate reconstruction.
5. **Frame:** millimetres; X normal to the front face, Y transverse, Z up. Front face X = 0 mm; inside face X = 2 mm; Y = −50.79…50.79 mm; lower exposed edge Z = 0 mm.
6. **Native geometry:** 12 source-bound vertices, eight planar faces and one closed body. Calculated boundary volume 3,187.970859406 mm³. The polygonal corner approximation retains the recorded raster uncertainty.
7. **Geometry checks:** source vertices, supporting planes, outward material orientation, complete face loops, closed-edge incidence, Euler characteristic 2 and boundary volume PASS. CAD comparison length threshold 0.0000001 mm; volume threshold 0.000001 mm³.
8. **Reader recovery:** native extrusion stores straight-curve directions as complete edge displacements with parameters 0…1. The supported endpoint policy preserves these original values; independent parameter evaluation matches the native endpoints within 0.000000000000008 mm. Original reader failure and saved payload are retained in execution evidence.
9. **Persistence and views:** immediate and per-step checkpoints saved; final native save/reopen and zero dropped entities PASS. Source hashes and native payload unchanged during reader recovery. YZ/isometric views inspected. Finished owned documents 679/680 closed after persistence checks.

## Sources — online

1. Hiwonder dimensioned chassis drawing, lower front panel at image X = 838…1082, Y = 599…637 pixels; width and overall-height callouts supply calibration. Source SHA-256 `491c573b2cee469e67ff3407aebf1367b4120c96925e5324076bf4b0d5d918d3`.
2. Hiwonder suspended tracked chassis, original product specification for 2 mm aluminium-alloy plate construction and exploded lower-plate identity.

## References — library

1. [Native front-face view](<view-2.png>).
2. [Native isometric view](<view-1.png>).
