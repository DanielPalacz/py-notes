# Przykład 2: Usuwanie konkretnych znaków (np. usuwanie samogłosk)
#
# Za pomocą maketrans możemy również usunąć określone znaki z tekstu.

# Tworzymy mapowanie, które usuwa samogłoski
trans_table = str.maketrans("", "", "aeiou")

# Przykładowy tekst
text = "This is an example sentence."

# Zastosowanie translate do usunięcia samogłosk
translated_text = text.translate(trans_table)

print(translated_text)  # Wydrukuje: Ths s n xmpl sntnc.
