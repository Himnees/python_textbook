# Program 18: A python program to find sum of two numbers using command line argument.
import sys

# Convert args into integer and then add them
sum = int(sys.argv[1])+int(sys.argv[2])
print('sum = ',sum)