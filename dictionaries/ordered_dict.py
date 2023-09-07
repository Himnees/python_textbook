# Ordered Dictionary
# Program 12: A python program to create a dictionary that does not change the order of element.
from collections import OrderedDict
d=OrderedDict()
d[10]='S'
d[11]='P'
d[12]='O'
d[13]='O'
d[14]='R'
d[15]='T'
d[16]='H'
d[17]='I'
for k,v in d.items():
    print(k,v)