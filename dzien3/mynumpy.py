import numpy as np

lista = [1,2,3,4,5,6,7,8,9,10]
# print(np.mean(lista))
# print(np.median(lista))
# print(np.std(lista))
# print(np.var(lista))
# print(np.min(lista))
# print(np.max(lista))

print(lista)
t1 = np.array([1,2,3,4,5,6,7,8,9,10])
t2 = t1 * 2
t3 = t1 + t2

print(t1)
print(t2)
print(t3)

for liczba in t1:
    print(liczba)

t4 = np.arange(100,1000, 100)
print(t4)

t5 = np.zeros(10)
print(t5)

print(np.random.random(10))

print(np.full(10,'a'))

print(t3[:4])
print(t3.shape)

t6 = np.array([[1,2,3,4,5], [1,2,3,4,5]])
print(t6)
print(t6.shape)