# The except block
# Program 11: A python program to understand the usage of try with finally block.
try:
    x=int(input('Enter a number:'))
    y=1/x

finally:
    print('We are not catching the exception.')
print("The inverse is",y)