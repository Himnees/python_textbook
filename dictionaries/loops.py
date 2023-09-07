# Using for loop with dictionaries 

# Program 6: A python program to show the usage of for loop to retrieve elements of dictionaries.
colors={'r':"red",'g':"green",'w':"white",'b':"blue"}
for k in colors:
    print(k)

for k in colors:
    print(colors[k])

for k,v in colors.items():
    print('keys={} value={}'.format(k,v))