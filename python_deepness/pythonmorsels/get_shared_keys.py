
def get_shared_keys(d1: dict, d2: dict) -> set:
    return d1.keys() & d2.keys()


expired = {'c95': '20200315', 'd45': '20200401', 'b38': '20200415'}
used_recently = {'a56': 8, 'b38': 1, 'e77': 4, 'd45': 3}


common_part = get_shared_keys(expired, used_recently)
