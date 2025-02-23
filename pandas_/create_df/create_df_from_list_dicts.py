import pandas as pd

data = [
    {"Imię": "Anna", "Wiek": 25, "Miasto": "Warszawa"},
    {"Imię": "Jan", "Wiek": 30, "Miasto": "Kraków"},
    {"Imię": "Piotr", "Wiek": 35, "Miasto": "Gdańsk"}
]

df = pd.DataFrame(data)
print(df)
