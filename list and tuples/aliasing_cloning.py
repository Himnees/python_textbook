# Aliasing and cloning lists
x=[10,20,30,40,50]
y=x # Aliasing
print(x)
print(y)
x[1]=1
print(x)
print(y)

y=x[:] #cloning method
x[2]=65
print(x)
print(y)
# copy method
x=[10,20,30,40,50]
y=x.copy()
print(x)
print(y)
x[3]=56
print(x)
print(y)