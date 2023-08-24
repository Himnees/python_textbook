# Indexing in string
# Program 1: A python program to access each element of a string in forward and reverse orders using while loop.
str='Core Python'
n=len(str)
i=0
while i<n:
    print(str[i],end='')
    i+=1
print()
i=-1
while i>=-n:
    print(str[i],end='')
    i-=1
    # or
print()
i=1
while i<=n:
    print(str[-i],end='')
    i+=1
print()
# Program 2: A program to access the characters of a tring using for loop.
str = 'Core Python'
for i in str:
    print(i,end='')
print()   
for i in str[::-1]:
    print(i,end='')
    