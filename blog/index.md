---
layout: default
title: Thanh's Blog
---
<div class="container">
  <div class="row">
    <div class="col-xs-12 col-md-9">
      {% for post in site.posts limit: 10 %}
      <div class="row">
        <div class="col-xs-12 col-md-10">
          <b><a href="{{ post.url }}">{{ post.title }}</a></b>
        </div>
        <div class="col-md-2" align="right">
          <i>{{ post.date | date_to_long_string }}</i>
        </div>
        <div class="col-md-12">
          {{ post.content }}
        </div>
      </div>
      <hr>
      {% endfor %}
    </div>

    <!-- Side bar start -->
    <div class="col-md-3">

      <div class="panel panel-default">
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
      </div>

    </div>
    <!-- Side bar end -->

  </div>
</div>
