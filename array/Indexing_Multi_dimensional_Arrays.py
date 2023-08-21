# Indexing in Multi-dimensional Arrays
# Program 35: A python program to retrieve the elements from 2d array display using for loop
from numpy import *
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(len(a)):
    print(a[i])
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')

# Program 36: A python program to retrieve the elemnts from 3d array.
from numpy import *
a=[[[1,2,3,4],[4,5,6,7,8]],[[6,7,8,9],[1,2,3,4]],[[3,2,1,3],[4,5,6,7]]]
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k])
        print()
    print()
