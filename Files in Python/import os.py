import os
reclen=20
size=os.path.getsize('cities.bin')
print('the size of file ={}'.format(size))
n=int(size/reclen)
print('No. of records = {}'.format(n))
with open('cities.bin','r+b') as f:
    position=0
    found=False
    for i in range(n):
        
        str=f.read(20)
        print(str)
        i+=1
        