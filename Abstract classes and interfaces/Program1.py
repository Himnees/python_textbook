# Program 1: A python program to understad that Myfunction method is shaed by all of its bjects.
class Myclass:
    def calculate(self,x):
        print('square value=',x*x)

obj=Myclass()
obj.calculate(2)

obj1=Myclass()
obj1.calculate(3)

obj2=Myclass()
obj2.calculate(4)