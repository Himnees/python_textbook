# The print("string") statement
print("Hello") # A string repreents a group of characters.
print('Hello') # Single qoutes and double qoutes have same meaning.
print("This is the \nfirst line") # '\n' indicates new line
print("This is the \tfirst line") # '\t' indicates tab space
print("this is the\\n Firt line") #'\' represents escape escape character.
print(3*"Hai") # we use repetation operator'*' to epeat the string.
print("City name ="+"Bangalore") # we use '+' on stings, it will join one string with another string (concatenation)
print("city name is","Bangalore")
# The print(variable list) Statement
# A list of variables can be supplied to the print() function as :
a,b = 2,4
print(a,b) 
print(a, b, sep='-') # The format is sep="character" which are used to separate the values in the output.
print(a, b, sep=':')
print(a, b, sep='----')
print("Hello")
print("Dear")
print('How are you?')
print("Hello", end='') # The way one can use it is end="character" which indicates the end characters for the line.
print("Dear", end='')
print('How are U ?')
print("Hello", end='\t') # If we use end='\t' then the output is displayed in the same line but tab space separtes them.
print("Dear", end='\t')
print('How are U ?')

# The print(object) Statement
# We can pass object like lists, tuple or dictioneries to the print() function to display element of those objects.
lst = [10,'A',23.56]
print(lst)
d = {'Idly' : 30.00, 'Roti' : 45.00, 'Chappati' : 55.50}
print(d)
# The print("string",variable list) Statement
# Most common use of the print() function is to use string along with ariables inside the print() fuction.
a=2
print(a,"is a even number")
print("You entered",a,'as input')
# The print(formated string) statement
# print("formatted string" %{variable list})
# In the "formated string", we can use %d or %i to represent decimal integer number. We can use %f to represent float values. Similarly, we can use %ss to represent strings.
x=10
print('value = %i'%x)
x,y =10,15
print('x=%i y=%d' %(x,y)) # when more than one variable is to be displayed, then parentheses are needed.
name = 'Spoorti'
print('Hi %s'%name) # To display a string, we can use %s in the formatted string.
print('Hi (%20s)'%name) # When we use %20s, it will allot 20 spaces and the string is displayed right aligned
print('Hi (%-20s)'%name) # To align the string towards left side in the spaces, we can use %-20s.
print('Hi %c%c%c' %(name[0],name[1],name[2]))
print("hi %s" %name[0:3])
num=123.234567
print('The value is: %f' %num) # To display floating point values, we can use %fbin the formatted string
print('The value is: %8.2f' %num) # If we use 8.2%f then the float value is displayed in 8 spaces and within these spaces, a decimal point and next 2 fractin.
print('The value is: %.3f' %num) # When we use %.3% then the float value is displayed with 3 fration digits after the decimal point.
# print('format string with replacement fields'.format(values))
# To display a single value using index in the replacement fiel, we can write as:
n1,n2,n3 = 1,2,3
print('number1={0}, number2={1}, number3{2}'.format(n1,n2,n3)) # In the statement, {0},{1},{2} represent the values of n1,n2,n3.
print('number1={1}, number2={0}, number3{2}'.format(n1,n2,n3)) # If we change the order of these fields, we will have order of the values to be changed in output as:
print('number1={}'.format(n1)) # To display a single value using index in the replacement field, we can write as
print('mumber1={one}, number2={two}, number3={three}'.format(one=n1,two=n2,three=n3)) # As an alternate, we can also use names in the replacement fields. But the values for these names should be provided in the format() method.
print('number1={} number2={} number3={}'.format(n1,n2,n3)) # We can also use the curly braces without mentioning indexes or names.
# All examples display the same output.
name,id,sal = 'Spoorti',156,25000.00
print('Hello {}, your id is {} and your salary is {}rs.'.format(name,id,sal))
print('Hello {0}, your id is {1} and your salary is {2}rs.'.format(name,id,sal))
print('Hello {n}, your id is {i} and your salary is {s}rs.'.format(n=name,i=id,s=sal))
print('Hello {:s}, your id is {:d} and your salary is {:.2f}rs.'.format(name,id,sal))
print('Hello %s, your id is %i and your salary is %.2frs.'%(name,id,sal))
print('Hello',name,'your id is',id,'and your salary is',sal,'\brs')