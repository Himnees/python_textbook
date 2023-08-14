# Program 17: A python program to display command line argument.

# To display command line args. Save tis as cmd.py
import sys

n=len(sys.argv) # n is the number of arguments
args= sys.argv # args list contains arguments
print('No. of command line args = ',n)
print('The args are: ',args)
print('The args one by on :')
for a in args:
    print(a)