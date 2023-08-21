# Slicing and Indexing in numpyArrays
# syntax: arrayname[start:stop:stepsize]

# Program 33: A python program to understand slicing operation on arrays.
from numpy import *
a=arange(10,16)
print(a)
b=a[1:6:2]
print(b)
c=a[::]
print(c)
d=a[:]
print(d)
e=a[-2:2:-1]
print(e)
f=a[:-2:] 
print(f)

# Program 34: A python program to rerieve and display elements of a numpy array using indexing.
from numpy import *
a=arange(11,18)
b=a[1:6:2]
print(a)
print(b)
i=0
while i<len(b):
    print(a[i])
    i+=1