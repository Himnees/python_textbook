# Program 11: A python program to sort the array element using bubble sort technique.
from array import *
a=array('i',[])

# store element into the array
print('How many elements: ',end='')
n = int(input()) # accept input into n
for i in range(n): # repeat for n times
    print('Enter the numbers:')
    a.append(int(input())) #badd the element to the array x

print('Orginal array:',a)
# buble sort
flag=False # when swapping is done, flag becomes rue
for i in range(n-1): # i is from 0 to n-1
    for j in range(n-1-i): # j is from 0 to one element less than i
        if a[j]>a[j+1]: # swap j and j+1 elements
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
            flag=True # swapping done, hence flag is True
    if flag==False: # no swapping means array is in sorted order
        break #come out of inner for loop
    else:
        flag=False # assign intial value to flag
print('Sorted array :',a)
