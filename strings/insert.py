# Inserting sub string into a string
# Program 14: A python program to insert a sub string in a string in a particular position.
str=input('Enter the string:')
sub=input('Ener the sub string:')
n=int(input('Enter position no.: '))
n-=1
l1=len(str)
l2=len(sub)
str1=[]
for i in range(n):
    str1.append(str[i])
for i in range(l2):
    str1.append(sub[i])
for i in range(n,l1):
    str1.append(str[i])

str1=''.join(str1)
print(str1)