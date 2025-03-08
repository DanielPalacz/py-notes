import sys

message = str(sys.stdin.read()).strip()

print(message[::-1])


# echo "Novum" | python how_to_opearate_on_stdin.py
# echo "Novum" > python how_to_opearate_on_stdin.py # Error, STDOUT not STDIN
# python how_to_opearate_on_stdin.py < input.txt
