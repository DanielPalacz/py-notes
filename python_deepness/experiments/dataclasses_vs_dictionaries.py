from dataclasses import dataclass
import time

# @dataclass
@dataclass(slots=True)
class Person:
    name: str
    age: int

d = {"name": "Alice", "age": 30}
p = Person("Alice", 30)

# Access speed test
N = 1_000_000

start = time.time()
for _ in range(N):
    x = d["name"]
print("Dict access:", time.time() - start)

start = time.time()
for _ in range(N):
    x = p.name
print("Dataclass access:", time.time() - start)

# 1. Without slots
# Dict access: 0.07030367851257324
# Dataclass access: 0.0686492919921875

# 2. With slots
# Dict access: 0.07261443138122559
# Dataclass access: 0.07339692115783691