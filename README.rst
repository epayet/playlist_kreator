================
Playlist Kreator
================

Create easily playlists based on a list of artists.
It will use the number of top songs per artist you choose.

Currently supported: Google Music.

Installing
----------

TODO (is ffmpeg needed?)
brew install ffmpeg
python3?

::

    pip install playlist-kreator

Example
-------

::

    playlist-kreator artists big_four_thrash.txt "Big Four of Thrash" [--max-songs-per-artist=10] [--email="foo@bar.com"]

This will create a playlist called "Big Four of Thrash".
The playlist will be composed of 10 top songs for each artist listed in the file `big_four_thrash.txt`.
Content of `big_four_thrash.txt`:

::

    Anthrax
    Megadeth
    Metallica
    Slayer

Known limitations
-----------------

TODO

Inspiration
-----------

Kreator is amazing

Contributing
------------

TODO

License
-------

TODO