# Prgram 39: A python program to create two decorator
def decor(fun):
    def inner():
        value=fun()
        return value+2
    return inner
def decor1(a):
    def inner():
        value=a()
        return value*2
    return inner
def num():
    return 10
a=decor(decor1(num))
print(a())

# Program 40: A python program to apply two decorators to the same function using @ symbol.
def decor(Spoorti):
    def inner():
        value=Spoorti()
        return value+2
    return inner
def decor1(Himneesh):
    def inner():
        value=Himneesh()
        return value*2
    return inner
@decor
@decor1
def num():
    return 10
print(num())
