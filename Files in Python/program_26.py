# Program 26: A python program to change to another directory.
import os
os.chdir('newsub/newsub2')
current=os.getcwd()
print('current directory=',current)