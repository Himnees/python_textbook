# Nested tuple
tup=(50,69,70,80,90,(200,201))
print(tup[5])

# Sorting Nested tuple
# Program 16: A python program to sort a tuple with nested tuples.
emp=((10,'Himneesh',10000),(11,'Spoorti',1200),(12,'Sunitha',11000))
print(sorted(emp))
print(sorted(emp, reverse=True))
print(sorted(emp, key=lambda x:x[1]))
print(sorted(emp, key=lambda x:x[2]) )