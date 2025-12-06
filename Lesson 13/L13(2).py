print('Printing a floyd triangle')
n = int(input('Enter the no. of rows: '))
num = 1
for r in range(1 , n + 1):
    for c in range(1 , r + 1):
        print(num , end= ' ')
        num = num + 1
    print()