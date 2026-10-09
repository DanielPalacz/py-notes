import math


def is_perfect_square(number, complex=False) -> bool:
    if number < 0 and not complex:
        return False

    if number < 0 and complex:
        return True

    root = math.isqrt(int(number))
    return root * root == number
