
def gen_fibonacci(n):
    x, y = 0, 1
    result = None
    while x < n:
        yield x
        x, y = y, x +y


def funct_fibonacci(n):
    numbers = []
    x, y = 0, 1
    result = None
    while x < n:
        numbers.append(y)
        x, y = y, x + y
    return numbers

