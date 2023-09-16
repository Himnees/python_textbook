# Programm 5: A python program in which Santro sub class implements the abstract methods of the super class, Car.
from program_3 import Car
class Santro(Car):
    def steering(self):
        print('This is Santro having Power steering')
        print('Have a good ride')

    def braking(self):
        print('Santro has gas braking')
        print('Try it')

m=Santro(1002)
m.open_tank()
m.steering()
m.braking()