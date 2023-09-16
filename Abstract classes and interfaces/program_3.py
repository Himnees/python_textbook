# Program 3: A python program to create a Car abstract class that combines an instance variable, a concrete method and two abstrac methods
from abc import *
class Car(ABC):
    def __init__(self,regno):
        self.regno=regno

    def open_tank(self):
        print('This open tank')
        print('You can fill')

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def braking(self):
        pass