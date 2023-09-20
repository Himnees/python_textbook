# Program 15: A python program to randomly access a record from a binary file.
reclen=20
with open('cities.bin','rb') as f:
    n=int(input('Enter record number:'))
    f.seek(reclen*(n-1))
    str=f.read(reclen)
    print(str.decode())         