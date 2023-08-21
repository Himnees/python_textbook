# Slicing the multi-dimensional arrays
from numpy import *
a=[[1,2,3,4],[4,5,6,7],[3,4,5,6]]
a=reshape(a,(4,3))
print(a)

a=arange(9)
a=reshape(a,(3,3))
print(a)

print(a[::],'\n')
print(a[::],'\n')
print(a[:,:],'\n')
print(a[:],'\n')
print(a[0:],'\n')
print(a[:0],'\n')
print(a[0:1,0:1],'\n')
print(a[1:2,1:2],'\n')
print(a[2:,1:2],'\n')

a=reshape(arange(11,36,1),(5,5))
print(a,'\n')
print(a[0:2,0:3])
print(a[0:2,2:])
print(a[2:,3:])
