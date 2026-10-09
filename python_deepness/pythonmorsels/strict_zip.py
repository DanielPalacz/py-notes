from typing import Iterator


def strict_zip(*seq_objects) -> Iterator[tuple]:
    zipped_objects = iter(zip(*seq_objects, strict=True))
    return zipped_objects
