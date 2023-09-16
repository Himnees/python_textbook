# Program 2: A python program to create abstract class and sub classes which implement the abstract method of the abstract classes.
from abc import ABC, abstractmethod
class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass

class sub1(Myclass):
    def calculate(self,x):
        print('Square value=',x*x)

import math
class sub2(Myclass):
    def calculate(self,x):
        print('Square root value=',math.sqrt(x))

class sub3(Myclass):
    def calculate(self,x):
        print('Cube value=',x**3)   


obj1=sub1()
obj1.calculate(5)
obj2=sub2()
obj2.calculate(16)
obj3=sub3()
obj3.calculate(7)