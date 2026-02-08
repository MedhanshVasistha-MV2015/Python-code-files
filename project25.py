'''Write a program to create a dog class, create a class variable animal and
inside the constructor, create another two variables - breed and colour inside
the constructor. Next up, create two different objects for different breeds of
dogs. Also, display the details of both breeds of dogs.'''
class dog:
    animal = 'dog'
    def __init__ (self,breed,colour):
        self.breed = breed
        self.colour = colour
dog1 = dog('Labrador','Black')
print('The breed of dog1 is: ', dog1.breed)
print('The colour of dog1 is: ', dog1.colour)
dog2 = dog('Pug','Brown')
print('The breed of dog2 is: ', dog2.breed)
print('The colour of dog2 is: ', dog2.colour)
