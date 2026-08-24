

def minmax(l, key=None):
    l = sorted(list(l), key=key)
    return min(l), max(l)

