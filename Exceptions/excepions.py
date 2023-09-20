# Exceptions
# Exception Handling 
# Program 7: A python program to handle the ZeroDivisionError exception.
try:
    f = open("mylove","w")
    a,b = [int(x) for x in input("Enter two numers:").split()]
    c=a/b
    f.write("writing %d into mylove"%c)

except ZeroDivisionError:
    print('Division by 0 is infinite')
    print('Please ener non zero number')

finally:
    f.close()
    print('File is closed')


# Program 8: A python program to handle syntax error given by eval() function.
try:
    date = eval(input('Enter date:'))
except SyntaxError:
    print('Invalid date entered')
else:
    print('You entered:',date)