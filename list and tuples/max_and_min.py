# Finding Bigges number and smallest elements in a list
x=[10,20,30,40,50]
print(max(x))
print(min(x))

# Program 6: A python program to find maximum and minimum elements in a list of elements.
x=[]
print('How many elements?',end='')
n=int(input())
for i in range(n):
    print('Enter elements: ',end='')
    x.append(int(input()))

print('The list is: ',x)
big=x[0]
small=x[0]

for i in range(1,n):
    if x[i]>big: big=x[i]
    #big
    if x[i]<small: small=x[i]
    # take it as small
print('Maximum is: ',big)
print('Minimum is: ',small)