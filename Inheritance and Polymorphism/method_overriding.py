# Method Overriding
# Program 24: A python program to overide the super class method in sub class.
import math
class square:
    def area(sel,x):
        print('Square area: %.4f'%(x*x))

class Circle(square):
    def area(self,x):
        print('Circle area=%.4f'%(math.pi*x*x))

c=Circle()
c.area(15)