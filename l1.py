# lista2 = ["ala", "ma", "kota", 1, 1, 4.5, True]
# print(lista2)
#
# print(lista2[1])
# print(lista2[1:3])
# print(lista2[1:])
# print(lista2[1:-1])
# print(lista2[1:-2])
# print(lista2[:-2])
#
# napis = "ala ma kota"
# print(napis[1])
# print(napis[:-1])

# inicjalizacja zbiorów
# klasa = {"Marek", "Janek", "Ania", "Ewa", "Marek", "Ania"}
# print(klasa)
#
# liczba = float("10")
# print(liczba)
# # a teraz zbiór znaków ze stringa 
# czar = set("czabunagunga")
# # czarl = list("czabunagunga")
# # czars = "czabunagunga"
# print(czar)
# # print(czarl)
# # print(czars)
# inny_czar = set("abrakadabra")
# print(inny_czar)
# print(czar - inny_czar)
# # są w czar, ale nie ma w inny_czar 
# print(czar.difference(inny_czar))
# # # to samo, ale inaczej 
# print(inny_czar - czar)
# # # to nie to samo, jak wiadomo z teorii 
# print(czar | inny_czar)
# # # znaki w czar lub inny_czar lub obu 
# print(czar & inny_czar)
# # # przecięcie czyli część wspólna 
# print(czar.intersection(inny_czar))
# # # można tak 
# print(czar ^ inny_czar)
# # # różnica symetryczna

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
print(dict1)
print(dict1["a"])

dni_tygodnia = {"poniedziałek": 1, "wtorek": 2, "sroda": 3, "czwartek": 4, "piątek": 5, "sobota": 6, "niedziela": 7}
print(dni_tygodnia)
print(dni_tygodnia.keys())
print(dni_tygodnia.values())
keys = list(dni_tygodnia.keys())
print(keys)
print(keys[0])
print(dni_tygodnia[keys[0]])

