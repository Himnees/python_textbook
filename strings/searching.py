# Searching in the string
# Program 11: A python program to search for the position of a string in a given group of strings
str=[]
n=int(input('How many strings?:'))
for i in range(n):
    print('Enter the string :',end='')
    str.append(input())
s=input('Enter the string to search:')
flag=False
for i in range(len(str)):
    if s==str[i]:
        print('String found at ',i+1)
        flag=True
if flag==False:
    print('String not found')