# Program 22: A python program to find the power value of a number when it is raised to a particular power.
import argparse

# Call the ArgumentParser()
parser = argparse.ArgumentParser()

# add the argument to the parser
parser.add_argument('nums',nargs=2)

# retrieve the argument into args object
args = parser.parse_args()
# find the power value
# args.nums represent a list
print('number =',args.nums[0])
print('Its power =',args.nums[1])

# Convert the argument into float and then find the power
result = float(args.nums[0])**float(args.nums[1])
print('result =',result)