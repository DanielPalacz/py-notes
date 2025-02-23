import pandas as pd

data = [
    ["Anna", 25, "Warszawa"],
    ["Jan", 30, "Kraków"],
    ["Piotr", 35, "Gdańsk"]
]

df = pd.DataFrame(data, columns=["Imię", "Wiek", "Miasto"])
print(df)
