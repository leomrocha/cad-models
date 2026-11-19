# skf sy20tf

1. **Library number:** 210.
2. **Type:** part.
3. **CAD file:** [skf-sy20tf.dwg](<skf-sy20tf.dwg>).
4. **DWG SHA-256:** `6ce365c13110d33a9267a35b7f383e6111c8b7edec86fcda4710548b48c21719`.
5. **Geometry preservation:** Existing saved DWG; byte-preserving repository migration.

## Technical specification

### Model

- File: SKF SY 20 TF component.
- Application: OpenCADStudio 2026.42.
- Executing model: GPT-6.1 Sol.
- Format: native 3D solids, DWG AC1032, millimetres.
- Frame: X along mounting feet, Y along shaft, Z upwards.
- Datums: mounting plane Z = 0; shaft axis X = 0, Z = 33.3 mm; bearing raceway centre Y = 0.
- Separate solids: housing, bearing inner ring, bearing outer ring, two contact seals, two metal flingers, two locking screws and grease fitting.
- Each solid carries source and reconstruction metadata under `SKF_SY20TF` XData.

### Local source originals

- SKF *SY 20 TF technical specification*, generated 2023-12-11, pages 3–5: `/tmp/opencode/out_technical-data-sheet-skf-sy-20-tf-sy-20-`.
  - SHA-256: `535dc804124556ae856efda3be2e606e5660c06b995d32738bc3401f367e0530`.
  - Source URL recorded in the component record: 
- SKF *Y-bearings and Y-bearing units*, PUB BU/P1 13728 EN, printed pages 92 and 122–123: `/tmp/opencode/out_0901d196802a2b8f_pdf_preview_medium.pdf`.
  - SHA-256: `0cfb9ebe4971bf1edeca0b3e937c268db885b8afc93c371e3f47b24556d0aa91`.

### Published dimensions represented

- Housing: length 127 mm, base width 32 mm, crown width 21 mm, overall height 64.5 mm, foot height 14 mm, shaft centre height 33.3 mm.
- Mounting slots: length 20.5 mm, width 11.5 mm, centres X = −48.5 and +48.5 mm.
- Bearing: bore diameter 20 mm, approximate inner-ring shoulder diameter 28.2 mm, inner-ring width 31 mm, locking-side face Y = −18.3 mm, opposite face Y = +12.7 mm.
- Catalogue bearing outer ring: maximum spherical diameter 47 mm and width 14 mm.
- Locking screws: nominal M6 × 0.75, socket across flats 3 mm, centres 4.5 mm from locking-side face, angular separation 120°.
- Grease fitting: nominal 1/4-28 thread, hexagon across flats 7 mm, head diameter 6.5 mm, housing location at 45° and axial offset 2 mm.
- Overall housing height uses the component-specific technical sheet's 64.5 mm. The 2013 catalogue specifies 65 mm.

### Drawing-derived geometry

- Housing front contour, shoulder transitions, lower relief and axial casting draft follow the manufacturer front and section views.
- Housing crown uses a sampled 31.2 mm radius about the shaft centre; axial draft interpolates from 32 mm at the mounting plane to 21 mm at the crown.
- Housing end opening diameter: 41.6 mm, reconstructed from the section view. The spherical bearing seat uses radius 23.5 mm.
- Outer-ring internal opening diameter: 38.6 mm, reconstructed from the bearing section.
- Seal radii: 14.1–19.3 mm; axial stations ±6.6 to ±8.0 mm. Flinger radii: 14.1–19.7 mm; axial stations ±8.0 to ±9.2 mm.
- Screw length follows the 4.1 mm radial ring wall; hexagonal socket depth is 1.5 mm. Threads use nominal cylinders.
- Grease-fitting turned profile follows the illustrated silhouette; the axial stations span radii 27–39.3 mm from the bearing axis. The tip passage diameter is 1.2 mm.
- Housing and slot curved contours use sampled polygon segments. Bearing-seat and outer-ring spherical surfaces use native sphere operations.
- The represented bearing geometry consists of its rings, contact seals, flingers and locking screws.

### Automated observations

- OCS document 49, geometry revision 4975: housing bounds X = −63.5 to +63.5 mm, Y = −16 to +16 mm, Z = 0 to 64.5 mm.
- Save and reopened drawing audits: ten 3D solids, zero errors, zero warnings, zero dropped entities.
- Reopened solid bounds are reported as zero by OCS measurement output.
- Outer-ring mesh volume before save: 7,159.821731 mm³. Analytic spherical-band volume with the constructed opening: 7,187.880216 mm³. Difference: −0.390358%. A strict equality check between these values fails.
- Reopened outer-ring mesh volume: 7,202.090918 mm³.
- All eight pre-existing component DWGs match their Git HEAD content byte-for-byte.

### Display check

- Status: DONE for visibility of the assembled component. The user-rotated view shows the arched housing, both mounting slots, bearing rings, shaft bore and grease fitting in 3D wireframe.
- Automation capture limitation: front and isometric view commands change camera state while captured pixels remain at a user-established orientation.
- Diagnostic captures with SHA-256 `5a416b987a1307c08ccd590ecdc70b74d2a923a374511b9421024aa64f190c6e`: front command and isometric command.
- The model file contains a named `SKF_Isometric` view. The active OCS document path is the SKF component DWG.

## Sources — online

1. skf sy20tf.

## Views

1. [skf sy20tf component user view](<skf-sy20tf-component-user-view.png>).

1. [skf sy20tf mounting reference](<../../../interface-references/mechanical/skf-sy20tf-mounting-reference/skf-sy20tf-mounting-reference.png>).

1. skf sy20tf stale front capture.

1. skf sy20tf stale isometric capture.
