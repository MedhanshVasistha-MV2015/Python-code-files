try:
    inp = int(input('Enter a number:'))
    print(inp)
except ValueError as e:
    print('Invalid input: ' , e)
