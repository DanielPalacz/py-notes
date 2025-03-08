import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
print()
lines_to_show = args.lines

for filename in args.filenames:
    iter = 1
    print("file:", filename)
    with open(filename, "r") as file_object:
        for line in file_object:
            print(iter, line, end="")
            if iter >= lines_to_show:
                break
            iter += 1
    print()
