'''Write a program to create a parent class Person (attributes - name, id number)
with a method display to display the attributes. Next, create a child class
Employee (attributes - name, id number, salary, post). Access the attributes of
parent class in child class. Then, create an object for child class and call the
display method to display the name and id number.'''
class Person( object ):		
		def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print(self.name)
				print(self.idnumber)
class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post
				Person.__init__(self, name, idnumber)
a = Employee('Bittu', 886012, 200000, "Intern")	
a.display()
