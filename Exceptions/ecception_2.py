# Program 9: A python program to handle IOError produced by open( function.
try:
    name=input('Ener file name:')
    f=open(name,'r')
except IOError:
    print('File not found')
else:
    n = len(f.readlines())
    print(name, 'has',n,'lines')
    f.close()
    print('Thnk you')

# Program 10: A python program to handle multiple exception.
def avg(list):
    tot=0
    for x in list:
        tot+=x
    avg=tot/len(list)
    return tot, avg
try:
    t,a =avg([1,2,3,4])
    print('Total={},Average={}'.format(t,a))
except TypeError:
    print('Type error, please provide number')
except ZeroDivisionError:
    print('ZeroDivision Error, pleae give numbers in list')