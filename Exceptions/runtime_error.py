# Runtime Errors
# Program 3: A python program to undersand runtime errors.
def concat(a,b):
    print(a+b)
concat('love',69)
'''Exception has occurred: TypeError
can only concatenate str (not "int") to str
  File "C:\Users\HP\OneDrive\Desktop\python text book examples\Exceptions\runtime_error.py", line 4, in concat
    print(a+b)
          ~^~
  File "C:\Users\HP\OneDrive\Desktop\python text book examples\Exceptions\runtime_error.py", line 5, in <module>
    concat('love',69)
TypeError: can only concatenate str (not "int") to str'''