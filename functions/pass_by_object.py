# Program 13: A python program to pass an integer to a function and modify it.
def modify(x):
    """ reassign a value to the variable """
    x=15
    print(x, id(x))

x=10
modify(x)
print(x, id(x))

# Program 14: A python program o pass a list to a function and odify it.
def modify(lst):
    ''' to add new element to list '''
    lst.append(9)
    print(lst, id(lst))

lst=[1,2,3,4]
modify(lst)
print(lst, id(lst))
print()

# Program 15: A python program to create a new object insidee the function does not modify outside object.
def modify(lst):
    """ to create a new lst"""
    lst=[10,20,30,40]
    print(lst, id(lst))

lst=[1,2,3,4]
modify(lst)
print(lst, id(lst))
print()
