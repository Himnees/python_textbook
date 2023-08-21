# Importing the array Module

# Program 1: A python program to create an integer type array.
import array
a = array.array('i',[5,6,7,8,9,10])
print('The array elements are:')
for elements in a:
    print(elements)
    # or
import array as arr
a = arr.array('i',[5,6,7,8,9,10])
print('The array elements are:')
for elements in a:
    print(elements)

# Program 2: A python program to create an integer type array.
from array import *
a = array('i',[1,2,3,4,5,6,7])
print('The array elements are:')
for elements in a:
    print(elements)

# Program 3: A python program to create array with group of characers
from array import *
a = array('u',['a','d','f','g','h','j'])
print('The array elements are:')
for i in a:
    print(i)

# Program 4: A python program to create one array from annother array.
from array import *
arr1=array('d',[1.5,4.3,5,7.3])

# use same typecode and multiply each element of arr1 with 3
arr2=array(arr1.typecode,(a*3 for a in arr1))
print('The array2 elements are:')
for i in arr2:
    print(i)