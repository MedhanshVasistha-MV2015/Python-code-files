import math
try:
    r = int(input('Enter the radius of the circle: '))
    circumference = 2 * math.pi * r
    print('The circumference of the circle is:', circumference)
except ValueError:
    print("Invalid input. Restart, and please enter a valid number.")