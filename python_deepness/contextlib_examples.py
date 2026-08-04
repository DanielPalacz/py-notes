# 1. contextmanager – najważniejszy element
#
# Najczęściej używana funkcja.
#
# Bez contextlib trzeba napisać:
#
# class Database:
#     def __enter__(self):
#         print("connect")
#         return self
#
#     def __exit__(self, exc_type, exc, tb):
#         print("disconnect")
#
# Natomiast z contextmanager:
#

from contextlib import contextmanager


@contextmanager
def database():
    print("connect")

    try:
        yield "connection"
    finally:
        print("disconnect")
#
# Użycie:
#
with database() as conn:
    print(conn)
#
# wynik
#
# connect
# connection
# disconnect



# 2. closing()
# 3. suppress()
# 4. ExitStack
# 5. nullcontext()
# 6. redirect_stdout()
# 7. chdir() (Python 3.11)
# 8. asynccontextmanager


# Czy warto znać jako Python Mid?
# Zdecydowanie tak. Powiedziałbym nawet, że warto znać przynajmniej te elementy:
#
# Element	Jak często spotykany	Warto znać?
# @contextmanager	    ⭐⭐⭐⭐⭐	    ✅ Koniecznie
# suppress	            ⭐⭐⭐⭐	    ✅ Tak
# ExitStack	            ⭐⭐⭐	        ✅ Tak
# nullcontext	        ⭐⭐⭐	        ✅ Tak
# closing	            ⭐⭐	        Dobrze znać
# redirect_stdout	    ⭐⭐	        Dobrze znać
# chdir         	    ⭐⭐	        Dobrze znać
# asynccontextmanager	⭐⭐⭐⭐        ✅ Tak, jeśli używasz asyncio


import contextlib
import io



with contextlib.redirect_stdout(io.StringIO()) as target:
    print(123)
    print(11123)

# print(target.getvalue())
