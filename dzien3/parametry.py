def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun(a=10, b=20, c=30)


def myfunPos(*args):
    for arg in args:
        print(arg)


myfunPos(10,20,30)
