from pandas import DataFrame
from numpy.random import default_rng


rng = default_rng(0)

# df = DataFrame(rng.normal(size=(5,3))).round(2)

idx = [0, 0, 1, 1, 2]
df = DataFrame(rng.normal(size=(5,3)).round(2), index=idx)
df.columns = [0, 1, 1]


print(
    df,
    df.loc[0],
    f"{type(df.loc[0])                              = }",

    df[0],
    f"{type(df[0])                                  = }",

    f"{type(df.loc[0])                              = }",
    f"{type(df.loc[2])                              = }",

    f"{df.iloc[0]                                    = }",
    f"{df.iloc[0].index                              = }",
    f"{df.iloc[0].name                               = }",
    # f"{type(df.iloc[0])                            = }",

    f"{df[0]                                    = }",
    f"{df[0].index                              = }",
    f"{df[0].name                               = }",

    f"{df.iloc[0][1]                            = }",
    f"{df[0][3:]                                = }",
    f"{df[0][2]                                = }",

    sep="\n----------------------------------------------------------------------------------------------\n", end="\n\n"
)

df.iloc[0, 0] = 0.


print(
    df,

    "\n\n",
    df._data,
)