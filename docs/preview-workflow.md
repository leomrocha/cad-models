---
layout: default
title: CAD preview workflow
permalink: /preview-workflow.html
---

Use this workflow to prepare catalogue images from an existing view or the exact
CAD revision listed on the model page. Preserve the original CAD file and
source images.

## 1. Identify the model and match an existing view

1. Match the model ID, CAD path, revision, and SHA-256 against the private
   migration inventory or the catalogue record. Keep renders and original
   view assets in the private work area until reviewed.
2. Check the companion's view references and the inventory's recorded preview
   sources. Reuse a view when its provenance ties it to the same saved model
   revision and it shows the intended geometry. Use model identity and revision
   evidence alongside the filename. Keep the original image and record its path
   beside the resized derivative. Leave the preview pending when the match
   cannot be established.
3. Clear redistribution for the image and visible content before moving it
   into the catalogue asset tree. Keep an unclear or restricted image on hold
   in private staging. A catalogue record can appear without images.

## 2. Render a missing view

1. Process one native document at a time. Verify the staged file's hash
   against the inventory. Open a working copy of that exact revision as an owned
   document in the CAD application. Keep the staged original intact.
2. Use document-scoped commands on the owned document only. Leave every
   pre-existing active or open document untouched. Stop the render if the
   application cannot confirm which document it owns or targets.
3. For a 3D model, use an isometric view as the primary image. Add a second
   angle when it shows a different relevant face or interface. For a 2D drawing,
   use a plan or orthographic view perpendicular to the drawing plane and frame
   the written dimensions or geometry needed to read the view.
4. Capture the model with clear edges and enough margin to show its full extent.
   Save the original capture in private staging. Record the CAD revision, view
   orientation, application and version, and capture path. Close the owned
   document after the capture. Preserve the CAD file without view or geometry
   edits.

## 3. Prepare catalogue assets

1. Make a PNG gallery image with a maximum canvas of **640 × 480 px**. Preserve
   aspect ratio and keep the entire view visible. Make a primary thumbnail of
   at most **256 × 192 px** from the same view.
2. Save each cleared image beside the CAD file and its Markdown companion
   under `data/packages/models/`. List the image in `package_assets` and in
   `previews`. Both fields use paths relative to `data/packages/`. Use the
   same path for the view and thumbnail when the bytes are identical. Add a
   view label and plain-text alt description.

```json
{
  "previews": [
    {
      "view": "Isometric",
      "file": "models/mechanical-parts/fasteners/screws/iso-4017-m6x20/isometric-1.png",
      "thumbnail_file": "models/mechanical-parts/fasteners/screws/iso-4017-m6x20/thumbnail.png",
      "alt": "Isometric view of the mounting plate and its four mounting holes"
    }
  ]
}
```

## 4. Check the catalogue

1. Confirm that gallery images and the thumbnail open, meet their pixel limits,
   and match the documented revision and view label. Verify the source CAD file
   still has its original SHA-256.
2. Rebuild the catalogue using the repository instructions. Open the model page
   and check that the gallery shows the primary image first, with any second
   view and its label. Search for the model by ID and check that the result card
   shows the primary thumbnail and opens the matching model page.
3. Check that a record with a rights hold or missing preview still opens and
   its search card has no broken image. Confirm that private captures and
   rights-held assets are absent from the site output.

Every displayed image uses its exact `raw.githubusercontent.com` URL. The build rejects site copies, duplicate asset bytes, and image paths outside the model folder.
