# Method Overloading
# Program 23: A python program to show method overloading to find sum of two or three members.
class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('Sum of three =',a+b+c)
        elif a!=None and b!=None:
            print('Sum of two =',a+b)
        else:
            print('Please enter the alteat one number')   

m=Myclass()
m.sum(10,20,30)
m.sum(20,40)
m.sum(100)