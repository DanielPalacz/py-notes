from typing import Sequence


def tail(iterable_obj: Sequence, n: int) -> list:
    if n <= 0:
        return []

    iterable_obj_list = list(iterable_obj)
    return iterable_obj_list[-n::]
