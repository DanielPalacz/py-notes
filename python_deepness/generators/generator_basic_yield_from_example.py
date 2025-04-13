def sub_generator():
    yield 1
    yield 2
    yield 3

def main_generator():
    yield 0
    yield from sub_generator()  # delegujemy iterację
    yield 4

for value in main_generator():
    print(value)
