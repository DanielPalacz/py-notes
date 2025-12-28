import tempfile
import os

with tempfile.NamedTemporaryFile(mode="w+", delete=True) as f:
    f.write("hello")
    f.seek(0)
    print(f.read())
# plik usuwany automatycznie po wyjściu z bloku

with tempfile.TemporaryFile(mode="w+") as f:
    f.write("data")
    f.seek(0)
    print(f.read())

with tempfile.TemporaryFile(mode="w+") as f:
    f.write("data")
    f.seek(0)
    print(f.read())


with tempfile.TemporaryDirectory() as tmpdir:
    path = os.path.join(tmpdir, "file.txt")
    with open(path, "w") as f:
        f.write("test")
# katalog i zawartość usunięte automatycznie


# fd, path = tempfile.mkstemp()
# trzeba samemu zamknąć fd i usunąć plik
# os.close(fd)
# os.remove(path)

