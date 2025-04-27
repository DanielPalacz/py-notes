import itertools
import pandas as pd
from pandas.core.indexes.range import RangeIndex


data = {'Region': ['Wschód', 'Zachód', 'Wschód', 'Południe', 'Północ', 'Zachód', 'Północ'],
        'Produkt': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
        'Sprzedaż': [100, 150, 120, 200, 180, 220, 90]}

df = pd.DataFrame(data)
print(df)
print("\n\n-----------------------------------------------------------------------------------------------------------")

srednia_sprzedaz_region = df.groupby('Region')['Sprzedaż'].mean()
print(srednia_sprzedaz_region)

suma_sprzedaz_region_produkt = df.groupby(['Region', 'Produkt'])['Sprzedaż'].sum()
print(suma_sprzedaz_region_produkt)
print("\n\n---------------------------------------------------------------------------------------------------------\n")

# 1. Utwórz DataFrame ze wszystkimi kombinacjami
regions = df['Region'].unique()
produkty = df['Produkt'].unique()

regions_product_product = list(itertools.product(regions, produkty))
all_combinations = pd.DataFrame(regions_product_product, columns=['Region', 'Produkt'])


# 2. Połącz (merge)
df_merged = pd.merge(all_combinations, df, on=['Region', 'Produkt'], how='left')

# 3. Zgrupuj i zsumuj
suma_sprzedaz_region_produkt = df_merged.groupby(['Region', 'Produkt'])['Sprzedaż'].sum()

# 4. Wypełnij NaN zerami
suma_sprzedaz_region_produkt = suma_sprzedaz_region_produkt.fillna(0)

print(suma_sprzedaz_region_produkt)
