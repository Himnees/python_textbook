# Defining a fuction
''' def function_name(para1,para2,....):
           "funcion docstring"
        function statement
        '''
# Program 1: A function that accepts two values and finds their sum.
def sum(a,b):
    """This function finds sum of two numbers"""
    c=a+b
    print(c)

sum(10,20)   # calling the function
sum(11.2,3.6)

# Program 2: A python program to find the sum of two numbers and return the result from the function
def sum(a,b):
    """This function finds sum of two numbers"""
    c=a+b
    return c
x=sum(12,34)
print(x)
y=sum(10.3,23.4)
print(y)

# Program 3: A function to test whether a number is even or odd
def even_odd(num):
    if num%2==0:
        print(num,'It is even')
    else:print(num,'is odd')
    return num
even_odd(12)
even_odd(13)

# Program 4: A python program to calculate factorial values of numbers.
def fact(n):
    ''' to find factorial value'''
    prod=1
    while n>=1:
        prod*=n
        n-=1
    return prod

for i in range(1,11):
    print('Factorial of {} is {}'.format(i,fact(i)))  

# Program 5: A python function to check if a given number is prime or not.
def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x
num=int(input('Enter the value:'))
result=prime(num) 
if result==1:
    print(num,'is a prime number')
else:
    print(num,'is not a prime number')

# Program 6: A python program that generates prime numbers with the help of a function to test prime or not
def prim(a):
        b=1
        for i in range(2,a):
            if a%i==0:
                b=0
            else:
                b=1
        return b
num=int(input('Enter the number:'))
result=prim(num)
if result==1:
    i=2
    c=1
    while True:
        if prim(i):
            print(i)
            c+=1
        i+=1    
        if c>num:
            break
