---
layout: default
title: "Thanh's Blog Tags"
---
<div class="container">
  <div class="container alert alert-info">
    {% for tag_ in site.tags %}
      {% capture tag %}{{ tag_ | first }}{% endcapture %}
      <a class="label label-info" href="#{{ tag }}">{{ tag }}</a>&nbsp;
    {% endfor %}
  </div>
</div>

<div class="container">
  <table class="table table-condensed table-hover">
    {% for tag_ in site.tags %}
      {% capture tag %}{{ tag_ | first }}{% endcapture %}
      <tr class="success">
        <th>{{ tag }}</th>
        <th><a name="{{ tag }}" class="anchor">&nbsp;</a></th>
      </tr>
      {% for post in site.posts %}
        {% if post.tags contains tag %}
          <tr>
            <td>{{ post.date | date: '%b %e, %Y' }}</td>
            <td><a href="{{ post.url }}">{{ post.title }}</a></td>
          </tr>
        {% endif %}
      {% endfor %}
    {% endfor %}
  </table>
</div>
