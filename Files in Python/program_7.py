# Program 7: A pyhon program to count number of lines, words and characters in a text file.
import os, sys
fname=input('Enter file name:')
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname," is not found")
    sys.exit()
cl=cw=cc=0
for line in f:
    words=line.split()
    cl+=1
    cw+=len(words)
    cc+=len(line)
print('No. of lines=',cl)
print('No. of words=',cw)
print('No. of characters=',cc)