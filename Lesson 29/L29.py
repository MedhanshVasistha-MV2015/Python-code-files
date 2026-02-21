'''Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo'''
class vehicle:
    def __init__ (self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def display(self):
        print('The name is ', self.name)
        print('The maximum speed is ', self.max_speed)
        print('The mileage is ', self.mileage)
class bus(vehicle):
    def __init__ (self,name,max_speed,mileage):
        vehicle.__init__(self,name,max_speed,mileage)
    def display(self):
        vehicle.display(self)
obj1 = bus('School Volvo', 180,12)
obj1.display()

