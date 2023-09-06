# Sorting the list elements
x=[10,30,2,56,78,100,5]
x.sort()
print(x)
x=[10,30,2,56,78,100,5]
x.sort(reverse=True)
print(x)

# Program 7: A python program to sort the list elements using bubble sort technique
x=[]
print('How many elements?',end='')
n=int(input())
for i in range(1,n):
    print('Enter elements? ',end='')
    x.append(int(input()))

print('Orginal list: ',x)

# bubble sort
flag=False
for i in range(n-1):
    for j in range(n-2):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
            flag=True
    if flag==False:
        break
    else:
        flag=False
print('Sored list: ',x)