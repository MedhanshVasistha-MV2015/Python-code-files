import random
class fruitquiz:
    def __init__(self):
        self.fruit = {'apple' : 'red' , 'banana' : 'yellow' , 'orange' : 'orange' , 'watermelon' : 'green'}
    def start(self):
        fruit,color = random.choice(list(self.fruit.items()))
        answer = input('What is the color of ' + fruit + '?')
        if answer == color:
            print('Correct answer')
        else:
            print('Wrong answer')
ob1 = fruitquiz()
ob1.start()
