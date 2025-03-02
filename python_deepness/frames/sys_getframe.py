
def funct():
    a, b, c = 1, 2, 3
    import sys
    _frame = sys._getframe()

    breakpoint()


funct()

