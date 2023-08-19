# Program 32: Write a python program to display prime number series.
# Define a function to check if a number is prime
a = int(input('How many prime number:'))
def is_prime(n):
    # If n is less than 2, it is not prime
    if n < 2:
        return False
    # Loop from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If i divides n evenly, n is not prime
        if n % i == 0:
            return False
    # If no divisor is found, n is prime
    return True

# Initialize a counter for the number of primes found
count = 0
# Initialize a variable for the current number to check
num = 2
# Loop until 30 primes are found
while count < a:
    # If num is prime, print it and increment the counter
    if is_prime(num):
        print(num)
        count += 1
    # Increment num by 1 for the next iteration
    num += 1

max = int(input('Upto what number:'))
for num in range(2,max+1):
    for i in range(2,num):
        if num%i ==0:
            break
    else:
            print(num)