# Nested Lists

# Program 11: A python program to create a nested list and display its elements.
list=[10,20,30,[80,90]]
print('Total list=',list)
print('First element= ',list[0])
print('Last element= ',list[3])
for x in list[3]:
    print(x)

# Program 12: A python program to retrieve elements from a matrix and display them.

mat = [[1,2,3],[4,5,6],[7,8,9]]
print('Display the list as it is: ')
print(mat)

print('Display row by row: ')
for r in mat:
    print(r)

print('Display column by row0: ')
for c in mat[0]:
    print('%d '%c,end='')
print()

print('Display column by row 1: ')
for c in mat[1]:
    print('%d '%c,end='')
print()

print('Display column by row2: ')
for c in mat[2]:
    print('%d '%c,end='')
print()

print('Display all elements using for: ')
for r in mat:
    for c in r:
        print(c, end=' ')
    print()

print('Display all elements using for: ')
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print('%d'%mat[i][j],end='')
    print()

# Program 13: A python program to add two matrices and display the sum matriix using list
m1=[[1,2,3,0],
    [4,5,6,0],
    [7,8,9,0]]

m2=[[1,2,3,4],
    [0,1,0,1],
    [2,-1,-2,1]]

m3=[4*[0] for i in range(3)]
for i in range(3):
    for j in range(4):
        m3[i][j]=m1[i][j]+m2[i][j]

for i in range(3):
    for j in range(4):
        print('%d ' %m3[i][j],end='')
    print()