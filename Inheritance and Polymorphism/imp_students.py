# Program 4: A python program to use the students class which already avaiable in stugent.py

from student import Student
s=Student()
s.setid(10)
s.setname('Himneesh')
s.setAddress('Bangalore, marathahalli')
s.setmarks(650.00)

print(s.getid())
print(s.getname())
print(s.getAddress())
print(s.getmarks())