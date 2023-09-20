# Program 16: A python program to search for city name to the file and display the record number that contains the city name.
import os
reclen=20
size=os.path.getsize('cities.bin')
print('size of file={}'.format(size))
n=int(size/reclen)
print('No. of records ={}'.format(n))
with open('cities.bin','rb') as f:
    name=input('Enter city name:')
    name=name.encode()
    position=0
    found=False
    for i in range(n):
        f.seek(position)
        str=f.read(20)
        if name in str:
            print('Found at record no. :',i+1)
            found=True
        position+=reclen

    if not found:
        print('City not found')