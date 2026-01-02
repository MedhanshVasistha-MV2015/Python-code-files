print('Printing a pyramid pattern of stars')
n = int(input('Enter the numbers of rows: '))
for r in range(n):
    for r in range(n - r):
        print(' ' , end= '*')
    print() 
 