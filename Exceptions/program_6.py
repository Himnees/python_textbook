# Program 6: A python program to understand the effect of an exception.
f = open("love","w")
a,b=[int(x) for x in input("Enter two numbers:").split()]
c=a/b
f.write("writing %d into my my love"%c)
f.close()
print('file closed')
# if 0 in denominator it shows:
'''Exception has occurred: ZeroDivisionError
division by zero
  File "C:\Users\HP\OneDrive\Desktop\python text book examples\Exceptions\program_6.py", line 4, in <module>
    c=a/b
      ~^~
ZeroDivisionError: division by zero'''