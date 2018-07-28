from contextlib import contextmanager


def read_artists(file_reader):
    with file_reader.open() as file:
        return file.read().splitlines()


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    @contextmanager
    def open(self):
        file = open(self.filename, 'r')
        yield file
        file.close()
