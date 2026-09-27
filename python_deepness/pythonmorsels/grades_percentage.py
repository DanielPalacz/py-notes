from typing import Union


def percent_to_grade(percentage: Union[float, int], *, suffix: bool = False) -> str:
    if suffix:

        if percentage < 60:
            return "F"
        elif 60 <= percentage < 63:
            return "D-"
        elif 63 <= percentage < 67:
            return "D"
        elif 67 <= percentage < 70:
            return "D+"

        elif 70 <= percentage < 73:
            return "C-"
        elif 73 <= percentage < 77:
            return "C"
        elif 77 <= percentage < 80:
            return "C+"

        elif 80 <= percentage < 83:
            return "B-"
        elif 83 <= percentage < 87:
            return "B"
        elif 87 <= percentage < 90:
            return "B+"

        elif 90 <= percentage < 93:
            return "A-"
        elif 93 <= percentage < 97:
            return "A"
        elif 97 <= percentage:
            return "A+"

    if percentage < 60:
        return "F"
    elif 60 <= percentage < 70:
        return "D"
    elif 70 <= percentage < 80:
        return "C"
    elif 80 <= percentage < 90:
        return "B"
    elif percentage >= 90:
        return "A"

    return None