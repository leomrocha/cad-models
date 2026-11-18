# Clevis joint, plain washer and tube-profile validation

## Model files

| Local draft | Native file | Design and checked features |
| --- | --- | --- |
| Fork body | [body.blend](models/body.blend) | Original 30 × 20 mm base, 4 mm thick, overall height 22 mm, two 4 mm ears and a 6.4 mm common bore. |
| Pivot pin | [pin.blend](models/pin.blend) | Ø6 × 24 mm cylindrical pin with a Y-axis pivot. |
| Spacing ring | [spacer.blend](models/spacer.blend) | Ø10 × 2 mm ring, 6.4 mm through bore. |
| Joint | [joint.blend](models/joint.blend) | One fork, one pin and two occurrences of the same ring mesh. Ring centres are at Y −5 and +5 mm. The pivot axis lies at Z 15 mm. |
| Nominal plain washer | [plain-washer-10p5-20-2.step](models/plain-washer-10p5-20-2.step) | Independent analytic ring with a 10.5 mm bore, 20 mm outside diameter and 2 mm axial thickness, base at Z 0. The STEP readback verifies radii, bounds, solid count and volume. |
| Rectangular tube outline | [tube-profile-organised.dxf](models/tube-profile-organised.dxf) | Navigation repair of the [original catalogue fixture](../../docs/downloads/tube-profile.dxf). Outer and inner contours have individually selectable named layers and identity strings. |

The clevis is a purpose-designed navigation example. The retained bounds and dimensions are original inputs. The six intake records are local drafts. Physical materials and standard designations are unknown. Colours differentiate objects for inspection.

## Assembly views

![Complete clevis joint, isometric](../../data/previews/model-navigation/joint-iso.png)

![View down the assembly Z axis](../../data/previews/model-navigation/joint-top.png)

![Matched isometric camera, structure collection hidden](../../data/previews/model-navigation/joint-pivot-spacers.png)

Separate isometric and axis-facing views of each clevis part are listed in its draft. To reproduce the views, use the Blender runner below.

## Existing public model repair

Before repair, both closed tube contours belonged to layer 0. The original document supplied no readable per-entity identity. The 40 × 20 mm outer profile and the 36 × 16 mm opening uniquely identify the two contours in this fixture. The repair assigns separate native layers and entity extended data. The reopened geometry check compares all polyline points, widths, bulges, normals, elevations, closed flags and drawing units. The original SHA-256 is recorded in the [original companion](../../docs/downloads/tube-profile.md). A duplicated contour makes the proposed assignment ambiguous and stops the write. A second application produces the same assignments.

![Original unclassified contours](../../data/previews/model-navigation/tube-before.png)

![Reopened, two independently selectable layers](../../data/previews/model-navigation/tube-after.png)

## Run the validation

Use this directory as the working directory. Blender 5.0.1 reads the native parts. The separate Python runners use ezdxf, Pillow and CadQuery. Set NAVIGATION_SKILL and FORMAT_SKILL to the selected local skill directories. Catalogue tools run against a new dataset built under the existing checkout's ignored work area. The checked-in product catalogue and its published dataset keep their existing contents.

```sh
blender -b --factory-startup --disable-autoexec --python-exit-code 1 --python clevis.py -- check
python tube_repair.py
python washer.py
python adversarial.py "$NAVIGATION_SKILL" "$FORMAT_SKILL"
python catalogue_check.py
```

1. The [reopened joint inventory](results/joint-reopened.json) records object names, stable IDs, parents, roles, groups, tags, display colours and coordinates. The two rings share geometry. The Blender check selects the right ring from its ID, hides it, confirms the left ring remains visible, and restores the view.
2. The [adversarial receipt](results/verification.json) records seven individually corrupted native derivatives, each reopened by Blender before comparison. The receipt also records a two-level DXF block fixture with inherited and explicit colours, off-layer visibility and an STL request requiring physical material.
3. The [catalogue receipt](results/catalogue.json) records the draft part and assembly searches on SQLite and DuckDB. All six draft manifests pass the catalogue intake checker. Model hashes and embedded-part dependencies resolve under this checkout.
4. The [washer receipt](results/washer.json) records independent STEP file readback. Its grain, alloy, finish and applicable standard are unspecified.
5. The joint and parts were modeled specifically for this local suite. Search of the existing catalogue for clevis returned no records. Draft identifiers are scoped to this validation dataset; the maintainer assigns final catalogue IDs.
