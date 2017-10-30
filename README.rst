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

    playlist-kreator artists big_four_thrash.txt "Big Four of Thrash" --max-songs-per-artist=10

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

- Google Music needs an application password, you can set it here: https://myaccount.google.com/apppasswords
- Google Music has a limit of 1000 songs per playlist

Contributing
------------

Pull requests are welcome!

Running locally
```````````````

`pip install -r requirements.txt`

Inspiration
-----------

Kreator is amazing. 🤘

|Kreator|

.. |Kreator| image:: http://kreator-terrorzone.de/images/releases/thumbs/cover_gods.jpg
