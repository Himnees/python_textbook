# Working with binary files
# Program 8: A python program to copy an image file into anotherr file.
f1 = open('logo.png','rb')
f2=open('copy.png','wb')
bytes=f1.read()
f2.write(bytes)
f1.close()
f2.close()