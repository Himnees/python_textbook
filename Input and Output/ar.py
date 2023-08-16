# Program 21 find sum of two given numbersusing argument parser
import argparse

# Create ArgumentParser class object
parser = argparse.ArgumentParser(description =' This is dricption')

# Add two arguments with the names num1 and num2 and type as float
parser.add_argument('num1',type=float,help='Enter first value')
parser.add_argument('num2',type=float,help='Enter first value')

# retrieve the arguments passed to the program 
args = parser.parse_args()

# convert the num1 and num2 into float type and then add them
result = float(args.num1)+float(args.num2)
print('sum =',result)