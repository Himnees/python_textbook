# Sorting the elements of a dictionary using lambdas.

# Program 8: A python program to sort the elements of a dictionary based on a key or value.
colors={10:'red',35:'green',15:'blue',25:'white'}
c1=sorted(colors.items(), key=lambda t:t[0])
c2=sorted(colors.items(), key=lambda t:t[1])
print(c1)
print(c2)