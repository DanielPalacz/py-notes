

# Prawdziwa siła defaultdict

import collections as c

d = c.defaultdict(int)
# d["a"]
# 0

# Nie było klucza "a".
# defaultdict wykonał:
# int()
# czyli 0
d["a"] += 1
d["b"] += 1
d["c"] += 1
d["d"] += 1
d["d"] += 1
d["d"] += 1

print(d)

# defaultdict(<class 'int'>, {'a': 1, 'b': 1, 'c': 1, 'd': 3})
