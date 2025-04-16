from typing import Generator, Optional


DB_FILEPATH = "/"


# Generator[yield_type, send_type, return_type]
# def iterate_over_csv_db_file(db_filepath: str | None = None) -> Generator[list[str], None, None]:

def iterate_over_csv_db_file(db_filepath: Optional[str] = None) -> Generator[list[str], None, None]:
    """Iterates line-after-line over content of DB file

    Uses DB with default file name: DB_FILENAME

    Yields:
        list: line content split to list as following:
              [line_number, company_name, krs_number, main_pkd, other_pkd, email, www, voivodeship, address]
    """
    if db_filepath is None:
        db_filepath = DB_FILEPATH

    with open(db_filepath, "r", encoding="utf-8") as companies_file:
        for line in companies_file:
            split_line = line.replace("\n", "").split(";")
            # line_number, company_name, krs_number, main_pkd, other_pkd, email, www, voivodeship, address = split_line
            yield split_line


def sum_numbers() -> Generator[None, int | None, int]:
    """Coroutine zliczająca sumę przesyłanych liczb.

    Wysyłaj liczby typu `int` za pomocą `send()`, a `None` zakończy działanie i zwróci sumę.
    """
    total = 0
    while True:
        x = yield
        if x is None:
            break
        total += x
    return total

# yield bez wartości sprawia, że coroutine "czeka" na dane przez send(x)
# int | None oznacza, że może przyjąć zarówno liczbę, jak i None
# return total zwróci sumę po zakończeniu coroutine (dostaniu None)
