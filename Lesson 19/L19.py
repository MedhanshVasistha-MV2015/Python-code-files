import random
playing = True
number = random.randint(10, 20)
print('Welcome  to the guessing game!')
print('The game ends when you get one number right! Make a guess between 10 to 20.')
while playing:
    guess = int(input('Give me your best guess! '))
    if guess == number:
        print('Correct! You win!')
        break
    else:
        print('Wrong! Try again!')