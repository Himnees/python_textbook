# Sorting of string
# Program 10: A python program to sort a group of strings into alphabetical order
str=[]
n=int(input('How many srings?:'))
for i in range(n):
    print('Enter string: ',end='')
    str.append(input())

str.sort()
str1=sorted(str)
print('\nThe sorted list:')
for i in str1:
    print(i)