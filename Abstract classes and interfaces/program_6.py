# Program 6" A python program to devlop an interface that connects to any database.
from abc import *
class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class oracle(Myclass):
    def connect(self):
        print('Connecting to oracle database...')
    def disconnect(self):
        print('Disconnected from oracle database.')

class sybase(Myclass):
    def connect(self):
        print('Connecting to skybase database...')
    def disconnect(self):
        print('Disconnected from skybase database.')

class Database:
    str=input('Enter tthe database:')

    classname = globals()[str]

    s = classname()
    s.connect()
    s.disconnect()