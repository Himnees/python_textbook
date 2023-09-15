# Polymorphism
# Program 15: A python program to invoke a mehod on an object without knowing the type of the object.
class Duck:
    def talk(self):
        print('Hi')

class Human:
    def talk(self):
        print('Babe')

def class_talk(obj):
    obj.talk()

d=Duck()
class_talk(d)
h=Human()
class_talk(h)

