try:
    num1 , num2 = eval(input('enter 2 numbers separated by a comma: '))
    result = num1/num2
    print('The result is: ' , result)
except ZeroDivisionError:
    print('You cannot divide by zero !!')
except SyntaxError:
    print('Please enter numbers only seperated by comma !!')
except ValueError:
    print('Please put numbers only !!')
else:
    print('No exceptions')
finally:
    print('Execution completed')

