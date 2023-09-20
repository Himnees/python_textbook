# Program 22: A python program to unzip the contents of the files that are available in a zip file.
from zipfile import *
f=ZipFile('test.zip','r')
f.extractall()