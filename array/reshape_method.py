# The reshape() method
from numpy import *
arr1=arange(10)
print(arr1)
arr2=arr1.reshape(2,5) # 2 ros and 5 cols
arr3=arr1.reshape(5,2) # 5 rows and 2 cols
print(arr2)
print(arr3)