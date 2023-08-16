# Program 1: A Python program to calculate the area of a circle.
import math # Here math module is imported
r = float(input('Enter the radius: '))
Area =math.pi*r**2 # pi is the constant in math module
print('Area of circle =',Area)
print('Area of circle = %.2f'%Area)
print('Area of circle {:.2f}'.format(Area))