import tracemalloc

tracemalloc.start()

data = [i for i in range(1_000_000)]

snapshot1 = tracemalloc.take_snapshot()

print("snapshot1.statistics:")

for stat in snapshot1.statistics("lineno")[:5]:
    print(stat)

print()
print()

current, peak = tracemalloc.get_traced_memory()

print(f"Aktualnie: {current / 1024**2:.2f} MB")
print(f"Peak:      {peak / 1024**2:.2f} MB")
print()
print()



data2 = [i for i in range(400_000)]

snapshot2 = tracemalloc.take_snapshot()

print("snapshot2.statistics:")

for stat in snapshot2.statistics("lineno")[:5]:
    print(stat)

print()
print()


current, peak = tracemalloc.get_traced_memory()

print(f"Aktualnie: {current / 1024**2:.2f} MB")
print(f"Peak:      {peak / 1024**2:.2f} MB")

tracemalloc.stop()
