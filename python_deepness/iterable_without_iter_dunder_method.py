# W Pythonie 3 większość wbudowanych kolekcji implementuje __iter__, ale są pewne wyjątki:
#  - Możemy ręcznie stworzyć obiekt, który implementuje tylko __getitem__, ale nie __iter__.
# - Python nadal pozwoli na iterację przy użyciu __getitem__, ale to bardziej hack niż powszechna praktyka.

class CustomSeq:
    def __getitem__(self, index):
        if index >= 5:
            raise IndexError
        return index * 2  # Prosty wzór

obj = CustomSeq()
iter_custom_seq = iter(obj)
numbers = [elem for elem in iter_custom_seq] # # [0, 2, 4, 6, 8]
# print(obj[2])  # 4 (Działa przez __getitem__)
# print(list(obj))  # [0, 2, 4, 6, 8] (Python używa __getitem__ do symulacji iteracji)
