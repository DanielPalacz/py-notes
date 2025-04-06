from pandas import Series, DataFrame
from numpy.random import default_rng

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

# Series().array._ndarray
# . index is coordinate system
# . index is hwo we label and access data

# pandas index is not data - something convertable to data - mechanism
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

s = Series(rng.integers(-10, +10, size=5))
print(s)

# for x in s.iteritems(): print("x:", x)
for _, x in s.items(): print(f"{x = }")
for x in s: print(f"{x = }")


df = DataFrame(rng.integers(-10, +10, size=(5, 3)), columns=[*"abc"])

print(df)
for x in df: print(f"{x = }")
for x in df.iterrows(): print(f"{x = }")
for _, x in df.items(): print(f"{x = }")
for x in df.itertuples(): print(f"{x = }")

