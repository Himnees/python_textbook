# Program 44: A python program that uses the functions of employee module and calculates he gross and net salaries and net salaries of an emplooyee
from own_module import *
# calculate gross salary of employee by taking basic
basic=float(input('Enter basic salary:'))

# calculate gross salary
gross=basic+da(basic)+hra(basic)
print('Your gross salary {:10.2f}'.format(gross))

# calculate net salary
net=gross-pf(basic)-itax(basic)
print('Your net salary is {:10.2f}'.format(net))
