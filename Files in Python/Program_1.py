# Program 1: A python program to create a text file to store indiviual characters.
f=open('myfile.txt','w')
str=input('Enter text:')
f.write(str)
f.close()