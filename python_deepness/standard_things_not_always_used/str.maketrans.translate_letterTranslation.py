# Przykład 1: Zamiana znaków (np. zamiana liter)
#
# Za pomocą maketrans i translate możemy zamieniać litery w tekście, na przykład zamieniając małe litery na duże i odwrotnie.

# Tworzymy mapowanie za pomocą maketrans
trans_table = str.maketrans("abc", "123")

# Przykładowy tekst
text = "abc is for apple."

# Zastosowanie translate do zamiany
translated_text = text.translate(trans_table)

print(translated_text)  # Wydrukuje: 123 is for apple.
