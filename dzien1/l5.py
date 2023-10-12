import os
import matma
import matma as m
import random
import sys

# sciezka = os.getcwd()
# print(sciezka)
# sciezka_do_pliku = os.path.join(sciezka, "plik.txt")
# print(sciezka_do_pliku)
# print(os.path.split(sciezka_do_pliku))
#
# print(matma.dodaj(1, 2))
# print(m.mnoż(2,3))
# print(m.dodaj(1.5, 2.5))
# print(m.dodaj("ala","kot"))


odp = ["odpowiedź 1", "odpowiedź 2", "odpowiedź 3", "odpowiedź 4", "odpowiedź 5", "odpowiedź 6", "odpowiedź 7",
       "odpowiedź 8", "odpowiedź 9", "odpowiedź 10"]
def answer(question):
    # return "odpowiedz"
    #return len(question)
    return random.choice(odp)


def przetworz(lines, wynik=sys.stdout, blad=sys.stderr):
    i = 1
    for line in lines:
        if line:
            print(f"{line} => {answer(line)}", file=wynik)
        else:
            print(f"błąd w linii nr {i}", file=blad)
        i += 1


plik = open("in.txt", "r", encoding="utf-8")
data = plik.read()
plik.close()
lines = data.split("\n")
wynik = open("out.txt", "w", encoding="utf-8")
blad = open("error.txt", "w", encoding="utf-8")
# przetworz(lines, wynik, blad)
przetworz(lines, wynik=wynik, blad=blad)
wynik.close()
blad.close()
