


def last_lines(filename: str) -> str:
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f.readlines()[::-1]:
            yield line


# def last_lines(filename: str):
#     with open(filename, "rb") as f:
#         f.seek(0, 2)

#         buffer = b""

#         while f.tell() > 0:
#             chunk_size = min(8192, f.tell())
#             f.seek(-chunk_size, 1)

#             buffer = f.read(chunk_size) + buffer

#             lines = buffer.split(b"\n")
#             buffer = lines.pop(0)

#             for line in reversed(lines):
#                 yield line.decode("utf-8")

#             f.seek(-len(buffer), 1)
