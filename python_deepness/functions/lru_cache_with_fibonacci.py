from timeit_decorator import print_timeit
from functools import lru_cache
from psutil import Process
from copy import deepcopy

@lru_cache(maxsize=None)  # Cache without limiting size
@print_timeit
def fibonacci(n):
    x, y = 0, 1
    result = None
    while x < n:
        x, y = y, x +y
    return x


for _ in range(10):
    @print_timeit
    def wrapper_fibonacci():
        fibonacci(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    wrapper_fibonacci()


p = Process()
print(p.memory_info())
