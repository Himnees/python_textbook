# Program 19: A python program to create phone book with names and phone number.
with open("phonebook.dat","wb") as f:
    n= int(input('How many entries:'))

    for i in range(n):
        name=input('Enter name:')
        phone=input('Enter Phone no.:')
        name=name.encode()
        phone=phone.encode()
        f.write(name+phone)
