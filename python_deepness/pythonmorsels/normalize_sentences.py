
# import re
#
#
# def normalize_sentences(text: str) -> str:
#     sentences = re.split(r"(?<=[.!?])[^\S\n]+", text)
#     return "  ".join(sentences)

#
# S1 = "Hello? Yes, this is dog!"
# x1 = normalize_sentences(S1)

###############################################################################

import re


def normalize_sentences(text: str) -> str:
    abbreviations = ("P.S.", "e.g.", "Dr.")

    for abbreviation in abbreviations:
        text = text.replace(abbreviation, abbreviation.replace(".", "§"))

    text = re.sub(r"(?<=[.!?])[ \t]+", "  ", text)

    for abbreviation in abbreviations:
        text = text.replace(abbreviation.replace(".", "§"), abbreviation)

    return text
