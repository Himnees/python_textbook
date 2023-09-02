# Formal and actual arguments
def sum(a,b):
    c=a+b
    print(c)
x=10;y=20
sum(x,y)

# Positional Arguments
# Program 16: A python program to understand the potential arguments of a function.
def attach(s1,s2):
    ''' o join s1 and s2 and display total string '''
    s3=s1+s2
    print('Total string:'+s3)

attach('Himneesh','Spoorti')
print()

# Keyword Argument
# Program 17: A python program to understand the keyword argument of a function.
def grocery(item,price):
    ''' to display the given value ''' 
    print('Item = %s'%item)
    print('Price= %.2f'%price)
grocery(item='sugar',price=50.00)
grocery(price=180.00,item='oil')
print()
# Default Arguments
# Program 18: A python program to undersand the use of default argument in a function
def grocery(item,price=40.00):
    ''' to display the given arguments '''
    print('Item = %s'%item)
    print('price = %.2f'%price)
grocery(item='Sugar',price=50)
grocery(item='Sugar')
print()
# Variable  Length Arguments
# Program 19: A python program to show variable length argument and its use
def add(farg,*args):
    ''' to add given numbers '''
    print('Formal arguments= ',farg)
    sum=0
    for i in args:
        sum+=i
        print('sum of all numbers= ',(farg+sum))

add(5,10)
add(5,10,20,30)
print()

# Program 20: A python program to understand keywords variable arguments.
def display(farg,**kwargs):
    ''' to display given value '''
    print('Formal arguments : ',farg)
    for x,y in kwargs.items():
        print('key = {} , value = {}'.format(x,y))
display(5,rNo=10)
display(5,rNo=20,Name='Himneesh')
print()