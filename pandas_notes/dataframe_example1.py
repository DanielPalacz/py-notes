from pandas import DataFrame, date_range
from numpy import repeat, tile
from numpy.random import default_rng
from string import ascii_lowercase

rng = default_rng(0)

tickers_symbols = rng.choice([*ascii_lowercase], size=(100, 4)).view('<U4').ravel()


# tickers_symbols = rng.choice([*ascii_lowercase], size=(100, 4))
#   - 100 wierszy
#   - 4 kolumny
#   - wiersz to ciąg 4 pojedynczych znaków, np: ['a', 'b', 'c', 'd']


# tickers_symbols = rng.choice([*ascii_lowercase], size=(100, 4)).view('<U4')
#   - Metoda view() w NumPy pozwala na zmianę interpretacji danych w pamięci bez zmiany samych danych.
#   - Tutaj NumPy nie tworzy nowej kopii danych. Zamiast tego, tworzy nowe "okno" lub "perspektywę" na istniejący blok pamięci,
#     interpretując te same bajty w inny sposób (np. o innym typie danych, kształcie czy kolejności bajtów).
#   - Argument '<U4' określa, jak te dane mają być interpretowane.
#   - U nas .view('<U4') reinterpretuje tę tablicę tak, że zamiast 100 wierszy i 4 kolumn pojedynczych znaków, otrzymujemy 100 wierszy zawierających ciągi znaków o długości 4.
#   - Teraz wiersz to np: ['abcd']


# tickers_symbols = rng.choice([*ascii_lowercase], size=(100, 4)).view('<U4').ravel()
#   - Metoda ravel() w NumPy zwraca spłaszczoną (jednowymiarową) wersję tablicy wejściowej.
#   - U nas Zastosowanie .ravel() spowoduje przekształcenie wejsciowej wielowymiarowej tablicy w jednowymiarową wersję zawierającą 100 4-znakowych ciągów.




dates = date_range("2000-01-01", "2000-12-31", name="date")

prices = (
    100 * rng.random(size=len(tickers_symbols))
    * rng.normal(loc=1, scale=0.01, size=(len(dates), len(tickers_symbols))).cumprod(axis=0)
).ravel()

volumes = rng.integers(-50_000, +50_000, size=len(dates) * len(tickers_symbols)).round(-2)

# df = DataFrame({
#     "date": repeat(dates, len(tickers_symbols)),
#     "ticker_symbol": tile(tickers_symbols, len(dates)),
#     "price": prices,
#     "volume": volumes
# }
# )

# pandas.core.indexes.range.RangeIndex

from pandas.core.indexes.range import RangeIndex

# df = DataFrame({
#     "date": repeat(dates, len(tickers_symbols)),
#     "ticker_symbol": tile(tickers_symbols, len(dates)),
#     "price": prices,
#     "volume": volumes
# }
# ).set_index([RangeIndex(start=0, stop=36600, step=1), "date", "ticker_symbol"])


df = (DataFrame({
    "date": repeat(dates, len(tickers_symbols)),
    "ticker_symbol": tile(tickers_symbols, len(dates)),
    "price": prices,
    "volume": volumes
}
))



# Dodaj istniejący indeks jako kolumnę
df["row_index"] = df.index
df = df.set_index(["row_index", "date", "ticker_symbol"])


print(
    df.head(3),
    # df.loc[0, "ticker_symbol"],
    # df.iloc[0, 0],
    # df.loc[0]["ticker_symbol"],
    # df.loc[0],
    # df.loc[:, "ticker_symbol"],
    sep="\n----------------------------------------------------------------------------------------------\n", end="\n\n"
)
