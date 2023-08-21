# Viewing and Copying Arrays

# Program 31: A pyhon program to create a view of an existing array.

from numpy import *
a=arange(1,6)
b=a.view()
print('Orginal array:',a)
print('New array:',b)
b[0]=23
print('Orginal array:',a)
print('New array:',b)


# Program 32: A python program to copy an array as another array.

from numpy import *
a=arange(1,6)
b=a.copy()
print('Orginal array:',a)
print('New array:',b)
b[1]=100
print('Orginal array:',a)
print('New array:',b)
