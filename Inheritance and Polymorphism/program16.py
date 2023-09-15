# Program 16: A python program to call a method that does not appear in the object passed to the method.
# Program 15: A python program to invoke a mehod on an object without knowing the type of the object.
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
    obj.talk()

d=Duck()
class_talk(d)
h=Human()
class_talk(h)
b=Dog()
class_talk(b) # error