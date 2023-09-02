# Anonymous Function or Lamdas

# Program 28: A python programer to create a lamda function that returns a square alue of a given number
f=lambda x: x*x 
print(f(5))

# Program 29: A lamda function to calculae he sum of two numbers.
f=lambda x,y:x+y
print(f(12,34))

# Progam 30: A lamda function to find the bigger number in two given numbers
max=lambda x,y:x if x>y else y
print(max(23,34))

# Using Lambdas with filer() Function
# synax: filter(function,sequence)
# Program 31: A python program using filter() to filter out een numbers from a list
def is_even(x):
    if x%2==0:
        return True
    else:
        return False
lst=[10,11,12,13,14,15,16]
lst1=list(filter(is_even,lst))
print(lst1)

# Program 32: A lambda that returns even numbers from a list
lst2=list(filter(lambda x:(x%2==0),lst))
print(lst2)

# Using Lambdas with map() Function
# syntax: map(function,sequence)

# Program 33: A python program to find square of elements in list.
def square(x):
    return x*x
lst=[1,2,3,4,5]
lst1=list(map(square,lst))
print(lst1)

# Program 34: A lambda function hat returns squares of elements in a list.
lst2=list(map(lambda x:(x*x),lst))
print(lst2)

# Program 35: A python program to find the products of elements of two different lists using lambda function.
l1=[1,2,3,4,5]
l2=[2,4,6,8,10]
l3=list(map(lambda x,y:(x*y),l1,l2))
print(l3)

# Using lambdas with reduce() functin
# Program 36: A lambda function to calculate products of elements of a list.
from functools import *
l=[1,2,4,3,5]
result=reduce(lambda a,b:(a*b),l)
print(result)
        
sum=reduce(lambda a,b:(a+b),range(1,51))
print(sum)