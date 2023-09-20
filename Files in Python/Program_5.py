# Program 5: A python program to append data to an existing file and then displaying th eentire file
f=open('love.txt','a+')
while str != '@':
    str=input()
    if (str!='@'):
        f.write(str+"\n")
f.seek(0.0)
print('The content lines are:')
str=f.read()
print(str)
f.close()