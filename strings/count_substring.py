# Counting Substring in a string
# syntax: stringname.count(substring)
# sringname.count(substring,bigining,end)
str='New Delhi'
n=str.count('Delhi')
print(n)
n=str.count('e',0,3)
print(n)
n=str.count('e',0,len(str))
print(n)

# Strings are immutable
str='abcd'
print(str[0])
try:
    str[0]='z'
except TypeError:
    print('Strings are not muttable')

s1=12
s2=11
print(id(s1))
print(id(s2))
s2=s1
print(id(s1),'\n','\b',id(s2))

 # Replacing a String with another string
   # syntax: strngname.replace(old,new)
str= 'She is very beautiful'
s1='She'
s2='Spoorti'
str1=str.replace(s1,s2)
print(str1)

# Splitting and Joining Strings
'''The split() method is used to break a sring into pieces. These pieces are returned as a list.'''
str='one,two,three,four'
str1=str.split(',')
print(str1)

# Program 8: A pyhton program to accept and display a group of numbers.
str=input('Enter numbers seperated by space: ')
lst=str.split(' ')
for i in lst:
    print(i)

# When a group are given, It is possible to join them all and make a singlr string.
# syntax:seperator.join()
str=('one','two','three')
a='-'.join(str)
print(a)
s=['Apple','guava','grapes','Mango']
sep=':'
q=sep.join(s)
print(q)