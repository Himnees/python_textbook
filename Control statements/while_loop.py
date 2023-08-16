# The while loop
'''The syntax of while loop:
  while condition:
      statements
      '''
# Program 9: A python program to display number from 1 to 10 using while loop.
x=1
while x<=10:
    print(x)
    x+=1
print('end')

x=1
while x<=10:
    print(x)
    x+=1
    print('end')

# Program 10: A python program to display even numbers between 100 and 200.
x=100
while x>=100 and x<=200:
    print(x)
    x+=2

# Program 11: A python program to display even numbers between m and n.
m,n =[int(i) for i in input('Enter the numbers:').split(',')]
x=m
if x%2!=0:
    x=x+1
while x>=m and x<=n:
    print(x)
    x+=2

# Program 18: A Python program to display and sum of a list of number using while loop.
l2=[2,4,6,7,8,9,10,2,3,4,5,6]
sum=0
i=0
while i<len(l2):
    print(l2[i])
    sum+=l2[i]
    i+=1
print('sum=',sum)