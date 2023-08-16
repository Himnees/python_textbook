# Program 22: To accept 1 or more arguments and display them as list elements
import argparse

# call the ArgumentParser()
parser = argparse.ArgumentParser()

# add the argument to the parser
parser.add_argument('nums',nargs='+')

# retrieve the argument into args object
args = parser.parse_args()

# display the arguments from the list: args.nums
for x in args.nums:
    print(x)