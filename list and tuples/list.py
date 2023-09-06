# Lists and tuples

# Program 1: A python program to create lists with different types of elements
num=[10,20,30,40,50]
print('Total list:',num)
print('First =%d, last=%d'%(num[0],num[4]))

names=['Himneesh','Spoorti','Sunitha','love','sex']
print('Total list:',names)
print('First =%s, last=%s'%(names[0],names[4]))

x=[10,20,10.5,'Spoorti','Sunitha']
print('Total list:',x)
print('First =%d, last=%s'%(x[0],x[4]))

# Creating lists using range() function
# Program 2: A python program o create lists using range() function
list1=list(range(0,10))
print(list1)
list2=list(range(5,10))
print(list2)
list3=list(range(5,10,2))
print(list3)

# Program 3: A python program to access list elements using loops.
lst=[10,20,30,40,50]
print('Using while loop')
i=0
while i<len(lst):
    print(lst[i])
    i+=1
print('Using for loop')
for i in lst:
    print(i)