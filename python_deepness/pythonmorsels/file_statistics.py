import sys

filename = sys.argv[1]

with open(filename) as f:
    text = f.read()
    lines_nr = len(text.splitlines())
    words_nr = len(text.split())


print("Lines:", str(lines_nr))
print("Words:", str(words_nr))


# with open(filename) as f:
#     for line_nr, line in enumerate(f, start=1):
#         print(line_nr, line.rstrip())
