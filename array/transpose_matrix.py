# Transpose of a Matrix

# Program 37: A python program to accept a matrix from the keyboard and display transpose matrix

from numpy import *
r,c =[int(x) for x in input('Enter number of rows and columns:').split(' ')]
str=input('Ener the matrix:\n')
x=reshape(matrix(str),(r,c))
print('The orginal matrix:')
print(x)
print('The transpose matrix:')
y=x.transpose()
z=x.getT()
print(y)
print(z)
