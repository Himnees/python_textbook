# Comparing arrays
# Program 25: A python program to compare two arrays and display the resultant Boolean type array
from numpy import *
a= array([1,2,3,4])
b=array([0,2,3,1])
c = a==b
print('Result a==b :',c)
c=a>b
print('Result a>b :',c)
c=a<b
print('Result a<b :',c)
c>=b
print('Result a>=b :',c)
c<=b
print('Result a<=b :',c)

# Program 26: A python program to know he effects of any() and all() functions.
from numpy import *
a= array([1,2,3,4])
b=array([0,2,3,1])
c=a>b
print('result:',c)
print('check any one element is coomon:',any(c) )
print('check all element is coomon:',all(c) )
if(any(a>b)):
    print('a contains atleast one element of b')

# Program 27: A python program to understand the use of logical functions in array.
from numpy import *
a= array([1,2,3,4])
b=array([0,2,3,1])

c= logical_and(a>0,a<4)
print(c)
c= logical_or(b>=0,b==1)
print(c)
c=logical_not(b)
print(c)

# Where() function
# syntax: where(condiion,expression1,expression2)
# Program 28: A python program to use where function 
from numpy import *
a=array([10,21,30,41,50],int)
c=where(a%2==0,a,0)
print(c)
b=array([1,21,3,40,51])
c=where(a>b,a,b)
print(c)

# Program 29: A python program to retrieve non zero element from an array.
from numpy import *
a=array([1,2,0,-1,0,6],int)
c= nonzero(a)
for i in c:
     print(i) # returns indexes
     print(a[c]) # displays elements
     