# The else suite
# Program for using else suite for for loop:
for i in range(5):
    print('yes')
else:
    print('no')
# It means, the for loop statement is executed and also the else suite is executed.

for i in range(0):
    print('yes')
else:
    print('no')

# Program 23: A python program to search for an element in the list of elements.

group1=[1,2,3,4,5]
s = int(input('Enter the element:'))
for i in group1:
    if i == s:
        print('Element found')
        break
else:
    print('Element not found')