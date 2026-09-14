
from collections import Counter

def _split_text_by_spaces(s: str) -> list:
    return s.split(" ")

def count_words(s: str) -> dict:
    s = s.replace("!", "").replace(".", "").replace("?", "").replace(",", "").replace("¿", "").replace("-", "")
    data = _split_text_by_spaces(s.lower())
    data_counter = Counter(data)
    return {k: v for k, v in data_counter.items()}

    # return Counter(data)



# from collections import Counter
# from string import punctuation
#
#
# def count_words(string):
#     """Return the number of times each word occurs in the string."""
#     return Counter(
#         word.strip(punctuation)
#         for word in string.lower().split()
#     )
