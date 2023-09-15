# Program 12: A python program to prove that only one class constructor is avaialable to sub class in multiple inheritance.
class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)

class B(object):
    def __init__(self):
        self.a='b'
        print(self.b)

class C(A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()

o=C()
