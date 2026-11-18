---
layout: default
title: Browse CAD models
permalink: /browse.html
---

## Browse by tag

{% include tag-list.html %}

## Browse by subject

{% assign subjects = site.data.catalogue | group_by: 'subject' | sort: 'name' %}
{% for subject in subjects %}
<h3>{{ subject.name | escape }}</h3>
<ul>
  {% for model in subject.items %}
  {% assign path = '/models/' | append: model.id | append: '.html' %}
  <li><a href="{{ path | relative_url }}">{{ model.name | escape }}</a></li>
  {% endfor %}
</ul>
{% endfor %}
