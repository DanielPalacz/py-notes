import sys
import shutil
from time import sleep


try:
    LUCAS_NUMBERS = sys.argv[1]
    FILL_MODE = False
    if LUCAS_NUMBERS == "--fill":
        FILL_MODE = True

except IndexError:
    LUCAS_NUMBERS = None
    FILL_MODE = False


def lucas(n):
    x, y = 2, 1
    result = None

    for _ in range(n):
        x, y = y, x + y

    return x


def lucas_numbers():

    x, y = 2, 1
    yield x
    yield y


    result = None

    while True:
        x, y = y, x + y
        yield y



if __name__ == '__main__':

    terminal_height = shutil.get_terminal_size().lines

    if LUCAS_NUMBERS is None:
        for lucas_nr in range(0, terminal_height - 1):
            print(lucas(lucas_nr))

    elif FILL_MODE:
        ln_generator = lucas_numbers()
        first = True

        while True:
            if not first:
                print(" ", end="")
            print(next(ln_generator), end="")
            first = False

    else:
        for lucas_nr in range(0, int(LUCAS_NUMBERS)):
            print(lucas(lucas_nr))
