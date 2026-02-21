'''Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.'''
from abc import ABC, abstractmethod
class baseclass(ABC):
    def display(self, value):
        print('Value: ', value)
    @abstractmethod
    def abstact(self):
        print('This is an abstract method')
class subclass(baseclass):
    def abstact(self):
        print('This is an method similar to the abstract method')
obj = subclass()
obj.abstact()
obj.display(5)

