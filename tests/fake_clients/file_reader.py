from contextlib import contextmanager


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
