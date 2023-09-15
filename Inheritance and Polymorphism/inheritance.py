# Constructors in Inheritance
# Program 6: A pthon program to access the base class constructor from sub class.

class Father:
    def __init__(self):
        self.property=80000000

    def display_property(self):
        print('Total value=',self.property)

class Son(Father):
    pass
s=Son()
s.display_property()

# Overriding Super Class Constructors and methods
# Program 7: A python program to override super class constructor and methods in sub class.

class Father:
    def __init__(self):
        self.property=8000000

    def display(self):
        print('Property value of Father=',self.property)

class Son(Father):
    def __init__(self):
        self.property=2000000

    def display(self):
        print('Son property=',self.property)

s=Son()
s.display()
