# Program1: A python program to accept a string from keyword and display it.
str = input("Enter a string: ")
print('You entered: ',str) #display entire string
# Program2: A python program to accept a character as a string.
ch = input("Enter a char:")
print('You entered:',ch)
# Program3: A python program to accept a single character from keyboard.
ch = input("Enter a char : ")
print("U entered : ",ch[0])
# Program4: A python program to accept an integer number from keyboard.
str = input("Enter the number:")
x = int(str)
print('You entered : ',x)
# Program5: A python program to accept an integer number from keyboard.-version 2
str= int(input('Enter the number :'))
print('You entered : ',str)
# Program 6: A pythn program to accept float number from keyboard.
x =float(input('Enter the number :'))
print('You entered:',x)
# Program 7: A pyhton program to accept two integer number from keybord
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('You entered: ',a,b)
print('You entered: ',a,b,sep=',')
print('You entered: %d %d '%(a,b))
# Program 8: A python program to accept two numbers and find their sum.
a= int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('The sum of',a,'and',b,'is',(a+b))
print('The sum of {} and {} is {}'.format(a,b,a+b))
# Program 9: A python program to find sum and product of two numbers.
a= int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('The sum of {} and {} is {}'.format(a,b,a+b))
print('The product of {} and {} is {}'.format(a,b,a*b))
# Program 10: A python program to convert numbers from other system into decimal number system.
s1 = input('Enter hexadecimal number: ')
x= int(s1,16)
print('Hexadecimal to decimal = ',x)

s1 = input('Enter octal number: ')
x= int(s1,8)
print('Octal to decimal = ',x)

s1 = input('Enter binary number: ')
x= int(s1,2)
print('Binary to decimal = ',x)