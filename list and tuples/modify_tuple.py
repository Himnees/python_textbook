# Inserting Elements in a tuple

# Program 17: A python program to insert a new elemen into a tuple of element at a specified position
names=('Himneesh','loves','Spoorti','Spoorti')
print(names)
lst=[(input('Enter new name: '))]
new=tuple(lst)
pos=int(input('Enter position: '))
names1=names[0:pos-1]
names1=names1+new
names=names1+names[pos-1:]
print(names)

# Program 18: A python program to modify or replace an existing element of a tuple with a new element.
num=(10,20,30,40,50)
print(num)
lst=[int(input('Enter new element:'))]
new=tuple(lst)
pos=int(input('Enter position: '))
num1=num[0:pos-1]
num1=num1+new
num=num1+num[pos:]
print(num)

# Pogram 19: A program to delete an element from a particular position in the tuple
num=(10,20,30,40,50)
print(num)
pos=int(input('Enter position: '))
num1=num[0:pos-1]
num=num1+num[pos:]
print(num)

