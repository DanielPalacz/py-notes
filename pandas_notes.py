# 🔹 Etap 1: Fundamenty (musisz to znać)
#
# Czym jest Series i DataFrame – podstawowe różnice
# Tworzenie DataFrame i Series ręcznie (słowniki/listy)
# Wczytywanie danych z pliku CSV (pd.read_csv)
# Podstawowe info o danych: df.head(), df.info(), df.describe()
# Typy danych (dtypes) i ich konwersje (astype)
# Podstawy indeksowania: df['kolumna'], df.kolumna
# Indeks w Pandas – co to jest i jak go ustawiać (set_index, reset_index)
# Różnice: .loc[], .iloc[], .at[], .iat[]
# Filtrowanie danych (warunki logiczne)
# Dodawanie/usuwanie kolumn i wierszy (df['nowa'] = ..., drop())



# 🔹 Etap 2: Operacje na danych
#
# Operacje arytmetyczne na kolumnach
# Łączenie kolumn (+, .str, .apply)
# Operacje na stringach (.str.lower(), .str.contains())
# Operacje na datach (pd.to_datetime, .dt.year, .resample())
# Sortowanie (sort_values, sort_index)
# Obsługa brakujących danych (isna(), fillna(), dropna())
#


# 🔹 Etap 3: Agregacje i grupowanie
#
# groupby() – podstawy i agregacje (mean(), sum(), count())
# Grupowanie po wielu kolumnach
# Używanie .agg() do wielu operacji na raz
# pivot() i pivot_table()
# melt() – zamiana kolumn w wiersze (unpivoting)
#


# 🔹 Etap 4: Łączenie i przekształcanie danych
# concat() – łączenie wierszy i kolumn
# merge() – jak JOIN w SQL (left, right, inner, outer)
# join() – alternatywny sposób łączenia
# Zmiana indeksu (reindex())
# Usuwanie duplikatów (drop_duplicates())
#


# 🔹 Etap 5: Zaawansowane triki
#
# apply() – funkcje użytkownika na wierszach/kolumnach
# Mapowanie wartości (map(), replace(), applymap())
# query() – filtrowanie jak w SQL
# Praca z MultiIndex (wielopoziomowy indeks)
# Tworzenie nowych kolumn warunkowo (np.where, np.select, mask)
# Obsługa typów kategorii (astype('category'))
#


# 🔹 Etap 6: Praca z realnymi danymi
#
# Czyszczenie danych (puste pola, whitespace, złe typy)
# Przekształcenie "brudnego Excela" w czysty DataFrame
# Eksport danych (to_csv, to_excel)
# Prosty wykres (df.plot(), integracja z matplotlib)
