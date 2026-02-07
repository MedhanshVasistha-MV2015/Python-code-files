'''Write a Python program to generate a random password consisting of lower case and
upper case characters along with numbers. You can also use random module for
shuffling the password generated.'''
import random
abc = {'lower' : 'abcdefghijklmnopqrstuvwxyz', 
       'upper' : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
num = '0123456789'
def password():
    password = []
    for i in range(4):
        password.append(random.choice(abc['lower']))
        password.append(random.choice(abc['upper']))
        password.append(random.choice(num))
    random.shuffle(password)
    return ''.join(password)
print(password())

    