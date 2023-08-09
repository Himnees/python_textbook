# single line comments
"""
This is a program to find net salary of an employee
based on the basic salary, provident funf, house rent allowance,
dearness allowance and income tax
"""
# or multi line comments can be written in ''' '''
'''
This is a program to find net salary of an employee
based on the basic salary, provident funf, house rent allowance,
dearness allowance and income tax
'''
#Docstring
# program with two fuctions
def add(x,y):
    """
    This function takes two numbers and finds their sum.
    It displays the sum a result.
    """
    print("sum = ",(x+y))
    
def message():
    '''
    This function displays a messag.
    This is a welcome message to the user.
    '''
    print("Welcome to python")
#Now call the function
add(10,25)
message()