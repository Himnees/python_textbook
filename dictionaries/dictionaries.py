# Program 1: A python program to create a dictionary with employee details and retrieve the value upon giving the keys
dict={'Name':'Spoorthi','Id':100,'Salary':10000}
print('Name of employee=',dict['Name'])
print('Id number=',dict['Id'])
print('Salary=',dict['Salary'])

# Operation on dictionary
dict={'Name':'Spoorthi','Id':100,'Salary':10000}
n=len(dict)
print('No. of key-value pairs:',len(dict))
dict['Salary']=15000
dict['dept']='Employee'
print(dict)
del dict['Id']
print(dict)
print('dept' in dict)
print('gender' in dict)
print('gender' not in dict)
a={'Spoorthi':100,'Himneesh':100,'Spoorthi':200}
print(a)

# Program 2: A python program to retrieve keys, values and key-value pairs from dictionary.
dict={'Name':'Spoorthi','Id':100,'Salary':10000}
print(dict)
print('Keys in dict=',dict.keys())
print('Values in dict=',dict.values())
print('Items in dict=',dict.items())