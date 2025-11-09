inp = int(input('Please enter a number: '))
ans = ''
while inp > 0:
    rem = inp % 2
    inp = inp // 2
    ans = str(rem) + ans
print('The binary equivalent is: ' , ans)