# Finding sub string
# syntax = mainstring.find(subtring,beginning,ending)
 # Program 4: A python to find the first occurance of sub string in a given string
str=input('Enter the main string:')
sub=input('Enter sub string:')
n=str.find(sub,0,len(str))
if n==-1:
    print('Sub string not found')
else:
    print('Sub sring found at',n+1)

# Program 5: A python program to find the first occurence of sub string in a given string using index() method.
str=input('Enter the main string:')
sub=input('Enter sub string:')
try:
    n=str.index(sub,0,len(str))
except ValueError:
    print('String not found')
else:
    print('Sub string found at position',n+1)

# Program 6: A python to display all position of a sub string in a given main string.
str=input('Enter the main string:')
sub=input('Enter sub string:')
i=0
flag=False
n=len(str)
while i<n:
    pos=str.find(sub,i,n)
    if n!=-1:
        print('Found at position at',pos+1)
        i=pos+1
        flag=True
        continue
    else:
        i+i+1
if flag==False:
    print('Sub string not found')