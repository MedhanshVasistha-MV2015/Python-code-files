''' 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions'''
class priclass:
    __privateVar = 13
    def __privMeth(self):
        print('This is a message.')
    def hello(self):
        print('The value of the Variable is: ', self.__privateVar)

obj = priclass()
obj.hello()
obj.__privMeth() #Trying to access a private method outside of the class which will result in an attribute error because private methods cannot be accessed outside of the class.
obj.__privateVar
