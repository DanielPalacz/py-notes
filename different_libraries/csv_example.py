import csv

input_file = "1.csv"
write_file = "2.csv"

with open(input_file, newline='') as csvfile:
    reader_obj = csv.reader(csvfile, delimiter=';')

    with open(write_file, newline='', mode="w+t") as csvfile_write:
        writer_obj = csv.writer(csvfile_write, delimiter=';')
        for row in reader_obj:
            row_write = [row[1]] + row
            writer_obj.writerow(row_write)
