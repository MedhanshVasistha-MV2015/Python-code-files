sp = float (input('Please enter the selling price of the product: '))
cp = float (input('Please enter the cost price of the product: '))
if sp > cp:
    profit = sp - cp
    print('You made a profit of: ', profit)
else:
    loss = sp - cp
    print('You had a loss of: ', loss)
    
