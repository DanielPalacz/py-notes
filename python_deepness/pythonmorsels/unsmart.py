from argparse import ArgumentParser, FileType

parser = ArgumentParser()
parser.add_argument("file", type=FileType(encoding="utf-8"))
args = parser.parse_args()

text = args.file.read()

# TODO unsmartify the text somehow
text = text.translate(str.maketrans('‘’“”', "''\"\""))

print(text.removesuffix("\n"))
