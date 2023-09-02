# Program 9: A python program to see how to assign a function to a variable
def love(str):
    return 'Spoorti loves '+str
x=love('Himneesh')
print(x)

# Program 10: A python program to know how to define a function inside another function.
def love(str):
    def message():
        return 'I love you '
    return message()+str
print(love('Spoorti'))

# Program 11: A python program to knoe how to pass a function as parameter to another function.
def love(heart):
    return 'I love you '+heart
def message():
    return 'Spoorti'
print(love(message()))

# Program 12: A python program to know how a function can return another function
def display():
    def message():
        return 'Spoorti loves Himneesh'
    return message
love=display()
print(love())
