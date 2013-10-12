---
title: "Thanh's Blog"
layout: default
---

<div class="row-fluid">
  <div class="col-md-2">
    <b>Recent Posts</b><br>
    {% for post in site.posts %}
    <a href="{{ post.url }}">{{ post.title }}</a><br>
    {% endfor %}
  </div>

  <div class="col-xs-12 col-md-10">
    {% for post in site.posts limit: 10 %}
    <div class="row-fluid">
      <div class="col-xs-12 col-md-10">
        <b><a href="{{ post.url }}">{{ post.title }}</a></b>
      </div>
      <div class="col-md-2" align="right">
        <i>{{ post.date | date_to_long_string }}</i>
      </div>
      <div class="col-md-12">
        <p>{{ post.content }}</p>
      </div>
    </div>
    <hr>
    {% endfor %}
  </div>
</div>
