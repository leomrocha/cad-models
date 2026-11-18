# Contribute to CAD Models

[Open a catalogue issue](https://github.com/leomrocha/cad-models/issues/new) or
prepare a draft pull request for a specific change. Small fixes to descriptions,
tags, citations, and links are welcome.

| Contribution | Include in the issue or draft |
|---|---|
| Bug report | Page URL or exact query, selected search engine and filters, expected result, and actual result |
| Record correction | Model ID or page, revision if listed, field to correct, and evidence |
| Improvement | Affected page or query, proposed change, and an example showing the expected result |
| New model or subject | Model name or subject, proposed category and tags, source, and any related entries |

Catalogue-wide issues can use a page or query as their reference. Contributors
who prefer a local form can run `python scripts/intake.py new bug`, substituting
`improvement`, `model`, or `subject` as needed. Save and fill the JSON draft, then
run `python scripts/intake.py check path/to/draft.json`. This checks the draft
structure. The maintainer reviews the proposed change.

## Propose a model or revision

1. Search for existing entries and variants first. Identify the object, the exact
   variant where known, and the geometry represented in the supplied file.
2. Suggest a subject, description, and useful tags. Cite the original source for
   available materials, dimensions, and standards. Record unavailable details
   as JSON `null`.
   Keep supplier and sales listing URLs out of public catalogue records and
   companions. Download links point directly to the CAD model file.
3. List reused CAD models and their exact revisions. State whether a model is
   linked, embedded, or used as a source for derived geometry. Describe any
   documented editable dimensions or separate adaptation recipe in the companion.
4. Start with metadata and citations. Confirm redistribution rights before
   attaching CAD files, derivatives, source documents, or preview images to a
   public issue or pull request.
5. Include available, redistribution-cleared previews. An isometric thumbnail is
   preferred. Front, side, top, and detail views are also useful. Store PNG,
   JPEG, or WebP files under `data/previews/` and list them in the model's
   `previews` array with `view`, `file`, and `alt` fields. Models can be listed
   while preview images are unavailable.

## Send a change for review

State what changed, which sources support it, and which checks you ran.
For catalogue data changes, rebuild the search assets and site using the
README commands. Verify the affected entry and a representative query in both
search engines. For a documentation change, build the site and check the
affected pages and links. Maintainers assign catalogue IDs, review rights and
evidence, and decide what to publish.
