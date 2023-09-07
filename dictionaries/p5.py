# Program 5: A python program to create a dictionary with cricket players names and scores in a match.
x={}
print('How many players:',end=' : ')
n=int(input())
for i in range(n):
    print('Enter key',end=' : ')
    k=input()
    print('Enter value',end=' : ')
    v=input()
    x.update({k:v})
print(x)
print()
print('Players in this match:')
for pname in x.keys():
    print(pname)
print('Enter player name:',end=' : ')
name=input()
runs=x.get(name,-1)
if(runs==-1):
    print('Player not found')
else:
    print('{} has scored {}'.format(name,runs))