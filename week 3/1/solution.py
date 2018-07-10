import sys


class FileReader:
    """Класс для чтения файла"""

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as f:
            try:
                return f.read()
            except(IOError):
                return ""

def main():
    reader = FileReader("3-2.csv")
    print(reader.read())
    reader = FileReader("График.txt")
    print(reader.read())

if __name__ == "__main__":
    main()