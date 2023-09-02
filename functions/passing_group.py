# Passing a group of elements to a function
# Program 24: A function to accept a group of number and find their total average.
def calculate(lst):
    ''' to find total and average '''
    n=len(lst)
    sum=0
    for i in lst:
        sum+=i
        
        avg=sum/n
    return sum,avg
print('Enter the number with space:')
lst=[int(x) for x in input().split()]
x, y=calculate(lst)
print('sum =',x)
print('average =',y)
   
# Program 25: A function o display a group of strings.
def display(lst):
    '''to display group of strings'''
    for i in lst:
        print(i)

print('Enter the names:')
lst=[x for x in input().split(',')]
display(lst)

# Recursive Function
# Program 26: A python program to calculate factorial values using recursion.
def factorial(n):
    ''' to find factorial of n '''
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
for i in range(1,11):
    print('Factorial of {} is {}'.format(i,factorial(i)))

# Program 27: A python program to solve towers of Honai problem.
def towers(n,a,c,b):
    if n==1:
        # if only 1 disk, then move it from A to C
        print(' Move disk %i from pole %s to pole %s'%(n,a,c))
    else: # if more than 1 disk
        # move n-1 disks from A to B using C as intermediate pole
        towers(n-1,b,c,a)

        #move remaining 1 disk from A to C
        print('Moe disk %i from pole %s to pole %s'%(n,a,c))

        # move n-1 disks from B to C using A as intermediate pole
        towers(n-1,b,c,a)

n=int(input('Enter number of disks:'))
# we should change n disks from A to C using B as intermediate pole
towers(n,'A','C','B')

