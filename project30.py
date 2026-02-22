'''Write a Python program to create two classes BMW and Ferrari. Both the
classes have similar methods - fuel_type and max_speed that will display the
fuel type and max speed for respective cars. Implement polymorphism on
these two classes.'''
class BMW:
    def fuel_type(self):
        print('BMW uses Diesel')
    def max_speed(self):
        print('BMW has a max speed of 250 km/h')
class Ferrari:
    def fuel_type(self):
        print('Ferrari uses petrol')
    def max_speed(self):
        print('Ferrari has a max speed of 350 km/h')
def car_info(car):
    car.fuel_type()
    car.max_speed()
bmw = BMW()
ferrari = Ferrari()
car_info(bmw)
car_info(ferrari)
