# Input Statement
str = input() # this will wait until string is entered
print(str)
# It is a better idea t diplay a message to the user so that the user understands what to enter. This can be done by writing a message inside the input() function as:
str = input('Enter you name : ')
print(str)
# Once the value comes into the variable 'str', it can be converted into 'int' or 'float' etc. This is useful to accept number as:
s1 = input('Enter a number :')
x = int(s1)
print(x)
# We can use the int() function before the input() function to accept an integer from the keyboard as:
x = int(input('Enter the number :'))
print(x)
# Similarly, to accept a float value from the keyboard, we can use the float() function along with the input() fuction as :
y = float(input('Enter a number :'))
print(y)