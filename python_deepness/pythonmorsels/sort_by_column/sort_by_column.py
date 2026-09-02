

import sys
import csv


input_file_name = sys.argv[1]


if "--with-header" == sys.argv[2]:
    columns = sys.argv[3:]
else:
    columns = sys.argv[2:]


with open(input_file_name, newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)
    lines = list(reader)

lines.sort(key=lambda x: tuple(x[int(column)] for column in columns))

writer = csv.writer(sys.stdout, lineterminator="\n")

writer.writerow(header)

for line in lines:
    writer.writerow(line)

