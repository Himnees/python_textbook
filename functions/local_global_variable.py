# Local and Global variable
def myfunction():
    a=1 # this is local var
    a+=1
    print(a)
myfunction()
try:
    print(a)
except NameError:
    print('a is not available')
print()
a=1
def myfunction():
    b=2 # this is local var
    print(b)
    print(a)

try:
    myfunction()
    print(a)
    print(b)
except NameError:
    print('b is not available')
print()
# Program 21: A python program to understand global and local variable
a=1 # this is global variable
def myfunction():
    a=2
    print('a=',a)
myfunction()
print('a=',a)
print()
# Program 22: A python program to access global variable inside a function and modify it.
a=1
def function():
    global a
    print('global a =',a)
    a=2
    print('modified a =',a)
function()
print('a=',a)
print()

# Program 23: A python program to get a copy of global variable into a function and work with it.
a=1
def my_function():
    a=2
    x=globals()['a']
    print('Global a =',x)
    print('lacal var =',a)
my_function()
print('a=',a)
print()


