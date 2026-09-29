
def flip_dict(d: dict, error_on_duplicates = False) -> dict:
    f_dict = {}

    for k, v in d.items():
        if error_on_duplicates and v in f_dict:
            raise ValueError("Dictionary has duplicate values")
        f_dict[v] = k

    return f_dict
