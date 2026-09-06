
from collections import Counter


def string_with_most_repeats(strings):
    """Return the string with the single most repeated character."""

    k_max_tmp = None
    v_rep_max_tmp = 0
    string_item_tmp = None

    for string_item in strings:
        data_counter = Counter(string_item)
        k22, v_rep = max(data_counter.items(), key=lambda x: x[1])

        if v_rep > v_rep_max_tmp:
            k_max_tmp = k
            v_rep_max_tmp = v_rep
            string_item_tmp = string_item

    # return k_max_tmp, v_rep_max_tmp, string_item_tmp
    return string_item_tmp
