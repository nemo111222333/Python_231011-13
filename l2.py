# liczba1 = 20
# liczba2 = 20
# if liczba1 < liczba2:
#     print("liczba1 jest mniejsza od liczba2")
#     print("druga linia")
# else:
#     if liczba1 > liczba2:
#         print("liczba1 jest wieksza od liczba2")
#     else:
#         print("liczba1 jest równa liczbie2")
#
# if liczba1 < liczba2:
#     print("liczba1 jest mniejsza od liczbie2")
# elif liczba1 == liczba2:
#     print("liczba1 jest rowna liczbie2")
# else:
#     print("liczba1 jest wieksza od liczbie2")
#
# dozwolone = {1, 2, 3, 20, 30}
# dozwoloneLista = [1, 2, 3, 20, 30]
#
# if liczba1 in dozwoloneLista:
#     print("liczba jest w dozwolone")
# else:
#     print("liczba nie jest w dozwolone")
#
# x = None
# y = ''
# z = 0
#
# if x:
#     print("x nie jest None")
# else:
#     print("x jest None")
#
# if y:
#     print("y nie jest None")
# else:
#     print("y jest None")
#
# if z:
#     print("z nie jest None")
# else:
#     print("z jest None")

# zakres = range(10)
# print(zakres)
# for i in zakres:
#     print(i)
#     # <0,10)
# zakres1 = ["a", "b", "c", "d", "e", "f"]
# print(zakres1)
# for litera in zakres1:
#     print(litera)

# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# print(dict1)
# for klucz in dict1:
#     print(klucz+"=>"+str(dict1[klucz]))
#     print(f"Dla klucza {klucz} mamy wartość => {dict1[klucz]}")
# print("koniec")

# warunek = 1
# while warunek < 5:
#     print(f"warunek {warunek} < 5 jest prawdziwy")
#     warunek += 1

x = 1
while True:
    print("Warunek jest prawdziwy")
    x += 1
    if x > 10:
        break
