

def characters(s: str, /, sort = False) -> list:

    list_s =  list(s.lower())
    if not sort:
        return list_s
    else:
        list_s.sort(key=ord)
        return list_s
