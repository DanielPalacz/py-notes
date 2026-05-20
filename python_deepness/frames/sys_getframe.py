
def funct():
    a, b, c = 1, 2, 3
    import sys
    _frame = sys._getframe()

    breakpoint()


funct()



# Stos Pythonowy:

    # +---------------------------------+      _frame [..., 'f_back', 'f_builtins', 'f_code', 'f_globals', 'f_lasti', 'f_lineno', 'f_locals', 'f_trace', 'f_trace_lines', 'f_trace_opcodes']
    # |  f_code                         |  <-- _frame.f_code
    # |   - co_name: 'funct'            |
    # |   - co_varnames: ('a', 'b', 'c')|
    # |   - co_names: ('sys', '_frame') |
    # +---------------------------------+


    # +---------------------------------+
    # |  Ramka <module>                 |  <-- _frame.f_back (kod globalny.f_code.)
    # |   - co_name: <module>           |
    # |   - co_varnames: ()             |
    # |   - co_names: ('funct',)        |
    # +---------------------------------+
