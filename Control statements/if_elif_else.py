# The if...elif...else Statement
# The syntax for if...elif...else Statement
'''
if condition1:
    statements1
elif condition2:
    statements2
else condition3:
     statements3
     '''
# Program 7: A python program to know if a given number is zero, positive or negative.
num=-5
if num==0:
    print(num,'is zero')
elif num>0:
    print(num,'is positive')
else:
    print(num,'is negative')

# Program 8: A python program to accept a numeric digit from keyboard and display in words.
x = int(input('Enter the number:'))
if x==0: print('zero')
elif x==1: print('one')
elif x==2: print('two')
elif x==3: print('three')
elif x==4: print('four')
elif x==5: print('five')
elif x==6: print('six')
elif x==7: print('seven')
elif x==8: print('eight')
elif x==9: print('nine')
else: print('Enter number between 1 to 9')