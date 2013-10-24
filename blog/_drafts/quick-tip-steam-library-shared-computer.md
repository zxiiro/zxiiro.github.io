---
layout: post
title: Quick Tip: Share steam library with multiple Linux accounts and systems
---
If you use Steam on Linux one of the annoying things I've found is that unlike on Windows, Steam for Linux installs
to your $HOME directory. This means every user will have their own Steam installed and what's more their own games
installed. So on a shared system you might end up with the same games being installed multiple times.

I recently discovered Steam has a feature that allows you to install games to a alternate location called Steam Libraries.
This feature allows you to create a Library at a new location such as an alternate harddrive or partition if you
don't like where Steam installs games by default. What I thought I'd try doing was creating a new user group on my
system which I called "steam" and I added all the users on my system which used Steam to this group. Then I created a
shared directory on my system called /steam-library which I then set the permissions to allow reading, writing and
executing files from this directory to anyone in the steam group.

Next I launched Steam and added /steam-library as a new Library in Steam and installed games to this location. After
installing the games you tell all other users who use Steam on this computer to do the same. If a game they want to
install is already in the Library, it'll just appear in their account, no unnecessary downloading.

<p>
  Steam Library
  - create /steam-library
  - create steam group
  - add steam library to steam on all pc's and users
</p>

For those who have multiple computers. You can share /steam-library as an NFS share over the network and mount it
on your other computers too. Having a single point where your shared library lives will save you from having to
download the same files multiple times over the internet.

