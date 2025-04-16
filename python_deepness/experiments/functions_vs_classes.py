
from python_deepness.functions.timeit_decorator import print_timeit

@print_timeit
def checking_100m_functions_creation():

    for _ in range(100000000): # 100 M
        def _temporary_funct():
            pass
        # def memoize(funct):
        #     cache = {}
        #
        #     def closure(number):
        #         if number not in cache:
        #             cache[number] = funct(number)
        #         return cache[number]
        #
        #     return closure


checking_100m_functions_creation()

@print_timeit
def checking_1m_classes_creation():

    for _ in range(1000000): # 1 M
        class _TEMP:
            pass

checking_1m_classes_creation()


@print_timeit
def checking_1m_classes_with_slots_creation():

    for _ in range(1000000): # 1 M
        class _TEMP:
            __slots__ = []

checking_1m_classes_with_slots_creation()

