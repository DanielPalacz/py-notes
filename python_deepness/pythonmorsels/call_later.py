from functools import partial
from typing import Callable


def call_later(funct: Callable, *args, **kwargs):
    return partial(funct, *args, **kwargs)
