# Converting lists into dictionary

# Program 9: A python program to convert the elements of two lists into key-value pair of dictionary.
countries=['India','Uk','Usa','Germany']
capitals=["New Delhi","London","Washington","Berlin"]
z=zip(countries,capitals)
d=dict(z)
print(d)
print('{:15s} -- {:15s}'.format('Country','CAPITAL'))
for k in d:
    print('{:15s} -- {:15s}'.format(k,d[k]))

# Converting strings into dictionary
# Program 10: A python program to convert a string into key-value pairs and store them into a dictionary.
str='Himneesh=21, Spoorthi=23'
lst=[]
for x in str.split(','):
    y=x.split('=')
    lst.append(y)
d=dict(lst)
print(d)
d1={}
for k,v in d.items():
    d1[k]=int(v)
print(d1)