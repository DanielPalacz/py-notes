import json
import sys

json_filename = sys.argv[1]


if len(sys.argv) == 3:
    json_output_filename = sys.argv[2]
else:
    starting_phrase = json_filename.split(".")[0]
    json_output_filename = starting_phrase + ".jsonl"

with open(json_filename) as json_file:
    data = json.load(json_file)

    with open(json_output_filename, "w+") as outfile:
        outfile.write("".join(json.dumps(item) + "\n" for item in data))
