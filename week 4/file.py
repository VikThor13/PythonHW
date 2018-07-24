import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path)
        self.list = []
        self.current = 0
        self.list.append([str.strip() for str in self.file])

    def write(self, data):
        with open(self.path, 'a+') as f:
            f.write(data)

        self.list.append(data)

    def __add__(self, other):
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file = File(temp.name)
            file.list.extend(self)
            file.list.extend(other)
        return file

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.list):
            raise StopIteration

        result = self.list[self.current]
        self.current += 1
        return result

    def __str__(self):
        return self.path
