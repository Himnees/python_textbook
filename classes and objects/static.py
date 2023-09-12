# Static Method
# Program 8: A python program to create a static method that counts the number of instances created for a class
class Myclass():
    n=0

    def __init__(self):
        Myclass.n=Myclass.n+1

    @staticmethod
    def noObj():
        print('No. of occurance',Myclass.n)

ob1=Myclass()
ob2=Myclass()
ob3=Myclass()
Myclass.noObj()

# Program 9: A python program to create a static method that calculates the square root value of a given number.

import math
class sample:
    @staticmethod
    def calculate(x):
        result=math.sqrt(x)
        return result
    
num=float(input('Enter the number:'))

res=sample.calculate(num)
print('The square root of {} is{:.2f}'.format(num,res))