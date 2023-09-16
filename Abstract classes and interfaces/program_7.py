# Program 7: A python program which contains prnter interface and its sub classes to send text to any printer.
from abc import *
class printer(ABC):
    @abstractmethod
    def printit(self,text):
        pass
    @abstractmethod
    def disconnect(self,text):
        pass

class IBM(printer):
    def printit(self, text):
        print(text)
    def disconnect(self):
        print('Printing completed on IBM printer.')


class Epson(printer):
    def printit(self, text):
        print(text)
    def disconnect(self):
        print('Printing completed on Epson printer.')

class UsePrinter:
    with open("config.txt","r") as f:
        str =f.readline()

        classname=globals()[str]

        s=classname()

        s.printit('Hello, this is sent to printer')
        s.disconnect()
