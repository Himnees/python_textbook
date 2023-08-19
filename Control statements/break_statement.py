# The break statement
'''The break statement can be used inside a for loop or while loop to ome out of the loop.
when'break' is executed, the python interpreter jumps out ofthe loop to process the next statement in the program.'''

# Program 24: A python program to display number from 10 to 6 and break the loop when the number about to display is 5.
x=10
while x>=1:
    print(x)
    x-=1
    if x==5:
        break   
print('out of loop')
    

x=10
while x>=1:
    print(x)
    x-=1
    if x==5:
        break 
        print('hi')  
print('out of loop')

x=10
while x>=1:
    print(x)
    x-=1
    if x==5:
        print('hi')
        break 
      
print('out of loop')