# Indexing and slicing on array
# Program 5: A python program to retrieve the elements of an array using array index.
from array import *
x = array('i',[1,2,3,4,5,6])

# find the of elements in the array
n = len(x)

# display array elements using indexing
for i in range(n):
    print(x[i], end=' ')
print()

# Program 6: A python program to retrieve elements of an array using while loop.
from array import *
x=array('i',[1,2,3,4,5,6])
n=len(x)
i=0
while i<n:
    print(x[i],end=' ')
    i+=1

# Program 7: A python program that helps to know the effects of slicing operation on an array.
from array import *
x=array('i',[10,20,30,40,50,60,70,80,90,100])
y=x[1:4]
print(y)

y=x[0:]
print(y)

y=x[-4:]
print(y)

y=x[-4:-1]
print(y)

y=x[0:7:2]
print(y)

# Program 8: A python program to retrieve and display only a range of elemens for an array using slicing.
from array import *
x=array('i',[10,20,30,40,50,60,70,80,90,100])
for i in x[2:6]:
    print(i)