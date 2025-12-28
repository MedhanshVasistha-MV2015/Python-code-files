try:
    age = int(input("Enter your age in 2026: "))

    print('\nYou are ' , age , ' years old in 2026.')
    if age % 2 == 0:
        print('The age ' , age , ' is even.')
    else:
        print('The age ' , age , ' is odd.')
except ValueError:
    print("Please enter a valid age.")  
