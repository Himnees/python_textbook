# User-defined Exception
# Program 14: A python program to create our own exception and raise it when needed.
class MyException(Exception):
    def __init__(self,arg):
        self.msg=arg
    
def check(dict):
    for k,v in dict.items():
        print('Name={:15s} Balance={:10.2f}'.format(k,v))
        if(v<2000.00):
            raise MyException('Balance amount is less in the account')

bank={'Spoorthi':23000,'Himneesh':1990,'Prasad':56000,'Himni':6700}
try:
    check(bank)

except MyException as me:
     print(me)



