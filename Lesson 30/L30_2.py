'''Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.'''
class computer:
    __maxprice = 10000
    def sell(self):
        print('The selling price is: ', self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice = price
obj = computer()
obj.__maxprice = 15000 #Trying to change the value of private variable which will not change the value of maxprice because it is a private variable and cannot be accessed outside of the class.
obj.sell()
obj.setmaxprice(20000)
obj.sell()