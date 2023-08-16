# The for loop
'''Syntax for for_loop
   for var in sequence:
        statements
        '''
# Program 12: A python program to display character of a string using for loop.
str='Hello'
for ch in str:
    print(ch)

# Program 13: A python program to display each character from a string using sequence index.
str='Hello'
n=len(str)
for i in range(n):
    print(str[i])

# Program 14: A python program to display odd number from 1 to 10 using range object.
for i in range(1,10,2):
    print(i)

# Program 15: A python program to display numbers from 10 to 1in decending order.
for i in range(10,0,-1):
    print(i)

# Program 16: A program to display the elements of a list using for loop
lst=[10,24.5,'Him','a']
for elements in lst:
    print(elements)

# Program 17: A progra, to display and find the sum of a list of number using for loop.
l1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in l1:
    print(i)
    sum+=i
print('sum= ',sum)
