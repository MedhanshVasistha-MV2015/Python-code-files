'''Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object'''
class vehicle:
    def __init__ (self,max_speed,milage):
        self.maxspeed = max_speed
        self.milage = milage
vehicle1 = vehicle(240,18)
print('The max speed is: ', vehicle1.maxspeed)
print('The milage is: ', vehicle1.milage)
