# Creating a class
# Program 1: A python program to define students class and create an object to it. Also, we will call the method and display the student's details
class student:
    def __init__(self):
        self.name='Spoorthi'
        self.age=23
        self.sal=15000.00

    def talk(self):
        print('I love',self.name)
        print('I am 21 and she is',self.age)
        print('She earn',self.sal)
    
s1=student()
s1.talk()

# Program 2: A python program to create student class with a constructor having more than one parameter.
class love:
    def __init__(self,n='',m=0):
        self.name=n
        self.sal=m

    def display(self):
        print('Hi',self.name)
        print('salary=',self.sal)

s1=love()
s1.display()
print('-------------------') 
s2=love('Spoorti',15000.00)
s2.display()       