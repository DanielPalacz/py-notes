import pandas as pd

data = {
    "Imię": ["Anna", "Jan", "Piotr"],
    "Wiek": [25, 30, 35],
    "Miasto": ["Warszawa", "Kraków", "Gdańsk"]
}

df = pd.DataFrame(data)
print(df)
