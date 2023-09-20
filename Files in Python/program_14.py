# Program 14: A python program to create a binary file and store a few records.
reclen=20
with open('cities.bin','wb') as f:
    n= int(input('How many cities:'))
    for i in range(n):
        city=input('Enter city name:')
        ln=len(city)
        city=city+(reclen-ln)*' '
        city=city.encode()
        f.write(city)