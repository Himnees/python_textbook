# Program 20: Using argument paser to find the square of agiven number.
# to find square of a given number. Save this as sq.py
import argparse

# create Argumentpaser class object
paser = argparse.ArgumentParser(description='This program displays the square value of given number')

# add one argument with the name num and type as integer
paser.add_argument("num",type=int,help="Please input integer type number.")

# retrieve the arguments passed to the program
args = paser.parse_args()

# find the square of the argument passed
result = args.num**2
print('Square value =',result)