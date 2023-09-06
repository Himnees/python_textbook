# Accessing the tuple element
tup=(50,60,70,80,90,100)
print(tup[0])
print(tup[5])
print(tup[-1])
print(tup[-6])
print(tup[:])
print(tup[1:4])
print(tup[::2])
print(tup[::-2])
print(tup[-4:-1])

student=(10,'Love', 50,60,65,61,70)
rn0, name=student[0:2]
marks=student[2:7]
print(rn0)
print(name)
for i in marks:
    print(i)