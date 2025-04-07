# https://www.youtube.com/watch?v=pjq3QOxl9Ok


from contextlib import contextmanager
from sys import gettrace, settrace
from pathlib import Path
from os import pardir

import pandas as pd
from pandas import Series, date_range
from numpy.random import default_rng

rng = default_rng(0)

@contextmanager
def tracing():

    old_trace = gettrace()
    depth, frames = 0, []

    def trace(frame, event, arg):
        nonlocal depth

        filename = frame.f_code.co_filename

        if filename.startswith('<'): return None
        filename = Path(filename)

        if not filename.is_relative_to(base_dir := Path("/")):
            return None

        if event == "return":
            depth -= 1

        if event == "call":
            depth += 1
            fr = filename.relative_to(base_dir,), frame.f_lineno, frame.f_code.co_name, depth
            frames.append(fr)
            return trace

    settrace(trace)

    try:
        columns_: list[str] = "filename lineno function depth".split()
        yield lambda: pd.DataFrame(data=frames, columns=columns_)

    finally:
        settrace(old_trace)




s1 = Series([1, 2, 3, 4, 5])
s2 = Series([2, 3, 4, 5, 6, 7] )

pandas_index1 = date_range("2000-01-01", periods=5, name="date")
s11 = Series(rng.integers(-10, +10, size=len(pandas_index1)), index=pandas_index1)

pandas_index2 = date_range("2000-01-02", periods=5, name="date")
s12 = Series(rng.integers(-10, +10, size=len(pandas_index1)), index=pandas_index2)

with tracing() as get_df:
    s11 + s12


df = get_df()

print(
    df,
    "\n\n",
    "\r"
    "Max depth:", max(df.depth),
    df[df['depth'] > 16],
    df[df['filename'].apply(lambda x: 'pandas/core/indexes' in str(x))],
)
