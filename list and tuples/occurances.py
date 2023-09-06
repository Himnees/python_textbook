# Number of occurrences of an element in the list
x=[10,20,30,40,40,50,40]
n=x.count(40)
print(n)

# Program 8: A python program to know how many occurances in the list.
x=[]
n=int(input('How many elements?'))

for i in range(n):
    print('Enter elements:',end='')
    x.append(int(input()))
print('The list is:',x)
y=int(input('Enter the element to count:'))
c=0
for i in x:
    if y==i: c+=1
print('{} is found {} times'.format(y,c)) 

# Finding Common elements in two lists

# Program 9: A python program to find common elements in two lists
x=['Himneesh','loves','Spoorti']
y=['Himneesh','sex','Sumitha']
s1=set(x)
s2=set(y)
s3=s1.intersection(s2)
print(list(s3))