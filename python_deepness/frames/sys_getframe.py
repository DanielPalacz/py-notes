
def funct():
    a, b, c = 1, 2, 3
    import sys
    _frame = sys._getframe()

    breakpoint()


funct()

# (Pdb) dir(_frame)
# [
#   '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__','__init_subclass__',
#   '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#
#   'clear', 'f_back', 'f_builtins', 'f_code', 'f_globals', 'f_lasti', 'f_lineno', 'f_locals', 'f_trace', 'f_trace_lines', 'f_trace_opcodes'
# ]

# (Pdb) _frame.f_back.f_code.co_varnames
# ()
# (Pdb) _frame.f_back.f_code.co_freevars
# ()
# (Pdb) _frame.f_back.f_code.co_names
# ('funct',)

# (Pdb) _frame.f_back.f_code.co_name
# '<module>'
# (Pdb) _frame.f_code.co_name
# 'funct'



# Stos Pythonowy:

    # +---------------------------------+
    # |  Ramka funct()                  |  <-- _frame (ramka funkcji)
    # |   - co_name: 'funct'            |
    # |   - co_varnames: ('a', 'b', 'c')|
    # |   - co_names: ('sys', '_frame') |
    # +---------------------------------+
    #         ↓ f_back
    # +---------------------------------+
    # |  Ramka <module>                 |  <-- _frame.f_back (kod globalny)
    # |   - co_name: <module>           |
    # |   - co_varnames: ()             |
    # |   - co_names: ('funct',)        |
    # +---------------------------------+
