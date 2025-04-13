from timeit_decorator import print_timeit
# from functools import lru_cache
from psutil import Process

def memoize(funct):
    cache = {}
    def closure(number):
        if number not in cache:
            cache[number] = funct(number)
        return cache[number]
    return closure


# @lru_cache(maxsize=None)  # Cache without limiting size
@memoize
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
