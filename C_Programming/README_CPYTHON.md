

# README_CPYTHON.md

#### Katalogi w repozytorium CPython:
```

Katalogi w repozytorium CPython:


Include/ — definicje i API (nagłówki).
           Python.h (praktycznie najważniejszy plik nagłówkowy całego projektu)
           object.h (Object i type object interfejs)
           ....
         
Objects/ — implementacje core’owych typów w C.
Lib/ — standardowa biblioteka w Pythonie (czysty Python).
Modules/ — standardowa biblioteka w C (moduły specjalne i wydajnościowe).
Python/ — zawiera kod wykonawczy interpretera (parser, kompilator bajtkodu, eval loop),
          ceval.c, compile.c
Parser/ - ..


Zatem:
    Core języka (Objects + Include),
    biblioteka użytkowa (Lib + Modules),
    kod wykonawczy interpretera (Python).

Inne:
    Parser/ — parser gramatyki i generator AST,
    PCbuild/, Tools/, Misc/ — narzędzia pomocnicze i konfiguracje.



```
