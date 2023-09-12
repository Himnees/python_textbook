# Program 10: A pyhon program too create a bank class where deposits and withdrawals can be handeled by using instance methods
import sys
class Bank(object):
    '''Bank related transaction'''

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    
    def withdraw(self,amount):
        if amount >self.balance:
            print('Balance amount is less')
        else:
            self.balance-=amount
            return self.balance
        
name=input('Enter name:')
b=Bank(name)

while(True):
    print('d- deposit, w- withdrawal, e- exit')
    choice= input('Your choice:')
    if choice=='E' or choice=='e':
        sys.exit()
    amt=float(input('Enter amount:'))
    if choice=='d' or choice=='D':
        print('Balance after deposit',b.deposit(amt))
    elif choice=='W' or choice=='w':
        print('Balance after withdrawal',b.withdraw(amt))
