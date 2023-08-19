# The pass statement
'''The pass statement does not do anything. It is used with 'if' statement or inside a loop to represent no operation
we use pass staement we need a statement syntactically but we do not want to do any operation.'''

# Program 26: A program t know that pass does nothing.
x=0
while x<10:
    x+=1
    if x==5:
        pass
    print(x)
print('out of loop')
# More meaning usage of pass statement

# Program 27: A pyhton program to retrieve only negative numbers from the list.
num = [-1,-2,-3,0,1,2,3]
for i in num:
    if i>0:
        pass
    else:
        print(i)