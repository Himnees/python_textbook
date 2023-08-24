# Changing case of a String
# Python offers 4 methods that are useful to change the case of a string. They are upper(), lower(), swapcase() and title()
str='Himneesh loves Spoorti'
print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.title())

# Checking Starting and Ending of a string
# syntax: str.startwith(substring)
str='Sunitha loves Himneesh'
print(str.startswith('Sunitha'))
print(str.endswith('Himneesh'))

# String Testing Method
sr='Bangalore01'
print(sr.isalnum())
print(sr.isalpha())
print(sr.isdigit())
print(sr.islower())
print(sr.isupper())
print(sr.istitle())
print(sr.isspace())

# Formating the stings
# syntax: 'format string with replacement field',format(values)

id =10
name='Sunitha'
sal=23000.00
str='{},{},{}'.format(id,name,sal)
print(str)
str='{}-{}-{}'.format(id,name,sal)
print(str)
str='id={}\nname={}\nsal{}'.format(id,name,sal)
print(str)
str='id={}\tname={}\tsal{}'.format(id,name,sal)
print(str)
str='id={2}\tame={1}\tsal{0}'.format(id,name,sal)
print(str)
str='id={0}\tame={1}\tsal{2}'.format(id,name,sal)
print(str)
str='id={one}\tame={two}\tsal{three}'.format(one=id,two=name,three=sal)
print(str)
str='id={:d}\tame={:s}\tsal{:f}'.format(id,name,sal)
print(str)
str='id={:d}\tame={:s}\tsal{:10.2f}'.format(id,name,sal)
print(str)
num=500
print('{:*>15d}'.format(num))
num=500
print('{:*^15d}'.format(num))
n=1000
print('Hexadecimal={:.>15x}\n Binary={:.>15b}'.format(n,n))
n=1000
print('Hexadecimal={:.>#15x}\n Binary={:.>#15b}'.format(n,n))

# Working with characters
# Program 9: A python to know the type of character entered by the user.
str=input('Enter a character:')
ch=str[0]
if ch.isalnum():
    print('It is alphabet or numeric character')
    if ch.isalpha():
        print('It is an alphabet')
        if ch.isupper():
            print('It is capital letter')
        else:
            print('It is a lowercase letter')
    else:
        print('It is numeric digit')
elif ch.isspace():
    print('It is a space')
else:
    print('It may be a special character')