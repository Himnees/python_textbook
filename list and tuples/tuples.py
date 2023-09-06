# Tuples
tup=1,3,4,5,6,32,3
t=tuple(sorted(tup))
print(t)

# Program 14: A python program in accept elements in the form of a tuple and display their sum and average
num=eval(input('Enter elements in ()')) 
sum=0
n=len(num)
for i in range(n):
    sum+=num[i]
print('Sum of numbers:',sum)
print('Average:',sum/n)

# Program 15: A python program to find the first occurance of an elemen.
str=input('Enter element:').split(',')
lst=[int(num) for num in str]
tup=tuple(lst)
print('Tuple is: ',tup)
ele=int(input('Enter elemen to search: '))
try:
    pos=tup.index(ele)
    print('Element at position no. :',pos+1)
except ValueError:
    print('Element not found')