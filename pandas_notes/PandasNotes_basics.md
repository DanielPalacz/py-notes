
#### [NOTES—2]  PANDAS INDICES / INDEXES
```
   - Pandas Index is coordination system with well-defined semantics (for data operation)
```

#### [NOTES—3] "index-aligned" operation impact - example
```
   - what happens when try to do an operation needing "index-aligned"
   - 2 basic series structures: s1 + s2 ~ 670 function calls...
```

#### [NOTES—4] iterating through DataFrame - itertuples is the fastest:
```
    - for x in df.itertuples(): print(f"{x = }")
    - for x in df.itertuples(name=None): print(f"{x = }")
    - for x in df.itertuples(index=False, name=None): print(f"{x = }")
```

#### [NOTES—5]  DataFrame access:
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

#### [NOTES—11] Having DatetimeIndex index you can resample it.

#### [NOTES—16] Indexes and Index Alignment
```
Indexes and Index Alignment and mechanics coming from how they work - everything what you can do on Pandas Series/DF can be determined/explained by these two.
```

#### [NOTES—17] pandas groupby: Split-Apply-Combine, DataFrameGroupBy, aggregation functions: mean, sum, count, min, max, std


#### [NOTES—23] reset_index, sometimes the easiest solution (then RangeIndex)


### What are basic/core pandas concepts?
```
    Index as a coordination system / mechanism
    The index is pandas' internal way of aligning and referencing data—like coordinates in a grid, not just row labels.

    Index alignment (and its rules)
    When performing operations on multiple Series/DataFrames, pandas aligns data by index labels, not by position. Mismatched labels result in NaN unless handled.

    Promotion and broadcasting
    Pandas extends scalars or smaller structures (e.g., a Series) across a larger one (e.g., a DataFrame) when needed. Follows NumPy-style broadcasting rules.

    Element-wise operations
    Operations apply individually to each element—often automatically vectorized for performance.

    Split–Apply–Combine (GroupBy concept)
    A powerful framework for aggregation and transformation:
        Split the data by group
        Apply a function to each group
        Combine the results into a new structure

Additional Foundational Concepts:

    Label-based vs. Position-based indexing
    Understanding the difference between .loc[] (label-based) and .iloc[] (position-based) is essential for reliable data selection.

    Copy vs. View
    A subtle but critical concept: sometimes slicing returns a reference (view), other times a copy. Modifying one might affect the original unless you're careful.

    Chained indexing (and why it's dangerous)
    For example, df[df['A'] > 0]['B'] = 99 may not work reliably because of ambiguous behavior—pandas may throw a SettingWithCopyWarning.
    For example, df[df['A'] > 0]['B'] = 99 may not work reliably because of ambiguous behavior—pandas may throw a SettingWithCopyWarning.

    Data alignment along axes
    Operations in pandas are axis-aware. For example, aggregation with .sum() defaults to axis=0 (column-wise), and you must specify axis=1 for row-wise operations.

    In-place vs. non-in-place operations
    Many methods have an inplace=True option, but pandas often returns a new object instead—understanding this affects performance and memory.
```

### What are basic/core pandas skills?
```
 - Selecting data, Filtering Data / Boolean Indexing
 - Basic Arithmetic and Element-wise Operations
 - Resetting and Setting Index
 - Renaming Columns or Indexes
 - Changing Data Types (type casting)
 - Adding/Removing columns or rows
 - Sorting data (by Columns):
 - Detect missing values, Fill missing values, Drop missing data
 - Grouping and aggregation
```


```
Selecting data:

    Question 1:
    How do you create a DataFrame from a Python dictionary? Could you show an example?
    
    Question 2:
    How do you select a single column from a DataFrame as a Series? Could you show an example using your current df?
    
    Question 3:
    How do you select multiple columns (as a new DataFrame) from df?
     - df[['col1', 'col3']]   
    
    Question 4:
    How can you filter rows in a DataFrame based on a condition (single, complex)?
    
    Question 5:
    Summary of Operators: AND, OR, NOT in Pandas vs Python?
    
    | Logic Type | Python Keyword | Pandas Operator | Needs parentheses? |
    | ---------- | -------------- | --------------- | ------------------ |
    | AND        | `and`          | `&`             | ✅ Yes              |
    | OR         | `or`           | `\|`            | ✅ Yes              |
    | NOT        | `not`          | `~`             | ✅ Yes              |

    
    Question 6:
    When selecting multiple columns or rows, pandas returns a copy of the data?



Adding/Removing columns:
    Adding new column 'age_plus_10':
    df['age_plus_10'] = df['age'] + 10
 
    Removing 'country' column (inplace=False/True):
    df = df.drop('country', axis=1)
    df.drop('country', axis=1, inplace=True)


Adding/Removing rows:
    Adding new row ['Eva', 29, 'Gdansk']:
    new_row = pd.DataFrame({'name': ['Eva'], 'age': [29], 'city': ['Gdansk']})
    df = pd.concat([df, new_row], ignore_index=True)
 
    Removes row / rows:
    df = df.drop(2, axis=0)  # Removes the row with index 2 (Charlie)
    df = df.drop([0, 1], axis=0)  # Removes rows with index 0 and 1 (Alice and Bob)


Sorting data (by Columns):
    df_sorted = df.sort_values(by='age')
    df_sorted_desc = df.sort_values(by='age', ascending=False)
    df_sorted_multi = df.sort_values(by=['city', 'age'])


Detect Missing Values
    Use a method to check which values are missing in the entire DataFrame:
    df.isna()

    Check if there are any missing values at all:
     - df.isna().any().any()

Fill/missing values:
    Replace all missing age values with 0:
    df_new = df.fillna(value={'age': 0})

    Replace missing city values with the string "unknown":
    df_new = df.fillna(value={'city': 'unknown'})


Drop Missing Data:
    Create a new DataFrame that drops any row with at least one missing value:
    df_new2 = df.dropna(axis=0)
 
    Drop rows only if age and city are missing:
    df_not_correct = df.dropna(subset=['age', 'city']) # This removes rows if either 'age' or 'city' is missing, not both.
    df_new = df[~(df['age'].isna() & df['city'].isna())]
```

#### Grouping and aggregation in pandas
```
-------- Split -------- Apply -------- Combine

df.group('city') -----------------------------
------ df.group('city')['age'].mean() -------- 

"Split - Apply - Combine" strategy is a powerful conceptual framework for understanding grouping and aggregation in pandas.
The Split - Apply - Combine method clarifies the flow of operations, helping you think about data in terms of:
  - Which groups do I want? (Split)
  - What do I want to do to each group? (Apply)
  - How do I combine the results back into one? (Combine)
    
    grouped = df.groupby('city'):
    It is a special DataFrameGroupBy object, nothing is calculated, you just said: “Group these rows by the city column.”
    then: grouped['age'].mean() EQUALS TO: df.groupby('city')['age'].mean()

    pandas code snippet that uses grouping to calculate the sum of ages per city:
    ages_per_city = df.groupby('city')['age'].sum()
```
