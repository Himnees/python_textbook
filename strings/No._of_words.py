# Finding Number of Characters and words
# Program 12: A python program to find the lenght of a string without using len fuction
str=input('Enter the string:')
i=0
for s in str:
    print(str[i],end='')
    i+=1
print('\nThe length of string is',i)

# Program 13: A python program to find the number of words in a string.
str=input('Enter the string:')
i=c=0
flag=True
for s in str:
    if flag==False and str[i]==' ':
        c+=1
    elif str[i]==' ':
        flag=True
    else:
        flag=False
    i+=1
print('Number of words are',c+1)
