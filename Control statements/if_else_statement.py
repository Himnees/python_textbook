# The if ... else Statement
''' The syntax of if ...else statement:
         if condition:
             statements
         else:
             statements       '''

# Program 4: A python program to test whether a number is even or odd.
# To know if a given number is even or odd
x=10
if x % 2 == 0:
    print(x,'is even number')
else:
    print(x,'is odd number')

# Program 5: A python program tp accept a number from the keyboard and test whether it is even or odd.
x = int(input('Enter the number: '))
if x%2==0:
    print(x,'is even number')
else:
    print(x,'is odd number')

# Program 6: A python program to test whether a given number is between 1 and 10
# Using and in if...else statement
x = int(input('Enter the number:'))
if x>=1 and x<=10 :
    print(x,'is between 1 and 10')
else:
    print(x,'is not between 1 and 10')

   