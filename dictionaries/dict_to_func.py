# Passing dictionary to function
# Program 11: A python function to accept a dictionary and display its elements.
def fun(dictionary):
    for i,j in dictionary.items():
        print(i,'--',j)
d={'Spoorti':23,'Himneesh':21}
fun(d)