# Function Decorators

# Program 37: A decorator to increase the value of a function b 2
def decor(fun):
    def inner():
        value=fun()
        return value+2
    return inner()
def num():
    return 10
result=decor(num)
print(result)

# Program 38: A python progam to apply a decorator to a function using @ symbol.
def decor(fun):
    def inner():
        value=fun()
        return value+2
    return inner
@decor
def num():
    return 20
print(num())

# Prgram 39: A python program to create two decorator
def decor(fun):
    def inners():
        value=fun()
        return value+2
    return inners()
def decor1(fun):
    def inner():
        value=fun()
        return value*2
    return inner()
def num():
    return 10
result=((decor(decor1(num))))
print(result)