from pandas import Series, DataFrame
from numpy.random import default_rng
from numpy import linspace

rng = default_rng(0)

# 1. Pandas df as Container.
# 2. Is for bizarre errors?
# 3. .values?
# 4. .reset_index
# 5. pandas is unpredictable

# numpy - speed



# Restricted Computation Domain
# pure python - Restricted Computation Domain - implementation domain
# numpy - math vector representation

# classic nested lists - not dimensions - no math meaning
# numpy.ndarray
#  - interpreted view of memory
#  - fixed size / dynamic shape
#  - math type


# xarray.DataArray
# - coordinate system

# Series().array._ndarray
# . index is coordinate system
# . index is how we label and access data




# pandas index is not data - something convertable to data - mechanism
# In the other words '.index' is operative metadata with well-defined semantics (for data operations)



from pandas import RangeIndex
idx = RangeIndex(0, 100_000_000_000_000)

# INDICES / INDEXES
#   - Index = coordination systems / cooperative metadata /
#   - a bunch of them - so there is set of coordination systems
#   - Index is extensible - but hard to get right
#   - many methods published by 'index api', a lot of mechanics implemented
#   - Pandas Index is always well-defined, Data not
#   - what are rules of .index / numpy / numpy promotion


# Look what happens when try to do an "index-aligned" operation...
# s1 + s2 ~ 670 function calls...

# The .index is cooperative metadata with well-defined semantics (in terms of data operation)

#
# s = Series(rng.integers(-10, +10, size=5))
# print(s)
# print("----------------")
# print(s.iloc[0])
# print(s.iloc[0:3])


idx101 = linspace(-20, +20, 5)
idx107 = [*'.aa.cfc.']

s101 = Series(rng.integers(-10, +10, size=5), index=idx101)
s107 = Series(rng.integers(-10, +10, size=len(idx107)), index=idx107)

print(
    s107,
    "\n",
    "\n",
    s107[".":"c"],
    "\n",
    s107["f"],
)

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
# s1 = Series(rng.integers(-10, +10, size=5), index=[1, 2, 3])



# 00:00


# 39:23
#  - There are many different types of index.

# 43:30
#  - Custom Indexes can be implemented from scratch (but it is hard to do this right, a lot of mechanics to implement)

# 45:40 (tracing mechanism)

# 48 ... pandas series metadata
# 49 ... pandas index metadata are persistent

# 57:00