---
layout: default
title: Thanh's Blog
---
<div class="container">
  <div class="row">
    <div class="col-xs-12 col-md-9">

      {% for post in site.posts limit: 10 %}
      <div class="container">
        <h3><a href="{{ post.url }}">{{ post.title }}</a></h3><hr style="margin:0px">
        <div class="container">
          <i>Posted on {{ post.date | date_to_long_string }}</i>
          <div class="container pull-right">
            {% for tag in post.tags %}
            <a class="badge" href="/blog/tags.html#{{ tag }}">{{ tag }}</a>&nbsp;
            {% endfor %}
          </div>
        </div>
        <hr style="margin:0px">

        <p>{{ post.content }}</p>
      </div>
      <hr>
      {% endfor %}

    </div>

    <!-- Side bar start -->
    <div class="col-md-3">

      <div class="panel panel-default" data-spy="affix">
        <div class="panel-heading"><small><b>Recent Posts</b></small></div>
        <div class="panel-body">

          <table class="table table-condensed table-hover">
            {% for post in site.posts limit:5 %}
            <tr>
              <td><i class="icon-li icon-caret-right"></i></td>
              <td>
                <small><a href="{{ post.url }}">{{ post.title }}</a></small><br>
              </td>
            </tr>
            {% endfor %}
          </table>
        </div>
        <!-- end Recent Posts -->

        <div class="panel-footer">
          <small><b><a href="/blog/archives.html">Archives</a></b></small><br>
          <small><b><a href="/blog/tags.html">Tags</a></b></small>
        </div>
        <!-- end Archives -->
      </div>

    </div>
    <!-- Side bar end -->

  </div>
</div>
