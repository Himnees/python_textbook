# Mathematical operation on arrays
from numpy import *
a1=array([1,2,3,4,5])
a2= array([5,4,3,2,1])
a3=a1+a2
print(a3)

# Program 24: A python program to perform some mathematical operations on a numpy array.
from numpy import *
arr = array([10,20,30.5,-40])
print('Orginal array:',arr)
print('add:',arr+5)
print('subtract:',arr-5)
print('multiply:',arr*5)
print('division:',arr/5)
print('modulus:',arr%5)
print('expression value:',(arr*5)**2-10)
print('sin value',sin(arr))
print('cos value',cos(arr))
print('tan value',tan(arr))
print('Biggest value:',max(arr))
print('Smallest value:',min(arr))
print('sum:',sum(arr))
print('mean:',mean(arr))