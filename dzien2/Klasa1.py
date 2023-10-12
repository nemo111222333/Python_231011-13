class Czlowiek:
    def __init__(self, imie, nazwisko, wiek, wzrost, kolor_oczu, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.wzrost_cm = wzrost
        self.kolor_oczu = kolor_oczu
        self.plec = plec
        if plec == "mezczyzna":
            if wiek >= 65:
                self.emeryt = True
            else:
                self.emeryt = False
        else:
            if wiek >= 60:
                self.emeryt = True
            else:
                self.emeryt = False
        self.znany = False
        self.dlugosc_wlosow = None

    @property
    def wzrost(self):
        return self.wzrost_cm / 100
    @wzrost.setter
    def wzrost(self, nowy_wzrost):
        if (nowy_wzrost < 100):
            self.wzrost_cm = nowy_wzrost*100
        else:
            self.wzrost_cm = nowy_wzrost

    def wyswietl(self):
        print(f"{self.imie} {self.nazwisko} {self.wiek}lat {self.wzrost_cm}cm [{self.wzrost}m] {self.kolor_oczu} {self.plec} {self.emeryt} znany? {self.znany} dlugosc włosów: {self.dlugosc_wlosow}")

    def poznaj(self):
        self.znany = True
        self.dlugosc_wlosow = 120


inny = Czlowiek("Maria", "Nowak", 60, 170, "czarny", "kobieta")
inny.poznaj()
inny.wyswietl()

# print(inny.wzrost)
# inny.wzrost = 180
# print(inny.wzrost)
inny.wzrost = 2.1
inny.wyswietl()

przestepca = Czlowiek("Jan", "Kowalski", 40, 180, "biały", "mezczyzna")
przestepca.wyswietl()
przestepca.wzrost = 160
przestepca.wyswietl()

