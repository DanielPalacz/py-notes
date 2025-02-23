import pandas as pd

s1 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print("s1:\n\n", s1, sep="")
print()
print()

s2 = pd.Series([10, "ss", 30, 40], index=["a", "b", "c", "d"])
print("s2:\n\n", s2, sep="")



