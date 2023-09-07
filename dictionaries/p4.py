# Program 4: A python program to create a dictionary from keyboard and display the elements.
x={}
print('How many elements:',end='')
n=int(input())
for i in range(n):
    print('Enter key',end='')
    k=input()
    print('Enter value',end='')
    v=input()
    x.update({k:v})
print(x)