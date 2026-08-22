
# python ini2csv.py .editorconfig.ini editorconfig.csv
# python ini2csv.py .editorconfig.ini editorconfig.csv --collapsed


import argparse
import configparser
import csv

parser = argparse.ArgumentParser(
                    prog='ini2csv converter',
                    description='INI-like file converting to a CSV-like file'
)
#


editor_config_ini = "editorconfig_ini"
editor_config_csv = "editorconfig_csv"

parser.add_argument(editor_config_ini, help="Editor config ini-file name.")
parser.add_argument(editor_config_csv, help="Editor config csv-file name.")
parser.add_argument("--collapsed", help="It will collapse the rows to one row per section.", action="store_true")
parser_out = parser.parse_args()

editor_config_ini_file = parser_out.editorconfig_ini
editor_config_csv_file = parser_out.editorconfig_csv

config = configparser.ConfigParser()
config.sections()
config.read(editor_config_ini_file)


if parser_out.collapsed:
    section_marker = 0
    with open(editor_config_csv_file, "w+") as csvfile:
        csvfile.write("header,indent_style,indent_size\n")

        for section in config.sections():
            for item_type, item_value in config[section].items():

                if section_marker % 2 == 0:
                    item_type_base = item_type
                    item_value1 = item_value
                    item_value2 = None
                else:
                    item_value2 = item_value

                section_marker += 1

            else:
                csvfile.write(f"{section},{item_value1},{item_value2}\n")

else:
    with open(editor_config_csv_file, "w+") as csvfile:
        writer_obj = csv.writer(csvfile, delimiter=',')

        for section in config.sections():
            for item_type, item_value in config[section].items():
                writer_obj.writerow([section, item_type, item_value])
