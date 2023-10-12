# def wyswietl(parametr):
#     print(f"wyswietlam {parametr}")
#     print("wyswietlam {0}".format(parametr))
#     if parametr[0] == 'a':
#         kod_powrotu = 1
#     else:
#         kod_powrotu = 0
#     # print(f"wynik to {kod_powrotu}")
#     return kod_powrotu
#
#
# def wyswietl1(parametr):
#     if parametr[0] == 'a':
#         return 1
#     else:
#         return 0
#
#
# def wyswietl2(parametr):
#     if parametr[0] == 'a':
#         return 1
#     return 0
#
#
# rc = wyswietl2("par1")
# print(rc)


def kodujZnak(znak):
    if znak.islower():
        return ord(znak) - 96
    if znak.isupper():
        return ord(znak) - 38
    else:
        return ord(znak) + 100


def kodujString(string):
    odp = ""
    for x in string:
        odp = f"{odp}{kodujZnak(x)} "
    return odp[:-1]


print(kodujZnak("z"))
print(kodujZnak("a"))
print(kodujZnak("A"))
print(kodujZnak("Z"))
print(kodujString("Test zdania"))
# Funkcja kodująca a=>1 .. z=>26?