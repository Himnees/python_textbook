# Program 17: A python program to check the object type to know whether the method exists in the object or not.
class Duck:
    def talk(self):
        print('Hi')

class Human:
    def talk(self):
        print('Babe')

class Dog:
    def bark(self):
        print('Bark')

def class_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
    else:
        print('Wrong object passed ....')

d=Duck()
class_talk(d)
h=Human()
class_talk(h)
b=Dog()
class_talk(b)