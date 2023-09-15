# Types of Inheritance

# Single Inheritance
# Program 10: A python program showing single inheritance in which two sub classes are divided from a single base class.
class Bank(object):
    cash=10000000
    @classmethod
    def available_cash(cls):
        print(cls.cash)

class AndhraBank(Bank):
    pass

class StateBank(Bank):
    cash=2000000
    @classmethod
    def available_cash(cls):
        print(cls.cash+Bank.cash)

a=AndhraBank()
a.available_cash()
s=StateBank()
s.available_cash()

# Multi Inheritance
# Program 11: A python program to implement multiple inheritance using two base classes.
class Father:
    def height(self):
        print('Height is 6.0 feet')

class Mother:
    def color(self):
        print('The color is brown')

class Child(Mother,Father):
    pass
c=Child()
c.height()
c.color()