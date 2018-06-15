Share steam library with multiple Linux accounts and systems
============================================================

If you use Steam on Linux one of the annoying things I’ve found is that unlike
on Windows, Steam for Linux installs to your ``$HOME`` directory. This means
every user will have their own Steam installed and what’s more their own games
installed. So on a shared system you might end up with the same games being
installed multiple times.

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

.. figure:: share-library.png

   Steam Libraries

Quick Steps
-----------

.. code-block:: bash

   mkdir /steam-library
   groupadd steam
   chgrp steam /steam-library
   chmod 770 /steam-library
   useradd -G steam your_user
   # add /steam-library to steam on all pc's and user accounts
