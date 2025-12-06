print('Printing a pyramid pattern of stars')
n = int(input('Enter the numbers of rows: '))
for r in range(n):
    for c in range(r + 1):
        print('*' , end= ' ')
    print() 