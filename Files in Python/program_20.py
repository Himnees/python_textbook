# Program 20: A python program to use mmap and performing various operation on a binary file.
import mmap, sys

print('1 fo display all entries')
print('2 for ph number')
print('3 for modify')
print('4 for exit')
ch=input('Enter your option:')
if ch=='4':
    sys.exit()
with open('phonebook.dat','r+b') as f:
    mm=mmap.mmap(f.fileno(),0)

    if ch=='1':
        print(mm.read().decode())

    if ch=='2':
        name=input('Enter the name:')
        n=mm.find(name.encode())
        n1=n+len(name)
        ph=mm[n1:n1+10]
        print('Phone no:',ph.decode())

    if ch=='3':
        name=input('Enter name:')
        n=mm.find(name.encode())
        n1=n+len(name)
        ph1=input('Enter new phone number:')
        mm[n1:n1+10]=ph1.encode()

    mm.close()
