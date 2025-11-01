'''Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
'''
unit = int (input('please enter the units: '))
if unit <= 50 :
    totalcost = (unit*2.60) + 25
elif unit > 50 and unit < 100:
    totalcost = (unit*3.25) + 35
elif unit > 100 and unit < 200:
    totalcost = (unit*5.26) + 45
else:
    totalcost = (unit*8.45) + 75
print('The total electricity bill is' , totalcost)