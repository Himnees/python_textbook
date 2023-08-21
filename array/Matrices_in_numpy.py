# Marices in numpy
# matrix-name=matrix(2d array or string)
from numpy import *
arr=[[1,2,3],[4,5,6]]
a=matrix(arr)
print(a)

str ='1 2 3; 4 5 6;7 8 9'
print(matrix(str))
# Getting Diagonal Elements of a Matrix
# # a= diagonal(a) 
a=matrix('1 2 3;4 5 6;7 8 9')
print(a)
d=diagonal(a)
print(d)

# Finding Maximum and Minimum elements
big=a.max()
small=a.min()
print(big,'\n',small)

# Finding sum and average of element
print(a.sum())
print(a.mean())

# Products of elements
m=matrix(arange(12).reshape(3,4))
print(m)
a=m.prod(0) # cols wise
b=m.prod(1) # rows wise
print(a)
print(b)

# Sorting the matrix
# sort(matrix,axis)

m=matrix([[1,2,3],[4,1,0]])
print(m)

a=sort(m)
print(a)

b=sort(m,axis=0)
print(b)

a=sort(m,axis=1)
print(a)