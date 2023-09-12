# Class Method
# Program 7: A python program to use class method to handle the common features of all the instances of Bird class
class bird:
    wings=2
    @classmethod
    def display(cls,name):
        print('{} has {} wings'.format(name,cls.wings))
bird.display('Dove')
bird.display('Eagle')