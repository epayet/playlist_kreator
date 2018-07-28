from contextlib import contextmanager

from playlist_kreator.util import read_artists


def test_read_artists():
    file_reader = FakeFileReader("Anthrax\nMegadeth\nMetallica\nSlayer")

    artists = read_artists(file_reader)

    assert artists == ["Anthrax", "Megadeth", "Metallica", "Slayer"]


class FakeFileReader:
    def __init__(self, file_content):
        self.file_content = file_content

    @contextmanager
    def open(self):
        yield FakeFile(self.file_content)


class FakeFile:
    def __init__(self, file_content):
        self.file_content = file_content

    def read(self):
        return FakeFileContent(self.file_content)


class FakeFileContent:
    def __init__(self, content):
        self.content = content

    def splitlines(self):
        return self.content.split('\n')
