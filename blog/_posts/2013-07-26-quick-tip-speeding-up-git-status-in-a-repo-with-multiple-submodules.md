---
layout: post
title: ! 'Quick Tip: Speeding up "git status" in a repo with multiple submodules'
categories:
- eclipse
tags:
- eclipse
status: publish
type: post
published: true
meta:
  geo_public: '0'
  _publicize_pending: '1'
  _wpas_done_757239: '1'
  publicize_reach: a:2:{s:7:"twitter";a:1:{i:757240;i:127;}s:2:"wp";a:1:{i:0;i:1;}}
  _wpas_mess: ! 'Quick Tip: Speeding up "git status" in a repo with multiple submodules
    http://wp.me/p2qXd0-1r'
  publicize_twitter_user: zxiiro
  _wpas_done_757240: '1'
  _publicize_done_external: a:1:{s:7:"twitter";a:1:{i:40547933;b:1;}}
  _elasticsearch_indexed_on: '2013-07-26 02:49:25'
---
Something that's always bothered me was when I work on a repo that has numerous submodules, as more and more get added it seems like it takes longer and longer to run the command "git status".

It turns out this is due to git scanning all the directories to find untracked files so when it shows you the status in the aggregator repo it'll tell which repos have untracked files. For me I'd rather just find out which submodules have modifications and if there's any new commits most of the time.

It is possible to have git status ignore these untracked files and as a result speed up "git status" by adding the following line to your ".git/config" for each submodule you want to ignore untracked files for:

{% highlight bash %}
ignore = dirty
{% endhighlight %}

Example:
{% highlight bash %}
[submodule "submodule.repo"]
    url = ssh://localhost/submodule.repo
    ignore = dirty
{% endhighlight %}
