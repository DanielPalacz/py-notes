from pathlib import Path
import sys

filename = sys.argv[1]
text = Path(filename).read_text().casefold()
apostrophe = "\N{right single quotation mark}"  # The "’" character

if apostrophe in text:
    print("Found smart apostrophe")
else:
    print("No smart apostrophe")
