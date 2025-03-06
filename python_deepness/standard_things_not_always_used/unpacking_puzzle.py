
def func():
    a, *b, c = ["Tony", "Phony", "Pony"]
    return "Phony" in [b] or a[:]

OUT = func() # "Tony" as b = ["Phony"] =>   => False


# def func2():
#     a, b, c = ["Tony", "Phony", "Pony"]
#     return "Phony" in [b] or a[:]
#
# OUT2 = func2() # True
