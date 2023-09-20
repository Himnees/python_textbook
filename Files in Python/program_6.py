# Knowing whether file exists or not
# Program 6: A python program to know whether a file exists or not.
import os, sys
fname= input('Enter file name:')
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+" is not found")
    sys.exit()
str=f.read()
print(str)
f.close()