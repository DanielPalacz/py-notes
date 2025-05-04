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



class Person:
    #__slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instance creation speed / memory consumption test
N = 1_000_000
items = []

init_memory_consumption = memory_usage_mb()

start = time.time()
for _ in range(N):
    items.append(Person("Alice", 30))
t1 = time.time()

mu1 = memory_usage_mb()


for item_ in items:
    x = item_.name



print("Classic classes 1M objects creation:"
      "\n"
      " - time needed [s]:\t\t\t\t", t1 - start,
      "\n",
      " - rss memory increase [MB]:\t", mu1 - init_memory_consumption,
      "\n\n",
      "Classic classes objects access:",
      "\n"
      " - time needed [s]:\t\t\t\t", time.time() - t1,
      "\n",
      " - rss memory increase [MB]:\t", memory_usage_mb() - mu1,
      sep=""
      )
