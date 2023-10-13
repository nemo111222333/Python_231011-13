import os
def mul(a, b):
    try:
        return a * b
    except TypeError:
        return "Błędne typy dane"
        # exit(0)
    except(FileNotFoundError):
        print("Błąd pliku")
    else:
        print("Inny błąd")



# try:
    os.remove('xxxx.yyy')
# except IOError as Err:
#     print("Błąd", Err)



print(mul(1,2))
print(mul(10,"a"))
print(mul("a","x"))
print(mul(5,4))

a = [0,1]
print(a[2])
print("x" * "y")