---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Steam Share Library With Linux"
subtitle: "Sharing to multiple Linux accounts and systems"
summary: ""
authors: ['zxiiro']
tags: ['Steam', 'Linux']
categories: []
date: 2013-10-27T04:00:00-04:00
lastmod: 2020-05-17T12:06:36-04:00
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

If you use Steam on Linux one of the annoying things I’ve found is that unlike
on Windows, Steam for Linux installs to your ``$HOME`` directory. This means
every user will have their own Steam installed and what’s more their own games
installed. So on a shared system you might end up with the same games being
installed multiple times.

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

Steam has a feature that allows you to install games to a alternate location
called Steam Libraries. This feature allows you to create a Library at a new
location such as an alternate harddrive or partition if you don’t like where
Steam installs games by default. We can use this to create a shared library
location of games. To do this create a new user group on my system called
``steam`` then add all the users on the system which use Steam to this group.

Then create a shared directory on my system called ``/steam-library``, then
set the permissions to allow reading, writing and executing files from this
directory to anyone in the steam group.

Next launch Steam and add ``/steam-library`` as a new Library in Steam and
installed games to this location. After installing the games you can tell all
other users who use Steam on this computer to do the same. If a game they want
to install is already in the Library, it’ll just appear in their account, no
unnecessary downloading.

![Steam Libraries](/img/steam-share-library.png)

## Quick Steps


    mkdir /steam-library
    groupadd steam
    chgrp steam /steam-library
    chmod 770 /steam-library
    useradd -G steam your_user
    # add /steam-library to steam on all pc's and user accounts
