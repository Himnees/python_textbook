str=input('Enter the main string:')
sub=input('Enter sub string:')
i=0
flag=False
n=len(str)
while i<n:
    pos=str.find(sub,i,n)
    if pos!=-1:
        print('Found at position at',pos+1)
        i=pos+1
        flag=True
        
    else:
        i+i+1
if flag==False:
    print('String not found')

