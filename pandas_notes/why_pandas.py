from numpy.ma.core import equal
from pandas import Series, DataFrame
from numpy.random import default_rng
from numpy import linspace

rng = default_rng(0)

# 1. Pandas df as Container.
# 2. Is for bizarre errors?
# 3. .values
# 4. .reset_index
#      - Czasami najprostszym rozwiązaniem jest zresetowanie indeksu do domyślnego indeksu liczbowego (RangeIndex) za pomocą metody .reset_index()
# 5. pandas is unpredictable


from pandas import RangeIndex
idx = RangeIndex(0, 100_000_000_000_000)


# s = Series(rng.integers(-10, +10, size=5))
# print(s)
# print("----------------")
# print(s.iloc[0])
# print(s.iloc[0:3])


idx101 = linspace(-20, +20, 5)
idx107 = [*'.aa.cfc.']


s101 = Series(rng.integers(-10, +10, size=5), index=idx101)
s107 = Series(rng.integers(-10, +10, size=len(idx107)), index=idx107)

# print(
#     s107,
#     "\n",
#     "\n",
#     s107[".":"c"],
#     "\n",
#     s107["f"],
# )

#
# # for x in s.iteritems(): print("x:", x)
# for _, x in s.items(): print(f"{x = }")
# for x in s: print(f"{x = }")
#
#
#
# print("-------------------------------------------------------------------------------")
# df = DataFrame(rng.integers(-10, +10, size=(5, 3)), columns=[*"abc"])
#
# print(df)
# print("-------------------------------------------------------------------------------")
# for x in df: print(f"{x = }")
# print("-------------------------------------------------------------------------------")
# for x in df.iterrows(): print(f"{x = }")
# print("-------------------------------------------------------------------------------")
# for _, x in df.items(): print(f"{x = }")
# for x in df.itertuples(): print(f"{x = }")
# for x in df.itertuples(name=None): print(f"{x = }")
# for x in df.itertuples(index=False, name=None): print(f"{x = }")





# 00:00


# 39:23
#  - There are many different types of index.

# 43:30
#  - Custom Indexes can be implemented from scratch (but it is hard to do this right, a lot of mechanics to implement)

# 45:40 (tracing mechanism)

# 48 ... pandas series metadata
# 49:55 ... pandas index metadata are persistent
# 50:06 - What are the rules of the '.index'?


# 50:09 - Lets talk about numpy:
# numpy broadcasting, promotion - what are rules
# xs[0] == xs  # Illogical in pure Python; will return False (In pure Python, there’s no automatic broadcasting)

from numpy import array, equal, allclose, meshgrid, log, exp

xs = array([x := 2**53, x + 1, x + 2, x + 3])
ys = exp(log(xs))

print(
    f"{(xs[0] == xs).all()                                                  = }",
    f"{equal(*meshgrid(xs, xs)).all()                                       = }",
    f"{allclose(*meshgrid(xs, xs), atol=1, rtol=1)                          = }",
    xs,
    sep="\n", end="\n\n"
)

# IEEE 754 i dokładność float64
# Liczby zmiennoprzecinkowe float64 mają mantysę 53-bitową (czyli ok. 16 cyfr dziesiętnych)
#   - 2**53 to największa liczba całkowita, która jest reprezentowana dokładnie.

print(
    f"{(ys[0] == ys).all()                                                  = }",
    f"{equal(*meshgrid(ys, ys)).all()                                       = }",
    f"{allclose(*meshgrid(ys, ys), atol=1, rtol=1)                          = }",
    ys,
    sep="\n", end="\n\n"
)

# 52:00 numpy promotion - rules quite important
# Rules of precision of numpy
# 52:05 - Promotion with associated loss of precision happens easily in 'pandas' and can be tricky to avoid (You may want other tool)





from pandas import Series
from numpy import int64

s1 = Series([x := 2**53, x + 1, x + 2, x + 3], dtype=int64, index=range(4))
s2 = Series([x := 2**53, x + 1, x + 2, x + 3], dtype=int64, index=range(1, 4+1))

print("-------------------------------------------------------------------------------------------------------------")
print(
    s1, s2,
    f"{(s1.values == s2.values).all()                                     = }",
    f"{(s1.index == s2.index).all()                                       = }",
    s1 + s2,
    (s1 + s2).dtype,
    s1.add(s2, fill_value=0).dtype,
    s1.add(s2, fill_value=0).dtype,
    sep="\n\n", end="\n\n"
)

# 53:00 pandas sometimes too easily re-type structure to float64

# 53:10 - Lets talk about numpy broadcasting (it should help with index alignment understanding)

print("-" * 80)


# 56:20

# indexing rules / broadcasting rules - have lot sense
#  -- can help with having better conceptual understanding of tool like Pandas


# Focus on this to see how everything fits together - here are the RULES OF BROADCASTING:
# -- dimensionality, right dimensionality


from numpy import newaxis, broadcast_to
from numpy.random import default_rng

rng = default_rng(0)

xs = rng.normal(size=(2, 3, 4)).round(1)
ys = rng.normal(size=2).round(1)[:, newaxis, newaxis]
zs = rng.normal(size=(3, 4)).round(1)

print(
    xs,
    f"{xs.shape                                                  = }",
    f"{xs.strides                                                = }",
    f"{xs[0].strides                                             = }",
    f"{xs[0, 1].strides                                          = }",
    f"{xs[:, 1].strides                                          = }",
    f"{ys.strides                                                = }",
    f"{broadcast_to(zs, xs.shape).strides                        = }",
    sep="\n", end="\n\n"
)

print("-" * 80)

# 57:30 - 59:00

# 1:00:43 - Lets talk about rules of INDEX ALIGNMENT:


##### -- 1:00:50 (Example 1) - The simplest case: no duplicate values
##### -- 1:01:32 (Example 2) - Indexes doesn't fully match

# Index - mechanism - rules associated - diffs indexes can have ... - INDEX ALIGNMENT - how the index considers the match to "be exact"
# --- this why "Date time" values can be put in Index - Index knows how to convert string into Data time to strings
# --- different Indexes modalities are not available on pandas series directly
    # Two ways of thinking:
    #  -- first transform series to shape
    #  -- first do index operation, then apply to data

# 1:04:30 - For complex data, It is often not easy to figure out how merge data in pandas. But when do index operations ...
# 1:04:34 - 'collections.Counter' is first-order approximation to a 'pandas.Series'


##### -- 1:04:50 (Example 3) - If there are duplicates in Index
##### ... Cartesian product
##### ... seems complex, but it is for what pandas is asked


# 1:06:41 - [Remember] - the '.index' is not guaranteed to be unique, sorted - it is not PK - it is jus mechanism



# 1:06:59 - 1:11:25 - Example of non-unique Index
# "non_unique_index.py"
# 1:11:25 - END



# 1:11:25 - Thinking beyond pandas 'Series', real data in 'DataFrame'

# "dataframe_example1.py"

# 1:13:18
#  Pandas is very One-Dimensional:
#   - A Series is singly-indexed one-dim dataset that have one index.
#   - DataFrame is doubly-indexed... structure
#        - storing, aligning data -
#   - DataFrame is doubly-indexed collection of like-indexed one-dimensional data


# In example:
#   - 4 datasets: "prices", "values", "dates" and "tickers" - COLLECTED with the same indexing
#   - in fact "dates" and "tickers" are not data - it is labelling => set_index(["date", "ticker_symbol"])
#   - so let's perform operation make use of this new "aligning"



# 1:15:48 - "dataframe_example2.py"

# 1:19:38 - "SettingWithCopyWarning" actually make sense
#            - example with coping row required due to when doing operation with heterogeneous data
# 1:23:00


# 1:23:19 - pandas dataframe is typified by... BlockManager (df._data)
#   - BlockManager very complex, topic for another day
#   - inner pandas data structure that manages of way how data are stored in DataFrame
#   - not part of public API - but have crucial meaning

# 1:24:04 - So what are rules of "index alignment" on DataFrame? Or combining Series and DataFrame?
#   - rows and columns match
#   - when df1 + df2 then if one has extra row/column then - row/column with NaN
#   - when df + s then rule is matching columns of DF against rows in Series (when no match then only NaNs)

# 1:26:17
#   -- example for df + s - when there is match(DF columns, series rows) for indexes values
#   -- real example 'factor Series' - here is potentially better to: 'df["price"] * factor' to not impact volumes - AND IT IS SMART... (or another DF with factors)


# 1:28:47 - So what is 'MultiIndex' and what are "index alignment" rules for it?
# 1:30:44 - 'MultiIndex' is not only hierarchical 'Index' - very big topic - for another day (and DatetimeIndex is MultiIndex)

# 1:32:10 - Operations in pandas should be thought - in terms of - how they operate on or affect the '.index'.
#           -  - ~80% of DataFrame API operations can be thought as something related to Index






# 1:32:15 - Indexes and Index Alignment - and mechanics coming from how they work - everything what you can do on Pandas Series/DF can be determined/explained by these two


# - example with groupby - many operations make sense for groupby in terms of index

# 1:32:25 - when you have structure that you want group by something,
#           and you want results to reflect indexing based on groups
#           whenever your groups are you want them to become new index => '.agg'
#           s.groupby(...).agg(lambda s: s.skew())

# 1:33:52 - transform - preserving original indexing
#           transform is about:
#             - take some structure with original indexing
#             - perform some operations/transformations/groupby, but keep original indexing look like
#             - s.groupby(...).transform(zscore)

# 1:34:23 - 'apply' is about saying you know what:
#             - I want brand-new indexing. apply is about ANY operation resulting NEW INDEX and concatenating back to pandas DataFrame layer
#             - s.groupby(...).apply(lambda df: df[df > 0].cumsum())


# 1:35:38 - ~80% of DataFrame API operations can be thought as something related to Index


# 1:35:45
