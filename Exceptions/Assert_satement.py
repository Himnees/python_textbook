# The Assert statement
# Program 13: A python program using the assert statement and catching AssertionError.
try:
    x=int(input('Enter a number between 5 and 10:'))
    assert x>=5 and x<=10
    print('The number entered:',x)
except AssertionError:
    print('The condition not fullfilled.')

# Program 14: A python program to create our own exception and raise it when needed.
try:
    x=int(input('Enter a number between 5 and 10:'))
    assert x>=5 and x<=10, "Your input is incorrect"
    print('The number entered:',x)
except AssertionError as obj:
    print(obj)