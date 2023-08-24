# Program 7: A program to display all position of a string in a given main string
str=input('Enter the main string:')
sub=input('Enter sub string:')
flag=False
pos=-1
n=len(str)
while True:
    pos=str.find(sub,pos+1,n)
    if pos==-1:
        break
    print('Found at position',pos+1)
    flag=True

if flag==False:
    print('Not found')
