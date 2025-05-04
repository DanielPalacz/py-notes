from dataclasses import dataclass
import os
import psutil
import time

def memory_usage_mb():
    # rss (Resident Set Size):
    #  - It is a measure for actual physical memory usage — it tells you how much RAM the process is currently using.
    #  - This is usually the number you care about for benchmarking or profiling memory usage.
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)


# @dataclass
@dataclass(slots=True)
class Person:
    name: str
    age: int


# Instance creation speed / memory consumption test
N = 1_000_000
items = []

init_memory_consumption = memory_usage_mb()

start = time.time()
for _ in range(N):
    # items.append(dict(name="Alice", age=30))
    items.append({"name": "Alice", "age": 30})
t1 = time.time()

mu1 = memory_usage_mb()


for item_ in items:
    x = item_['name']



print("Dictionaries 1M objects creation:"
      "\n"
      " - time needed [s]:\t\t\t\t", t1 - start,
      "\n",
      " - rss memory increase [MB]:\t", mu1 - init_memory_consumption,
      "\n\n",
      "Dictionaries 1M objects access:",
      "\n"
      " - time needed [s]:\t\t\t\t", time.time() - t1,
      "\n",
      " - rss memory increase [MB]:\t", memory_usage_mb() - mu1,
      sep=""
      )


# Dictionaries 1M objects creation:
#  - time needed [s]:			0.246445894241333
#  - rss memory increase [MB]:	239.0
#
# Dictionaries 1M objects access:
#  - time needed [s]:			0.06141376495361328
#  - rss memory increase [MB]:	0.0


