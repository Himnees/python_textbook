# Program 3: A python program to store a group of strings into a text file
f=open('love.txt','w')
print('Enter @ at last:')
while str !='@':
    str =input()
    if (str !='@'):
        f.write(str+"\n")
f.close()

    