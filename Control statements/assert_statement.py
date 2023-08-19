# The assert statement
'''The assert statement is useful to check if a particular condition is fullfilled or not
syntax 
     assert expression, message  '''
# Program 28: A program to assert that the user enters a number greater than zero.

x= int(input('Enter a number greater than 0 :'))
assert x>0, "wrong input entered"
print('u entered: ',x)
