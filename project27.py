'''Create a class circle and create a constructor with a variable radius inside it.
Create two functions, area and perimeter, to calculate and return respective
values for the initial radius values. For the value of the radius, take input from
the user.'''
class circle:
    def __init__(self):
        self.radius = int(input('Enter the radius of the circle: '))
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
obj = circle()
print('Area of the circle is: ', obj.area())
print('Perimeter of the circle is: ', obj.perimeter())
