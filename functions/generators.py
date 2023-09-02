# Generators
# Program 41: A python program to create a generator to create a generator that reurns a sequence of numbers from x and y
def mygen(x,y):
    while x<=y:
        yield x
        x+=1
g=mygen(5,10)
for i in g:
    print(i)

# Program 42: A generator that returns characters from A to C
def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
g=mygen()
print(next(g))
print(next(g))
print(next(g))
print(next(g)) # error