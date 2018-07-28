from tests.fake_clients.file_reader import FakeFileReader
from playlist_kreator.util import FileReader


def test_file_reader():
    fake_file_reader = FakeFileReader("Anthrax\nMegadeth\nMetallica\nSlayer")
    file_reader = FileReader("example_artists/big_four_thrash.txt")

    with fake_file_reader.open() as file:
        fake_content = file.read().splitlines()
    with file_reader.open() as file:
        content = file.read().splitlines()

    assert fake_content == content == ["Anthrax", "Megadeth", "Metallica", "Slayer"]
