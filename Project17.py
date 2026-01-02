import math
try:
    n = float(input('Please enter the angle in degrees: '))
    radians = math.radians(n)
    sin_value = math.sin(radians)
    print('The sine value of', n, 'degrees is:', sin_value)
    cos_value = math.cos(radians)
    print('The cosine value of', n, 'degrees is:', cos_value)
    tan_value = math.tan(radians)
    print('The tangent value of', n, 'degrees is:', tan_value)
except ValueError:
    print("Invalid input. Restart, and please enter a valid number.")