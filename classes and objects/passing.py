# Passing member of ine class to another class
# Program 11: A python program to create Emp class and make all the members of the Emp class availale to another class i.e method.
class Emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def display(self):
        print('Id= ',self.id)
        print('Name=',self.name)
        print('Salary=',self.salary)

class Myclass:
    @staticmethod
    def mymethod(e):
        e.salary+=1000
        e.display()

e=Emp(10,'Spoorthi',15000.75)
Myclass.mymethod(e)

# Program 12: A python program to calculate power value of a number with the help of a static method.
class Mymethod:
    @staticmethod
    def display(x,n):
        result=x**n
        print('{} to the power {} is {}'.format(x,n,result))

Mymethod.display(4,5)
Mymethod.display(5,4)

