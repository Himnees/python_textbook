# Program 13: A python program to create Dob class within Person class.
class Person:
    def __init__(self):
        self.name='Spoorthi'
        self.db=self.Dob()

    def display(self):
        print('Name=',self.name)

    class Dob:
        def __init__(self):
            self.dd=14
            self.mm=10
            self.yy=1998
        def display(self):
            print('D.O.B = {}/{}/{}'.format(self.dd,self.mm,self.yy))

p=Person()
p.display()

x=p.db
x.display()

# Program 14: A python program to create another version of dob class within person class
class per:
    def __init__(self):
        self.name='Spoorthi'
    def display(self):
        print('Name=',self.name)

    class db:
        def __init__(self):
            self.dd=12
            self.mm=10
            self.yy=1998

        def display(self):
            print('D.O.B={}/{}/{}'.format(self.dd,self.mm,self.yy))

y=per()
y.display()
q=per().db()
q.display()
print(q.yy)