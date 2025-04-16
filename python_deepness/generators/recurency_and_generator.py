from pathlib import Path

def iter_files(path: Path):
    for entry in path.iterdir():
        if entry.is_file():
            yield entry
        elif entry.is_dir():
            yield from iter_files(entry)

# for file in iter_files(Path('/ścieżka/do/katalogu')):
#     print(file)
