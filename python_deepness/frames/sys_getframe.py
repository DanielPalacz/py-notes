
def funct():
    a, b, c = 1, 2, 3
    import sys
    _frame = sys._getframe()

    breakpoint()


funct()



# Stos Pythonowy:

    # +---------------------------------+
    # |  Ramka funct()                  |  <-- _frame (ramka funkcji.f_code.)
    # |   - co_name: 'funct'            |
    # |   - co_varnames: ('a', 'b', 'c')|
    # |   - co_names: ('sys', '_frame') |
    # +---------------------------------+
    #         ↓ f_back
    # +---------------------------------+
    # |  Ramka <module>                 |  <-- _frame.f_back (kod globalny.f_code.)
    # |   - co_name: <module>           |
    # |   - co_varnames: ()             |
    # |   - co_names: ('funct',)        |
    # +---------------------------------+
