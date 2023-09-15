# The Super() Method
# Program 8: A python program to call the super class constructor in the sub class using super().

class Father:
    def __init__(self,property=0):
        self.property=property

    def display(self):
        print('The value=',self.property)

class Son(Father):
    def __init__(self,property,property1):
        super().__init__(property)
        self.property1=property1

    def display(self):
        print(' Total property=',self.property+self.property1)

s=Son(8000000,2000000)
s.display()

# Program 9: A python program to access base class constructor and method in the sub class using super()

class square:
    def __init__(self,x):
        self.x=x
    def area(self):
        print('Area of Square=',self.x*self.x)

class rectangle(square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def area(self):
        super().area()
        print('Area of Rectangle=',self.x*self.y)

a, b=[float(x) for x in input('Enter two measuements:').split()]
r=rectangle(a,b)
r.area()