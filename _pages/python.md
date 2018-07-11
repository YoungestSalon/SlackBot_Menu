-----
layout: archives
permalink: /Python/
title: "Python posts by YoungestSalon"
author_profile: true
header:
  image: "/images/2.jpg"
-----

Introduction of Python

1. List
2. Dictionary
3. Type of Data
4. while
5. for

{% include base_path %}
{% include group-by-array collection=site.posts field="tags" %}

{% for tag in group_names %}
  {% assign posts = group_items[forloop.index0] %}
  <h2 id="{{ tag | slugify }}" class="archive__subtitle">{{ tag }}</h2>
  {% for post in posts %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}
