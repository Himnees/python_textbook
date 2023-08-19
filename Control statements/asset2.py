# The 'AssertionError' in output is called exception. An exception is an error that occurs during runtime.
'''To avoid such type of exception, we can handle them using 'try... except' statement'''

# Program 29: A python program to handle the AssertionError exception that is given by assert sttement.
x = int(input('Enter a number greater than 0: '))
try:
    assert(x>0)
    print('u entered: ',x)
except AssertionError:
    print('Wrong input entered')