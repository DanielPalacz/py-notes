# zen2.py
"""
Zen of Python 2.0 — praktyczne dobre praktyki w Pythonie (wersja kolorowa ANSI).
"""

RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"

ZEN2_TEXT = f"""
{BOLD}{MAGENTA}🐍 Zen of Python 2.0 — praktyczny kodeks dobrych praktyk{RESET}

{YELLOW}1.{RESET} Piękno jest ważne, ale czytelność jest obowiązkowa.
   {CYAN}Kod czyta się częściej, niż pisze. Zadbaj o wcięcia (4 spacje), spójne formatowanie i sensowne białe znaki.{RESET}

{YELLOW}2.{RESET} Nazwy mówią same za siebie.
   {CYAN}user_count jest lepsze niż uc.
   Funkcje → snake_case, Klasy → PascalCase, Stałe → UPPER_CASE.{RESET}

{YELLOW}3.{RESET} Proste jest lepsze niż skomplikowane, ale jawne jest lepsze niż ukryte.
   {CYAN}Unikaj „magii” w kodzie. Lepiej dopisać dwie linie, niż tworzyć zagadkę.{RESET}

{YELLOW}4.{RESET} Komentarze wyjaśniają DLACZEGO, a nie CO.
   {CYAN}Kod sam pokazuje „co” się dzieje. Komentarz powinien mówić o powodach lub kontekście.{RESET}

{YELLOW}5.{RESET} Docstring jest instrukcją obsługi.
   {CYAN}Używaj PEP257: trzy cudzysłowy, krótki opis w pierwszej linii, szczegóły poniżej.{RESET}

{YELLOW}6.{RESET} Linia powinna mieścić się w 79 znakach (PEP8).
   {CYAN}Dzięki temu kod jest czytelny nawet w terminalu i na podzielonym ekranie.{RESET}

{YELLOW}7.{RESET} Jedna rzecz na raz.
   {CYAN}Każda funkcja powinna robić jedną rzecz dobrze. Jeśli jest za długa, podziel ją.{RESET}

{YELLOW}8.{RESET} Lepiej mieć jedną oczywistą drogę niż kilka chytrych skrótów.
   {CYAN}Jeśli problem można rozwiązać prostą konstrukcją for-loop, nie musisz od razu pisać trzech comprehensionów w jednej linii.{RESET}

{YELLOW}9.{RESET} Bądź konsekwentny w całym projekcie.
   {CYAN}Jeśli formatujesz kod black-iem, rób to wszędzie. Jeśli używasz flake8, nie ignoruj błędów.{RESET}

{YELLOW}10.{RESET} Automatyzuj dobro, zanim złe się rozrośnie.
    {CYAN}Używaj linters (flake8, pylint), formatterów (black), testów (pytest) i type checkerów (mypy) od początku projektu.{RESET}

{YELLOW}11.{RESET} Nie bój się refaktoryzacji.
    {CYAN}Kod się starzeje. Lepiej go czasem posprzątać, niż łatać dziury.{RESET}

{YELLOW}12.{RESET} Eksperymentuj w REPL-u, ale utrwalaj w testach.
    {CYAN}Interaktywny interpreter to poligon, ale ostateczne rozwiązania powinny mieć testy jednostkowe.{RESET}
"""

def __repr__():
    print(ZEN2_TEXT)
    return ''

print(ZEN2_TEXT)
