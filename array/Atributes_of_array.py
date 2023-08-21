# Attributes of an array
# Numps's array class is called ndarray.

# The ndim array
# The ndim atribute represents the number of dimensions or axes of the array
from numpy import *
arr1=array([1,2,3,4,5])
print(arr1.ndim)
arr2=array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2.ndim)

# The shape Attribute
# The shape attribute gives the shape of an array 
print(arr1.shape)
print(arr2.shape)
arr2.shape=(5,2)
print(arr2)

# The size atttribute
arr1=array([1,2,3,4,5])
print(arr1.size)
arr2=array([[1,2,3],[4,5,6]])
print(arr2.size)

# The itemsize attrabute
arr1=array([1,2,3,4,5])
print(arr1.itemsize)
arr1=array([1.3,2.4,3.5,4.6,5.7])
print(arr1.itemsize)

# The dtype Attribute
arr1= array([1,2,3,4,5])
print(arr1.dtype)
arr1= array([1.1,2.2,3.3,4.4,5.5])
print(arr1.dtype)

# The nbyes Atributes
arr2=array([[1,2,3,4],[5,6,7,8]])
print(arr2.nbytes)