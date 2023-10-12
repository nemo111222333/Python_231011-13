# def dodaj(a, b):
#      return a + b
#
#
# print(dodaj(1,3))
#
#
#dodaj1 = lambda a, b: a + b
# print(d(1,3))
#
# kw = lambda x: x*x
# kw1 = lambda x: x**2
# dziel_sume = lambda x, y, z: (x+y)/z


# values = dict(one=1, two=2, three=3)
# print(values)
# print(sorted(values))
# print(sorted(values.items()))
# print(sorted(values.items(), key=lambda item: item[0]))
# print(sorted(values.items(), key=lambda item: item[1]))

def suma(a, b, c, d=0, e=0):
    return a + b + c + d + e


def suma1(*params):
    s = 0
    for param in params:
        s += param
    return s

print(suma(1, 2, 3))

print(suma1(1, 2, 3, 4, 5, 6))
