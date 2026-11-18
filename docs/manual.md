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
   Next arrows above or below the results to change pages.
3. If the results are empty, try a shorter query or clear the filter.
   [Browse subjects]({{ '/browse.html' | relative_url }}) lists the catalogue
   by subject and works without browser search.

## Read an entry and download files

Open the result and check the name, description, geometry scope, and sources.
A source specification describes the physical object. A dimension attributed
to a CAD file describes that saved geometry. Missing details may be marked
**Needs more information**.

Select an available preview to see it at full size. Follow the direct GitHub download link
when one is listed. The companion describes the supplied file, its references,
and any documented adaptation instructions.

## Help improve the catalogue

Use the [contribution guide]({{ '/contributing.html' | relative_url }}) to
report an error, suggest a change, or propose a model or subject. If you want
to query the catalogue from a script or agent, see the
[agent guide]({{ '/agents.html' | relative_url }}).
