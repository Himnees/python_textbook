# creating array using array()
# program 17: A python program to create a characer type array using with a group of characters.
from numpy import *
a=array(['a','s','d','f','g'])
print(a)

# Program : A python program to create a int and float type array using with a group of characters.
from numpy import *
a=array([1,2,3,4,5],int)
b=array([2,3,4,5,6])
c=array([10,20,30.4,5.6,3])
d=array([1,2,3,4,5],float)
print(a)
print(b)
print(c)
print(d)

# Program 18: A python program to create a string type array using numpy.
from numpy import *
arr=array(['Himneesh','loves','Spoorti'])
ar=array(['Spoorti','loves','Himneesh'],dtype=str)
print(arr)
print(ar)

# Program 19: A python program to creae an array from another array.
from numpy import *
a=array([1,2,3,4,5])
b=array(a) # create arrray using array() function
c=a #ccreate c by assigning a to c
print(a)
print(b)
print(c)

# Creating array using linspace
# Program 20: A python program to creating an array with 5 equal points using linspace
from numpy import *
a=linspace(0,10) # if n' is not ommited, then it is taken as 50.
print(a)
a=linspace(0,10,5)
print(a)

# Creating array using logspace
# logspace is similar to linspace produces evenly spaced poins on a logarithmically spaced scale.

# Program 21: A python program o create an array using logspace()
from numpy import *
b=logspace(1,4)
print(b)
b=logspace(1,4,5)
print(b)
for i in range(len(b)):
    print('%.1f '%a[i],end=' ')

# Creating Array using arrange() function
# syntax: arrange(start,stop,stepsize)

# Program 22: A python program to create an array using arange() function
from numpy import *
a=arange(10)
b=arange(5,10)
c=arange(1,10,3)
d=arange(2,11,2)
print(a)
print(b)
print(c)
print(d)

# Creating arrays using zeros() and ones() function

# Program 23: A python program to create arrays using zeros() and ones().
from numpy import *
a=zeros(5)
b=zeros(5,int)
c=zeros(5,float)
d=zeros(5,str)
print(a)
print(b)
print(c)
print(d)
a=ones(5)
b=ones(5,int)
c=ones(5,float)
d=ones(5,str)
print(a)
print(b)
print(c)
print(d)