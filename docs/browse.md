---
layout: default
title: Browse CAD models
permalink: /browse.html
---

{% assign subjects = site.data.catalogue | group_by: 'subject' | sort: 'name' %}
{% for subject in subjects %}
<h2>{{ subject.name | escape }}</h2>
<ul>
  {% for model in subject.items %}
  {% assign path = '/models/' | append: model.id | append: '.html' %}
  <li><a href="{{ path | relative_url }}">{{ model.name | escape }}</a></li>
  {% endfor %}
</ul>
{% endfor %}
