artykuly = {'a1': ("artykuł1", 5.0), 'a2': ("artykuł2", 10.0), 'a3': ("Karty do gry", 20.0)}

while True:
    a = input("Proszę podać artykuł: ")
    if a in artykuly:
        i = input("Proszę podać ilość: ")
        print(artykuly[a][0])
        print(artykuly[a][1])
    elif a == "":
        print("Dziękujemy za skorzystanie z programu")
        break
    else:
        print("Artykuł nie istnieje")

# ToDo: Przygotować funkcję wypisującą w jednej linii elementy:
# lp, artykul, ilosc, cena jednostkowa, wartosc
