# It is possible to assign the same value to two variables in the same statement as:
a=b=1
print(a,b)
# Another example is where we can assign different values to two variables as:
a=1;b=2
print(a,b)
#The same can done using the following statement:
a,b = 1,2
print(a,b)
x,y = 5,10
z=x+y # Assignment operator. Stores right side value into left side variable, i.e. x+y is stored into z.
print(z)
z+=x #Additional assignment operator. Adds right operand by the left operand and stores the result into left operand,i.e z=z+x
print(z)
z-=x # Subtraction assignment operator. Subtracts right operand by the left operand and stores the result into left operand,i.e z=z-x
print(z)
z*=x # Multiplication assignment operator. Mutiplies right operand by the left operand and stores the result into left operand,i.e z=z*x
print(z)
z/=x # Division assignment operator. Divides left operand by the right operand and stores the result into left operand,i.e z=z/x
print(z)
z%=x # Modulus assignment operator. Divides left operand by the right operand and stores the remainder into left operand,i.e z=z%x
print(z)
z=15
z**=x # Exponentiation assignment operator. Performs power value and then stores the result into left operand, i.e. z=z**y
print(z)
z//=x #  Floor division assignment operator. Performs floor division and then stores the result into left operand, i.e. z=z//y
print(z)