# The continue statement
'''The continue statement is used in a loop to go back to begining of the loop, It means, when continue is executed, 
the next repetition will start. When continue is executed, the subsequent statements in the loop are not executed.'''

# Program 25: A python program to display number from 1 to 5 using continue statement.
x=0
while x<=10:
    
    x+=1
    if x>5:
        
        continue 
        
    print(x)
print('out of loop')

x=0
while x<=10:
    
    x+=1
    if x>5:
        print('hi')
        continue 
        
    print(x)
print('out of loop')