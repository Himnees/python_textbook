# Program 19: A python program to find the sum of even number using command line argument.
import sys
# Read command line arguments except the program name
args = sys.argv[1:]
print(args)

sum=0
# find sum of even arguments
for a in args:
    x = int(a)
    if x%2==0:
        sum+=x
print('Sum of even = ',sum)  