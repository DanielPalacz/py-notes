
# Zadanie 1

# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner
#
# f = outer()
# f()


# Zadanie 2

# def make_multipliers():
#     return [lambda x: i * x for i in range(4)]
#
# multipliers = make_multipliers()
# print([m(2) for m in multipliers])


# Ten kod:
# [lambda x: i * x for i in range(4)]
# jest semantycznie równoważny z:
# result = []
# for i in range(4):
#     result.append(lambda x: i * x)


# Gdzie ewentualnie mam „braki”? Raczej nie brak wiedzy, tylko:
#     Lambda ≈ def – trzeba zapamiętać, że nie ma magii, tylko inny zapis.
#     Comprehension ≈ pętla for – nic więcej, żadnych dodatkowych priorytetów.
#     Closure = referencja, nie kopia – i to jest klucz, który eliminuje 90% nieporozumień.
#
# Jak sobie to poukładać?
#     Myśl: lambda = zwykła funkcja.
#     Myśl: list comprehension = zwykła pętla for.
#     A jeśli coś wygląda „magicznie” → zrób dis (disassembly bytecode) i sprawdź.
#       Bardzo często wtedy okazuje się, że Python wcale nie robi nic nadzwyczajnego.


# Zadanie 3
# x = 5
#
# def foo():
#     print(x)
#     x = 10
#
# foo()

# Wyjaśnienie w kontekście Execution Model:
#
# Compile stage:
# Funkcja foo zostaje skompilowana do bytecodu.
# Python tworzy symbol table dla foo, oznaczając x jako lokalną zmienną, ponieważ jest przypisywana w ciele funkcji.
#
# Runtime:
# Wywołanie foo() tworzy nowy frame z pustą lokalną przestrzenią.
# print(x) próbuje odwołać się do lokalnej x → jeszcze nie przypisana → UnboundLocalError.
# x=5 w globalnym scope jest niewidoczna w tym momencie, bo lokalne x zasłania globalną.



# def ops(a=): pass   # (Parsing Stage) SyntaxError: invalid syntax


# # Zadanie 4
# # Co wypisze poniższy program i dlaczego?
#
# import sys
#
# def recursive(n):
#     if n == 0:
#         return 1
#     return n * recursive(n-1)
#
# try:
#     print(recursive(1000))
# except RecursionError as e:
#     print("RecursionError:", sys.getrecursionlimit())


# Zadanie 5
# Rozważ wątek wykonania i GIL:

import threading

counter = 0
lock = threading.Lock()  # Tworzymy Lock do synchronizacji

# def increment():
#     global counter
#     for _ in range(1000000):
#         # Blokujemy dostęp do counter w tym fragmencie
#         with lock:
#             counter += 1
#
# # Tworzymy wątki
# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)
#
# # Start i join
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print(counter)  # Wynik zawsze: 2000000
