# It is possible to write one loop inside another loop. For example, we can write a for loop inside a while loop or a for loop inside another for loop.
# A python program for neste loop.
for i in range(3):
    for j in range(4):
        print('i=',i,'\t','j=',j)

# Program 19: A python program that displays stars in right anglrd trianglar form uing nested loop
for i in range(1,11):
    for j in range(1,i+1):
        print('* ',end='')
    print()

# Program 20: A pyhton program that displays stars in right angled triangular form using a single loop
for i in range(1,11):
    print('* '*(i))


# Program 21: A python program to display the star in an equalateral triangular form using single for loop
n=40
for i in range(1,11):
    print(' '*n,end='')
    print('* '*i)
    n-=1

for i in range(1,11):
    print(' '*(n-i)+'* '*i)

# we will write program using nested loops to displaynumbers from 1 to 100 in 10 rows and 10 columns.
for x in range(1,11):
    for y in range(1,11):
        print(x*y,end='')
    print()

# Program 22: A python program to display numbers from 1 to 100 in a proper format.
for x in range(1,11):
    for y in range(1,11):
        print('{:8}'.format(x*y),end='')
    print()
    
    