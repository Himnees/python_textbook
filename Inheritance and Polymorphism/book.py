# Program 20: A python program to overload the addition operator (+) to make it act on class object.
class BookX:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,others):
        return self.pages+others.pages

class BookY:
    def __init__(self,pages):
        self.pages=pages

b1=BookX(100)
b2=BookY(150)
print('Total pages:',b1+b2)

# Program 21: A python program to overload greaer than(>) operator to make it act on class object.
class Ramayana:
    def __init__(self,pages):
        self.pages=pages
    def __gt__(self,other):
        return self.pages>other.pages
    

class Mahabaratha:
    def __init__(self,pages):
        self.pages=pages  

r=Ramayana(1000)
m=Mahabaratha(1500)
if(r>m):
    print('Ramayana is more than Mahabaratha')
else:
    print('Mahabaratha is more than Ramayana')


# Program 22: A python program to overload the multiplication (*) operator to make it act on object.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __mul__(self,others) :
        return self.salary*others.days
    
class Attendence:
    def __init__(self,name,days):
        self.name=name
        self.days=days

a=Employee('Spoorthi',500)
b=Attendence('Spoorthi',25)
print('Total salary =',a*b)