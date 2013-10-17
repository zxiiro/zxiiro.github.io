---
layout: default
title: Thanh's Blog Archives
---
<div class="container">
  <h2>Blog Archives</h2>

  <table class="table table-condensed table-hover">
    {% for post in site.posts %}

      {% unless post.next %}
        <thead><tr><td><h3>{{ post.date | date: '%Y' }}</h3></td></tr></thead>
      {% else %}
        {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
        {% capture nyear %}{{ post.next.date | date: '%Y' }}{% endcapture %}
        {% if year != nyear %}
          <thead><tr><td><h3>{{ post.date | date: '%Y' }}</h3></td></tr></thead>
        {% endif %}
      {% endunless %}

      <tbody><tr><td>{{ post.date | date:"%b" }}</td><td><a href="{{ post.url }}">{{ post.title }}</a></td></tr></tbody>
    {% endfor %}
  </table>

</div>
