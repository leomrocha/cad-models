---
layout: default
title: CAD Models catalogue
---

Search parts, reference drawings and assemblies by name, identifier, subject or technical detail.

<form id="search">
  <label for="query">Search models</label>
  <div class="query"><input id="query" type="search" placeholder="Try LS-PS310K or ISO 4017"><button type="submit">Search</button></div>
  <div class="filters">
    <label>Search engine<select id="engine"><option value="sqlite">SQLite</option><option value="duckdb">DuckDB with Parquet</option></select></label>
    <label>Filter<select id="field"><option value="">Any</option><option value="subject">Subject</option><option value="tags">Tag</option><option value="materials">Material</option><option value="standards">Standard</option><option value="dimensions">Dimension</option><option value="needs">Needs more information</option></select></label>
    <label>Filter value<input id="value" placeholder="e.g. brick"></label>
  </div>
</form>
<p id="status" role="status"></p>
<section id="results" class="results" aria-label="Search results"></section>
<script type="module" src="{{ '/app.mjs' | relative_url }}"></script>
