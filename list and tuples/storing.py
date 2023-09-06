# Storing different types of data in a list
emp=[]
n=int(input('How many employees'))
for i in range(n):
    print('Enter id:',end='')
    emp.append(int(input()))
    print('Enter name: ',end='')
    emp.append(input())
    print('Ener Salary: ',end='')
    emp.append(float(input()))

print('The list is created with employee data.')

id=int(input('Enter employee id: '))

for i in range(len(emp)):
    if id==emp[i]:
        print('Id= {:d}, Name= {:s}, Salary= {:.2f}'.format(emp[i],emp[i+1],emp[i+2]))
        break

