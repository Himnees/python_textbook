# Program 11: A python program to accept 3 integers in the same line and display the sum.
var1,var2,var3 = [int(x) for x in input("Enter three numbers: ").split()]
print('Sum = ',var1+var2+var3)
# Program 12: A python program to accept 3 interger in the same line and display their sum and product.
var1,var2,var3 = [int(x) for x in input('ENter three numbers').split(',')]
print('sum= ',var1+var2+var3)
print('Product = ',var1*var2*var3)
# Program 13: A python program to accept a group of string seperated by commas and display them again.
lst = [x for x in input('Enter names : ').split(',')]
print('Names are :\n',lst)
# Program 14: A python program to accept a list and display it.
ls = eval(input('Enter the list :'))
print('List = ',ls)
a,b = 5,10
result = eval("a+b-3")
print(result)
# Program 15: Evaluating an expression entered from keybord
x = eval(input('Enter the expression :'))
print("result = %d"%x)
# Program 16: A python program to accept a tuple and display it.
tpl = eval(input('Enter a tuple: '))
print("tuple= ",tpl)