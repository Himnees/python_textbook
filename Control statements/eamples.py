# Program 33: Write a program to generate Fibonaci series.
n = int(input('How many Fibonaci:'))
f1=0 # this is first Fibonacci number
f2=1 # this is second number
c=2 # counts the number of fabonaccis
if n==1:
    print(f1)
elif n==2:
    print(f1,'\n',f2,sep='')
else:
    print(f1,'\n',f2,sep='')
    while c<n:
        f=f1+f2 # add two Fibonaccis to ge the new line
        print(f)
        f1,f2=f2,f
        c+=1 # increment counter

# Program 34: Write a pyhon program to calculate the sine value of a given angle degree by evaluating the sine series 

# accept user input
x,n = [int(i) for i in input('Enter the angle value, no. of iteration:').split(',')]
# convert the angle from degrees into radians
r=(x*3.14159)/180

# this becomes the first term
t=r

# till now, find the sum 
sum=r
# display the iteration number and sum
print('Iteration=%d\tsum=%f' %(1,sum))

# denominator for the second term
i=2

# repeat for 2nd to nth terms

for j in range(2,n+1):
    t=(-1)*t*r*r/(i*(i+1)) # find the next term
    sum=sum+t; # add it to sum
    print('Iteration=%d\tsum=%f' %(j,sum))
    i+=2 # increse i value by 2 for denominator for next term


# Program 35: Write a pyhon program to calculate the sine value of a given angle degree by evaluating the cosine series
# accept user input
x,n = [int(i) for i in input('Enter the angle value, no. of iteration:').split(',')]
# convert the angle from degrees into radians
r=(x*3.14159)/180

# this becomes the first term
t=r

# till now, find the sum 
sum=r
# display the iteration number and sum
print('Iteration=%d\tsum=%f' %(1,sum))

# denominator for the second term
i=2

# repeat for 2nd to nth terms

for j in range(2,n+1):
    t=(-1)*t*r**2/(i*(i+1)) # find the next term
    sum=sum+t; # add it to sum
    print('Iteration=%d\tsum=%f' %(j,sum))
    i+=2 # increse i value by 2 for denominator for next term
