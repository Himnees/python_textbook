Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=15
>>> print(type(a))
<class 'int'>
>>> a=15.5
>>> print(type(a))
<class 'float'>
>>> a= 'Hello'
>>> print(type(a))
<class 'str'>
>>> a = [1,2,3,4]
>>> print(type(a))
<class 'list'>
>>> a = (1,2,3,4,5)
>>> print(type(a))
<class 'tuple'>
>>> a = 1+j
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a = 1+j
NameError: name 'j' is not defined
>>> a= 1+J
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a= 1+J
NameError: name 'J' is not defined
>>> a= 1+4j
>>> print(type(a))
<class 'complex'>
>>> a = {1,2,3,4,5}
>>> print(type(a))
<class 'set'>
>>> a = frozenset({1,2,3,4,5})
>>> print(type(a))
<class 'frozenset'>
>>> a ={1:'a',2:'b',3:'c'}
>>> print(type(a))
<class 'dict'>
