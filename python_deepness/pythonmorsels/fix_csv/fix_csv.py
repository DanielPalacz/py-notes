import csv
import sys

try:
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
except IndexError:
    input_file_name = "input.csv"
    output_file_name = "output.csv"


with open(input_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')


    with open(output_file_name, newline='\n', mode="w+t") as csvfile_write:
        writer_obj = csv.writer(csvfile_write, delimiter=',')


        for row in csv_reader:
            # row_write = ", ".join(row)
            writer_obj.writerow(row)
