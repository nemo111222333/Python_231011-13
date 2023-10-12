import os
import shutil

# ToDo: Ścieżkę wejściową i wyjściową pobrać jako parametr wywołania pliku Pythona
#       python dzien2/z1.py dzien2/Dane dzien2/Wyniki


def lista(sciezka):
    lista_plikow = os.listdir(sciezka)
    lista_katalogow = []
    # print(lista_plikow)
    for plik in lista_plikow:
        sciezka_do_pliku = os.path.join(sciezka, plik)
        # print(plik)
        if os.path.isdir(sciezka_do_pliku):
            # print("to jest katalog")
            lista_katalogow.append(sciezka_do_pliku)
        elif os.path.isfile(sciezka_do_pliku):
            pass
            # print("to jest plik")
        else:
            # print("to nie jest plik lub katalog")
            pass
        # print(os.getcwd())
        # p = open(plik, "r")
    return lista_katalogow


lista_katalogow = lista("Dane")
print(lista_katalogow)

for katalog in lista_katalogow:
    # print(os.path.basename(katalog))
    shutil.make_archive(os.path.join("Wynik", os.path.basename(katalog)), "zip", katalog)
