# Program 30: A python program to display all contents of the current directory.
import os
for dirpath, dirnames, filenames in os.walk('.'):
    print('Current path:',dirpath)
    print('Directories:',dirnames)
    print('Files:',filenames)
    print()