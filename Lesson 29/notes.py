class Parent:
    def __init__(self, aggr,eye_color):
        self.aggr = aggr
        self.eye_color = eye_color
        
    def display(self):
        print('The eye color is ', self.eye_color)
        print('Aggressive in Nature ', self.aggr)

class Child(Parent): #declaration of child class
    def __init__(self, name, age, aggr, eye_color):
        self.name = name
        self.age = age
        Parent.__init__(self, aggr, eye_color) #inheriting properties from parent class

    def display(self):
        print('The name is ', self.name)
        print('The age is ', self.age)
        Parent.display(self) #inheriting method from parent class

c1 = Child('Pingu', 9, True, 'Hazel')
c1.display()

    

