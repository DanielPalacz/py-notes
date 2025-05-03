## [NOTES—1]  - pure python vs numpy / xarray / pandas:
```
  - numpy speed comes from several factors
  - Restricted Computation Domain = implementation domain
  - numpy ~ math vector representation

  - numpy.ndarray
       - interpreted view of memory
       - fixed size / dynamic shape
       - math type

  - xarray.DataArray (xarray library, not part of pandas)
       - xarray.DataArray = numpy ndarray + additional features
       - coordinate system

  - pandas (adds powerful labeling, indexing, and data handling on top of NumPy)

  - pure python - classic nested lists:
       - no dimensions - no math meaning
```


## [NOTES—2]  PANDAS INDICES / INDEXES
```
   - Index = coordination system or cooperative metadata with well-defined semantics (for data operation)
   - Index it is something convertable to data - mechanism

   - there - in pandas - exist a bunch of indexes (so there is set of coordination systems)
   - Index is extensible - but hard to get it right - lot of mechanics to implement
   - many methods published by 'index api', a lot of mechanics implemented
   - Pandas Index has always well-defined semantics, Data not
   - what are rules of .index  (numpy / numpy promotion rules can be good introduction start)
```

## [NOTES—3] "index-aligned" operation impact - example
```
   - what happens when try to do an operation needing "index-aligned"
   - 2 basic series structures: s1 + s2 ~ 670 function calls...
```

## [NOTES—4] iterating through DataFrame - itertuples is the fastest:
```
    - for x in df.itertuples(): print(f"{x = }")
    - for x in df.itertuples(name=None): print(f"{x = }")
    - for x in df.itertuples(index=False, name=None): print(f"{x = }")
```

## [NOTES—5]  DataFrame access:
```
    - df["col1"]
    - df.loc["row1"]
    - df.iloc[0] (row 1)
    - df.iloc[0, 0] (row 1, column 1)
    - df.at["row1", "col1"], df.iat[0,0]

    - this is not purely iloc example:
      df.iloc[0][1]
      here: 1. iloc returns series object; 2. S[1] access-lookup is based on indexes.
```

### [NOTES—6] Types promotion with associated loss of precision happens easily in 'pandas'. pandas sometimes too easily re-type structure to float64.
## [NOTES—7] Pandas indexing rules - understanding can be supported by numpy knowledge (indexing rules / broadcasting rules).
## [NOTES—8] INDEX ALIGNMENT RULES - it is how the indexes consider the match to "be exact".


## [NOTES—9] DataFrame - doubly-indexed structure (storing, aligning data like-indexed one-dimensional data).
## [NOTES—10] numpy.random.default_rng - interesting definition of DatetimeIndex:
```
  - idx_example = to_datetime("2000-01-01") + to_timedelta(rng.integers(0, 60*60, size=1_000).cumsum(), unit="s")  Timestamp, TimedeltaIndex, DatetimeIndex
```

## [NOTES—11] Having DatetimeIndex index you can resample it:
```
       - resample("TIME_INTERVAL") - technically, it creates new Grouped Index structure (can create new index samples with NaN as data values) with grouped data for time intervals (TIME_INTERVAL can be: "1min", "5min", "1H", "D")
       - apart from generating new index samples resample() works like groupby(), but it groups "by time" not column-values, so it can be said: "time-aware groupby" [so it works similar to: reindex + fill]
       - then after resampling (data grouping) you can use tools available for grouped data - supported operations: .sum(), .mean(), .agg(), .count(), .first(), .last(), .std()
```

## [NOTES—12] SettingWithCopyWarning
```
    - .loc[], query(), slicing - because pandas doesn't know if it is COPY or VIEW. iloc[] always create COPY or row and new Series object (no warnings).
    - pandas series is based on numpy.ndarray - numpy.ndarray wants memory to be contiguous - then copy is made
```

## [NOTES—13] df2 = df.query("score > 75") - possible SettingWithCopyWarning - to avoid: df2 = df.query("score > 75").copy()

## [NOTES—14]pandas BlockManager is very complex - but in the nutshell, it is inner pandas data structure that manages of way how data are stored in DataFrame
## [NOTES—15] MultiIndex and what are MultiIndex "index alignment" rules - very big topic


## [NOTES—16] Indexes and Index Alignment - and mechanics coming from how they work - everything what you can do on Pandas Series/DF can be determined/explained by these two
## [NOTES—17] pandas groupby: Split-Apply-Combine, DataFrameGroupBy, aggregation functions: mean, sum, count, min, max, std

## [NOTES—18] pandas groupby + aggregation functions
```
             can be used on:
               - all Series/DataFrame objects - gives single summary value
               - after grouping by groupby - stats for every group
               - inside agg function - for using many aggregation functions
```

## [NOTES—19] pandas groupby + aggregation functions - agg
```
    - you want new indexing based on groups
    - you can have many aggregation function inside agg
      df = df.groupby('Region').agg(łączna_sprzedaż=lambda x: x['Sprzedaż'].sum())
      df = df.groupby('Region').agg(łączna_sprzedaż=('Sprzedaż', 'sum'), średnia_cena=('Cena', 'mean'))
      s.groupby(...).agg(lambda s: s.skew())
    - agg(body) waits for: single aggregation funct, list of aggregation functions, or dictionary with appropriate content
```

## [NOTES—20] pandas groupby + aggregation functions - perform (keep original indexing)

## [NOTES—21] pandas groupby + aggregation functions - apply
```
    - 'apply' method is about ANY operation resulting NEW INDEX and concatenating back to pandas DataFrame layer
    - I want brand-new indexing (not like agg or perform)
    - s.groupby(...).apply(lambda df: df[df > 0].cumsum())
```

## [NOTES—22] pandas groupby + aggregation functions - apply pandas and align as diagnostic tool

## [NOTES—23] reset_index, sometimes the easiest solution (then RangeIndex)

## [NOTES—24] How to progress with pandas?
             After every operation:
               - think on what index it works?
               - how pandas align these data?
               - for example: df + df: have the same indexes / columns

             Understanding Pandas Data Model
               - index it is coordinates system: the way how Pandas addresses memory - every operation = transformation(based on coordinates)

             Mindset 'How Pandas would do this' not 'How to do this in Pandas'
             Learn Pandas horizontally: [Find more Use Cases]

             Look to output of index / columns ALWAYS - every operation changes something in data structure
             Be suspicious to values / iloc - you can have not understood something in "indexing thinking"



## "How Pandas would do this" concepts:
```
a) Vectorized Thinking
    Pandas wants you to think in columns, not rows.
    Operations are applied to entire Series/DataFrames at once, not one element at a time.

b) Declarative over Imperative
    You describe what you want (e.g. "group by column and aggregate"), not how to get there (e.g. "loop over rows and compute").

c) Leverage Core Data Structures
    Embrace the DataFrame and Series models.
    Each column is a Series. The index matters.
    Understand alignment: Pandas will often do the "right thing" when shapes match.

d) Chaining
    Compose transformations fluently (via .pipe(), method chaining), similar to data pipelines.
    Avoid intermediate variables unless needed for clarity.

e) Index as a First-Class Citizen
    Indexing isn’t just row numbers; it's a mechanism for alignment, selection, and hierarchy (via MultiIndex).

f) Avoid For-Loops
    Think in terms of broadcasting, masking, filtering, and applying operations column-wise.

g) Time Series Awareness
    Pandas has native support for time-based indexing, slicing, rolling, and resampling — treat time as a dimension.

h) GroupBy Philosophy
    “Split-Apply-Combine” is a core Pandas mental model. Grouping isn’t just for stats; it’s for transformations.
```


## Use Cases based on "How Pandas would do this" approach
```
Here’s how this mindset changes how you’d tackle problems:
a) Data Cleaning
    How Pandas would do it: .dropna(), .fillna(), .mask(), .where(), .replace() — all operate column-wise or DataFrame-wise.
    Use Case: Cleaning sensor data or survey responses with missing or placeholder values.

b) Feature Engineering
    How Pandas would do it: Use .assign() with vectorized calculations instead of creating columns inside a loop.
    Use Case: Creating new features for a machine learning pipeline.

c) Data Aggregation
    How Pandas would do it: .groupby().agg() instead of manually building aggregates.
    Use Case: Summarizing sales data by region and month.

d) Time Series Processing
    How Pandas would do it: Use .resample(), .rolling(), .shift() to manipulate time-based windows.
    Use Case: Creating moving averages or lagged features for financial modeling.

e) Relational Joins
    How Pandas would do it: Use .merge() rather than iterating to align datasets.
    Use Case: Joining customer demographics to transaction history.

f) Categorical Data Transformation
    How Pandas would do it: Use .map(), .get_dummies(), .astype('category') for encoding and transforming.
    Use Case: Preprocessing text labels or transforming survey responses into machine-friendly formats.

g) Pipeline-Style Data Transformation
    How Pandas would do it: Chain transformations using .pipe() and method chaining.
    Use Case: Data wrangling in reproducible ETL workflows or notebooks.
```