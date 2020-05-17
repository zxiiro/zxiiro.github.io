---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Testing network performance with iperf"
subtitle: ""
summary: ""
authors: ['zxiiro']
tags: ['Linux']
categories: []
date: 2013-10-29T00:00:00-04:00
lastmod: 2020-05-17T12:23:27-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

[iperf](https://code.google.com/archive/p/iperf/) is a handy tool to check
network performance between 2 computers. You can install this tool using your
distro’s package manager.

There are 2 modes this tool runs in. Server and Client, you will need to run it
in server mode on one end and client mode on the other end.

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-8372191724800927"
     data-ad-slot="2013710351"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

**Server usage:**

    iperf -s

**Client usage:**

    iperf -c <host/ip>

Basically you want to run it with the ``-s`` option on the server side and the
``-c`` option on the client side. On the client end you will also need to
provider the server's *hostname* or *IP address*.

Here's an example of what it looks like when run.

    ------------------------------------------------------------
    Client connecting to 192.168.32.50, TCP port 5001
    TCP window size: 22.9 KByte (default)
    ------------------------------------------------------------
    [  3] local 192.168.32.152 port 40885 connected with 192.168.32.50 port 5001
    [ ID] Interval       Transfer     Bandwidth
    [  3]  0.0-10.0 sec   897 MBytes   752 Mbits/sec
