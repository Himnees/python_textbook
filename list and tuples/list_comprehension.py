# List Comprehension
# Example 1: We want to create a list with squares of integers from 1 to 10. We can write code as:
squares=[]
for x in range(1,11):
    squares.append(x**2)
print(squares)
# In list comprehension mehos
sq=[x**2 for x in range(1,11)]
print(sq)

# Example 2: Suppose, we want to get squares of integers from 1 to 10 and take only the even number from the result, we can write a list comprehension as:
even_square=[x**2 for x in range(1,11) if x%2==0]
print(even_square)
# Similar
even_sq=[x**2 for x in range(1,11,2)]
print(even_sq)

# Example 3: If we have two lists 'x' and 'y' and we want to add each element of 'x' with each element of 'y', we can write for loops as:
x=[10,20,30]
y=[1,2,3,4]
lst=[]
for i in x:
    for j  in y:
        lst.append(i+j)
print(lst)
# similar 
l1=[i+j for i in x for j in y]
print(l1)
l2=[i+j for i in [10,20,30] for j in [1,2,3,4]]
print(l2)
l3=[i+j for i in 'ABC' for j in 'DE']
print(l3)

# Example 4: Let's take a list 'words' that contains a group of words or strings as:
words=['Apple','Grapes','Bannana','Orange']
ls=[] 
for i in words:
    ls.append(i[0])
print(ls)
# similar
l4=[w[0] for w in words]
print(l4)

# Example 5: Let's take two lists 'num1' and 'num2' with some number as:
num1=[1,2,3,4,5]
num2=[10,11,1,2]
num3=[]
for i in num1:
    if i not in num2:
        num3.append(i)
print(num3)
# similar
n=[i for i in num1 if i not in num2]
print(n)

# Example 6:Like list comprehension. It is also possible to create set comprehension and dictionary comprehension in the same manner as discussed to the previous example. 
dict={101:'Himneeh',102:'Spoorti',103:'Sunitha'}
dic1={value: key for key,value in dict.items()}
print(dic1)