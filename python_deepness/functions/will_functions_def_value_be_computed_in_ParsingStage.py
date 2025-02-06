def def_value():
    print("def_value executed")
    return 42


def foo(a=def_value()):  # `def_value()` jest wykonywane TERAZ, podczas tworzenia `foo`
    print(a)


# if False:
#     def foo(a=def_value()):  # Jeśli `def_value()` wykonywałoby się w Parsing Stage, to ten kod by się wywalił
#         print(a)


print("End of script")

# def ops(a=):
#     pass
