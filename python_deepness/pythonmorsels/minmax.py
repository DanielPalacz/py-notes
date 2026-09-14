
from typing import Optional
from typing import Callable


def minmax(l: list, *, key: Optional[Callable] = None) -> tuple:
    if key is None:
        sorted_l = sorted(l)
    else:
        sorted_l = sorted(l, key=key)

    if not sorted_l:
        raise ValueError("Empty list ValueError.")

    return sorted_l[0], sorted_l[-1]
