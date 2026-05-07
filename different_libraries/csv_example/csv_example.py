import csv

input_file_name = "1.csv"
write_file = "2.csv"

with open(input_file_name, newline='\n') as file_to_read_obj:
    csvfile_reader_obj = csv.reader(file_to_read_obj, delimiter=';')

    with open(write_file, newline='\n', mode="w+t") as csvfile_write:
        writer_obj = csv.writer(csvfile_write, delimiter='-')

        for row in csvfile_reader_obj:
            row_write = [row[1]] + [row[0]]
            writer_obj.writerow(row_write)
