import argparse
import configparser


def read_cmd_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("ini_like_file")
    parser.add_argument("csv_like_file")
    args = parser.parse_args()

    return args.ini_like_file, args.csv_like_file


def rewrite_ini_config(ini_filename, csv_filename):
    config = configparser.ConfigParser()
    config.read(ini_filename)

    with open(csv_filename, 'w') as csv_f:

        for k, v in config.items():
            if k == "DEFAULT":
                continue

            for kk, vv in v.items():
                csv_f.write(f'{k},{kk},{vv}\n')



if __name__ == '__main__':
    ini_file, csv_file = read_cmd_config()
    rewrite_ini_config(ini_file, csv_file)

