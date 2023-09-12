# Types of Variable
# Instance variable
# Class variable or Static variable

# Program 3: A python program to understand instance variable.
class sample:
    def __init__(self):
        self.x=10
    
    def modify(self):
        self.x+=1

s1=sample()
s2=sample()
print('x=',s1.x)
print('x=',s2.x)
s1.modify()
print('x=',s1.x)
print('x=',s2.x)

# Program 4: A python program to understand class variable or static variable.
class sample:
    x=10

    @classmethod
    def modify(cls):
        cls.x+=1

s1=sample()
s2=sample()
print('x=',s1.x)
print('x=',s2.x)
s1.modify()
print('x=',s1.x)
print('x=',s2.x)

class student:
    n=10

print(student.n)
student.n+=1
print(student.n)
s1=student()
print(s1.n)
s2=student()
print(s2.n)

class stu:
    a=10
s1=stu()
print(s1.a)
s1.a+=1
print(s1.a)
s2=stu()
print(s2.a)