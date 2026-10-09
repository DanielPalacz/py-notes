import csv
import sys

try:
    input_file_name = sys.argv[1]
except IndexError:
    input_file_name = "expenses.csv"


with open(input_file_name, newline='\n') as file_to_read_obj:
    csvfile_reader_obj = csv.reader(file_to_read_obj, delimiter=';')

    next(csvfile_reader_obj)

    air_travel_cost = 0.0

    for row in csvfile_reader_obj:
        row_ = row[0].split(",")
        if row_[3] == "Air Travel":
            air_travel_cost += float(row_[2])

    print(f"{air_travel_cost:.2f}")
