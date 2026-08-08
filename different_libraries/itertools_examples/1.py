# Która funkcja z modułu 'itertools' pozwoli na nieskończone powtarzanie elementów sekwencji?


import itertools
from time import sleep
#
#
# seq = "-napis!"
#
# it_ = itertools.repeat(seq)
#
# for x in it_:
#     for y in x:
#         print(y)
#         sleep(1)
#
#
# it_ = itertools.cycle(seq)
#
# for z in it_:
#     print(z)
#     sleep(1)
#
#

#
# Pytanie 11
#
# Co zostanie wypisane przez poniższy fragment kodu asynchronicznego?
# Python

import asyncio
import time
from functools import wraps


def timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} wykonana w {end - start:.6f} s")
        return result

    return wrapper


@timer
async def main():
    print("Start")
    await asyncio.sleep(0)
    print("End")


asyncio.run(main())



