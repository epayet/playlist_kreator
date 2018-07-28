from playlist_kreator.util import read_artists
from tests.fake_clients.file_reader import FakeFileReader


def test_read_artists():
    file_reader = FakeFileReader("Anthrax\nMegadeth\nMetallica\nSlayer")

    artists = read_artists(file_reader)

    assert artists == ["Anthrax", "Megadeth", "Metallica", "Slayer"]
