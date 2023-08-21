# Matrix addition and multiplication
from numpy import *
a= matrix('1 2 3;4 5 6')
b=matrix('2,2,2;1 -1 2')
print(a,'\n')
print(b,'\n')
print(a+b,'\n')
print(a/b,'\n')

# Program 38: A python program to accept two matices and find their product.
import sys
from numpy import *
r1,c1=[int(x) for x in input('Enter rous and columns:').split()]
r2,c2=[int(y) for y in input('Enter rous and columns:').split()]
if c1!=r2:
    print('Multiplication not possible.')
    sys.exit()
str1=input('Enter the matrix elements:')
a=reshape(matrix(str1),(r1,c1))
str2=input('Enter the matrix elements:')
b=reshape(matrix(str2),(r2,c2))
c=a*b
print(c)
