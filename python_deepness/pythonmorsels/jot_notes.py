
from datetime import datetime
from os.path import expanduser


text = input("jot: ")
jot_path = expanduser("~/jot.txt")

today = datetime.now().strftime("%Y-%m-%d")
with open(jot_path, mode="at") as jot_file:
    jot_file.write(f"{today} {text}\n")
