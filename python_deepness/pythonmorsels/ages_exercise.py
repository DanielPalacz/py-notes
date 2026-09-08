from datetime import datetime


def get_age(birthdate: str) -> int:
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()

    age = today.year - birthdate.year

    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age


def is_over(age: int, birthdate: str) -> bool:
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    try:
        limit = birthdate.replace(year=birthdate.year + age)
    except ValueError:
        limit = birthdate.replace(
            year=birthdate.year + age,
            day=28,
        )

    return datetime.now() >= limit


x1 = is_over(18, '2007-03-15')
x2 = is_over(18, '1982-02-01')
x3 = is_over(17, '2008-02-29')

y1 = get_age('1982-02-01')
