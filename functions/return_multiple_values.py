# Program 7: A python program o understand how a function returns two values.
def sum_sub(a,b):
    '''This function returns results of
    addition and subtraction of a, b '''
    c=a+b
    d=a-b
    return c,d
x,y=sum_sub(15,10)
print(x)
print(y)

# Program 8: A function that retuns the results of addition, subtraction, multiplication, and division.
def operations(a,b):
    '''This function returns the result of addition,subtraction,
    multiplication and division'''
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f
u,v,w,x=operations(23,45)
print()
print(u)
print(v)
print(w)
print(x)