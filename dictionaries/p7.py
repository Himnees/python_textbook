# A python program to find the number of occurances of each letter in a string using dictionary
str='Spoorthi'
dict={}
for x in str:
    dict[x]=dict.get(x,0)+1
print(dict)
for k,v in dict.items():
    print('key={}\tocurance={}'.format(k,v))
