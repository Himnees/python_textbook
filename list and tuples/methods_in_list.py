# Method in list
# Program 5: A python program to understand list processing methods
num=[10,20,30,40,50]
print(len(num))
num.append(69)
print(num)
num.insert(0,5)
print(num)
num1=num.copy()
print(num1)
num.extend(num1)
print(num)
n=num.count(50)
print(n)
num.remove(50)
print(num)
num.pop()
print(num)
num.sort()
print(num)
num.reverse()
print(num)
num.clear()
print(num)