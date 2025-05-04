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
    items.append(Person("Alice", 30))
t1 = time.time()

mu1 = memory_usage_mb()


for item_ in items:
    x = item_.name



print("Dataclass 1M objects creation:"
      "\n"
      " - time needed [s]:\t\t\t\t", t1 - start,
      "\n",
      " - rss memory increase [MB]:\t", mu1 - init_memory_consumption,
      "\n\n",
      "Dataclass 1M objects access:",
      "\n"
      " - time needed [s]:\t\t\t\t", time.time() - t1,
      "\n",
      " - rss memory increase [MB]:\t", memory_usage_mb() - mu1,
      sep=""
      )

# 1. Without slots
# Dataclass 1M objects creation:
#  - time needed [s]:				0.6954214572906494
#  - rss memory increase [MB]:	161.125
#
# Dataclass 1M objects access:
#  - time needed [s]:				0.060688018798828125
#  - rss memory increase [MB]:	0.0


# 2. With slots
# Dataclass 1M objects creation:
#  - time needed [s]:				0.4909524917602539
#  - rss memory increase [MB]:	53.875
#
# Dataclass 1M objects access:
#  - time needed [s]:				0.05853986740112305
#  - rss memory increase [MB]:	0.0


