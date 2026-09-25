MARKER = object()

from typing import NamedTuple
from typing import Any


class MinMax(NamedTuple):
    min: Any
    max: Any


def minmax(iterable_obj, *, key=None, default=MARKER):
    iterable_obj = list(iterable_obj)

    if not iterable_obj and default == MARKER:
        raise ValueError("Empty list.")

    elif not iterable_obj and default is not None:
        return (default, default)

    elif not iterable_obj and default is None:
        return (default, default)

    if key is None:
        iterable_obj.sort()
    else:
        iterable_obj.sort(key=key)

    result = MinMax(iterable_obj[0], iterable_obj[-1])
    return result
