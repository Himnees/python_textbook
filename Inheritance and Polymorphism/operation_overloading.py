# Operator ovrloading
# Program 18: A python program to use addition operator to act on different types of object.
print(10+15)
s1='red'
s2='fort'
print(s1+s2)

a=[10,20,30,40]
b=[60,70,80,90]
print(a+b)

# Program 19: A python program to use addition operator to add the content of two objects.
class BookX:
    def __init__(self,pages):
        self.pages=pages

class BookY:
    def __init__(self,pages):
        self.pages=pages

b1=BookX(100)
b2=BookY(150)
print('Total pages:',b1+b2) # error
