import pandas as pd
import numpy as np
import time

# Tworzymy przykładowy DataFrame
df = pd.DataFrame(np.random.randint(-10, 10, size=(10000, 10)), columns=list("ABCDEFGHIJ"))

# 1. itertuples()
start = time.time()
for row in df.itertuples(index=False, name=None):
    pass
itertuples_time = time.time() - start

# 2. iterrows()
start = time.time()
for _, row in df.iterrows():
    pass
iterrows_time = time.time() - start

# 3. iloc[]
start = time.time()
for i in range(len(df)):
    row = df.iloc[i]
    pass
iloc_time = time.time() - start

print(f"itertuples: {itertuples_time:.6f} seconds")
print(f"iterrows: {iterrows_time:.6f} seconds")
print(f"iloc: {iloc_time:.6f} seconds")


# # default_rng() to nowy generator liczb losowych w NumPy, wprowadzony w wersji 1.17.0 (2020)
# rng = np.random.default_rng()
# df = pd.DataFrame(rng.integers(-10, 10, size=(13, 3)), columns=["a", "b", "c"])
# print(df)
