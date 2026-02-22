'''Write a program to create a class Parrot and perform the following tasks - 1.
Create a class variable species 2. Create a init_method that has instance
variables - name and age 3. Create instances of class Parrot, passing arguments
as well 4. Print Class variable by accessing it 5. Print Instance variables as well
'''
class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blue = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
print("Blue is a {}".format(blue.species))
print("Woo is also a {}".format(woo.species))
print("{} is {} years old".format( blue.name, blue.age))
print("{} is {} years old".format( woo.name, woo.age))