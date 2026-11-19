---
layout: default
title: Catalogue user guide
permalink: /manual.html
---

## Find a model

1. Open [Search]({{ '/' | relative_url }}) and enter a part number, a designation,
   or a few keywords. Try `LS-PS310K`, `ISO 4017`, or `rectangular tube`.
2. Choose **SQLite** or **DuckDB with Parquet**. Both engines search the same
   catalogue. To narrow results, choose a filter and enter a value such as
   `brick` for **Material**. Select **Needs more information** to find flagged
   entries. Click an existing tag to apply it directly. Use the Previous and
   Next arrows above or below the results to change pages. **Models per page**
   defaults to 20 and also offers 50 or 100.
3. To return to the full catalogue, clear the search field, select **Any**
   for the filter, and select **Search**.
   [Browse subjects]({{ '/browse.html' | relative_url }}) lists the catalogue
   by subject and works without browser search.

## Read an entry and download files

Open the result and check the name, description, geometry scope, and available files.
A source specification describes the physical object. A dimension attributed
to a CAD file describes that saved geometry. Missing details may be marked
**Needs more information**.

Select an available preview to see it at full size. Follow the direct GitHub download link
when one is listed. The companion describes the supplied file, its references,
and any documented adaptation instructions.

## Help improve the catalogue

Follow the [preview workflow]({{ '/preview-workflow.html' | relative_url }})
when contributing a model image or search thumbnail.

Use the [contribution guide]({{ '/contributing.html' | relative_url }}) to
report an error, suggest a change, or propose a model or subject. If you want
to query the catalogue from a script or agent, see the
[agent guide]({{ '/agents.html' | relative_url }}).
