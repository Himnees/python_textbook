# Multi-Dimensional array
# Th array() fuction
from numpy import *
a=array([1,2,3,4,5])
b=array([[1,2,3,4],[4,5,6,7]])
print(a,'\n',b)

# The ones() and zeros() 

c=ones((3,4),int)
d=zeros((2,3),float)
print(c,'\n',d)

# The eye() function
e=eye(3)
f=eye(4,dtype=int)
print(e,'\n',f)
print('\n\n\n\n')

# The reshape() function

a=array([1,2,3,4,5,6])
b=reshape(a,(2,3))
print(b)
print('\n\n\n\n')
arr1=arange(12)
c=reshape(arr1,(3,2,2))
print(c)