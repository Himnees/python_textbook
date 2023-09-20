# Program 12: A python to pickle Emp class object.
import program_11, pickle
f=open('emp.dat','wb')
n= int(input('How many employees:'))
for i in range(n):
    id=int(input('Enter id:'))
    name=input('Ente name:')
    sal=float(input('Enter salary:'))

    e=program_11.Emp(id,name,sal)

    pickle.dump(e,f)

f.close()
