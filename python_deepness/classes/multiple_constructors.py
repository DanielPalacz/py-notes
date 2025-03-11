class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    @classmethod
    def z_danych_tekstowych(cls, dane_tekstowe):
        """
        Alternatywny konstruktor, który tworzy obiekt Osoba z ciągu tekstowego.
        """
        imie, wiek = dane_tekstowe.split(",")
        return cls(imie, int(wiek))

    @classmethod
    def z_listy(cls, lista_danych):
        """
        Alternatywny konstruktor, który tworzy obiekt Osoba z listy.
        """
        if len(lista_danych) != 2:
            raise ValueError("Lista powinna zawierać imię i wiek.")
        return cls(lista_danych[0], lista_danych[1])

    def przedstaw_sie(self):
        return f"Nazywam się {self.imie} i mam {self.wiek} lat."

# Użycie standardowego konstruktora
osoba1 = Osoba("Anna", 30)
print(osoba1.przedstaw_sie())

# Użycie alternatywnego konstruktora z danych tekstowych
dane_tekstowe = "Piotr,25"
osoba2 = Osoba.z_danych_tekstowych(dane_tekstowe)
print(osoba2.przedstaw_sie())

#uzycie alternatywnego konstruktora z listy
lista_danych = ["Marek", 40]
osoba3 = Osoba.z_listy(lista_danych)
print(osoba3.przedstaw_sie())

#uzycie niepoprawnej listy
try:
    lista_bledna = ["Jan"]
    Osoba.z_listy(lista_bledna)
except ValueError as e:
    print(f"Błąd: {e}")
