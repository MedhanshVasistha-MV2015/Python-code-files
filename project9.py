n = int(input('please enter a number: '))
s = 0
while n > 0:
    s = s+1
    n = n //10
print('The number of digits in the number is: ' , s)