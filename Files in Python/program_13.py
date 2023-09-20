# Program 13: A python program to unpickle Emp class object.
import program_11, pickle
f=open('emp.dat','rb')
print('Employee details') 
while True:
    try:
        obj=pickle.load(f)
        obj.display()

    except EOFError:
        print('End of file')
        break
f.close()