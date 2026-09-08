NUMBERS = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
    15: "XV",
    16: "XVI",
    17: "XVII",
    18: "XVIII",
    19: "XIX",
    20: "XX",
    21: "XXI",
    25: "XXV",
    30: "XXX",
    40: "XL",
    50: "L",
    60: "LX",
    70: "LXX",
    80: "LXXX",
    90: "XC",
    100: "C",
    500: "D",
    600: "DC",
    1000: "M",
    1888: "MDCCCLXXXVIII",
    1948: "MCMXLVIII",
    1999: "MCMXCIX",
    2000: "MM",
}


def _parse_number(roman):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    number = 0

    for i, char in enumerate(roman):
        value = values[char]

        if i + 1 < len(roman) and value < values[roman[i + 1]]:
            number -= value
        else:
            number += value

    lt = number // 1000
    lh = number // 100 % 10
    ld = number // 10 % 10
    li = number % 10

    return lt, lh, ld, li


def _get_integer(roman_s: str) -> int:

    integer_marker = 0

    for integer, roman_val_item in NUMBERS.items():
        if roman_val_item == roman_s:
            return integer

        if isinstance(roman_val_item, tuple):
            for roman_val in roman_val_item:
                if roman_val == roman_s:
                    return integer

    # return 0
    lt, lh, ld, li = _parse_number(roman_s)

    return lt * 1000 + lh * 100 + ld * 10 + li




class RomanNumeral:

    def __init__(self, value):
        self.value = value

    def __int__(self):
        return _get_integer(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"RomanNumeral({self.value!r})"

    @staticmethod
    def from_int(number):
        return NUMBERS[number]
