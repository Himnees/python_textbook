# Program 4: A python program in which Maruthi sub class implemented the abstract method of the super class, car
from program_3 import Car
class Maruthi(Car):
    def steering(self):
        print('This is Maruti having manual steering')
        print('Have a good ride')

    def braking(self):
        print('Maruthi has hydraulic braking')
        print('Try it')

m=Maruthi(1001)
m.open_tank()
m.steering()
m.braking()