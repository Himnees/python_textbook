# Program 12: A python program to search for the position of an element in an array using sequential search.
from array import *
x=array('i',[])
print('How many elements:')
n = int(input())
for i in range(n):
    print('Enter the elements:')
    x.append(int(input()))
print('Orginal array: ',x)
print('Enter the element to be found:')
s=int(input())
flag=False
for i in range(len(x)):
    if s==x[i]:
        print('Element found at location :',i+1)
        flag=True
if flag==False:
    print('Element not found')

# Program 13: A pthon program to search for the posiion of an element in an array using index() method.
from array import *
x=array('i',[])
print('How many elements:')
n = int(input())
for i in range(n):
    print('Enter the elements:')
    x.append(int(input()))
print('Orginal array: ',x)
print('Enter the element to be found:')
s=int(input())
try:
    pos = x.index(s)
    print('Location found at',pos+1)
except ValueError:
    print('Not found in the array')