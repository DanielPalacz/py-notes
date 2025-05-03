
from pandas import to_datetime, to_timedelta, Series, DataFrame
# from numpy import isclose
from numpy.random import default_rng

rng = default_rng(0)

idx = to_datetime("2000-01-01") + to_timedelta(rng.integers(0, 60*60, size=1_000).cumsum(), unit="s") # DatetimeIndex



s = Series(rng.normal(loc=1, scale=.1, size=len(idx)).cumprod(), index=idx)

print()

print(
    # s,

    # s.resample("1min").mean(),
    # s.groupby(s.index.round("1min")).mean(),

    # resample vs groupby operation:
    # s.resample("1min").agg(set), # not values, but index:
    # s.resample("1min").agg(lambda s_: {*s_.index}),
    # s.groupby(s.index.round("1min")).agg(lambda s_: {*s_.index}),

    # DataFrame({
    #     "resample": s.resample("1min").agg(lambda s_: {*s_.index}),
    #     "groupby": s.groupby(s.index.round("1min")).agg(lambda s_: {*s_.index})
    # }),

    # DataFrame({
    #     "resample": s.resample("1min").agg(lambda s_: {*s_.index}),
    #     "groupby": s.groupby(s.index.round("1min")).agg(lambda s_: {*s_.index})
    # }).apply(lambda s_: s_['resample'] == s_['groupby'], axis='columns'),

    "comp_idx:",
    "\n\n",

    (comp_idx := DataFrame({
        "resample": (rs := s.resample("1min").agg(lambda s_: {*s_.index})),
        "groupby": (gb := s.groupby(s.index.round("1min")).agg(lambda s_: {*s_.index}))
    }).apply(lambda s_: s_['resample'] == s_['groupby'], axis='columns')),

    # "\n\n",
    # comp_idx.where(comp_idx).index,
    "\n\n",
    "same_idx:",
    "\n\n",
    same_idx := comp_idx[comp_idx].index,

    "\n\n",
    f"{(rs.loc[same_idx] == gb.loc[same_idx]).all() = }",
    "\n\n",

    common_idx := rs.index.intersection(gb.index),
    "\n\n",
    diff_idx := common_idx.difference(same_idx),
    "\n\n",
    f"{(rs.loc[diff_idx] != gb.loc[diff_idx]) = }",

    "\n\n",
    len(s), len(s.resample("1min").mean()),
    len(s.groupby(s.index.round("1min")).mean()), len(comp_idx.where(comp_idx).index),

    len(same_idx), len(common_idx), len(diff_idx)
)

#  - when you have a large dataset and another dataset:
#  - it is not uncommon to do index operations (like subset)
#  - if you not use index then you probably operate on Raw data (there is many columns - you probably make a lot of Raw data copies - so expensive copies)
#       - code with many for loops that nobody understands

#  - here, we test how below are differ:
    # s.resample("1min").mean(),
    # s.groupby(s.index.round("1min")).mean(),
#          1. take these two structures, figure out what indexes samples are included in each buckets
#          2. find all cases where these indexes values are the same in these buckets
#          3. compute all places where use the same bucket and different bucket
#          4. go to original data to find what the corresponding calculation was for those buckets
#          5. and then verify... in our case the difference between resample vs groupby (buckets, windows, right-closed, left-closed)

