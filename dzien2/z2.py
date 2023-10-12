artykuly = {'a1': ("artykuł1", 5.0), 'a2': ("artykuł2", 10.0), 'a3': ("Karty do gry", 20.0)}


def pozycja_faktury(lp, artykul_opis, ilosc, cena):
    # print(f"{lp} {artykul_opis} {ilosc} {cena} {cena * ilosc}")
    return lp + 1, (lp, artykul_opis, ilosc, cena, cena * ilosc)


pozycje = []
lp = 1
while True:
    a = input("Proszę podać artykuł: ")
    if a in artykuly:
        i = input("Proszę podać ilość: ")
        lp, pozycja = pozycja_faktury(lp, artykuly[a][0], i, artykuly[a][1])
        pozycje.append(pozycja)
    elif a == "":
        print("Dziękujemy za skorzystanie z programu")
        break
    else:
        print("Artykuł nie istnieje")

naglowek = ('Lp', 'Artykuł', 'ilość', 'cena jednostkowa', 'wartość')
print("{:>4}{:^20}{:<5}{:>6}{:>10}".format(*naglowek))
suma = 0.0
for pozycja in pozycje:
    print("{:>4}{:^20}{:<5}{:>6}{:>10}".format(*pozycja))
    suma += pozycja[4]
print(f'Razem: {suma}')
