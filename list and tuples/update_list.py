# Udating the elements of list
# Program 4: A python program to display the elements of a list  in reverse order
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturaday','Sunday']
days.reverse()
print(days)
my_l1=list(reversed(days))
print(my_l1)
print(my_l1[::-1])
i=len(my_l1)-1
print('\n In reverse order')
while i>=0:
    print(my_l1[i])
    i-=1
print('\n In reverse order')
i=-1
while i>=-len(my_l1):
    print(my_l1[i])
    i-=1

l1=list(range(1,6))
print(l1)
l1.append(6)
print(l1)
l1[1:3]=10,11
print(l1)
del l1[1]
print(l1)
l1.remove(1)
print(l1)

# Concatenation of two lists
x=[10,20,30,40,50]
y=[100,110,120]
print(x+y)

# Repetation of list
print(x*2)

# Membership in lists
a=20
print(a in x)
print(a not in x)

