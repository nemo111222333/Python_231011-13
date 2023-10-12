import os
import matma
import matma as m

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


def answer(question):
    # return "odpowiedz"
    return len(question)


plik = open("in.txt", "r", encoding="utf-8")
data = plik.read()
lines = data.split("\n")
i = 1
for line in lines:
    if line:
        print(f"{line} => {answer(line)}")
    else:
        print(f"błąd w linii nr {i}")
    i += 1
plik.close()