
```
1)

„Late binding” oznacza, że wartość zmiennej jest brana w momencie wywołania funkcji, a nie w momencie jej stworzenia.

fruits = ["apple", "pear", "banana", "mango"]
l_fruits = [lambda: fruit for fruit in fruits]
x_fruits = [x() for x in l_fruits] # ['mango', 'mango', 'mango', 'mango']


2)

def solution(data: list) -> int:
    data.sort(reverse=True) # złożoność czasowa: O(n log n) (sortowanie w Pythonie to Timsort)

    if data[-1] < 0:
        data.pop()  # złożoność czasowa: O(1)

    return sum(data)  # złożoność czasowa O(n)

Złożoność czasowa łącznie: O(n log n + n) ≈ O(n log n).

Złożoność pamięciowa:
 - sortowanie w Pythonie (Timsort) wymaga O(n) dodatkowej pamięci w najgorszym przypadku
   chociaż w niektórych przypadkach jest bliżej O(1) (w praktyce implementacja robi niewielkie bufory, ale nie zmienia to asymptoty)
 - pop() i sum() nie wymagają dodatkowych struktur poza istniejącą listą
 - łącznie: O(n) + O(1) + O(1)
```
